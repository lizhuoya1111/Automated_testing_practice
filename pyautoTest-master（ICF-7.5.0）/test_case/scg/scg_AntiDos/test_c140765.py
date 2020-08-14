
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
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 140765

def test_c140765(browser):
	try:
		login_web(browser, url=dev1)
		add_black_or_white_list_wxw(browser, name='$#&?>', desc='描述', any='yes/no',
							   		single_ip='yes/no', sip='',
							   		ip='yes/no', custom='', mask='',
							   		address='yes', srange='A:any',
							   		white='yes', black='no', never='yes',
							   		date='yes/no', expire_date='2019-03-06', expire_time='02:00:00',
							   		save='yes', cancel='yes/no')

		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "名称输入错误，请重新输入" in web_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "名称输入错误，请重新输入" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])