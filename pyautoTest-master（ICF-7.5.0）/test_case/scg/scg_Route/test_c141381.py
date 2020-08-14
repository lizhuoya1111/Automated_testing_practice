import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_dev import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141381"
# ISP导入目的ip file文件名包含空格、$#&?>


def test_c141381(browser):

	try:
		login_web(browser, url=dev2)

		add_multi_isp_save_wxw(browser, name='isp571', desc='miaoshu')

		import_ip_config_file_wxw(browser, name='isp571', save='yes', cancel='no', file='isp_37571.txt')
		time.sleep(1)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)

		del_multi_isp_byname(browser, name='isp571')

		try:
			assert "导入IP格式错误" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "导入IP格式错误" in alert


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])