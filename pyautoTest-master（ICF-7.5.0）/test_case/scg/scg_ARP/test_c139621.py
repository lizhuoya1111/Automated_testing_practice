import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139621"

def test_c139621(browser):

	try:
		login_web(browser, url=dev1)
		add_ipmac_list(browser, ipadd="192.165.12.3", inteface=interface_name_3, mac="02:11:31:f8:52:13",
						   host_name="aaa3")
		set_bandinglist_to_static_arp(browser, index_list="all")
		time.sleep(2)
		loginfo1 = get_log_info(browser, log_type=管理日志)
		del_static_arp(browser, index_list="all")
		del_bindinglist(browser, index_list="all")

		try:
			assert "成功" in loginfo1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1

		del_bindinglist(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])