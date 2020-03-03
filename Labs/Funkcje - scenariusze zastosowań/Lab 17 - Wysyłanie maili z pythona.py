import smtplib
import sys

mail_From = 'Tomasz'
mail_To = 'tomasz.matuszewski8802@gmail.com'
mail_Subject = 'Test'
mailBody = '''To jest mail probny
do Tomasza Matuszewskiego z pythona'''

message = ''' From {}
Subject{}
{}'''.format(mail_From,mail_Subject,mailBody)

user = 'tomasz.matuszewski8802@gmail.com'
password = 'Myczkow123@'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com','465')
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mail_To,message)
    server.close()
    print('Mail sent')
except:
    print('Error send mail!!',sys.exc_info())
    
