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

test_id = 142884
# 能够刷新system日志信息
def test_c142884(browser):
	try:
		login_web(browser, url=dev1)

		get_log(browser, 系统日志)

		info1 = browser.find_element_by_xpath('//*[@id="for_config_tb_title_mix"]/ul/li').text
		# print(info1)
		try:
			assert "系统日志" in info1

			rail_pass(test_run_id, test_id)
		except:
			# 当日志仅有一页时,该脚本会执行失败,在这里可以添加SSH登陆或者接口downup去产生日志，保证重新执行时可以PASS
			# INTERFACE DOWN UP
			generate_log(browser, dev=dev1, log_type=系统日志, num="20")
			rail_fail(test_run_id, test_id)
			assert "系统日志" in info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
