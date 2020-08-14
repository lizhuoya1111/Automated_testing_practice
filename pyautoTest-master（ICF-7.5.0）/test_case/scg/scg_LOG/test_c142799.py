
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

test_id = 142799
def test_c142799(browser):
	try:
		login_web(browser, url=dev1)
		for x in range(1, 11):
			add_email_alarm_jyl(browser, enable="no", email_name="email_alart_jia_"+str(x), email_add="jyl@baomutech.com",
							cc_email="yes", cc_email_add="m18822678505@163.com", format="syslog", project="yes",
							project_content="300", disk_full="yes", admin_event="yes", av_vrius_found="yes",
							server_monitor="yes", save="yes")
		for x in range(1, 11):
			delete_email_alarm_server_jyl(browser, email_alarm="email_alart_jia_"+str(x))
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
