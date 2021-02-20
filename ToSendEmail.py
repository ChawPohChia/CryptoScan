import yagmail
from datetime import datetime

def sendEmail(content):
    user = 'cryptoscan123@gmail.com'
    app_password = 'cryptoscan321'
    to = 'chawchia@hotmail.co.uk'

    now = datetime.now()
    currentTimeInStr = now.strftime("%d/%m/%Y %H:%M")

    subject = 'Crytoscan Report - '+ currentTimeInStr

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully on '+currentTimeInStr)





