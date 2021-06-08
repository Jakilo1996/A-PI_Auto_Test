# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     send_email
# Author:      Jakiro
# Datetime:    2020/12/10 14:15
# Description:
# -----------------------------------------------------------------------------------

# 封装发送邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 发送邮件模块，邮箱 为163邮箱，提供了可修改接收邮箱参数
class SendEmail(object):
    def send_email(self, report_path, title, receiver='17709005281@163.com;18781127115@163.com'):
        try:
            # #### 1、配置邮箱服务器信息 ####
            # (1)配置服务器主机名（地址）
            # SMTP, Simple Mail Transfer Protocol
            # 提供可靠且有效的电子邮件传输的协议
            # 是建立在FTP文件传输服务上的一种邮件服务
            smtp = 'smtp.163.com'
            # 配置端口
            # 不同邮箱服务器端口不同，163邮箱端口号：25
            port = '25'
            # 配置登录用户
            sender = '17709005281@163.com'
            # 配置邮箱的授权码
            # 此密码不是邮箱登陆密码，而是授权码
            # 获取授权码：邮箱网页：设置 --> POP3/SIMP/IMAP中，开启IMAP/SMTP服务、POP3/SMTP服务，手机确认后，获得授权码
            # 每次开启服务，授权码只能获取一次，需要记住
            auth_code = 'VFTNSCROJCRVSZVV'  # authorization 授权
            # 配置接收用户
            # (4)配置接收方
            # 如果接受方不变可以写死
            # receiver = '17709005281@163.com;18781127115@163.com'

            # #### 2、创建邮件对象 ####
            # 实例化邮箱对象 用来设置邮件的发送信息
            msg = MIMEMultipart()
            # (1)设置邮件抬头信息
            msg['from'] = sender  # 由谁发送
            msg['to'] = receiver  # 发送给谁
            msg['subject'] = title  # 邮件主题
            # (2)读取报告内容
            # 读取报告内容
            # 读取报告内容（.html）到body
            # 报告是以Bytes方式读入的，有的邮箱正文不能解析Bytes，需要将内容重编码成utf-8格式
            with open(report_path, mode='rb') as report:
                body = report.read().decode(encoding='utf8')

            # #### 3、编写正文 ####
            # (1)实例化MIMEText对象
            # 生成HTML类型的MIME文档，传入报告内容
            # MIME, Multipurpose Internet Mail Extensions 多用途互联网邮件扩展类型
            # 是指定某种扩展名的文件用一种应用程序来打开的方式类型
            # _subtype默认为plain，纯文本
            # _charset的编码方式要与body的encoding统一
            mime_text = MIMEText(body, 'html', 'utf8')
            # 2、(3)编写正文，写入邮件对象
            # 不同浏览器解析不同，显示的正文不同
            msg.attach(mime_text)  # 添加正文到邮箱对象

            # #### 4、添加附件 ####
            # (1)实例化MIMEText对象
            # 生成base64压缩文件类型的MIME文档，传入报告内容
            att = MIMEText(body, 'base64', 'utf8')
            # (2)指定附件类型
            # "Content-Type"指定附件类型：是纯文本
            # 服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，一般会默认使用浏览器打开
            # 比如txt、jpg文件，会直接在浏览器中显示
            att['Content-Type'] = 'application/octet-stream'
            # (3)提示选择文件的操作：保存并预览
            # "Content-Disposition"设置文件操作的可选项：保存并预览,添加邮件预览功能
            # 不设置可以保存，但无预览功能且文件为二进制格式
            # 选择预览文件，不会再用浏览器打开，而是会使用对应的程序打开（eg：txt-->记事本）
            # 预览并保存文件："attachment:filename = %s"%file_ath
            # filename指定文件名，必须带上文件后缀，否则生成的附件不是想要的格式
            att['Content-Disposition'] = 'attachment;filename = %s' % report_path
            # 2、(4)添加附件，写入右键对象
            msg.attach(att)

            # #### 5、发送邮件 ####
            # 发送邮件 实例化邮件传输协议对象 通过smtplib模块实例化SMTP对象
            # 实例化SMTP对象
            # （SMTP邮箱服务器类的对象）
            smtp1 = smtplib.SMTP()
            # 连接服务器
            # （传入服务器主机名（地址）、端口）
            smtp1.connect(smtp, port)
            # 登录服务器
            # （使用用户账号和密码（授权码）登录）
            smtp1.login(sender, auth_code)
            # 发送邮件
            # （传入发送方、接收方、邮件对象）
            # 接收方(单个：字符串，多个：元组或列表
            # msg.as_string()：邮件对象以字符串形式发送
            # 多个接收方需要分割成列表
            smtp1.sendmail(sender, receiver.split(';'), msg.as_string())
            # self.email_log.error("报告邮件发送成功")
            print("报告邮件发送成功")

        except Exception as e:
            # self.email_log.error("报告邮件发送失败")
            print("报告邮件发送失败，因为{}".format(e))


if __name__ == '__main__':
    # 实例化发送邮件类
    email_send = SendEmail()
    html_path = r'C:\Users\Administrator\codes\test\project\ranzhi_project\result\report\report-2020-12-09-17-22-51.html'
    email_send.send_email(html_path, 'send_email_test')
