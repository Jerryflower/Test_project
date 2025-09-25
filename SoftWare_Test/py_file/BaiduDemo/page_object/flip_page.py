"""
    page_object 页面对象类(page_object)：用于定位输入框和搜索按钮点击
    功能说明：封装页面元素定位与操作方法，便于在测试用例中直接调用，提高代码复用性
"""
from base_page.base_page import BasePage  # 导入自定义的BasePage类，封装了基础的Selenium操作方法
import logging  # 导入日志模块，用于记录程序运行信息
import allure  # 导入Allure，用于生成测试报告并添加截图等附件

# 配置日志输出格式和日志级别，输出时间、日志级别和日志信息
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 获取当前模块的logger对象，用于打印日志信息


class FlipPage(BasePage):  # 定义FlipPage类，继承BasePage，封装特定页面的操作

    page_text = '//*[@id="page"]/div/a/span[contains(text(), "{index}")]'  # 定义翻页按钮的xpath模板，{index}用于动态替换页码

    def take_screenshot(self, name="screenshot"):
        """
        截图并附加到 Allure 报告中
        :param name: 截图名称，默认值为"screenshot"
        """

        allure.attach(
            self.driver.get_screenshot_as_png(),  # 获取当前页面截图，返回二进制PNG数据
            name=name,  # 指定截图名称
            attachment_type=allure.attachment_type.PNG  # 指定附件类型为PNG图片
        )  # 使用Selenium的get_screenshot_as_png方法获取截图，并通过Allure attach方法添加到报告中

    def flip_(self, flip_num):
        """
        翻页操作：点击指定页码的翻页按钮
        :param flip_num: 目标页码，传入数字
        """
        # 使用BasePage封装的click方法，通过xpath定位并点击指定页码的按钮
        self.click('xpath', self.page_text.format(index=flip_num))  # 动态替换xpath中的{index}为flip_num
        self.wait(5)  # 等待5秒，保证页面加载完成，可根据实际情况调整等待时间
