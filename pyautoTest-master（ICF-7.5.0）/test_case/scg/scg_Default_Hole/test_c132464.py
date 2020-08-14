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

test_id = 132464
def test_c132464(browser):
	try:
		login_web(browser, url=dev1)
		get_into_default_hole_jyl(browser)
		# 点击详情
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/a').click()
		webinfo1 = browser.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]/div').text.rstrip()

		try:
			assert "漏洞名称" and "漏洞类型" and "发生时间" and "漏洞统一编号" and "漏洞来源" and "危害等级" \
				   and "触发设备" and "事件处理" and "规则来源" and "受影响厂商" and "攻击条件" and "规则描述" \
				   and "特征名称" and "风险等级" and "优先级" and "特征编号"in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "漏洞名称" and "漏洞类型" and "发生时间" and "漏洞统一编号" and "漏洞来源" and "危害等级" \
				   and "触发设备" and "事件处理" and "规则来源" and "受影响厂商" and "攻击条件" and "规则描述" \
				   and "特征名称" and "风险等级" and "优先级" and "特征编号"in webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
