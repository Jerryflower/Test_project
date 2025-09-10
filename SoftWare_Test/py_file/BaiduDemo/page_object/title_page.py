"""
    page_object 页面对象类(page_object)：用于抓取搜索结果并翻页
"""
from base_page.base_page import BasePage  # 导入基类
import logging  # 引入日志模块

# 配置日志记录格式和日志级别
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class TitlePage(BasePage):  # 定义 TitlePage 类，继承 BasePage
    """
    TitlePage 类用于封装抓取搜索结果标题和翻页操作的行为。

    功能作用：
    - 提供获取搜索结果标题的方法。
    - 提供翻页功能（默认翻5页，每页都可截图）。
    """

    # 搜索结果标题定位符
    result_titles = ('xpath', '//h3[@class="t"]/a')

    # 翻页按钮的 XPath 模板，页码从 2 开始（第一页不需要点）
    page_button_template = '//*[@id="page"]/div/a[{index}]/span'

    def get_titles(self):
        """
        获取当前页的所有搜索结果标题文本。
        返回：
            list[str]: 当前页的标题列表
        """
        logger.info("开始获取当前页的搜索结果标题...")
        elements = self.driver.find_elements(*self.result_titles)
        titles = [el.text for el in elements if el.text.strip()]
        logger.info("本页共获取到 %d 个标题", len(titles))
        return titles

    def go_to_page(self, page_num):
        """
        点击指定的翻页按钮跳转到对应页。
        参数：
            page_num(int): 页码（第2页对应 a[1]，第3页对应 a[3]...）
        """
        if page_num < 2:
            logger.warning("页码小于2，无需翻页：%d", page_num)
            return

        # 根据规律生成 XPath
        xpath = self.page_button_template.format(index=page_num - 1)
        logger.info("准备跳转到第 %d 页，XPath=%s", page_num, xpath)
        self.click("xpath", xpath)
        self.wait(3)  # 等待页面加载
        logger.info("已跳转到第 %d 页", page_num)

    def get_titles_with_pagination(self, max_pages=5, screenshot_func=None):
        """
        抓取多页的搜索结果标题。
        参数：
            max_pages(int): 最大翻页数（默认5页）
            screenshot_func(callable): 截图函数，接收(driver, name)
        返回：
            list[str]: 所有页的标题合集
        """
        all_titles = []

        for page in range(1, max_pages + 1):
            logger.info("=== 正在处理第 %d 页 ===", page)
            titles = self.get_titles()
            all_titles.extend(titles)

            # 截图（如果传入了截图函数）
            if screenshot_func:
                screenshot_func(self.driver, f"Page_{page}_Titles")

            # 翻页（最后一页不再翻）
            if page < max_pages:
                self.go_to_page(page + 1)

        logger.info("总共抓取到 %d 条标题", len(all_titles))
        return all_titles
