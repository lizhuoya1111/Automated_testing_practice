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
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def import *

test_id = 142616
def test_c142616(browser):
	try:
		login_web(browser, url=dev1)
		# 在10.2.2.81上配置地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("maplist map_jia_1")
		a.close()

		# 在10.2.2.82上配置去往83的路由，以及配置10.2.2.82的地址
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", oriipfrom="12.1.1.0", oriipto="12.1.1.255", sticky="yes",
					 transipfrom="13.1.1.3", transipto="13.1.1.255")

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="预定义", srcaddress_predefine="A:any",
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result1 = a.output()
		a.close()
		print(result1)

		edit_snat_byname(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="自定义", srcip_custom="12.1.1.0", srcmask_custom="24",
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result2 = a.output()
		a.close()
		print(result2)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("object network address add_jia_1")
		a.execute("network-object ip-address 12.1.1.0/24")
		a.execute("network-object ip-address 13.1.1.0/24")
		a.execute("exit")
		a.execute("object network address-group add_gro_jia_1")
		a.execute("group-object address add_jia_1")
		a.execute("exit")
		# a.execute("work-mode route")
		# a.execute("exit")
		# a.execute("interface gigabitethernet "+interface_name_2)
		# a.execute("ip address 12.1.1.1 24")
		# a.execute("exit")
		# a.execute("interface vlan "+interface_name_2+".22")
		# a.execute("ip address 13.1.1.1 24")
		# a.execute("exit")
		a.close()

		edit_snat_byname(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="预定义", srcaddress_predefine="A:add_jia_1",
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result3 = a.output()
		a.close()
		print(result3)

		edit_snat_byname(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="预定义", srcaddress_predefine="G:add_gro_jia_1",
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result4 = a.output()
		a.close()
		print(result4)

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")

		edit_snat_byname(browser, name="snat_jia_1", ip_range="yes",
						 ip_range_start="13.1.1.1", ip_range_end="13.1.1.255", save='yes')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result5 = a.output()
		a.close()
		print(result5)

		add_snat(browser, name="snat_jia_2", save='yes')

		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击移动按钮
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[12]/a[1]/img').click()

		loginfo1 = get_log(browser, 管理日志)

		del_snat_byname(browser, name="snat_jia_1")
		del_snat_byname(browser, name="snat_jia_2")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no object network address add_jia_1")
		a.execute("no object network address add_gro_jia_1")
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
			assert "ms" in result3
			assert "ms" in result4
			assert "ms" in result5
			assert "成功" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "ms" in result2
			assert "ms" in result3
			assert "ms" in result4
			assert "ms" in result5
			assert "成功" in loginfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
