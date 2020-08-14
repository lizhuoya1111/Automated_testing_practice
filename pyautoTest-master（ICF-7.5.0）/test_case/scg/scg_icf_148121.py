import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.common.ssh import *
test_id = "148121"

def test_main(browser):
	login_web(browser, url="10.2.2.87", username="admin", password="admin@139", verificationCode="0613")
	add_ipsecRemoteGW_inhand(browser, ipsecRGWname="gateway", ipsecRGWinterSeq="ge0/5", ipsecRGWgateway="13.1.1.2",
	                         AuthenticationMethod="预共享密钥", PresharedKey="123456",
	                         localid="", remoteid="", localsubnet="12.1.1.1/24", remotesubnet="21.1.1.1/24")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "scg_icf_" + str(test_id) + ".py"])