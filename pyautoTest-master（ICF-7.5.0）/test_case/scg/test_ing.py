import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

# 验证删除子接口是否挂掉


def test_route_wxw(browser):


	login_web(browser, url=dev1)
	into_fun_old(browser, op1=防火墙, op3=IPv4访问控制列表)
	time.sleep(1)
	into_fun_old(browser, op1=防火墙, op2=display_NAT, op3=目的NAT)
	time.sleep(1)
	into_fun_old(browser, op1=对象, op3=计划任务)
	time.sleep(1)
	into_fun_old(browser, op1=防火墙, op2=display_NAT, op3=源NAT)
	time.sleep(1)
	into_fun_old(browser, op1=日志, op2=display_日志设置, op3=日志格式)
	time.sleep(1)
	print("sssssss")



if __name__ == '__main__':
	pytest.main(["-v", "-s", "ting.py"])