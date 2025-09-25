"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
"""
from base_page.base_page import BasePage  # 从base_page模块导入BasePage基类，提供封装好的基础操作方法
import logging  # 导入日志模块，用于记录程序运行信息，便于调试和维护

# 配置日志输出格式和等级
logging.basicConfig(  # 配置logging模块的基本设置
    level=logging.INFO,  # 设置日志级别为INFO，表示输出INFO及以上级别的日志（INFO、WARNING、ERROR、CRITICAL）
    format="%(asctime)s - %(levelname)s - %(message)s"  # 设置日志输出格式：时间 - 日志级别 - 日志消息
)
logger = logging.getLogger(__name__)  # 获取当前模块的日志记录器logger，便于在不同模块中区分日志来源


class ScrollPage(BasePage):  # ScrollPage类继承BasePage，封装页面滑动相关操作
    scroll_times = 3  # 页面滑动的次数，可根据页面内容长度调整

    def scroll_(self):  # 定义页面滑动方法scroll_
        """
        分多次向下滚动页面，通常用于懒加载或动态加载内容的页面。
        """
        for i in range(1, self.scroll_times + 1):  # 循环scroll_times次，每次滑动页面高度的1/scroll_times
            # 使用JavaScript执行页面滚动：
            # window.scrollTo(x, y) 将页面滚动到指定位置
            # document.body.scrollHeight 获取整个页面的总高度
            # f-string中 i/self.scroll_times 计算当前滚动比例
            self.driver.execute_script(
                f"window.scrollTo(0, document.body.scrollHeight * {i}/{self.scroll_times});"
            )
            self.wait(2)  # 滚动后等待2秒，让页面加载新的内容，避免操作过快导致内容未加载
