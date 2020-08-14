import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "143941"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143941(browser):

	try:
		login_web(browser, url=dev3)

		add_acl_group_complete(browser, name='acl_group_1', enable='yes', sour=interface_name_3, dest='Z:any',
	                       desc='miaoshu',
	                       save='yes', cancel='no')

		for i in range(0, 5):
			add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_1', source_zone_interface=interface_name_4,
                          toip='13.1.1.0', tonetmask='24', dest_zone_interface=interface_name_3)

		# browser.switch_to.default_content()
		# 		# # 切换到左侧frame
		# 		# browser.switch_to.frame("lefttree")
		# 		# # 点击防火墙
		# 		# browser.find_element_by_xpath(防火墙).click()
		# 		# # 点击IPv4访问组列表
		# 		# browser.find_element_by_xpath(IPv4访问控制列表).click()
		# 		# # 定位到默认frame
		# 		# browser.switch_to.default_content()
		# 		# # 定位到内容frame
		# 		# browser.switch_to.frame("content")

		into_fun(browser, IPv4访问控制列表)

		# 定位到需要的acl组,n是组的id
		n = 1
		get_acl_sum = 0
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
		get_acl_sum = int(
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
		while getname != 'acl_group_1':
			n = n + 1
			getname = browser.find_element_by_xpath(
				'//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
			get_acl_sum = int(
				browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
		# 获取当前组是否展开，若没有展开，需要点击展开
		# print("获取当前组是否展开，若没有展开，需要点击展开")
		image_info = browser.find_element_by_xpath(
			'//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').get_attribute('src')
		if "defButton_f.gif" in image_info:
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
		# print(n-1)
		time.sleep(2)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到frame
		browser.switch_to.frame("content")
		browser.switch_to.frame("iFrame" + str(n - 1))
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[6]/ul/li/a[1]').click()
		info1 = True
		for y in range(1, 6):
			# print(y)
			time.sleep(0.5)
			info = browser.find_element_by_xpath(
				'//*[@id="storage_new_zone"]/div[' + str(y) + ']/ul/li[1]/input[1]').is_selected()
			if info is False:
				info1 = False

		try:
			assert info1 is True
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert info1 is True

		del_acl_group_wxw(browser, name='acl_group_1')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev3)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])