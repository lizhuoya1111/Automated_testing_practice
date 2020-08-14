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

test_id = 142791
def test_c142791(browser):
	try:
		login_web(browser, url=dev1)
		add_email_alarm_jyl(browser, enable="yes", email_name="email_alert_jia_1", email_add="jyl@baomutech.com",
							cc_email="yes", cc_email_add="m18822678505@163.com", format="syslog", project="yes",
							project_content="300", disk_full="yes", save="yes")
		edit_email_alarm_jyl(browser, email_alert="email_alert_jia_1", email_add="jia@baomutech.com",
							 cc_email_add="s18822678505@163.com", save="yes")
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		delete_email_alarm_server_jyl(browser, email_alarm="email_alert_jia_1")
		try:
			assert "配置 [EMAIL ALERT]对象成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置 [EMAIL ALERT]对象成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
