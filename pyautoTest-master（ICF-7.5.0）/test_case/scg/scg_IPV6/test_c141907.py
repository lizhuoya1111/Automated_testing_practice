import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_ipv6 import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 141907
def test_c141907(browser):
	try:
		login_web(browser, url=dev1)
		edit_neighbor_discovery_jyl(browser, physical_interface=interface_name_4, retransmission_time=" ",
									base_reachable_time="3600001", duolicate_add_retry_count="1", save="yes")
		web_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		edit_neighbor_discovery_jyl(browser, physical_interface=interface_name_4, retransmission_time="1000",
									base_reachable_time="30000", duolicate_add_retry_count="1", save="yes")
		try:
			assert "非法整型值" in web_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "非法整型值" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
