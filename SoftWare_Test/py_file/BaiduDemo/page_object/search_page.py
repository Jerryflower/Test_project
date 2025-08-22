"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class SearchPage(BasePage):
    home_search_box = ('id', 'kw')
    home_search_button = ('id', 'su')

    search_box = ('xpath', '//*[@id="chat-textarea"]')
    search_button = ('xpath', '//*[@id="chat-submit-button"]')

    def home_search_(self, text):
        logger.info(f"输入搜索内容：{text}")
        self.input(*self.home_search_box, text=text)

        logger.info("点击搜索按钮")
        self.click(*self.home_search_button)
        self.wait(3)

    def search_(self, text):
        logger.info(f"输入搜索内容：{text}")
        self.input(*self.search_box, text=text)

        logger.info("点击搜索按钮")
        self.click(*self.search_button)
        self.wait(3)
