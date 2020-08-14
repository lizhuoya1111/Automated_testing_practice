
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath

test_id = 142787
def test_c142787(browser):
	try:
		login_web(browser, url=dev1)
		add_email_alarm_jyl(browser, enable="yes", email_name="jia_1", email_add="jyl@baomutech.com", cc_email="yes",
							cc_email_add="m18822678505@163.com", format="syslog", project="yes", project_content="200",
							disk_full="yes", save="yes")
		loginfo = get_log(browser, 管理日志)
		delete_email_alarm_server_jyl(browser, email_alarm="jia_1")
		try:
			assert "成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
