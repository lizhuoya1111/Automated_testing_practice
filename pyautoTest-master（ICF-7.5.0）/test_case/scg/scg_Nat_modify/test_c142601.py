
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_nat_modify import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *
# 没有完成，设涉及到多条snat会话，目前无法实现
from page_obj.scg.scg_def import *
test_id = 142601
def test_c142601(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("maplist map_jia_1")
		a.execute("exit")
		a.execute("maplist map_jia_2")
		a.execute("exit")
		a.execute("maplist map_jia_3")
		a.execute("exit")
		a.close()

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone=interface_name_2, des_inter_zone=interface_name_3,
				 other_match_switch="no",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist="map_jia_1", save='yes', cancel='no')

		add_snat(browser, name="snat_jia_2", desc="", src_inter_zone=interface_name_2, des_inter_zone=interface_name_3,
				 other_match_switch="no",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist="map_jia_2", save='yes', cancel='no')

		add_snat(browser, name="snat_jia_3", desc="", src_inter_zone=interface_name_2, des_inter_zone=interface_name_3,
				 other_match_switch="no",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist="map_jia_3", save='yes', cancel='no')

		edit_snat_byname(browser, name="snat_jia_1", other_action_maplist="map_jia_2", save="yes")





		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", oriipfrom="12.1.1.0", oriipto="12.1.1.255", one_to_one_mapping="yes",
					 transipfrom="13.1.1.3")
		loginfo1 = get_log(browser, 管理日志)

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", delete_ip="yes", oriipfrom="12.1.1.50", oriipto="12.1.1.200",
					 one_to_one_mapping="yes", transipfrom="13.1.1.200")
		loginfo2 = get_log(browser, 管理日志)

		# 编辑maplist
		edit_maplist(browser, name="map_jia_1", delete_ip="yes", oriipfrom="10.0.0.0", oriipto="10.0.2.0",
					 one_to_one_mapping="yes", transipfrom="192.168.0.0")
		loginfo3 = get_log(browser, 管理日志)

		del_snat_byname(browser, name="snat_jia_1")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no maplist map_jia_1")
		a.execute("no maplist map_jia_2")
		a.execute("no maplist map_jia_3")


		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
