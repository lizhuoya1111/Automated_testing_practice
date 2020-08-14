import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_physical_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141707

def test_c141707(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.execute("exit")
		a.close()
		switch_physical_interface_snat(browser, interface=interface_name_2, snat="open")

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone=interface_name_3, des_inter_zone=interface_name_2,
				 other_match_switch="yes",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:ICMP', trans_local_ip="no", single_ip='13.1.1.5',  save='yes', cancel='no')

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(1)
		a.execute("exit")
		result1 = a.output()
		# print(result1)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.execute("exit")
		a.close()
		switch_physical_interface_snat(browser, interface=interface_name_2, snat="close")
		del_snat_byname(browser, name="snat_jia_1")

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])