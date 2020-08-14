import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 140596


def test_c140596(browser):
	try:
		login_web(browser, url=dev1)
		antiddos_settings_wxw(browser, function_enable='yes', function_disable='no',
							  syn_cookie='yes', allways_on='no', intelligent_defense='yes',
							  log_enable='no', log_messages='1',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("show antidos global")
		time.sleep(0.5)
		result = a.output()
		a.close()
		# print(result)

		antiddos_settings_wxw(browser, function_enable="no", function_disable='yes',
							  syn_cookie='no', allways_on='no', intelligent_defense='yes',
							  log_enable='no', log_messages='1',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')

		try:
			assert "mode: ON" in result
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "mode: ON" in result

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])