from selenium.webdriver.common.by import By
"""百年奥莱"""


"""首页"""
# 我的按钮
home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

"""注册页面"""
# 已有账号,去登录
exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")

"""登录页面"""
# 账户
login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
# 密码
login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
# 登录按钮
login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
# 关闭登录页面按钮
login_close_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

"""个人中心页面"""
# 我的优惠券
person_coupons_id = (By.ID, "com.yunmall.lc:id/txt_my_coupons")
# 设置按钮
person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""设置页面"""
# 退出按钮
logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
# 弹窗确认退出按钮
logout_acc_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
