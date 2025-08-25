"""
    测试用例层(test_cases)：用于实现操作流程
"""
import pytest  # 引入pytest库，用于管理测试用例的执行
import allure  # 引入allure库，用于生成Allure报告
import yaml  # 引入yaml库，用于读取YAML格式的测试数据
from base_page.driver_page import driver_  # 从页面对象模块导入driver_类，用于管理浏览器驱动
from page_object.search_page import SearchPage  # 从页面对象模块导入SearchPage类，用于实现页面的搜索功能
from page_object.open_page import OpenPage  # 从页面对象模块导入OpenPage类，用于打开指定的网站
import logging  # 引入logging库，用于记录日志

# 配置日志记录格式和日志级别，记录日志的详细信息（时间戳、日志级别、日志消息）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)  # 创建一个名为__name__的logger实例，用于记录日志信息


def attach_screenshot(driver, name):
    """
    截图函数，用于将当前页面截图并附加到Allure报告中，便于问题追踪。
    参数:
        driver: 浏览器驱动对象
        name (str): 截图的名称
    """
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
    logger.info(f"已添加截图到Allure报告，截图名称：{name}")  # 记录截图动作


@pytest.fixture(scope='module')
def setup():
    """
    初始化测试环境，加载测试数据，并返回页面操作对象。
    - 读取YAML文件中的测试数据。
    - 初始化浏览器驱动。
    - 实例化SearchPage和OpenPage对象。
    - 在测试结束后清理资源。

    返回:
        sp (SearchPage): 搜索页面对象。
        op (OpenPage): 打开页面对象。
        data (dict): 测试数据字典.
    """
    logger.info("开始加载测试数据...")
    with open(r'D:\Tianyi_Cloud\learn\Py_ProJect\SoftWare_Test\py_file\BaiduDemo\test_data\order.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    logger.info("测试数据加载完成")

    logger.info("初始化浏览器驱动...")
    driver = driver_()
    sp = SearchPage(driver)
    op = OpenPage(driver)
    logger.info("页面对象已实例化，准备开始测试")

    yield sp, op, data

    logger.info("测试结束，正在关闭浏览器驱动...")
    driver.quit()
    logger.info("浏览器驱动已关闭")


def test_open(setup):
    """
    测试打开页面功能。
    - 从fixture中获取打开页面对象。
    - 执行打开页面操作。
    """
    sp, op, data = setup
    logger.info("开始执行页面打开测试...")
    op.openurl()
    logger.info("页面打开操作完成")
    attach_screenshot(op.driver, "Open_Login")


def test_search(setup):
    """
    测试页面搜索功能。
    1. 在网站首页输入第一条数据，进入搜索结果显示页面。
    2. 在搜索结果页面循环输入剩余的数据并点击搜索按钮进行二次搜索。
    """
    sp, op, data = setup
    text_list = data['text_list']

    if not text_list:
        logger.warning("测试数据为空，跳过搜索测试")  # 提前提示
        pytest.skip("测试数据为空，跳过测试")

    # 第一步：首页输入第一个搜索内容
    logger.info(f"首页搜索：{text_list[0]['content']}")
    sp.home_search_(text_list[0]['content'])
    logger.info("首页搜索完成，准备截图")
    attach_screenshot(sp.driver, "Home_Search")

    # 第二步：在搜索结果页循环输入剩余的搜索内容
    for i, text in enumerate(text_list[1:], 1):
        logger.info(f"结果页第 {i} 次搜索：{text['content']}")
        sp.search_(text['content'])
        logger.info(f"第 {i} 次搜索完成，准备截图")
        attach_screenshot(sp.driver, f"Result_Search_{i}")
