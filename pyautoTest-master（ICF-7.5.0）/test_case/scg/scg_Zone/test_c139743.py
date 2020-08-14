import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139743"


def test_c139743(browser):

	try:
		login_web(browser, url=dev1)
		add_br(browser)
		add_br(browser)
		add_obj_zone(browser, "t23246", "d", ["br_0", "br_1", "br_2"])
		time.sleep(2)
		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		if info1 == "操作成功":
			zone_name = find_zone_byname(browser, "t23246")
			if zone_name == "br_0"+" "+"br_1"+" "+"br_2":
				loginfo = get_log_info(browser, 管理日志)
				# print("日志："+loginfo)
				try:
					assert "对象成功，添加内部对象 [t23246]，具体属性 : 所选接口为 [br_0,br_1,br_2,]" in str(loginfo)
					rail_pass(test_run_id, test_id)

				except Exception as err1:
					print(err1)
					rail_fail(test_run_id, test_id)
					assert "对象成功，添加内部对象 [t23246]，具体属性 : 所选接口为 [br_0,br_1,br_2,]" in str(loginfo)
			else:
				assert False
		else:
			assert False

		del_obj_zone_byname(browser, "t23246")
		del_br_all(browser)


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])