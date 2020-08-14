import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath

test_id = 142760
def test_c142760(browser):
	try:
		login_web(browser, url=dev1)
		add_ftp_server_jyl(browser, status="enable", server_name="ftp_jia_1", ftp_server_name="192.165.12.3",
						   path="jia", user="jia_admin_1", password="123456", format="syslog",
						   project="yes", project_content="200", save="yes")
		loginfo = get_log(browser, 管理日志)
		delete_ftp_server_jyl(browser, ftp_server="ftp_jia_1")
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
