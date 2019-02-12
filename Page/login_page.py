from Base.base import Base
import Page

class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, username, passwd):
        """
        登录方法
        :param username: 登录账号
        :param passwd: 登录密码
        :return:
        """
        # 输入账号
        self.send_element(Page.login_account_id, username)
        # 输入密码
        self.send_element(Page.login_passwd_id, passwd)
        # 点击登录按钮
        self.click_element(Page.login_btn_id)
    def close_login_page(self):
        # 关闭登录页面
        self.click_element(Page.login_close_btn_id)


    def if_login_btn(self):
        """
        如果登录按钮存储在返回True 不存在返回False
        :return:
        """
        try:
            self.search_element(Page.login_btn_id)
            return True
        except:
            return False