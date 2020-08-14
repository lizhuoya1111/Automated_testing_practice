import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *

test_id = 142563
def test_c142563(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("object zone zone_jia_1")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_4+".22")
		a.execute("exit")
		a.execute("object network address add_jia_1")
		a.execute("exit")
		a.execute("object network address-group add_gro_jia_1")
		a.execute("exit")
		a.execute("obje service ser_jia_1 tcp src-port 80 65535 dst-port 80 65535 timeout 23")
		a.execute("maplist map_jia_1")
		a.execute("exit")
		a.close()
		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="no",
				 src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
				 des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist='no', save='yes', cancel='no')
		# 编辑网桥接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="br_0",
					 edit_des_inter_zone="yes", des_inter_zone="br_0", save="yes")
		# 编辑对象接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone="Z:zone_jia_1",
					 edit_des_inter_zone="yes", des_inter_zone="Z:zone_jia_1", save="yes")
		# 编辑物理接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone=interface_name_3,
					 edit_des_inter_zone="yes", des_inter_zone=interface_name_5, save="yes")
		# 编辑子接口
		edit_snat_byname(browser, name="snat_jia_1", edit_src_inter_zone="yes", src_inter_zone=interface_name_4+".22",
					 edit_des_inter_zone="yes", des_inter_zone=interface_name_4+".22", save="yes")
		# 编辑源地址和目的地址，掩码
		edit_snat_byname(browser, name="snat_jia_1", other_match_switch="yes", src_ipadd_switch="自定义",
					 srcip_custom="192.165.12.0", srcmask_custom="24", des_ipadd_switch="自定义",
					 desip_custom="192.166.12.0", desmask_custom="24",  save="yes")
		# 编辑预定义的地址对象
		edit_snat_byname(browser, name="snat_jia_1", other_match_switch="yes",  src_ipadd_switch="预定义",
						 srcaddress_predefine="A:add_jia_1",
						 des_ipadd_switch="预定义", desaddress_predefine="A:add_jia_1", save="yes")
		# 编辑预定义的地址组对象
		edit_snat_byname(browser, name="snat_jia_1", other_match_switch="yes", src_ipadd_switch="预定义",
						 srcaddress_predefine="G:add_gro_jia_1",
					 des_ipadd_switch="预定义", desaddress_predefine="G:add_gro_jia_1", save="yes")
		# 编辑预定义服务对象
		edit_snat_byname(browser, name="snat_jia_1", other_match_switch="yes", server="P:ICMP",  save="yes")
		# 编辑自定义服务对象
		edit_snat_byname(browser, name="snat_jia_1", other_match_switch="yes", server="C:ser_jia_1", save="yes")
		# 编辑其它动作，不映射
		edit_snat_byname(browser, name="snat_jia_1", other_action_nomap="no", other_action_maplist="yes", save="yes")
		# 编辑其它动作，映射
		edit_snat_byname(browser, name="snat_jia_1", other_action_maplist="map_jia_1", save="yes")
		# 编辑描述
		edit_snat_byname(browser, name="snat_jia_1", edit_desc="yes", desc="zxcvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhg"
						"fdsaqwertyuiopxcvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhgfdsaqwertyuiopl"
						"cvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhgfdsaqwertyuiopxcvbnmlkjhgfdszz"
						"wertyuiopxcvbnmlkjhgfdsaqwertyuiop01234", save="yes")
		loginfo1 = get_log(browser, 管理日志)

		del_snat_byname(browser, name="snat_jia_1")
		loginfo2 = get_log(browser, 管理日志)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no object zone zone_jia_1")
		a.execute("no interface v "+interface_name_4+".22")
		a.execute("no object network address add_jia_1")
		a.execute("no obj network address-group add_gro_jia_1")
		a.execute("no obj service ser_jia_1 ")
		a.execute("no maplist map_jia_1")
		a.execute("exit")
		a.close()

		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
