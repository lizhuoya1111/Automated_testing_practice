import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37203
# 对于只有ISP name的条目，点击条目后面的import ip
# 可以弹出导入ip界面，导入ip后，可正常排列与该ISP后


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp203', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp203', save='yes', cancel='no')

        ip = get_isp_show_ip_wxw(browser, name='isp203')
        # print(ip)

        del_multi_isp_byname(browser, name='isp203')

        try:
            assert ip == "121.1.1.0/24"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ip == "121.1.1.0/24"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])