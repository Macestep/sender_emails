import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

def send_email(recipients_emails: list, msg_text: str):
    sender = ''
    password = ''

    msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
    msg['Subject'] = Header('Важно!!!', 'utf-8')
    msg['From'] = sender
    msg['To'] = ', '.join(recipients_emails)
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    

    try:
    	server.starttls() 
    	server.login(sender, password)
    	server.sendmail(msg['From'], recipients_emails, msg.as_string())
    except Exception as ex:
    	print(ex)
    finally:
    	smtplib.SMTP('smtp.yandex.ru', 587).quit()

def main():
    
    send_email(recipients_emails = [''], msg_text = (' '))



if __name__ == '__main__':
	main()


