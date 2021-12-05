import smtplib
from email.message import EmailMessage

def email_alert(news, reason, to, name,email,mobile):
    msg = EmailMessage()
    body = 'Phone: {}\n'.format(mobile) + "Email: {}\n".format(email) +  'News: {}\n'.format(news)
    msg.set_content(body)
    # Name = name
    # Mobile = mobile
    msg['subject'] = '{} : {}'.format(name, reason) 
    msg['to'] = to
    
    user = "reefoundation05@gmail.com"
    msg['from'] = user
    password = "mjzwvvutnukqcyed"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
    
# if __name__ == '__main__':
#     email_alert('Hey', 'Hello World', 'nrainer001@gmail.com')