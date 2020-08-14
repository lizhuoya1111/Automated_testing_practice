import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37271
# 添加一条静态路由，指定目的ip


def test_physical_interface_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='13.1.1.1',
									enable='yes')

		ssh = SSH("10.1.1.202", 'root', 'root', 22)
		ssh.connect()
		ssh.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
		result1 = ssh.execute('ping 13.1.1.3 -c 3 -i 0.2')
		time.sleep(5)
		# print(result1)
		ssh.close()

		# 删除83上的路由
		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 20.1.1.0/24 gateway 13.1.1.1")

		# print('这是一条分界线111111111111111111111')

		time.sleep(2)

		ssh = SSH("10.1.1.202", 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 13.1.1.3 -c 2 -i 0.2')
		time.sleep(5)
		ssh.execute('route del -net 13.1.1.0/24 gw 20.1.1.1')
		# print(result2)
		ssh.close()

		try:
			assert "ttl" in result1
			assert "100% packet loss" in result2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result1
			assert "100% packet loss" in result2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])