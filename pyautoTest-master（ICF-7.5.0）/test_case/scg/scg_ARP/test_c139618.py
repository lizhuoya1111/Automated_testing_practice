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

test_id = "139618"


def test_c139618(browser):

	try:
		login_web(browser, url=dev1)
		for x in range(1, 5):
			add_ipmac_list(browser, ipadd="192.165.12."+str(x), inteface=interface_name_3, mac="02:11:31:f8:52:1"+str(x),
						   host_name="aaa"+str(x))
		del_bindinglist(browser, index_list=[1])
		loginfo1 = get_log_info(browser, log_type=管理日志)
		del_bindinglist(browser, index_list="all")
		loginfo2 = get_log_info(browser, log_type=管理日志)

		try:
			assert "成功删除" in loginfo1
			assert "成功删除" in loginfo2
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功删除" in loginfo1
			assert "成功删除" in loginfo2

		del_bindinglist(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])