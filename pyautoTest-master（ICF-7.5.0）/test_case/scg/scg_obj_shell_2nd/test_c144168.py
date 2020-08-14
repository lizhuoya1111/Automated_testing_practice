import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144168"
# 添加一个和predefine的serv同名的小写serv,内容也一样


def test_c144168(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_serv_grp_wxw(browser, name='h323', desc='zhe是ge描shu', serv_obj='P:any')

		time.sleep(1)
		promit = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(promit)

		try:
			assert promit == "h323已经存在"
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert promit == "h323已经存在"

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])