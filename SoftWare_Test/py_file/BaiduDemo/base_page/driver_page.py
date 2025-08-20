"""
    page_object 页面对象类(page_object)：浏览器驱动类
"""
from selenium.webdriver.chrome.options import Options  # 从selenium库中导入Chrome浏览器选项类
from selenium.webdriver.chrome.service import Service  # 从selenium库中导入Chrome浏览器服务类
from selenium.webdriver import Chrome  # 从selenium库中导入Chrome浏览器类


def driver_():  # 定义一个返回Chrome浏览器对象的函数
    """
    配置并启动Chrome浏览器，返回一个Chrome WebDriver对象。
    - 通过添加启动选项来优化浏览器的配置，避免被识别为自动化工具。
    - 返回一个已配置的Chrome浏览器实例，用于后续的自动化测试操作。

    返回:
        Chrome: 配置好的Chrome WebDriver对象。
    """
    opt = Options()  # 创建一个Options对象，用于存储浏览器启动选项

    opt.add_argument("--disable-blink-features=AutomationControlled")  # 禁用浏览器的自动化控制特性，使检测自动化的脚本更难
    opt.add_argument("--disable-webrtc")  # 测试用例不涉及 WebRTC，通常这个错误不会影响测试用例的执行，可以安全忽略。
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])  # 隐藏自动化测试标志，避免被识别为自动化工具
    opt.add_experimental_option('useAutomationExtension', False)  # 禁用Chrome的自动化扩展，进一步避免检测
    opt.add_argument('--disable-extensions')  # 禁用所有浏览器扩展，确保测试环境的纯净
    opt.add_argument('--disable-webgl')  # 禁用WebGL，防止图形渲染相关的检测或异常
    opt.add_argument('--no-sandbox')  # 禁用沙箱模式，通常用于提高稳定性或解决某些权限问题
    opt.add_argument('start-maximized')  # 启动浏览器时窗口最大化，确保网页元素的可见性和交互性

    service_path = r'D:\Tianyi_Cloud\learn\Py_ProJect\FishC_Python\Python_file\driver\chromedriver.exe'  # 指定ChromeDriver的路径
    return Chrome(service=Service(service_path), options=opt)  # 返回一个使用指定服务和选项启动的Chrome浏览器对象
