from Base.base import Base
import Page

class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_coupons_text(self):
        """获取个人中心我的优惠券文本内容"""
        return self.search_element(Page.person_coupons_id).text

    def click_setting_btn(self):
        """点击个人中心设置按钮"""
        self.click_element(Page.person_setting_btn_id)