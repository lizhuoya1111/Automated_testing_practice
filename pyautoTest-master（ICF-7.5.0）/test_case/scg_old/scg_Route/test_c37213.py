import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37213
# 点击add route，选择single gw，填写单网关ip，选择device
# 操作成功；shell先显示和UI一致；admin log正常


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp213', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp213', save='yes', cancel='no')

        add_isp_route_wxw(browser, name='isp213', single_gateway='yes', device='ge0/2', gateway='12.1.1.6',
                          multi_gateway='no', gateway_group='',
                          enable='yes', disable='no')

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_multi_isp_byname(browser, name='isp213')

        try:
            assert "成功为ISP" in loginfo
            assert "添加或修改路由，网关" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "成功为ISP"in loginfo
            assert "添加或修改路由，网关" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])