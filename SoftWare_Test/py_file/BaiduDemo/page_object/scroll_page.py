"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage
import logging

# 配置日志输出格式和等级
logging.basicConfig(  # 配置logging模块的基本设置
    level=logging.INFO,  # 设置日志级别为INFO，表示只输出INFO及以上级别的日志（INFO、WARNING、ERROR、CRITICAL）
    format="%(asctime)s - %(levelname)s - %(message)s"  # 设置日志输出格式：时间 - 日志级别 - 日志消息
)
logger = logging.getLogger(__name__)  # 获取一个以当前模块名命名的日志记录器logger，便于在不同模块中区分日志来源


class ScrollPage(BasePage):  # SearchPage类继承BasePage，封装搜索相关的操作
    scroll_times = 3  # 页面滑动次数

    def scroll_(self):
        """
        功能：
            1.实现翻页截图
        """
        for i in range(1, self.scroll_times + 1):
            self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i}/{self.scroll_times});")  # 翻页位置
            self.wait(2)
