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
from page_object.scroll_page import ScrollPage
from page_object.flip_page import FlipPage

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


@pytest.fixture(scope="module")  # 使用pytest的fixture装饰器，设置作用域为module级别（整个测试模块只执行一次）
def setup():
    """
    初始化测试环境：
    - 读取测试数据
    - 初始化浏览器驱动
    - 实例化页面对象
    """
    logger.info("开始加载测试数据...")  # 记录日志：开始加载测试数据
    with open(  # 使用with语句安全地打开文件
            r"D:\Tianyi_Cloud\learn\Py_ProJect\SoftWare_Test\py_file\BaiduDemo\test_data\order.yaml",  # yaml测试数据文件路径
            "r",  # 以只读模式打开
            encoding="utf-8"  # 使用UTF-8编码
    ) as file:
        data = yaml.safe_load(file)  # 使用yaml安全加载文件内容到data变量
    logger.info("测试数据加载完成")  # 记录日志：测试数据加载完成

    logger.info("初始化浏览器驱动...")  # 记录日志：开始初始化浏览器驱动
    driver = driver_()  # 调用driver_函数获取浏览器驱动实例
    sp, op, scp, fp = SearchPage(driver), OpenPage(driver), ScrollPage(driver), FlipPage(driver)  # 实例化搜索页面和打开页面对象
    logger.info("页面对象实例化完成")  # 记录日志：页面对象实例化完成

    yield sp, op, scp, fp, data  # 使用yield返回fixture提供的测试资源（页面对象和测试数据）

    logger.info("测试结束，关闭浏览器...")  # 记录日志：测试结束，开始关闭浏览器
    driver.quit()  # 退出浏览器驱动


@allure.feature("打开页面")  # 使用allure标记测试用例所属的功能模块为"打开页面"
def test_open(setup):
    """
    测试打开百度首页
    """
    sp, op, scp, fp, data = setup  # 从setup fixture中获取页面对象和测试数据
    logger.info("执行 test_open：打开百度首页")  # 记录日志：开始执行打开首页测试
    op.openurl()  # 调用OpenPage对象的openurl方法打开百度首页
    attach_screenshot(op.driver, f"打开百度官网")  # 调用截图函数，将当前页面截图并附加到Allure报告
    logger.info("首页打开完成")  # 记录日志：首页打开操作完成


@allure.feature("搜索功能")  # 使用allure标记测试用例所属的功能模块为"搜索功能"
@allure.story("循环搜索关键词")  # 使用allure标记测试用例的用户故事为"循环搜索关键词"
def test_search(setup):
    """
    测试页面搜索功能：
        1. 搜索结果页循环输入剩余内容
    """
    sp, op, scp, fp, data = setup  # 从setup fixture中获取页面对象和测试数据
    text_list = data.get("text_list", [])  # 从测试数据中获取搜索关键词列表，默认为空列表
    flip_num = 5  # 翻页次数

    # 循环搜索剩余关键词
    for i, word in enumerate(text_list):  # 遍历关键词列表，i为索引，word为当前关键词字典
        logger.info(f"结果页第 {i + 1} 次搜索：{word['content']}")  # 记录日志：显示当前是第几次搜索及搜索内容

        sp.search_(word["content"])  # 调用SearchPage对象的search_方法执行搜索操作
        for p in range(2, flip_num + 2):
            attach_screenshot(sp.driver, f"搜索结果_第{p - 1}页_搜索：{word['content']}-页首")  # 调用截图函数，将搜索结果页截图并附加到Allure报告
            scp.scroll_()  # 页面滚动
            attach_screenshot(sp.driver, f"搜索结果_第{p - 1}页_搜索：{word['content']}-页尾")  # 调用截图函数，将搜索结果页截图并附加到Allure报告
            fp.flip_(p)  # 翻页位置








