from run import creat_browser_driver

edu_url = 'http://localhost/admin.php'

class Login():
	def __init__(self,dv=''):
		b=dv
		if b=='':
			self.b=creat_browser_driver()
			self.b.implicitly_wait(30)
			self.b.maximize_window()
		else:
			self.b=b
			
	def Open_url(self,url=edu_url):
		self.b.get(url)
		
		
	def Close_url(self):
		self.b.quit()