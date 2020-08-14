import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40369
# 添加一个obj grp,在ACL中引用,验证obj grp中R是否有显示


def test_add_obj_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击对象
		browser.find_element_by_xpath(对象).click()
		# 点击ipv4
		browser.find_element_by_xpath(IPv4).click()
		# 点击地址组
		browser.find_element_by_xpath(IPv4地址组).click()

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_369', desc='zhe是yi个描述1', addr_obj='A:any')

		acl_ref_addr_obj_wxw(browser, gname='aclgroup_369', addr_obj='G:obj_grp_369')

		get_grp_obj_ref_wxw(browser, name='obj_grp_369')

		# 获取引用
		ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

		try:
			assert ref == "acl-group"
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert ref == "acl-group"

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c40369.py"])
