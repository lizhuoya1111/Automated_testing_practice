import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_policy_route import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37596
# 源和目的都为0.0.0.0/0的策略路由添加


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_policy_route_single_wxw(browser, in_device='ge0/3', src_ip='0.0.0.0', src_mask='0',
									dst_ip='0.0.0.0', dst_mask='0', service='no', serv='any',
									service_grp='no', serv_grp='H323',
									out_device='ge0/2', gateway='13.1.1.1', enable='yes', disnable='no',
									desc='maioshu')

		time.sleep(1)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)

		try:
			assert "不支持源和目的均为任意的策略路由"in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "不支持源和目的均为任意的策略路由" in alert


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.83")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])