import pytest  # pytest 测试框架，用于组织和执行测试用例
import allure  # allure 报告，用于生成测试报告并支持截图、步骤等
import logging  # logging 日志模块，用于记录测试执行信息
from selenium.webdriver.remote.webdriver import WebDriver  # WebDriver 类型注解，用于类型提示
from page_object.search_page import SearchPage  # 搜索页对象，封装搜索相关操作
from page_object.open_page import OpenPage  # 打开页面对象，封装打开网页操作
from page_object.scroll_page import ScrollPage  # 滚动页面对象，封装页面滚动操作
from page_object.flip_page import FlipPage  # 翻页对象，封装翻页操作
from page_object.titles_page import TitlesPage  # 获取标题对象，封装获取页面标题操作

# 配置日志格式和日志等级
logging.basicConfig(
    level=logging.INFO,  # 设置日志输出等级为 INFO，输出 info 及以上级别日志
    format="%(asctime)s - %(levelname)s - %(message)s"  # 日志输出格式，包含时间、日志级别和消息
)
logger = logging.getLogger(__name__)  # 获取当前模块的 logger，用于记录模块内日志


def screenshot_step(driver: WebDriver, name: str):
    """
    功能：直接截图并附加到 Allure 测试报告，不再重复标题
    参数：
        driver (WebDriver): 当前页面的浏览器驱动
        name (str): 截图名称，显示在 Allure 报告中
    """
    logger.info("截图操作：%s", name)  # 日志记录截图操作
    # 获取当前页面截图（PNG 格式）并附加到 Allure 报告
    allure.attach(
        driver.get_screenshot_as_png(),  # 获取截图数据
        name=name,  # 截图名称
        attachment_type=allure.attachment_type.PNG  # 指定附件类型为 PNG
    )


@pytest.fixture(scope="module")
def pages(driver, test_data):
    """
    功能：模块级 fixture，实例化所有页面对象，并返回测试数据
    参数：
        driver: selenium WebDriver 实例
        test_data: YAML 或其他格式的测试数据
    返回：
        dict: 包含搜索页、打开页、滚动页、翻页页对象和测试数据
    """
    logger.info("实例化页面对象")  # 日志记录页面对象初始化
    return {
        "search": SearchPage(driver),  # 搜索页对象，用于执行搜索操作
        "open": OpenPage(driver),  # 打开页面对象，用于打开指定网址
        "scroll": ScrollPage(driver),  # 滚动页面对象，用于滚动页面
        "flip": FlipPage(driver),  # 翻页对象，用于执行翻页操作
        "titles": TitlesPage(driver),  # 标题对象，用于获取和打印页面标题
        "data": test_data,  # 测试数据，从 fixture 或 YAML 文件中获取
    }


@allure.feature("打开页面")  # Allure 功能模块标记，用于报告分类
def test_open(pages):
    """
    功能：测试打开百度首页
    步骤：
        1. 打开百度首页
        2. 截图并附加到 Allure 报告
    """
    op = pages["open"]  # 获取打开页面对象
    logger.info("开始打开百度首页")  # 日志记录操作开始
    op.openurl()  # 执行打开首页操作
    logger.info("已打开百度首页，准备截图")  # 日志记录截图前提示
    screenshot_step(op.driver, "打开百度官网")  # 调用截图函数，并附加到 Allure
    logger.info("百度首页打开并截图完成")  # 日志记录操作完成


@allure.feature("搜索功能")  # Allure 功能模块标记
@allure.story("循环搜索关键词")  # Allure 用户故事标记
def test_search(pages):
    """
    功能：循环搜索关键词并翻页截图
    步骤：
        1. 遍历测试数据中的搜索关键词
        2. 执行搜索操作
        3. 每页滚动并截图页首和页尾
        4. 翻页继续搜索下一个关键词
    """
    # 获取页面对象，方便后续调用各类操作
    sp, scp, fp, tp = pages["search"], pages["scroll"], pages["flip"], pages['titles']
    text_list = pages["data"].get("text_list", [])  # 获取搜索关键词列表，默认为空列表
    flip_num = pages["data"].get("flip_num")  # 从配置文件读取翻页次数
    logger.info("开始搜索关键词，共 %d 个", len(text_list))  # 日志记录关键词数量

    for idx, word in enumerate(text_list, start=1):
        keyword = word["content"]  # 获取当前搜索关键词
        logger.info("第 %d 次搜索: %s", idx, keyword)  # 日志记录当前搜索序号和关键词
        sp.search_(keyword)  # 执行搜索操作
        logger.info("已执行搜索: %s", keyword)  # 日志记录搜索完成

        for page in range(1, flip_num + 1):
            tp.titles_(page)  # 获取并打印当前页标题
            logger.info("第 %d 页操作开始: %s", page, keyword)  # 日志记录当前页操作开始
            screenshot_step(sp.driver, f"{keyword}-第{page}页-页首")  # 截图页首
            scp.scroll_()  # 页面滚动到底部
            logger.info("已滚动页面: %s-第%d页", keyword, page)  # 日志记录滚动完成
            screenshot_step(sp.driver, f"{keyword}-第{page}页-页尾")  # 截图页尾
            fp.flip_(page + 1)  # 执行翻页操作，跳转到下一页
            logger.info("已翻页到第 %d 页", page + 1)  # 日志记录翻页完成

    logger.info("搜索关键词循环完成")  # 日志记录所有搜索操作完成
