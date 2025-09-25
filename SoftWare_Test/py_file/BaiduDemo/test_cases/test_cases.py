import pytest  # pytest 测试框架
import allure  # allure 报告
import logging  # logging 日志模块
from selenium.webdriver.remote.webdriver import WebDriver  # WebDriver 类型注解
from page_object.search_page import SearchPage  # 搜索页对象
from page_object.open_page import OpenPage  # 打开页面对象
from page_object.scroll_page import ScrollPage  # 滚动页面对象
from page_object.flip_page import FlipPage  # 翻页对象
from page_object.titles_page import TitlesPage  # 获取标题对象

# 配置日志格式和日志等级
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")  # 日志输出格式
logger = logging.getLogger(__name__)  # 获取当前模块的 logger


def screenshot_step(driver: WebDriver, name: str):
    """
    直接截图并附加到 Allure，不再重复标题
    """
    logger.info("截图操作：%s", name)  # 日志记录截图
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)  # 直接附加截图


@pytest.fixture(scope="module")
def pages(driver, test_data):  # 模块级 fixture，提供页面对象和测试数据
    """
    功能：实例化所有页面对象，并返回测试数据
    返回：
        dict: 包含搜索页、打开页、滚动页、翻页页对象和 yaml 测试数据
    """
    logger.info("实例化页面对象")  # 日志记录页面对象初始化
    return {
        "search": SearchPage(driver),  # 搜索页对象
        "open": OpenPage(driver),  # 打开页面对象
        "scroll": ScrollPage(driver),  # 滚动页面对象
        "flip": FlipPage(driver),  # 翻页对象
        "titles": TitlesPage(driver),  # 翻页对象
        "data": test_data,  # 测试数据
    }


@allure.feature("打开页面")  # Allure 功能模块标记
def test_open(pages):
    """
    功能：测试打开百度首页
    步骤：
        1. 打开页面
        2. 截图并附加到 Allure
    """
    op = pages["open"]  # 获取打开页面对象
    logger.info("开始打开百度首页")  # 日志记录开始操作
    op.openurl()  # 执行打开首页操作
    logger.info("已打开百度首页，准备截图")  # 日志记录截图前
    screenshot_step(op.driver, "打开百度官网")  # 截图并附加到 Allure
    logger.info("百度首页打开并截图完成")  # 日志记录完成


@allure.feature("搜索功能")  # Allure 功能模块标记
@allure.story("循环搜索关键词")  # Allure 用户故事标记
def test_search(pages):
    """
    功能：循环搜索关键词并翻页截图
    步骤：
        1. 遍历测试数据中的搜索关键词
        2. 执行搜索
        3. 每页滚动并截图页首和页尾
        4. 翻页继续
    """
    sp, scp, fp, tp = pages["search"], pages["scroll"], pages["flip"], pages['titles']  # 获取页面对象
    text_list = pages["data"].get("text_list", [])  # 获取搜索关键词列表，默认为空
    flip_num = 5  # 设置翻页次数
    logger.info("开始搜索关键词，共 %d 个", len(text_list))  # 日志记录关键词数量

    for idx, word in enumerate(text_list, start=1):
        keyword = word["content"]
        logger.info("第 %d 次搜索: %s", idx, keyword)  # 日志记录
        sp.search_(keyword)  # 点击搜索按钮
        logger.info("已执行搜索: %s", keyword)  # 日志记录搜索完成

        for page in range(1, flip_num + 1):
            tp.titles_(page)  # 打印标题
            logger.info("第 %d 页操作开始: %s", page, keyword)  # 日志记录页数
            screenshot_step(sp.driver, f"{keyword}-第{page}页-页首")  # 截图页首
            scp.scroll_()  # 页面滚动
            logger.info("已滚动页面: %s-第%d页", keyword, page)  # 日志记录滚动完成
            screenshot_step(sp.driver, f"{keyword}-第{page}页-页尾")  # 截图页尾
            fp.flip_(page + 1)  # 翻页
            logger.info("已翻页到第 %d 页", page + 1)  # 日志记录翻页完成

    logger.info("搜索关键词循环完成")  # 日志记录所有搜索完成
