"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage  # 从 base_page 模块中导入 BasePage 基类
import logging  # 引入logging库，用于记录日志

# 配置日志记录格式和日志级别，记录日志的详细信息（时间戳、日志级别、日志消息）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 创建一个名为__name__的logger实例，用于记录日志信息


class SearchPage(BasePage):  # 定义一个名为 SearchPage 的类，继承自 BasePage，用于处理搜索页面相关操作
    """
    SearchPage 类用于封装搜索页面的操作行为，继承自 BasePage 基类。
    - 包含搜索框和搜索按钮的定位器。
    - 提供搜索操作的方法，支持在搜索框中输入内容并点击搜索按钮。
    """

    search_box = ('xpath', '//*[@id="chat-textarea"]')
    search_button = ('xpath', '//*[@id="chat-submit-button"]')

    def search_(self, text):  # 定义一个名为 search_ 的方法，用于执行搜索操作
        """
        在搜索页面执行搜索操作。
        - 在搜索框中输入指定的文本内容。
        - 点击搜索按钮以触发搜索。
        - 等待搜索结果加载完成。

        参数:
            text (str): 需要输入到搜索框中的文本内容。
        """
        logger.info(f"输入搜索内容：{text}")  # 记录日志，表示正在加载测试数据
        self.input(*self.search_box, text=text)  # 调用基类中的 input 方法，将传入的文本输入到搜索框中

        logger.info("点击搜索按钮")  # 记录日志，表示正在加载测试数据
        self.click(*self.search_button)  # 调用基类中的 click 方法，点击搜索按钮
        self.wait(3)
