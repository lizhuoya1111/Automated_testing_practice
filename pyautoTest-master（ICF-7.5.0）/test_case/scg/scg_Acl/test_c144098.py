import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144098"
# 输入非法参数 1
# 添加一个分组，在名称中使用一些非法字符，如￥……


def test_c144098(browser):

	try:
		login_web(browser, url=dev1)

		add_acl_group_before_save(browser, name=str_32_en+"test", enable='yes', sour='Z:any', dest='Z:any', desc='miaoshu')

		time.sleep(0.5)
		# 保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
		# # 返回
		# browser.find_element_by_xpath('//*[@id="link_but"]').click()
		gname = get_groupname_byid(browser, group_id=2)
		# print(gname)

		try:
			assert gname != str_32_en+"test"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert gname != str_32_en+"test"

		del_acl_group_wxw(browser, name=gname)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])