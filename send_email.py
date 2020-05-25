from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def main():

    try:
        msg = MIMEMultipart()

        msg['From'] = 'dhruvkhannastar@gmail.com'
        msg['To'] = 'contact@rdciti.com'
        msg['Subject'] = 'This is a test'

        message = "Hello! this is test message..."

        msg.attach(MIMEText(message))

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('emailID', 'pass')

        s.send_message(msg)

        print("Email sent successfully")

    except Exception as e:
        print('There is an error: {0}'.format(repr(e)))

if __name__ == '__main__':
    main()