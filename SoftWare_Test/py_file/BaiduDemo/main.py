# -*- coding: utf-8 -*-
# @Time		: 2025/8/20 10:48
# @Author	: Jerry
# @File		: main.py
# @Software	: PyCharm

import pytest  # 导入 pytest 模块，用于运行测试并生成报告
import os  # 导入 os 模块，用于执行操作系统命令

if __name__ == '__main__':  # 检查是否直接运行当前脚本
    # 运行 pytest，指定将测试结果保存到 ./temps/result 目录中
    pytest.main(['--alluredir', './temps/allure-report'])  # '--alluredir' 是 pytest 的选项，用于生成可供 Allure 展示的测试报告

    # 使用操作系统命令 'allure serve' 来启动 Allure 本地服务，并在浏览器中展示生成的测试报告
    os.system("allure serve ./temps/allure")  # 'allure serve' 会读取指定的目录，并生成可视化的测试报告


"""
    在 cmd 中文件夹内执行完整的测试代码可实现一键测试、保存、展示三个功能
    pytest && allure generate -c -o temps/allure-report && allure serve ./temps/allure

# 2 连接拼接 https://www.baidu.com
//*[@id="page"]/div/a[1]/@href
# 2 跳转书签名称
//*[@id="page"]/div/a[1]/span/text()


# 3 连接拼接
//*[@id="page"]/div/a[2]/@href
# 3 跳转书签名称
//*[@id="page"]/div/a[2]/span/text()


# 4 连接拼接
//*[@id="page"]/div/a[3]/@href
# 4 跳转书签名称
//*[@id="page"]/div/a[3]/span/text()


完成翻页功能嵌入test_cases代码中
"""