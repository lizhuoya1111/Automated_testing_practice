import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141011"
# 点击“import ip”，导入ip config file，点击cancel


def test_c141011(browser):

    try:
        login_web(browser, url=dev1)

        add_multi_isp_save_wxw(browser, name='isp201', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp201', save='no', cancel='yes')

        gettext = browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').get_attribute('value')
        # print(gettext)

        ip = get_isp_show_ip_wxw(browser, name='isp201')
        # print(ip)

        del_multi_isp_byname(browser, name='isp201')

        try:
            assert ip == "ip is null"
            assert '增加' in gettext
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ip == "ip is null"
            assert '增加' in gettext

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])