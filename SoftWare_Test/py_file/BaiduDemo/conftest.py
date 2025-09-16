import pytest  # pytest 测试框架
import yaml  # 读取 YAML 文件
import logging  # 日志模块
from base_page.driver_page import driver_  # 导入自定义的浏览器驱动生成方法

# 配置日志输出格式和等级
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")  # 设置日志格式
logger = logging.getLogger(__name__)  # 获取当前模块的 logger 实例


@pytest.fixture(scope="session")
def driver():  # 定义 driver fixture，在整个测试会话范围内只执行一次
    """
    功能：
        - 初始化浏览器驱动，提供给测试用例使用
    返回：
        WebDriver 对象
    """
    logger.info("初始化浏览器驱动...")  # 日志记录初始化操作
    driver = driver_()  # 调用 driver_ 函数创建浏览器驱动实例
    yield driver  # 将 driver 提供给测试用例
    logger.info("测试结束，关闭浏览器...")  # 日志记录结束操作
    driver.quit()  # 关闭浏览器驱动，释放资源


@pytest.fixture(scope="session")
def test_data():  # 定义 test_data fixture，在整个测试会话范围内只执行一次
    """
    功能：
        - 加载 YAML 测试数据，提供给测试用例使用
    返回：
        dict: 解析后的测试数据
    """
    data_path = r"D:\Tianyi_Cloud\learn\Py_ProJect\SoftWare_Test\py_file\BaiduDemo\test_data\order.yaml"  # 指定 YAML 文件路径
    logger.info("开始加载测试数据: %s", data_path)  # 日志记录文件路径
    with open(data_path, "r", encoding="utf-8") as file:  # 打开 YAML 文件
        data = yaml.safe_load(file)  # 解析 YAML 内容
    logger.info("测试数据加载完成，共 %d 条", len(data.get("text_list", [])))  # 日志记录加载完成和数量
    return data  # 返回测试数据字典
