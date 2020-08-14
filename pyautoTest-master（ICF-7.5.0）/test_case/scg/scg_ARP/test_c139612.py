import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139612"


def test_c139612(browser):

	try:
		login_web(browser, url=dev2)
		into_fun(browser, 绑定列表)
		time.sleep(1.5)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
		time.sleep(1.5)
		get_smthing = browser.find_element_by_xpath('//*[@id="note_area"]/div/form/ul/li[1]').text


		try:
			assert "启用IP-MAC绑定表与静态ARP表同步" in get_smthing
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "启用IP-MAC绑定表与静态ARP表同步" in get_smthing


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])