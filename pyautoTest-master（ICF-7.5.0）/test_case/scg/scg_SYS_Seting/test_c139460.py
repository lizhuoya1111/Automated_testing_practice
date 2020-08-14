import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "139460"



def test_c139460(browser):
	try:
		# login_web(browser, url=dev1)
		# # 点击管理员
		# set_language(browser, language_sw="英文")
		# result1 = judge_language(browser, language_sw="英文")
		#
		# set_language(browser, language_sw="简体中文")
		# result2 = judge_language(browser, language_sw="简体中文")
		#
		# set_language(browser, language_sw="繁体中文")
		# result3 = judge_language(browser, language_sw="繁体中文")
		#
		#
		# try:
		# 	assert result1 and result2 and result3
		# 	rail_pass(test_run_id, test_id)
		# except:
		# 	rail_fail(test_run_id, test_id)
		# 	assert result1 and result2 and result3

		rail_fail(test_run_id, test_id)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		# reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])