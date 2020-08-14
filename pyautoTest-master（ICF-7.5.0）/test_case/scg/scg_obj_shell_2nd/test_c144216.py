import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_dev import *
from page_obj.common.ssh import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144216"
# ACL 8
# 添加一条ACL,目的地址被设定为addr grp1,action为deny,尝试删除该obj
# 匹配源地址的包不可以过,该obj不能被删除


def test_c144216(browser):

	try:
		login_web(browser, url=dev3)

		# 禁用默认防火墙，以免产生干扰
		enable_acl_group_wxw(browser, aclgroup_name='default', enable='no')

		# 添加一个addr组
		add_obj_address_wxw(browser, name='obj_add_216', desc='zhe是yi个描述1', subnetip='34.1.1.0', subnetmask='24')
		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_216', desc='zhe是yi个描述1', addr_obj='A:obj_add_216')

		# 添加防火墙组
		add_acl_group_complete(browser, name='acl_group_216', enable='yes', sour='Z:any', dest='Z:any', desc='miaoshu',
							   save='yes', cancel='no')
		# 添加acl规则
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_216', source_zone_interface='Z:any',
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='G:obj_grp_216',
								  dest_zone_interface='Z:any',
								  service='P:any', schdule='-- 无 --',
								  accept='no', drop='yes',
								  auth='-- 无 --', icf='no', log='no')
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_216', source_zone_interface='Z:any',
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface='Z:any',
								  service='P:any', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no')

		# 在81和84上添加路由
		# 给84加上去81的路由
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 34.1.1.3")
		a.execute("exit")
		# 给81加上去84的路由
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
		a.execute("exit")
		# ping 34.1.1.4
		a.execute("ping 34.1.1.4")
		time.sleep(5)
		result1 = a.output()
		# print(result1)

		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(5)
		result2 = a.output()
		# print(result2)

		del_obj_grp_wxw(browser, name='obj_grp_216')
		time.sleep(2)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]').text
		# print(alert)

		# 恢复配置
		enable_acl_group_wxw(browser, aclgroup_name='default', enable='yes')

		del_acl_group_wxw(browser, name='acl_group_216')

		del_obj_grp_wxw(browser, name='obj_grp_216')

		del_obj_address_wxw(browser, name='obj_add_216')


		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 13.1.1.0/24 gateway 34.1.1.3")
		a.execute("exit")
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
		a.execute("exit")

		try:
			assert "Destination Host Unreachable"in result1
			assert"ms" in result2
			assert "对象正在使用" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Destination Host Unreachable" in result1
			assert "ms" in result2
			assert "对象正在使用" in alert

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3, dev4])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])