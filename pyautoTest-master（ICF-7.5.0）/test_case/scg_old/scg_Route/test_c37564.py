import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37564
# ISP中两个ISP路由条目目的ip 完全相同的路由条目


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.82")

		add_multi_isp_save_wxw(browser, name='isp564', desc='miaoshu')

		import_ip_config_file_wxw(browser, name='isp564', save='yes', cancel='no')

		add_multi_isp_save_wxw(browser, name='isp564_2', desc='miaoshu')

		import_ip_config_file_wxw(browser, name='isp564_2', save='yes', cancel='no')
		time.sleep(1)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)

		del_multi_isp_byname(browser, name='isp564')
		del_multi_isp_byname(browser, name='isp564_2')

		try:
			assert "导入IP重复" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "导入IP重复" in alert


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		# reload(hostip="10.2.2.82")
		# print(err)
		# rail_fail(test_run_id, test_id)
		# time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])