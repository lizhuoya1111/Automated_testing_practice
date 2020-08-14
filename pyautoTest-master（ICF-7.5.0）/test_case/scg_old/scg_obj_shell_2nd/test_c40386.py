import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40386
# 添加一个serv obj grp,在ACL中引用,验证serv obj grp中R是否有显示


def test_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击对象
        browser.find_element_by_xpath(对象).click()
        # 点击ipv4
        browser.find_element_by_xpath(IPv4).click()
        # 点击服务
        browser.find_element_by_xpath(服务).click()
        # 点击服务组
        browser.find_element_by_xpath(服务组).click()

        add_obj_serv_grp_wxw(browser, name='serv_grp_386', desc='zhe是ge描shu', serv_obj='P:any')

        acl_ref_service_obj_wxw(browser, gname='aclgroup_s386', service_obj='G:serv_grp_386')

        get_serv_grp_obj_ref_wxw(browser, name='serv_grp_386')

        # 获取引用
        ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

        try:
            assert ref == "acl-group"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ref == "acl-group"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40386.py"])