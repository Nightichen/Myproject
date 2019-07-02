from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po.login import Login

class Student_List(Login):
	"""学生列表页面"""
	# 对象层
	btn_menbercenter_loc = (By.LINK_TEXT, u'会员中心')
	lnk_studentlist_loc = (By.LINK_TEXT, u'学生列表')
	iframe_main_loc = (By.ID, 'mainframe')
	btn_addstudent_loc = (By.LINK_TEXT, u'添加学生')
	msg_phone_number_loc = (By.XPATH, ".//*[@id='recordList']/tr[1]/td[2]")
	lnk_logout_loc = (By.XPATH, ".//*[@id='header']/p/a[3]")
	#操作层
	def enter_student_list(self):
		self.b.find_element(*self.btn_menbercenter_loc).click()
		self.b.find_element(*self.lnk_studentlist_loc).click()
		obj = self.b.find_element(*self.iframe_main_loc)
		WebDriverWait(self.b, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(obj))
		self.b.find_element(*self.btn_addstudent_loc).click()
	def get_addstudent_success_msg(self):
		ele = WebDriverWait(self.b, 10, 0.5).until(EC.visibility_of_element_located(self.msg_phone_number_loc))
		return ele.text
	
	def click_logout_button(self):
		self.b.find_element(*self.lnk_logout_loc).click()