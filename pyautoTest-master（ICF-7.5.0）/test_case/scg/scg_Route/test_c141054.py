import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141054"
# 点击左树里的“route monitor”


def test_c141054(browser):

    try:
        login_web(browser, url=dev1)

        into_fun(browser, 路由监控)

        gettext = browser.find_element_by_xpath('//*[@id="notes"]/table/tbody/tr[1]/td').text.strip()
        # print(gettext)

        try:
            assert "监控过滤" in gettext
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "监控过滤" in gettext

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])