import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_default_hole import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *


test_id = 132447


def test_c132447(browser):
	try:
		login_web(browser, url=dev1)
		get_into_default_hole_jyl(browser)
		webinfo1 = browser.find_element_by_xpath('//*[@id="for_tb_title"]').text.rstrip()
		webinfo2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]').text.rstrip()

		try:
			assert "索引"and "漏洞名称" and "发布时间"and "启用状态"and "事件处理"and "危险等级"and "操作"in webinfo1
			assert "高" in webinfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "索引"and "漏洞名称" and "发布时间"and "启用状态"and "事件处理"and "危险等级"and "操作"in webinfo1
			assert "高" in webinfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
