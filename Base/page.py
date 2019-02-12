from Page.home_page import HomePage
from Page.sign_page import SingPage
from Page.login_page import LoginPage
from Page.person_page import PersonPage
from Page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)
    def get_sign_page(self):
        """返回注册页面实例化对象"""
        return SingPage(self.driver)

    def get_login_page(self):
        """返回登录页面对象"""
        return LoginPage(self.driver)
    def get_person_page(self):
        """返回个人中心页面对象"""
        return PersonPage(self.driver)
    def get_setting_page(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)