import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "139479"
# time栏的异常输入：12:00:00/1:00:60/1:61:00/25:00:00/!@#/中文/英文/12-00-01
# date栏的异常输入：2007-02-29/2008-02-30/2008-13-1/2008-12-32/@#$/中文/英文/11-22-2008，验证能否提交成功，查看log
# 不能提交
# "1:00:60"


def test_c139479(browser):
	try:
		login_web(browser, url=dev5)
		for y in ["2007-02-29", "2008-02-30", '2008-13-1', '!@#', '中文', 'www', '2008-12-32', '11-22-2008']:
			login_web(browser, url=dev5)
			set_time(browser, date_input=y, time_input='11:00:10')
			alert2 = browser.switch_to_alert().text
			time.sleep(0.5)
			browser.switch_to_alert().accept()
			# print(alert2)

		for n in ['!@#', '中文', 'www', '12-00-01', "1:61:00"]:
			login_web(browser, url=dev5)
			set_time(browser, date_input="2019-06-08", time_input=n)
			alert1 = browser.switch_to_alert().text
			browser.switch_to_alert().accept()
			time.sleep(0.5)
			# print(alert1)

		for x in ['25:00:00']:
			login_web(browser, url=dev5)
			set_time(browser, date_input="2019-06-08", time_input=x)
			try:
				info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
				time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
			except:
				info1 = browser.switch_to_alert().text
				browser.switch_to_alert().accept()





		try:
			assert "时间输入错误，请重新选择" in alert1 and "日期输入错误，请重新选择" in alert2 and ("更新配置到配置文件出错" in info1 or "时间输入错误，请重新选择" in info1)
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "时间输入错误，请重新选择" in alert1 and "日期输入错误，请重新选择" in alert2 and ("更新配置到配置文件出错" in info1 or "时间输入错误，请重新选择" in info1)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])