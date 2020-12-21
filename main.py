import smtplib                     # smtp  -  Simple Mail Transfer Protocol
import config

def send_mail(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.toMail,message) #config.py is a seperate file in the same directory with the email address and password
        server,quit()
    except:
        print("Email failed to be sent")
    print("Email Sent Sucessfully")

subject = 'Test Subject'
msg = 'Hello This is testmail for checking the python script'
send_mail(subject,msg)
        


