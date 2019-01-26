#Sending multiple emails using email class
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Your email address & password
email = 'pqr@gmail.com'
password = 'pqr1234567890'

#Mentioned email address in the list
send_to_email = ['abc@gmail.com', 'xyz@gmail.com']

subject = 'test'
message = 'Message line'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = ', '.join(send_to_email)
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
except:
    print('Please enter valid Email or Password...!!')
else:
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print('Mail sent successfully...!!')
