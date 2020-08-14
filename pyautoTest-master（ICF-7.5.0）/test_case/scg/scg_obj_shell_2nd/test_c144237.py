import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_dev import *
from page_obj.common.ssh import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144237"
# nat 9
# 添加一条dnat，源地址、目的地址都引用address group，尝试删除该对象
# obj不能被删除


def test_c144237(browser):

	try:
		login_web(browser, url=dev3)

		# 添加addr
		add_obj_address_wxw(browser, name='obj_add_2371', desc='zhe是yi个描述1', subnetip='13.1.1.1', subnetmask='24')
		add_obj_address_wxw(browser, name='obj_add_2372', desc='zhe是yi个描述1', subnetip='34.1.1.3', subnetmask='24')
		# 添加addr组
		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_2371', desc='zhe是yi个描述1', addr_obj='A:obj_add_2371')
		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_2372', desc='zhe是yi个描述1', addr_obj='A:obj_add_2372')

		# 添加dnat
		add_dnat(browser, name='dnat_237', desc="miaoshu", src_inter_zone="Z:any", src_ipadd_switch="预定义", srcaddress_predefine="G:obj_grp_2371",
				 srcip_custom="", srcmask_custom="", des_ipadd_switch="预定义", desaddress_predefine="G:obj_grp_2372",
				 desip_custom="", desmask_custom="", arp_proxy="no", server='P:any', trans_ip='34.1.1.4', trans_port='no',
				 other_action_nomap='no', other_action_load='no')

		del_obj_grp_wxw(browser, name='obj_grp_2371')
		time.sleep(2)
		alert1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]').text
		# print(alert1)

		del_obj_grp_wxw(browser, name='obj_grp_2372')
		time.sleep(2)
		alert2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]').text
		# print(alert2)


		# 恢复配置
		del_dnat_byname(browser, name='dnat_237')

		del_obj_grp_wxw(browser, name='obj_grp_2371')

		del_obj_grp_wxw(browser, name='obj_grp_2372')

		del_obj_address_wxw(browser, name='obj_add_2371')

		del_obj_address_wxw(browser, name='obj_add_2372')

		try:
			assert "对象正在使用" in alert1
			assert "对象正在使用" in alert2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "对象正在使用" in alert1
			assert "对象正在使用" in alert2


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])