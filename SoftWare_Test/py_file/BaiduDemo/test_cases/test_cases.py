"""
    测试用例层(test_cases)：用于实现完整的搜索与抓取流程
"""
import pytest
import allure
import yaml
import logging
from base_page.driver_page import driver_
from page_object.search_page import SearchPage
from page_object.open_page import OpenPage

# 配置日志输出格式和等级
logging.basicConfig(  # 配置logging模块的基本设置
    level=logging.INFO,  # 设置日志级别为INFO，表示只输出INFO及以上级别的日志（INFO、WARNING、ERROR、CRITICAL）
    format="%(asctime)s - %(levelname)s - %(message)s"  # 设置日志输出格式：时间 - 日志级别 - 日志消息
)
logger = logging.getLogger(__name__)  # 获取一个以当前模块名命名的日志记录器logger，便于在不同模块中区分日志来源


def attach_screenshot(driver, name: str):  # 定义一个函数，用于截图并附加到Allure报告，参数driver为浏览器驱动对象，name为截图名称
    allure.attach(  # 调用allure的attach方法，用于将截图添加到Allure测试报告中
        driver.get_screenshot_as_png(),  # 使用driver获取当前页面的截图（PNG格式二进制数据）
        name=name,  # 指定截图的名称，在Allure报告中会显示
        attachment_type=allure.attachment_type.PNG  # 指定附件类型为PNG图片
    )
    logger.info(f"已截图并附加到Allure报告：{name}")  # 记录日志，提示截图操作已完成并附加到报告


@pytest.fixture(scope="module")
def setup():
    """
    初始化测试环境：
    - 读取测试数据
    - 初始化浏览器驱动
    - 实例化页面对象
    """
    logger.info("开始加载测试数据...")
    with open(
            r"D:\Tianyi_Cloud\learn\Py_ProJect\SoftWare_Test\py_file\BaiduDemo\test_data\order.yaml",
            "r",
            encoding="utf-8"
    ) as file:
        data = yaml.safe_load(file)
    logger.info("测试数据加载完成")

    logger.info("初始化浏览器驱动...")
    driver = driver_()
    sp, op = SearchPage(driver), OpenPage(driver)
    logger.info("页面对象实例化完成")

    yield sp, op, data

    logger.info("测试结束，关闭浏览器...")
    driver.quit()


@allure.feature("打开页面")
def test_open(setup):
    """
    测试打开百度首页
    """
    sp, op, data = setup
    logger.info("执行 test_open：打开百度首页")
    op.openurl()
    logger.info("首页打开完成")


@allure.feature("搜索功能")
@allure.story("循环搜索关键词")
def test_search(setup):
    """
    测试页面搜索功能：
    1. 搜索结果页循环输入剩余内容
    """
    sp, op, data = setup
    text_list = data.get("text_list", [])

    # 第一步：循环搜索剩余关键词
    for i, word in enumerate(text_list):
        logger.info(f"结果页第 {i} 次搜索：{word['content']}")
        sp.search_(word["content"])
        attach_screenshot(sp.driver, f"搜索结果_第{i}次_搜索：{word['content']}")
