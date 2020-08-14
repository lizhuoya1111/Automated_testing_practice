import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 139382

# 使用超级管理员登录设备，超过3次登陆设备认证失败后，提示超级管理员被冻结，1分钟后再次用正确的用户名和密码登录
# 1分钟后超级管理员被解冻，可以登录成功
# 次数和冻结时间需预先设置
# 此脚本先设置次数和时间 再进行冻结解冻验证

def test_c139382(browser):
    try:
        login_web(browser, url=dev1)
        # 设置登录次数3 冻结时间1min
        sys_set_only_frozen_expire_retry(browser, frozen_time="60", retry="3")
        # 退出当前账户
        sign_out_jyl(browser)
        # 用admin登录 输入错误密码3次
        for x in range(1, 4):
            login_web_when_password_wrong(browser, url=dev1, username="admin", password="admin"+str(x))
            print('第 %s 次登录'%(x))
        # 输入正确密码 获取冻结提示
        info1 = return_frozon_info_when_login_in(browser, url="10.2.2.81", username="admin", password="admin@139",
                                         verificationCode="0613")
        print(info1)
        time.sleep(65)
        # 用admin登录
        login_web(browser, url=dev1)
        # # 获取“系统”
        into_fun(browser, 系统状态)
        text1 = browser.find_element_by_xpath('//*[@id="box_title_sys_info"]/h4').text
        sys_set_only_frozen_expire_retry(browser, frozen_time="600")

        try:
            assert "冻结" in info1 and "系统信息" in text1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "冻结" in info1 and "系统信息" in text1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])