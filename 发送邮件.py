import yagmail


"""
to : 用来指定发送的对象即收件人
subject : 邮件主题
contents : 邮件内容,即正文.一般为字符串
attachments : 附件,有多个附件时用列表
cc : 抄送邮件，将邮件同时发送给收件人以外的人
"""
# 发件人
username = '***********@163.com'
# 授权码密码
password = '****************'
# 创建yagmail服务,需要加上服务器地址
server = yagmail.SMTP(username, password, host='smtp.163.com')
# 收件人
receivers = '***********@163.com'
text = '这是测试报告内容'  # 报告内容
title = '自动化测试报告'  # 邮件标题
img = yagmail.inline('../PyDemo/test/0.jpg')  # 把图片显示到正文
fujian = '../PyDemo/test/0.jpg'
server.send(contents=[text, img], to=receivers, subject=title, attachments=fujian)
