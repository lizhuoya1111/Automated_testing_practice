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

test_id = 142623
def test_c142623(browser):
	try:
		login_web(browser, url=dev3)

		add_maplist_wxw(browser, name='maplist_jia_1', desc='', save1='yes', cancel='no',
							oriipfrom='13.1.1.1', oriipto='13.1.1.255',
						transipfrom='34.1.1.10', transipto='34.1.1.50', one_to_one_mapping="no",
							sticky='no', portfrom='1', portto='65535', save2="yes", cance2='no')

		# 添加snat
		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone="Z:any", des_inter_zone="Z:any",
				 other_match_switch="yes", src_ipadd_switch="预定义", srcaddress_predefine="A:any", trans_local_ip="yes",
				 other_action_nomap='no', other_action_maplist="maplist_jia_1", save='yes')

		# 在10.2.2.81上配置去往84的路由
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 34.1.1.4")
		time.sleep(4)
		result1 = a.output()
		a.close()
		print(result1)

		# 删除10.2.2.83snat
		del_snat_byname(browser, name="snat_jia_1")
		# 删除10.2.2.83maplist
		del_maplist_by_name_jyl(browser, name="maplist_jia_1")

		# 在10.2.2.81上删除去往84的路由
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
		a.execute("exit")
		a.close()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False

	try:
		assert "ms" in result1
		rail_pass(test_run_id, test_id)
	except:
		rail_fail(test_run_id, test_id)
		assert "ms" in result1


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
