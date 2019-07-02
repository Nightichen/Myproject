import yagmail
import time
yag = yagmail.SMTP( user="1290337913@qq.com", password="tlsisumsgakajdda", host="smtp.qq.com")
# yag = yagmail.SMTP( user="ju1290337913@126.com", password="Xdj567875", host='smtp.126.com')
currenttime = time.strftime('%y%m%d%H%M%S ')
report_name='report_' + currenttime
file='D:\\project\\work\\report\\{}.html'.format(report_name)
dd='D:\\project\\work\\report\\report_190610155824 .html'
print(dd)
print(file)
# 邮箱正文
contents ='test001'
# 发送邮件
# yag.send('jun15397897901@outlook.com', '测试报告', contents, 'D:\project\work\report\{}.html'.format(report_name))
yag.send('ju1290337913@126.com', '测试报告', contents, 'D:\\project\\work\\report\\report_190610155824 .html')

