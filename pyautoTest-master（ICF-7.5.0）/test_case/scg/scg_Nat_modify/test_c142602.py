import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_nat_modify import *
from page_obj.common.rail import *
from page_obj.scg.scg_def import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *

test_id = 142602
def test_c142602(browser):
	try:
		login_web(browser, url=dev1)
		# 在10.2.2.81上配置地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("maplist map_jia_1")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 192.165.12.1 24")
		a.execute("exit")
		a.close()

		# 在10.2.2.82上配置去往83的路由，以及配置10.2.2.82的地址
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 192.165.12.2 24")
		a.execute("exit")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", oriipfrom="12.1.1.0", oriipto="12.1.1.255", one_to_one_mapping="yes",
					 transipfrom="13.1.1.3")

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", oriipfrom="192.165.12.0", oriipto="192.165.12.255", one_to_one_mapping="yes",
					 transipfrom="13.1.1.3")

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone=interface_name_2, des_inter_zone=interface_name_3,
				 other_match_switch="no",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes', cancel='no')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result1 = a.output()
		a.close()
		print(result1)

		del_snat_byname(browser, name="snat_jia_1")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no maplist map_jia_1")
		a.execute("conf t")
		a.execute("no maplist map_jia_1")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 192.165.12.1")
		a.close()
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 192.165.12.2")
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
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
