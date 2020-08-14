
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
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *

test_id = 142800
def test_c142800(browser):
	try:
		login_web(browser, url=dev1)
		add_email_alarm_jyl(browser, enable="yes", email_name="email_alart_jia_1", email_add="jyl@baomutech.com",
							cc_email="yes", cc_email_add="m18822678505@163.com", format="syslog", project="yes",
							project_content="300", disk_full="yes", admin_event="yes", av_vrius_found="yes",
							server_monitor="yes", save="yes")
		get_info = get_email_alert_all_jyl(browser)
		# print(get_info)
		delete_email_alarm_server_jyl(browser, email_alarm="email_alart_jia_1")

		try:
			assert ['email_alart_jia_1', 'jyl@baomutech.com', 'ITEM', '300', 'enable'] in get_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert ['email_alart_jia_1', 'jyl@baomutech.com', 'ITEM', '300', 'enable'] in get_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
