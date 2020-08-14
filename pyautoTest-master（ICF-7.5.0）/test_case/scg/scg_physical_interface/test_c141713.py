import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141713

def test_c141713(browser):

	try:
		login_web(browser, url=dev3)
		edit_interface_senior_jyl(browser, interface=interface_name_2, negotiation="强制", speed="10", duplex="全双工",
							  force_mtu="1500")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(1)
		result1 = a.output()
		a.close()
		# print(result1)

		get_log(browser, 管理日志)
		edit_interface_senior_jyl(browser, interface=interface_name_2, negotiation="强制", speed="100", duplex="全双工",
							  force_mtu="1500")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(1)
		result2 = a.output()
		a.close()
		# print(result2)

		get_log(browser, 管理日志)
		edit_interface_senior_jyl(browser, interface=interface_name_2, negotiation="强制", speed="1000", duplex="全双工",
							  force_mtu="1500")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(1)
		result3 = a.output()
		a.close()
		# print(result3)

		get_log(browser, 管理日志)
		edit_interface_senior_jyl(browser, interface=interface_name_2, negotiation="强制", speed="100", duplex="半双工",
							  force_mtu="1500")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(3)
		result4 = a.output()
		a.close()
		# print(result4)

		get_log(browser, 管理日志)
		edit_interface_senior_jyl(browser, interface=interface_name_2, negotiation="自动", anto_mtu="1500")
		try:
			assert "ms" in result1
			assert "ms" in result2
			assert "ms" in result3
			assert "ms" in result4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "ms" in result2
			assert "ms" in result3
			assert "ms" in result4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])