import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.scg.scg_def import *



def test_c14867(browser):

	n = 0
	# while 1:
	for x in range(0, 9999):
		try:
			login_web(browser, url=dev1)
			runtime = get_uptime(browser)
			# print(runtime)
			if "0 min" in runtime or "1 min" in runtime or "2 min" in runtime:
				n += 1
				print(n)
			add_snat(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", des_inter_zone="Z:any",
					 other_match_switch="no",
					 src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
					 des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
					 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
					 other_action_nomap='no', other_action_maplist='no', save='yes', cancel='no')

			del_snat_byname(browser, name="snat_jia_1")

			# add_dnat(browser, name='dnat_235', desc="miaoshu", src_inter_zone="Z:any", src_ipadd_switch="预定义",
			# 		 srcaddress_predefine="A:any",
			# 		 srcip_custom="", srcmask_custom="", des_ipadd_switch="预定义", desaddress_predefine="A:any",
			# 		 desip_custom="", desmask_custom="", arp_proxy="no", server='P:DNP3_UDP', trans_ip='34.1.1.4',
			# 		 trans_port='no',
			# 		 other_action_nomap='no', other_action_load='no')
			#
			# del_dnat_byname(browser, name='dnat_235')
			#
			# add_ipv4_aclgroup_lzy(browser, group_name='lzy')
			# # 添加规则
			# add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3,
			# 						  dest_zone_interface=interface_name_4)
			# del_all_acl_group_lzy(browser)
			# login_web(browser, url=dev4)
			# runtime = get_uptime(browser)
			# # print(runtime)
			# if "0 min" in runtime or "1 min" in runtime or "2 min" in runtime:
			# 	n += 1
			# 	print(n)
			# add_snat_tmp(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", des_inter_zone="Z:any",
			#          other_match_switch="no",
			#          src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
			#          des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
			#          server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
			#          other_action_nomap='no', other_action_maplist='no', save='yes', cancel='no')
			#
			# del_snat_byname_tmp(browser, name="snat_jia_1")






		except:
			print(n)
			pass


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_scg.py"])