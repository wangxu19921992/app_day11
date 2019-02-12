import sys, os
sys.path.append(os.getcwd())

from Base.initdriver import get_driver
from Base.page import Page
from selenium.common.exceptions import TimeoutException
import pytest, allure
from Base.get_data import Get_Data
def get_login_data():
    # 成功数据列表
    suc_list = []
    # 失败数据列表
    fail_list = []
    # with open("./Data/test_data.yml", "r") as f:
        # data = yaml.load(f).get("Test_Login_Data")
    data = Get_Data().get_yml_data("test_data").get("Test_Login_Data")
    for i in data.keys():
        if data.get(i).get("toast_mes"):
            fail_list.append((data.get(i).get("username"), data.get(i).get("passwd"),
                              data.get(i).get("toast_mes"),data.get(i).get("expect")))
        else:
            suc_list.append((data.get(i).get("username"), data.get(i).get("passwd"),
                              data.get(i).get("expect")))
    return {"suc": suc_list,"fail": fail_list}

class Test_Login:

    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 实例化Page类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(autouse=True) # 解决依赖条件
    def in_login_page(self):
        # 点击我
        self.page_obj.get_home_page().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_sign_page().click_exits_accout()

    @pytest.mark.parametrize("user, pwd, exp",get_login_data().get("suc"))
    def test_succ_login(self, user, pwd, exp):

        # 登录
        self.page_obj.get_login_page().login(user, pwd)
        try:
            # 取我的优惠券
            coupons_text = self.page_obj.get_person_page().get_coupons_text()
            try:
                assert exp == coupons_text
            except AssertionError:
                # 截图
                self.page_obj.get_person_page().screen_shot(name="登录成功")
                assert False

            finally:
                # 点击设置按钮
                self.page_obj.get_person_page().click_setting_btn()
                # 执行退出操作
                self.page_obj.get_setting_page().logout()

        except TimeoutException:
            # 关闭登录页面
            self.page_obj.get_login_page().close_login_page()
            assert False

    @pytest.mark.parametrize("user, pwd, toast, exp", get_login_data().get("fail"))
    def test_fail_login(self, user, pwd, toast, exp):

        # 登录
        self.page_obj.get_login_page().login(user, pwd)
        # 断言
        try:
            # 获取提示消息
            toast_data = self.page_obj.get_setting_page().get_toast(toast)
            try:
                # 断言提示消息 和 登录按钮
                assert toast_data == exp and self.page_obj.get_login_page().if_login_btn()
            except AssertionError:
                self.page_obj.get_setting_page().screen_shot(name="登录失败")
                assert False
            finally:
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
        except TimeoutException:
            # 截图
            self.page_obj.get_person_page().screen_shot()
            try:
                # 点击设置按钮
                self.page_obj.get_person_page().click_setting_btn()
                # 执行退出操作
                self.page_obj.get_setting_page().logout()
            except TimeoutException:
                self.page_obj.get_login_page().close_login_page()