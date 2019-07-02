from selenium import webdriver
import unittest
from lib.Public_module import InsertLog_P
from lib.Public_module import GetSkipScripts_P
from lib.Public_module import GetSkipTestCases_P
from lib.Public_module import get_test_suite
import time
import yagmail
from BeautifulReport import BeautifulReport
bs='gc'
def creat_browser_driver(b=bs):
	try:
		if b=='gc':
			dv=webdriver.Chrome()
		elif b=='ff':
			dv=webdriver.Firefox()
		elif b=='ie':
			dv=webdriver.Ie()
		else:
			pass
		return dv
	except BaseException as msg:
		log=InsertLog_P()
		log.error(msg)
def run_test():
	try:
		dirpath='./scripts'
		# discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
		# dirpath = './scripts'
		discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
		#获取不需要执行的模块名称
		configpath='./po/config.xlsx'
		m=GetSkipScripts_P(configpath)
		#获取不需要执行的用例名称
		casepath='./testcase/测试用例.xlsx'
		n=GetSkipTestCases_P(casepath)
		#获取不需要执行的脚本
		s=get_test_suite(discover,m,n)
		currenttime = time.strftime('%y%m%d%H%M%S ')
		report_path='./report'
		report_name='report_' + currenttime
		result=BeautifulReport(s)
		result.report(filename=report_name, description='测试报告',log_path=report_path)
		# 链接邮箱服务器
		yag = yagmail.SMTP(user="1290337913@qq.com", password="tlsisumsgakajdda", host="smtp.qq.com")
		# 邮箱正文
		contents = '测试报告'
		# 发送邮件
		yag.send('1738951907@qq.com', '测试报告', contents, 'D:\\project\\work\\report\\{}.html'.format(report_name))
	except BaseException as msg:
		log=InsertLog_P()
		log.error(msg)
	
if __name__=='__main__':
	run_test()