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

test_id = 142830
def test_c142830(browser):
	try:
		login_web(browser, url=dev1)
		add_ftp_server_jyl(browser, status="enable", server_name="ftp_jia_1", ftp_server_name="192.165.12.3",
						   path="jia_1", user="jia_admin__1", password="123456", format="syslog",
						   project="yes", project_content="200", save="yes")
		loginfo1 = get_log(browser, 管理日志)
		delete_ftp_server_jyl(browser, ftp_server="ftp_jia_1")
		add_ftp_server_jyl(browser, status="enable", server_name="ftp_jia_2", ftp_server_name="192.165.12.4",
						   path="jia_2", user="jia_admin_2", password="123456", format="csv",
						   project="yes", project_content="200", save="yes")
		loginfo2 = get_log(browser, 管理日志)
		delete_ftp_server_jyl(browser, ftp_server="ftp_jia_2")
		add_ftp_server_jyl(browser, status="enable", server_name="ftp_jia_3", ftp_server_name="192.165.12.5",
						   path="jia_3", user="jia_admin_3", password="123456", format="welf",
						   project="yes", project_content="200", save="yes")
		loginfo3 = get_log(browser, 管理日志)
		delete_ftp_server_jyl(browser, ftp_server="ftp_jia_3")
		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
