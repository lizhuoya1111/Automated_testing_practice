import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
# 连续登陆ssh

test_id = "9999999"

def test_main(browser):
	for x in range(1, 32):
		a = Shell_SSH()
		a.connect("10.2.2.73")
		time.sleep(1)
		a.execute("en")
		a.execute("exit")
		a.execute("exit")
		time.sleep(1)


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])