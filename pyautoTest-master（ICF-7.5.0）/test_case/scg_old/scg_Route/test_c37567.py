import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37567
# ISP导入目的ip file中输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256、


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		add_multi_isp_save_wxw(browser, name='isp567', desc='miaoshu')

		import_ip_config_file_wxw(browser, name='isp567', save='yes', cancel='no', file='isp_37567_1.txt')
		time.sleep(1)
		alert1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert1)

		import_ip_config_file_wxw(browser, name='isp567', save='yes', cancel='no', file='isp_37567_2.txt')
		time.sleep(1)
		alert2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert2)

		import_ip_config_file_wxw(browser, name='isp567', save='yes', cancel='no', file='isp_37567_3.txt')
		time.sleep(1)
		alert3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert3)

		del_multi_isp_byname(browser, name='isp567')

		try:
			assert "导入IP格式错误" in alert1
			assert "导入的IP文件有误" in alert2
			assert "导入IP格式错误" in alert3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "导入IP格式错误" in alert1
			assert "导入的IP文件有误" in alert2
			assert "导入IP格式错误" in alert3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.82")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])