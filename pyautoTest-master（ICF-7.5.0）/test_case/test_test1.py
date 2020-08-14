import pytest
import time
import sys
import os
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_firewall import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_machine_learning import *



def test_c23246(browser):
	try:
		login_web(browser, url=dev1)
		export_cli_file(browser, mode="all", encry="no", passwd="")
		f = open(path_download+'\\export.conf', encoding='utf-8')
		data = f.read()
		f.close()
		# print(data)
		del_chrome_download_file_all()

	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_test1.py"])