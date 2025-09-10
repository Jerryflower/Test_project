"""
    page_object 页面对象类(page_object)：用于打开操作页面
"""
from base_page.base_page import BasePage  # 从 base_page 模块导入 BasePage 类，作为所有页面类的基类
import logging  # 引入logging库，用于记录日志信息
import allure  # 引入allure库，用于生成Allure测试报告

# 配置日志记录格式和日志级别，记录日志的详细信息（时间戳、日志级别、日志消息）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 创建一个名为当前模块(__name__)的logger实例，用于记录日志


class OpenPage(BasePage):  # 定义 OpenPage 类，并继承自 BasePage 类
    """
    OpenPage 类用于封装打开指定网址的操作，继承自 BasePage 基类。

    功能作用：
    - 提供打开指定网页的方法。
    - 通过调用基类方法完成具体的浏览器行为。
    """
    url = r'https://www.baidu.com'  # 定义类属性 url，存储要打开的目标网址（此处为百度首页）

    def openurl(self):  # 定义 openurl 方法，用于打开指定网址
        """
        使用预定义的 URL 打开网页。

        功能作用：
        - 调用基类中的 open 方法，通过类属性 url 打开页面。
        - 确保页面能正确加载，方便后续的操作。
        """
        logger.info("准备打开网址: %s", self.url)  # 记录日志，说明准备打开目标网址
        self.open(self.url)  # 调用 BasePage 类的 open 方法，使用 url 打开网站
        self.take_screenshot("打开百度官网")
        logger.info("成功打开网址: %s", self.url)  # 记录日志，确认页面已被成功打开

    def take_screenshot(self, name="screenshot"):  # 定义截图的方法，并将截图附加到Allure报告中
        """
        截图并附加到 Allure 报告中
        :param name: 截图名称
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)  # 获取截图并附加到Allure报告，类型为PNG格式
