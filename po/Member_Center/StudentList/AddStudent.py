import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from po.login import Login


class AddStudentPage(Login):
    """添加学生页面"""
    ##对象层##
    ipt_username_loc = (By.ID,'username')
    ipt_realname_loc = (By.ID,'realname')
    ipt_password_loc = (By.ID,'password')
    radio_sex_loc = (By.XPATH,".//*[@id='form']/div/div[4]/div")
    select_role_loc = (By.NAME,"roleid")
    ipt_start_student = (By.ID,"isstart")
    #上传头像模块
    btn_upload_loc = (By.LINK_TEXT,'上传头像')
    btn_local_loc = (By.XPATH,"html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]")
    # btn_browse_parent_object_loc = (By.CLASS_NAME,"ke-upload-area")
    # btn_browse_loc = (By.TAG_NAME,'input')
    
    btn_confirm_loc = (By.XPATH,"/html/body/div[3]/div[1]/div[3]/span[1]/input")

    select_category_loc = (By.ID,'oneCategory')
    ipt_email_loc = (By.ID,'email')
    ipt_phone_loc = (By.ID,'phone')
    btn_save_loc = (By.ID,'btn_sub')
    btn_comeback_loc = (By.CLASS_NAME,"btn-general")

    ##操作层##
    def set_username_input(self,value):
        '''输入用户名'''
     ## WebDriverWait(self.b,10,0.5).until(EC.visibility_of_element_located(By.CLASS_NAME,'main-cont'))
        self.b.find_element(*self.ipt_username_loc).send_keys(value)

    def set_realname_input(self, value):
        '''输入昵称'''
        self.b.find_element(*self.ipt_realname_loc).send_keys(value)

    def set_password_input(self, value):
        '''输入登录密码'''
        self.b.find_element(*self.ipt_password_loc).send_keys(value)

    def select_sex_radio(self, sex=0):
        '''选择性别'''
        rd = self.b.find_element(*self.radio_sex_loc)
        sx = sex
        if sx == 1:
            rd.find_element_by_xpath('//input[@value="1"]').click()
        elif sx == 2:
            rd.find_element_by_xpath('//input[@value="2"]').click()
        elif sx == 0:
            rd.find_element_by_xpath('//input[@value="0"]').click()

    def select_role_select(self, text):
        '''选择角色'''
        s = self.b.find_element(*self.select_role_loc)
        Select(s).select_by_visible_text(text)

    def select_start_student_input(self):
        '''选择明星学员'''
        self.b.find_element(*self.ipt_start_student).click()

    def upload_head_portrait(self):
        '''上传头像操作'''
        self.b.find_element(*self.btn_upload_loc).click()
        self.b.find_element(*self.btn_local_loc).click()
        # tpm = self.b.find_element(*self.btn_browse_parent_object_loc)
        # obj = tpm.find_elements(*self.btn_browse_loc)[1]
        btn_browse_loc = self.b.find_elements_by_class_name('ke-upload-area')[1]
        ActionChains(self.b).click(btn_browse_loc).perform()
        os.system(r"D:\project\work\po\Member_Center\StudentList\upload\aa.exe")
        self.b.find_element(*self.btn_confirm_loc).click()

    def select_category_select(self, text):
        s = self.b.find_element(*self.select_category_loc)
        Select(s).select_by_visible_text(text)

    def set_email_input(self, value):
        self.b.find_element(*self.ipt_email_loc).send_keys(value)

    def set_phone_input(self, value):
        self.b.find_element(*self.ipt_phone_loc).send_keys(value)

    def click_save_button(self):
        tmp = self.b.find_element(*self.btn_save_loc)
        ele = WebDriverWait(self.b,10,0.5).until(EC.visibility_of_element_located(self.btn_save_loc))
        js = "window.scrollTo(0,10000)"
        self.b.execute_script(js)
        ele.click()
        # time.sleep(10)

    def click_alert_confirm_button(self):
        WebDriverWait(self.b, 10, 0.5).until(EC.alert_is_present())
        self.b.switch_to.alert.accept()

    def click_comeback_button(self):
        ele = self.b.find_element(*self.btn_comeback_loc)
        self.b.execute_script("arguments[0].scrollIntoView();", ele)
        ele.click()

if __name__ == '__main__':
    pass

