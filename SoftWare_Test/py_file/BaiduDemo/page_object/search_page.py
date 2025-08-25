"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage
import logging

# 配置日志输出格式和级别
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class SearchPage(BasePage):  # SearchPage类继承BasePage，封装搜索相关的操作
    # 百度首页搜索框和搜索按钮定位符
    # home_search_box = ('id', 'kw')
    # home_search_button = ('id', 'su')
    home_search_box = ('id', 'chat-textarea')
    home_search_button = ('id', 'chat-submit-button')

    # 页面通用搜索框和搜索按钮定位符（如聊天输入框场景）
    search_box = ('id', 'chat-textarea')
    search_button = ('id', 'chat-submit-button')

    def home_search_(self, text):  # 在百度首页进行搜索
        """
        功能：在百度首页搜索框输入文本并点击搜索按钮
        参数：
            text(str): 要搜索的文本内容
        """
        logger.info(f"准备在百度首页搜索框输入内容：{text}")  # 日志：输入内容
        self.input(*self.home_search_box, text=text)  # 输入内容

        logger.info("点击百度首页搜索按钮")  # 日志：点击按钮
        self.click(*self.home_search_button)  # 点击搜索按钮

        logger.info("等待搜索结果加载完成")  # 日志：等待结果
        self.wait(3)  # 等待结果加载

    def search_(self, text):  # 在通用搜索框进行搜索
        """
        功能：在页面的搜索框（如聊天输入框）输入文本并点击搜索按钮
        参数：
            text(str): 要搜索的文本内容
        """
        logger.info(f"准备在页面搜索框输入内容：{text}")  # 日志：输入内容
        self.input(*self.search_box, text=text)  # 输入内容

        logger.info("点击页面搜索按钮")  # 日志：点击按钮
        self.click(*self.search_button)  # 点击搜索按钮

        logger.info("等待搜索结果加载完成")  # 日志：等待结果
        self.wait(3)  # 等待结果加载
