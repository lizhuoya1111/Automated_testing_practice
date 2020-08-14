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

test_id = "139615"


def test_c139615(browser):

	try:
		login_web(browser, url=dev2)
		ssh_82 = Shell_SSH()
		ssh_82.connect(hostip=dev2)
		ssh_82.execute("en")
		ssh_82.execute("conf t")
		for x in range(10, 30):
			# add_ipmac_list(browser, ipadd="55.1.1."+str(x), inteface=interface_name_4, mac="02:11:31:f8:52:"+str(x))
			ssh_82.execute("ip-mac-binding interface "+interface_name_4+" ip 55.1.1."+str(x)+" mac 02:11:31:f8:52:"+str(x))
			time.sleep(0.5)
		ssh_82.close()
		# 获取当前列表总数 ip-mac-binding interface P3 ip 1.1.1.1 mac sss
		into_fun(browser, 绑定列表)
		try_num = 0
		while try_num < 5:
			try:
				browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()
				break
			except:
				time.sleep(1)
				try_num += 1
		time.sleep(2)
		sum_list = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		if sum_list == "20":
			del_bindinglist(browser, index_list="all", pagesize="20")

		sum_list1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		loginfo = get_log_info(browser, log_type=管理日志)

		try:
			assert '20' in sum_list and '0' in sum_list1 and "成功删除IP MAC绑定条目" in loginfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert '20' in sum_list and '0' in sum_list1 and "成功删除IP MAC绑定条目" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])