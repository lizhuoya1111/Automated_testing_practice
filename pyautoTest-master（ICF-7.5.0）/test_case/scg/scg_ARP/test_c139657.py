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

test_id = "139657"

def test_c139657(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1 count 10")
		a.execute("exit")
		set_dynamic_arp_to_static_arp_jyl(browser, dynamic_arp_ip="13.1.1.3")
		del_bindinglist(browser, index_list="all")
		set_arp_static_to_binding(browser, ipadd="13.1.1.3")
		loginfo1 = get_log_info(browser, log_type=管理日志)
		delete_static_arp_jyl(browser, static_arp_ip="13.1.1.3")

		try:
			assert "成功添加IP MAC绑定表项" in loginfo1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功添加IP MAC绑定表项" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])