import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def import *


test_id = 142761
def test_c142761(browser):
	try:
		login_web(browser, url=dev1)
		add_ftp_server_jyl(browser, status="enable", server_name="ftp_jia_1", ftp_server_name="192.165.12.3",
						   path="jia", user="jia_admin_1", password="123456", format="syslog", time="yes", time_num="200",
						    cancel="yes")
		webinfo = browser.find_element_by_xpath('//*[@id="rules_count"]').text.rstrip()
		try:
			assert "1" == webinfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "1" == webinfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
