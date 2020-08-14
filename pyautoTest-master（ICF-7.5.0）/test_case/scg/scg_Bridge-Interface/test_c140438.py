import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140438
def test_c140438(browser):
	try:
		login_web(browser, url=dev1)
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入网桥名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("bridge10")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		print(webinfo1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		bridge_add_jyl(browser, bridge_name="br_1")
		# 点击增加
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入网桥名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("@#￥%#￥")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo2 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text.rstrip()
		print(webinfo2)

		bridge_add_jyl(browser, bridge_name="br_1")
		# 点击增加
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入网桥名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("98375aksd")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		print(webinfo3)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		bridge_add_jyl(browser, bridge_name="br_1")
		# 点击增加
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入网桥名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("br_0")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo4 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		print(webinfo4)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		bridge_add_jyl(browser, bridge_name="br_1")
		# 点击增加
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo5 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text.rstrip()
		print(webinfo5)
		# print(webinfo1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("exit")

		try:
			assert "无效网桥名称" in webinfo1
			assert "名称输入错误" in webinfo2
			assert "无效网桥名称" in webinfo3
			assert "br_0已经存在" in webinfo4
			assert "名称输入错误" in webinfo5
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "无效的网桥名称" in webinfo1
			assert "名称输入错误" in webinfo2
			assert "无效网桥名称" in webinfo3
			assert "br_0已经存在" in webinfo4
			assert "名称输入错误" in webinfo5
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
