import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141868

def test_c141868(browser):

	try:
		login_web(browser, url=dev1)

		# no掉物理接口的地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.close()

		# 添加子接口
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")

		# 子接口添加IP地址
		add_vlan_inte_add(browser, interface_name=interface_name_2+".22", ipadd="12.1.1.1", mask="24")

		# 判断路由是否存在
		result = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
		print(result)

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.close()

		time.sleep(0.5)

		try:
			assert result is True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result is True

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])