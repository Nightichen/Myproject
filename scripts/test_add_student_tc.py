import sys
import os
import unittest
sys.path.append('../')
from lib.business_module import login_B
from lib.Public_module import InsertLog_P
from po.Member_Center.student_list import Student_List
from po.Member_Center.StudentList.AddStudent import AddStudentPage
from lib.Public_module import Connection_MySQLData
from BeautifulReport import BeautifulReport
class AddStudentTest(unittest.TestCase):
    '''添加学生功能测试'''
    img_path = '../img'
    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.b.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))
    def setUp(self):
        self.b = login_B()
        self.obj_sp = Student_List(self.b)
        self.obj_ap = AddStudentPage(self.b)
    def tearDown(self):
        self.obj_ap.Close_url()


    def addstudent_verify(self,username,realname,password,sex,role,category,email,phone):
        try:
            self.obj_sp.enter_student_list()
            self.obj_ap.set_username_input(username)
            self.obj_ap.set_realname_input(realname)
            self.obj_ap.set_password_input(password)
            self.obj_ap.select_sex_radio(sex)
            self.obj_ap.select_role_select(role)
            self.obj_ap.select_start_student_input()
            self.obj_ap.upload_head_portrait()
            self.obj_ap.select_category_select(category)
            self.obj_ap.set_email_input(email)
            self.obj_ap.set_phone_input(phone)
            self.obj_ap.click_save_button()
            self.obj_ap.click_alert_confirm_button()
            self.obj_ap.click_comeback_button()
            msg = self.obj_sp.get_addstudent_success_msg()
            return msg
        except BaseException as msg:
            log = InsertLog_P()
            log.error(msg)

    def test_addstudent_success(self):
         '''成功添加学生账号测试'''
         sql="delete from xsmart_users where phone='13811112222'"
         Connection_MySQLData().DeleteData(sql)
         msg = self.addstudent_verify('13811112222','test007','123456',1,'全部开放','南通大学','xiaoxin@163.com','13811112222')
         self.assertEqual(msg,'13811112222')

if __name__ == '__main__':
    unittest.main(verbosity=2)