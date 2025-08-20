"""
    page_object 页面对象类(page_object)：用于打开操作页面
"""
from base_page.base_page import BasePage  # 从 base_page 模块导入 BasePage 类
import logging  # 引入logging库，用于记录日志

# 配置日志记录格式和日志级别，记录日志的详细信息（时间戳、日志级别、日志消息）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 创建一个名为__name__的logger实例，用于记录日志信息


class OpenPage(BasePage):  # 定义 OpenPage 类，并继承自 BasePage 类
    """
    OpenPage 类用于封装打开指定网址的操作，继承自 BasePage 基类。
    - 包含一个存储目标网址的类属性。
    - 提供一个方法用于打开网址并确保页面加载完成。
    """
    url = r'https://www.baidu.com'  # 定义类属性 url，存储要打开的目标网址

    def openurl(self):  # 定义 openurl 方法，用于打开指定网址
        """
        使用预定义的 URL 打开网页。
        - 调用基类中的 open 方法，通过指定的 URL 打开页面。
        - 等待页面加载完成，确保后续操作能够顺利执行。
        """
        logger.info("打开百度首页")  # 记录日志，表示正在加载测试数据
        self.open(self.url)  # 调用 BasePage 类的 open 方法，使用 url 打开网站
