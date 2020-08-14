import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_nat_modify import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def import *

test_id = 142607
def test_c142607(browser):
	try:
		login_web(browser, url=dev1)
		# 在10.2.2.81上配置地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("maplist map_jia_1")

		# 在10.2.2.82上配置去往83的路由，以及配置10.2.2.82的地址
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", oriipfrom="12.1.1.0", oriipto="12.1.1.255", one_to_one_mapping="yes",
					 transipfrom="13.1.1.3", sticky="yes", portfrom="1", portto="65535")

		add_snat(browser, name="snat_jia_1", other_action_nomap='no', other_action_maplist="map_jia_1", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result1 = a.output()
		a.close()
		print(result1)

		edit_maplist(browser, name="map_jia_1", delete_ip="yes", oriipfrom="12.1.1.0", oriipto="12.1.1.255",
					 transipfrom="13.1.1.1", transipto="13.1.1.255", sticky="yes", portfrom="1", portto="65535")

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 other_action_nomap='no', other_action_maplist="map_jia_1",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result2 = a.output()
		a.close()
		print(result2)

		del_snat_byname(browser, name="snat_jia_1")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no object zone zone_jia_1")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.1 24")
		a.close()

		# 在10.2.2.82上删除去往83的路由，
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		try:
			assert "ms" in result1
			assert "ms" in result2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "ms" in result2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
