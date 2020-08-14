import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
test_id = 8888888
# 批量添加静态路由

def test_c8888888(browser):
	for x in range(1, 200):
		a = Shell_SSH()
		a.connect("10.2.2.73")
		a.execute("en")
		a.execute("conf t")
		for x in range(1, 200):
			a.execute("ip route 192.130."+str(x)+".0/24 gateway 192.166.12.1")
		time.sleep(1)


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
