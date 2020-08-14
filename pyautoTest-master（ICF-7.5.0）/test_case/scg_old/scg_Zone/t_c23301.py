import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_nat import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "23301"


def test_c23301(browser):

	try:
		login_web(browser, url='10.2.2.81')
		delete_physical_interface_ip_wxw(browser, "ge0/4", "20.1.1.1")
		add_vlan_inte(browser, physicl_interface="ge0/4", vlan_id="22")
		add_vlan_inte_add(browser, "ge0/4.22", "20.1.1.1", "255.255.255.0")
		add_obj_zone(browser, "zone1", "d", ["ge0/4.22"])

		# 进入命令行 设备ge0/4为access模式
		scg = Shell_SSH()
		scg.connect("10.2.2.81")
		scg.execute("en")
		scg.execute("conf t")
		scg.execute("inte gigabitethernet ge0/4")
		scg.execute("switchmode  access")
		scg.execute("exit")
		scg.execute("exit")


		to_ssh = Shell_SSH()
		to_ssh.connect("10.1.1.202", "root", "root")
		to_ssh.execute("route add -net 12.1.1.0/24 gw 20.1.1.1")
		to_ssh.execute("ping 12.1.1.2 -c 2")
		time.sleep(10)
		ssh_info = to_ssh.output()
		print(ssh_info)
		if "100% packet loss" in ssh_info:
			add_snat(browser, name="test1", src_inter_zone="Z:zone1", des_inter_zone="ge0/2")
			to_ssh.connect("10.1.1.202", "root", "root")
			to_ssh.execute("ping 12.1.1.2 -c 3")
			time.sleep(2)
			ssh_info1 = to_ssh.output()
			print(ssh_info1)

			try:
				assert "ttl" in str(ssh_info1)
				rail_pass(test_run_id, test_id)

			except Exception as err1:
				print(err1)
				rail_fail(test_run_id, test_id)
				assert "ttl" in str(ssh_info1)

		else:
			rail_fail(test_run_id, test_id)
			reload()
			assert False

		del_snat_byname(browser, "test1")
		del_obj_zone_byname(browser, "zone1")
		del_vlan_inte_all(browser)
		add_physical_interface_ip_wxw(browser, interface="ge0/4", ip="20.1.1.1", mask="24")
		to_ssh.execute("route del -net 12.1.1.0/24 gw 20.1.1.1")
		# dhcp_server_edit_or_delete(browser, fuction="delall")
		# login_web(browser, url='10.2.2.84')
		# change_addrmod_physical_inte(browser, "ge0/3", "静态")
		# add_net_ineterface(browser, "24.1.1.4", "255.255.255.0", "ge0/3")

	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
