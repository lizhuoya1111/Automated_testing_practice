import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139814"
# 检查zone name是否支持< > ” ’ & \ ? $ #? 这9个字符
# 无法成功配置，系统报错


def test_c139814(browser):
    try:
        login_web(browser, url=dev1)
        # 添加zone name为<
        add_obj_zone(browser, "<", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info1 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info1)
        browser.find_element_by_class_name('layui-layer-btn0').click()

        # 添加zone name为”
        add_obj_zone(browser, "”", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info2 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info2)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为’
        add_obj_zone(browser, "’", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info3 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info3)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为&
        add_obj_zone(browser, "&", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info4 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info4)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为\
        add_obj_zone(browser, "\\", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info5 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info5)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为?
        add_obj_zone(browser, "?", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info6 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info6)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为$
        add_obj_zone(browser, "$", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info7 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info7)
        browser.find_element_by_class_name('layui-layer-btn0').click()
        # 添加zone name为#
        add_obj_zone(browser, "#", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        info8 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info8)
        browser.find_element_by_class_name('layui-layer-btn0').click()

        try:
            assert '请重新输入' in info1 and '请重新输入' in info2 and '请重新输入' in info3 and '请重新输入' in info4 and '请重新输入' in info5 and '请重新输入' in info6 and '请重新输入' in info7 and '请重新输入' in info8
            rail_pass(test_run_id, test_id)
        except Exception as err1:
            print(err1)
            rail_fail(test_run_id, test_id)
            assert '请重新输入' in info1 and '请重新输入' in info2 and '请重新输入' in info3 and '请重新输入' in info4 and '请重新输入' in info5 and '请重新输入' in info6 and '请重新输入' in info7 and '请重新输入' in info8
    except Exception as err:
        # 如果上面的步骤有报错，重启设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])