from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po.login import Login

class Login_page(Login):
	#对象层
	ipt_username_loc = (By.ID, 'username')
	ipt_password_loc = (By.ID, 'password')
	btn_login_loc = (By.XPATH, '//*[@id="loginFrm"]/input')
	msg_login_success_loc = (By.XPATH, '//*[@id="header"]/p/span[1]/strong')
	msg_login_username_error_loc = (By.ID, 'username_msg')
	#操作层
	def set_username(self, username):
		self.b.find_element(*self.ipt_username_loc).clear()
		self.b.find_element(*self.ipt_username_loc).send_keys(username)
	
	def set_password(self, password):
		self.b.find_element(*self.ipt_password_loc).clear()
		self.b.find_element(*self.ipt_password_loc).send_keys(password)
	
	def click_login_button(self):
		self.b.find_element(*self.btn_login_loc).click()
	
	def get_login_success_msg(self):
		r = self.b.find_element(*self.msg_login_success_loc).text
		return r
	
	def get_login_username_empty_msg(self):
		WebDriverWait(self.b, 10, 0.5).until(
			EC.text_to_be_present_in_element(self.msg_login_username_error_loc, '帐号或密码不能为空'))
		r = self.b.find_element(*self.msg_login_username_error_loc).text
		return r
	
