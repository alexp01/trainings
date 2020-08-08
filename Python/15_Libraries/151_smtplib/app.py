
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/10057972#overview

import smtplib
from email.message import EmailMessage

email_content = """
Un email trimis prin python

regards
Cucu
"""
email = EmailMessage()
email['Subject'] = 'sugi o ceapa'
email['From'] = 'alexpostole01@gmail.com'
email['To'] = 'alexpostole01@gmail.com'
email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('andrei.matache01@gmail.com', 'crocodil2011')

smtp_connector.send_message(email)
