import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139668"


def test_c139668(browser):

	try:
		login_web(browser, url=dev1)
		cli_list = []
		ssh_81 = Shell_SSH()
		ssh_81.connect(hostip=dev1)
		ssh_81.execute("en")
		ssh_81.execute("conf t")
		for x in range(11, 16):
			ssh_81.execute(
				"ip-mac-binding interface " + interface_name_4 + " ip 55.1.1." + str(x) + " mac 02:11:31:f8:52:" + str(
					x))
			cli_list.append("ip-mac-binding interface " + interface_name_4 + " ip 55.1.1." + str(x) + " mac 02:11:31:f8:52:" + str(
					x))
			time.sleep(0.5)
		ssh_81.close()

		export_cli_file(browser, mode="neighmacipmacbind", encry="no", passwd="")
		file_info = open_file(file_name='export.conf', return_type="all")
		# print(file_info)
		del_chrome_download_file_all()

		del_bindinglist(browser, index_list="all")
		# loginfo1 = get_log_info(browser, log_type=管理日志)
		# for x in cli_list:
		# 	print(x)

		try:
			assert cli_list[0] in file_info and cli_list[1] in file_info and cli_list[2] in file_info and cli_list[3] in file_info and cli_list[4] in file_info
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert cli_list[0] in file_info and cli_list[1] in file_info and cli_list[2] in file_info and cli_list[3] in file_info and cli_list[4] in file_info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])