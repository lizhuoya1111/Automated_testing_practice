
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

test_id = 142959
def test_c142959(browser):
	try:
		login_web(browser, url=dev1)
		add_log_server_jyl(browser, status="enable", server_name="log_server_jia_1", ip="192.165.12.3", port="162",
						   format="syslog", protocol="tcp", charset="UTF-8", save="yes")
		loginfo1 = get_log(browser, 管理日志)
		print(loginfo1)

		add_ftp_server_jyl(browser, status="enable", server_name="ftp_server_jia_1", ftp_server_name="192.165.12.3",
						   path="jia", user="user", password="123456", format="syslog", time="yes", time_num="500",
						   save="yes")
		loginfo2 = get_log(browser, 管理日志)
		print(loginfo2)

		delete_log_server_jyl(browser, log_server="log_server_jia_1")
		delete_ftp_server_jyl(browser, ftp_server="ftp_server_jia_1")

		try:
			assert "配置日志服务器成功" in loginfo1
			assert "配置 [EXPORT]对象成功" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置日志服务器成功" in loginfo1
			assert "配置 [EXPORT]对象成功" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
