import unittest
from po.Login_page import Login_page

class TestLogin(unittest.TestCase):
    '''EDU登录模块功能验证'''
    def setUp(self):
        self.obj = Login_page()
        self.obj.Open_url()

    def tearDown(self):
        self.obj.b.quit()

    def test_login_success_001(self):
        '''登录成功验证'''
        self.obj.set_username('admin')
        self.obj.set_password('admin')
        self.obj.click_login_button()
        r = self.obj.get_login_success_msg()
        self.assertEqual(r,'admin')

    def test_login_empty_username_002(self):
        '''用户名为空验证'''
        self.obj.set_username('')
        self.obj.set_password('admin')
        self.obj.click_login_button()
        r = self.obj.get_login_username_empty_msg()
        self.assertEqual(r,'帐号或密码不能为空')
if __name__=="__main__":
	unittest.main()