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

test_id = 142762
def test_c142762(browser):
	try:
		login_web(browser, url=dev1)
		add_ftp_server_jyl(browser, status="enable", server_name="fep_server_jia_1", ftp_server_name="192.161.12.3",
						   path="路径1", user="user", password="123456", format="syslog", time="yes", time_num="10",
						   save="yes")
		add_ftp_server_jyl(browser, status="enable", server_name="fep_server_jia_2", ftp_server_name="192.161.12.3",
						   path="路径1", user="user", password="123456", format="syslog", time="yes", time_num="1440",
							save="yes")
		delete_ftp_server_jyl(browser, ftp_server="fep_server_jia_1")
		delete_ftp_server_jyl(browser, ftp_server="fep_server_jia_2")
		loginfo1 = get_log(browser, 管理日志)
		try:
			assert "删除内部对象" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "删除内部对象" in loginfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
