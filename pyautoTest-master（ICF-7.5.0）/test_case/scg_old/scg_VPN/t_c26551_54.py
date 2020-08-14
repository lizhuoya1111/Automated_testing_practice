import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_interface import *
from page_obj.common.rail import *

test_id = "26551"

def test_c26551(browser):

    login_web(browser)

    add_ca(browser)

    add_cer_local(browser, cer_name="local1", cer_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\server.crt", cer_key_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\server.key")

    add_cer_remote(browser, cer_name='remote1', cer_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\server1.crt")

    info = add_ipsec_gw_cer(browser,"testcer1","111","ge0/1","5.5.5.5","local1","remote1","80.1.2.0/24","65.15.2.0/24")

    if info == "操作成功":

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "成功添加远程网关隧道" in loginfo
            rail_pass(178,test_id)
            rail_pass(178,"26553")
            rail_pass(178,"26554")

        except:
            rail_fail(178, test_id)
            assert "成功添加远程网关隧道" in loginfo

    else:
        rail_fail(178,test_id)

        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c26551_54.py"])