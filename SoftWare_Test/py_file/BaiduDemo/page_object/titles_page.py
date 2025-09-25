"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage  # 引入自定义的BasePage基类，封装了常用的Selenium操作
import logging  # 引入Python标准库logging，用于日志记录

# 配置日志记录格式和输出级别，INFO级别会输出一般运行信息（含时间戳、日志级别、消息内容）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 获取当前模块的日志记录器实例


class TitlesPage(BasePage):  # 定义页面对象类TitlesPage，继承BasePage
    """
    页面对象类 TitlesPage：
    - 继承自 BasePage，具备基础的浏览器操作能力。
    - 主要功能：定位页面中的 h3 元素（通常为标题），并输出标题文本。
    """

    # 元素定位器：页面上所有的 <h3> 标签
    # 使用元组形式 ('定位方式', '定位表达式')，与 Selenium find_elements 方法兼容
    titles = ('xpath', '//h3')  # 元素定位器，使用xpath定位页面中所有<h3>标签（一般表示标题）

    def titles_(self, page):  # 定义方法titles_，参数page表示第几页
        """
        获取并打印当前页面所有标题文本。

        :param page: 当前页码，用于在日志中标记输出结果所属的页面
        """
        titles = self.driver.find_elements(*self.titles)  # 使用WebDriver查找所有匹配的<h3>元素，返回元素列表
        for idx, t in enumerate(titles, start=1):  # 遍历获取到的标题元素，idx从1开始计数
            # 输出日志，格式：[第X页-第Y条] 标题文本
            # 例如：[第2页-第3条] Python自动化测试框架
            logger.info(f"[第{page}页-第{idx}条] {t.text}")
