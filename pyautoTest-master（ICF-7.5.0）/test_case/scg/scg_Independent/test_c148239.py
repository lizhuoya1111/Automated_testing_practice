import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "148239"


def test_c148239():
	try:
		n = 0
		for x in range(0, 80000):
			scg = Shell_SSH()
			scg.connect("10.2.2.72")
			scg.execute("en")
			scg.execute("show clock")
			output = scg.output()
			print(output)
			scg.execute("exit")
			scg.execute("exit")
			time.sleep(1)
			scg.close()
			n += 1
			print("---"+str(n)+"---")
		scg = Shell_SSH()
		scg.connect("10.2.2.72")
		scg.execute("en")
		scg.execute("show clock")
		output1 = scg.output()
		print("end:"+output1)

		try:
			assert "date" in output1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "date" in output1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		# reload(hostip="10.2.2.72", reloadtime=70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])