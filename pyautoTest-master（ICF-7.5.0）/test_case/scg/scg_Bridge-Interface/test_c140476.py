import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140476
def test_c140476(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_1")
		a.execute("exit")
		a.execute("interface bridge br_2")
		a.execute("exit")
		a.execute("interface bridge br_3")
		a.execute("exit")
		a.execute("interface bridge br_4")
		a.execute("exit")
		a.execute("interface bridge br_5")
		a.execute("exit")
		a.execute("interface bridge br_6")
		a.execute("exit")
		a.execute("interface bridge br_7")
		a.execute("exit")
		a.execute("interface bridge br_8")
		a.execute("exit")
		a.execute("interface bridge br_9")
		a.execute("exit")
		a.execute("interface bridge br_10")
		a.execute("exit")
		delete_bridge(browser)
		loginfo = get_log(browser, 管理日志)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no interface bridge br_2")
		a.execute("no interface bridge br_3")
		a.execute("no interface bridge br_4")
		a.execute("no interface bridge br_5")
		a.execute("no interface bridge br_6")
		a.execute("no interface bridge br_7")
		a.execute("no interface bridge br_8")
		a.execute("no interface bridge br_9")
		a.execute("no interface bridge br_10")
		a.execute("exit")

		try:
			assert "删除" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "删除" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
