import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139763"


def test_c139763(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t23296", "d", [interface_name_4])
		add_dnat(browser, name="test", src_inter_zone="Z:t23296", server="P:BGP", trans_ip="15.1.1.22")
		del_obj_zone_byname(browser, "t23296")
		del_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(del_info)
		edit_zone_simple(browser, name="t23296", new_desc="wwwwww")
		edit_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(edit_info)

		try:
			assert "对象正在使用" == str(del_info) and "操作成功" == str(edit_info)
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "对象正在使用" == str(del_info) and "操作成功" == str(edit_info)

		del_dnat_byname(browser, "test")
		del_obj_zone_byname(browser, "t23296")


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
