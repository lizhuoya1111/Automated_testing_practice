# coding=utf-8
import pytest
import time
import click

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  -s 指定运行目录或文件，例: -s  ./test_case/ ,  -s  /test_case/test_demo.py
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
3、运行方式：
> python run_tests.py  # 回归模式，生成HTML测试报告 
> python run_tests.py  -mode debug  # debug模式, 不生成报告
'''


@click.command()
@click.option('-mode', default="run", help="输入运行模式：run 或 debug")
def run(mode):
    if mode == "run":
        now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        pytest.main(["-s", "./test_case/scg/scg_SSLVPN",
                     "--html", "./test_report/" + now_time + "SSLVPN" + "_report.html",
                     "--self-contained-html",
                     "--reruns", "1"])
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Zone",
        #              "--html", "./test_report/" + now_time + "Zone" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_SYS_Seting",
        #              "--html", "./test_report/" + now_time + "SYS_Seting" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_OSPF",
        #              "--html", "./test_report/" + now_time + "OSPF" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Acl",
        #              "--html", "./test_report/" + now_time + "Acl" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Administrator",
        #              "--html", "./test_report/" + now_time + "Administrator" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_AntiDos",
        #              "--html", "./test_report/" + now_time + "AntiDos" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_ARP",
        #              "--html", "./test_report/" + now_time + "ARP" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Bridge-Interface",
        #              "--html", "./test_report/" + now_time + "Bridge-Interface" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_DCHP_Server",
        #              "--html", "./test_report/" + now_time + "DCHP_Server" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Default_Hole",
        #              "--html", "./test_report/" + now_time + "Default_Hole" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_DHCP_Client",
        #              "--html", "./test_report/" + now_time + "DHCP_Client" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_LOG",
        #              "--html", "./test_report/" + now_time + "LOG" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # # # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Machine-Learning",
        #              "--html", "./test_report/" + now_time + "Machine-Learning" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Nat_modify",
        #              "--html", "./test_report/" + now_time + "Nat_modify" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_obj_shell_2nd",
        #              "--html", "./test_report/" + now_time + "obj_shell_2nd" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_physical_interface",
        #              "--html", "./test_report/" + now_time + "physical_interface" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Route",
        #              "--html", "./test_report/" + now_time + "Route" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Security_Event",
        #              "--html", "./test_report/" + now_time + "Security_Event" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Sub-interface",
        #              "--html", "./test_report/" + now_time + "Sub-interface" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_Timeout_setting",
        #              "--html", "./test_report/" + now_time + "Timeout_setting" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_UI",
        #              "--html", "./test_report/" + now_time + "UI" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])
        # #
        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_VPN",
        #              "--html", "./test_report/" + now_time + "VPN" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])

        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # pytest.main(["-s", "./test_case/scg/scg_test",
        #              "--html", "./test_report/" + now_time + "VPN" + "_report.html",
        #              "--self-contained-html",
        #              "--reruns", "1"])

    elif mode == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", "-s", "./test_case"])
        print("运行结束！！")


if __name__ == '__main__':
    run()
