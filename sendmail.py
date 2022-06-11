##
#  copy this code and paste in on lambda function folder
#  then call the sendmail() function inside the lambda function.
##

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import codecs

def send(Text):
    strFrom = 'ebrarawsbot@gmail.com'
    password = 'lzjpccikekslitam'
    strTo = ['ebrar.karademir@englishhome.com.tr']
    #strTo='korhanozdemir90@gmail.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'E MAIL AUTOMATION'
    msgRoot['From'] = strFrom
    msgRoot['To'] = ",".join(strTo)

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(Text,'html')
    msgAlternative.attach(msgText)

   # ust_fp = open('/home/ReviewDetectorbot/.local/mail/ust.png', 'rb')
    #msgust = MIMEImage(ust_fp.read())
    #ust_fp.close()
    #msgust.add_header('Content-ID', '<ust>')
    #msgRoot.attach(msgust)
    #alt_fp = open('/home/ReviewDetectorbot/.local/mail/alt.png', 'rb')
    #msgalt = MIMEImage(alt_fp.read())
    #alt_fp.close()

    #msgalt.add_header('Content-ID', '<alt>')
    #msgRoot.attach(msgalt) 

    import smtplib
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login(strFrom, password=password)
    print('Login success!')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    print('Mail send!')
    smtp.quit()


f = codecs.open("templates/message.html", 'r')

send(f.read())