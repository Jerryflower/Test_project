"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage
import logging
import allure

# 配置日志输出格式和等级
logging.basicConfig(  # 配置logging模块的基本设置
    level=logging.INFO,  # 设置日志级别为INFO，表示只输出INFO及以上级别的日志（INFO、WARNING、ERROR、CRITICAL）
    format="%(asctime)s - %(levelname)s - %(message)s"  # 设置日志输出格式：时间 - 日志级别 - 日志消息
)
logger = logging.getLogger(__name__)  # 获取一个以当前模块名命名的日志记录器logger，便于在不同模块中区分日志来源


class FlipPage(BasePage):  # SearchPage类继承BasePage，封装搜索相关的操作
    page_text = '//*[@id="page"]/div/a/span[contains(text(), "{index}")]'

    def take_screenshot(self, name="screenshot"):  # 定义截图方法，将截图附加到Allure报告中
        """
        截图并附加到 Allure 报告中
        :param name: 截图名称
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)  # 获取当前页面的截图并附加到Allure报告中，格式为PNG

    def flip_(self, flip_num):
        """
        功能：
            1.实现翻页功能
        """
        self.click('xpath', self.page_text.format(index=flip_num))
        self.wait(5)


