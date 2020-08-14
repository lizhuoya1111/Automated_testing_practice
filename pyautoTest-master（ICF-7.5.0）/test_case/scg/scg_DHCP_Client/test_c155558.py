import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_route import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *

test_id = "155558"


def test_c155558(browser):
	try:
		# login_web(browser, url=dev1)
		# driver = webdriver.Firefox()
		# driver.get("http://www.xxxx.net/")
		# sleep(3)
		# # xpath层级和属性结合定位
		# driver.find_element_by_xpath("//form[@id='xxxx']/ul/input[1]").send_keys("xxxx")
		# # xpath逻辑运算组合定位
		# # driver.find_element_by_xpath("//input[@class='xxxx' and @name='xxxx']").send_keys("xxxx")
		# sleep(4)
		# driver.find_element_by_xpath("//form[@id='xxxxx']/ul/input[2]").send_keys('xxxxx')
		# sleep(6)
		# driver.quit()

		rail_fail(test_run_id, test_id)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])