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

test_id = 142605
def test_c142605(browser):
	try:
		login_web(browser, url=dev1)
		# 在10.2.2.81上配置地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.execute("interface bridge br_1")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface bridge br_2")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.close()

		# 网桥接口，添加成员
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)
		bridge_edit_interface_jyl(browser, bridge_interface="br_2", interface=interface_name_3)

		# 在10.2.2.82上配置去往83的路由，以及配置10.2.2.82的地址
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone="br_1", des_inter_zone="br_2",
				 single_ip="13.1.1.1", save='yes', cancel='no')

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(7)
		result1 = a.output()
		a.close()
		print(result1)

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no interface bridge br_2")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("work-mode route")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("work-mode route")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_2+".22")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.close()

		# 编辑物理接口和子接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone=interface_name_2,
						 single_ip="13.1.1.1", edit_des_inter_zone="yes", des_inter_zone=interface_name_2+".22",
						 save="yes")

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result2 = a.output()
		a.close()
		print(result2)

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_2+".22")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_2+".22")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.close()

		# 编辑物理接口和子接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone=interface_name_2+".22",
					 edit_des_inter_zone="yes", des_inter_zone=interface_name_3,
						 single_ip="13.1.1.1", save="yes")
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result3 = a.output()
		a.close()
		print(result3)

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_2+".22")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("object zone zone_jia_1")
		a.execute("zone-object interface "+interface_name_2)
		a.execute("exit")
		a.execute("object zone zone_jia_2")
		a.execute("zone-object interface "+interface_name_3)
		a.execute("exit")
		a.close()

		# 编辑对象接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:zone_jia_1",
						 single_ip="13.1.1.1", edit_des_inter_zone="yes", des_inter_zone="Z:zone_jia_2",
						 save="yes")

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

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no object zone zone_jia_2")
		a.execute("exit")
		a.close()

		# 编辑对象接口和物理接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:zone_jia_1",
						 single_ip="13.1.1.1", edit_des_inter_zone="yes", des_inter_zone=interface_name_3,
						 save="yes")

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(4)
		result5 = a.output()
		a.close()
		print(result5)

		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:any",
					 edit_des_inter_zone="yes", des_inter_zone="Z:any", save="yes")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("exit")
		a.execute("interface bridge br_1")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3)

		# 编辑对象接口和物理接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:zone_jia_1",
					 edit_des_inter_zone="yes", des_inter_zone="br_1",  single_ip="13.1.1.1", save="yes")

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(6)
		result6 = a.output()
		a.close()
		print(result6)

		del_snat_byname(browser, name="snat_jia_1")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no maplist map_jia_1")
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
			assert "Destination" in result2
			assert "ms" in result3
			assert "ms" in result4
			assert "ms" in result5
			assert "ms" in result6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "Destination" in result2
			assert "ms" in result3
			assert "ms" in result4
			assert "ms" in result5
			assert "ms" in result6
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
