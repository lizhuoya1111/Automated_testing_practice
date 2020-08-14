
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

test_id = 142954
def test_c142954(browser):
	try:
		login_web(browser, url=dev1)
		add_log_server_jyl(browser, status="enable", server_name="#@$%^&*", ip="192.165.12.3", port="162",
						   format="syslog", protocol="tcp", charset="UTF-8", save="yes")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info1 = alert.text
		# print(web_info1)
		# 接受告警
		browser.switch_to_alert().accept()

		add_ftp_server_jyl(browser, status="enable", server_name="#@$%^&*", ftp_server_name="192.165.12.8",
						   path="jia", user="user", password="123456", format="syslog", project="yes",
						   project_content="300", save="yes", cancel="")

		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info2 = alert.text
		# print(web_info2)
		# 接受告警
		browser.switch_to_alert().accept()

		add_email_alarm_jyl(browser, enable="yes", email_name="#@$%^&*", email_add="jyl@baomutech.com",
							cc_email="yes", cc_email_add="m18822678505@163.com", format="syslog", project="yes",
							project_content="300", disk_full="yes", admin_event="yes", av_vrius_found="yes",
							server_monitor="yes", save="yes")

		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info3 = alert.text
		# print(web_info3)
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "名称输入错误" in web_info1
			assert "名称输入错误" in web_info2
			assert "名称输入错误" in web_info3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "名称输入错误" in web_info1
			assert "名称输入错误" in web_info2
			assert "名称输入错误" in web_info3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
