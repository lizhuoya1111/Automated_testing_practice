import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144056"


def test_c144056(browser):
	try:
		login_web(browser, url=dev1)
		# 删除初始配置，将#5口修改为路由口，并配地址
		del_br_addr(browser, br_name="br_0", ipadd="21.1.1.1")
		transparent_interface_change_physics_interface_lzy(browser, intefacex=interface_name_5)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_5, ip='21.1.1.1', mask='24')
		# 给PC2 添加路由
		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
		#   ssh_pc3 = Shell_SSH()
		#   ssh_pc3.connect(hostip="10.1.1.212", name="root", passwd="root", po=22)
		#   ssh_pc3.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')
		# SNAT开启
		add_snat(browser, name="snat_jia_2", desc="", src_inter_zone=interface_name_4, des_inter_zone=interface_name_5,
		         other_match_switch="no",
		         server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
		         other_action_nomap='no', other_action_maplist="no", save='yes', cancel='no')

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(9)
		pc2topc3_ftp_info = ssh_pc2.output()
		# ssh_pc2.execute('exit')
		# print(pc2topc3_ftp_info)
		# print("------------------------------------------------------------------")
		ssh_pc2.close()

		try:
			assert "230 Login successful." in pc2topc3_ftp_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "230 Login successful." in pc2topc3_ftp_info

		delete_physical_interface_ip_jyl(browser, interface=interface_name_5, ip="21.1.1.1")
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_5)
		bridge_ip_add(browser, bridge_interface="br_0", address_mode="manual", ip="21.1.1.1", mask="24")
		# switch_physical_interface_snat(browser, interface=interface_name_5, snat="close")
		del_snat_byname(browser, name="snat_jia_2")
		# ssh_pc2.execute('exit')
		ssh_pc2_4 = Shell_SSH()
		ssh_pc2_4.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2_4.execute('route del -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc2_4.close()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1, switch="重启")
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
