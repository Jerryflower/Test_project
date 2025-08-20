"""
    BasePage层：基类，主要实现常规的Selenium操作行为
"""
from time import sleep  # 导入 sleep 函数，用于强制等待


class BasePage:
    """
    BasePage 类封装了与网页元素交互的基本方法，供其他页面对象类继承使用。
    - 包含打开网页、定位元素、输入文本、点击元素和强制等待等通用方法。
    """

    def __init__(self, driver):  # 构造方法：在实例化 BasePage 类时，初始化浏览器驱动，并设置隐式等待时间为 10 秒
        """
        初始化 BasePage 实例。
        - 接收浏览器驱动并设置隐式等待时间。

        参数:
            driver (WebDriver): 用于与浏览器交互的 WebDriver 实例。
        """
        self.driver = driver  # 将传入的浏览器驱动对象赋值给实例变量 self.driver
        self.driver.implicitly_wait(10)  # 设置隐式等待时间为 10 秒，等待元素加载

    def open(self, url):  # 访问指定的 URL
        """
        打开指定的网页。
        - 使用 WebDriver 的 get 方法访问指定 URL。

        参数:
            url (str): 需要访问的网页 URL。
        """
        self.driver.get(url)  # 使用浏览器驱动访问指定的 URL

    def locator(self, by, value):  # 定位元素
        """
        定位页面元素。
        - 根据给定的定位方式和定位值返回单个元素对象。

        参数:
            by (str): 定位方式，如 ID、XPath 等。
            value (str): 定位值，对应于定位方式的实际值。

        返回:
            WebElement: 定位到的元素对象。
        """
        return self.driver.find_element(by, value)  # 返回定位到的单个元素对象

    def input(self, by, value, text):  # 输入文本
        """
        在指定元素中输入文本。
        - 先清空元素中的现有文本，再输入新的文本。

        参数:
            by (str): 定位方式。
            value (str): 定位值。
            text (str): 需要输入的文本内容。
        """
        el = self.locator(by, value)  # 通过 locator 方法获取元素对象
        el.clear()  # 清除元素中的现有文本
        el.send_keys(text)  # 在元素中输入指定的文本

    def click(self, by, value):  # 点击元素
        """
        点击指定的页面元素。
        - 使用定位器找到元素后，执行点击操作。

        参数:
            by (str): 定位方式。
            value (str): 定位值。
        """
        self.locator(by, value).click()  # 定位到元素并点击

    def text_info(self, by, value):
        """
        获取指定位置中的文本元素的值。

        参数:
            by (str): 定位方式。
            value (str): 定位值。

        返回:
            str: 获取到的文本内容。
        """
        return self.locator(by, value).text  # 获取元素中的文本信息

    @staticmethod  # 强制等待指定的时间，定义为静态方法，无需实例化类即可调用
    def wait(time):
        """
        强制等待指定的时间。
        - 使用 sleep 方法暂停执行，通常用于等待页面加载或动画完成。

        参数:
            time (int | float): 需要等待的秒数。
        """
        sleep(time)  # 强制等待指定的秒数

    def new_window(self):
        """
        切换到最新的窗口。
        - 使用 WebDriver 的 window_handles 切换到最新打开的窗口。
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到最新打开的窗口
