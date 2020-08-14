import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *

test_id = "141706"


def test_c141706(browser):
	try:

		login_web(browser, url=dev1)
		switch_physical_interface_snat(browser, interface=interface_name_3, snat="open")

		into_fun(browser, 源NAT)
		# 获取目前有多少个SNAT
		time.sleep(1)
		snat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
		# print(snat_sum)


		try:
			assert snat_sum == 0
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert snat_sum == 0

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])