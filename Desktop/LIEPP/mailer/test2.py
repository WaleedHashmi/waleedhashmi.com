
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'LIEPPTEST001@gmail.com'
email_password = 'uEwn#bhGUsdJj!2&ejNAer_!xweF4av-'
email_send = 'morgane.laouenan@sciencespo.fr'

subject = 'Test Email sent from the script'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi Morgane! \n\n This is the test email sent from the python script. I have also attached a sample file. For the future we can attach this script to a list of emails and resumes, which this script can run over. For the time complexity of this script, it is taking a on average 7.5 seconds to send one email, I expect this time to go up to 20 seconds when an actual resume is generated. On friday, I will start working on the website with this email. \nBest Regards, \n\nWaleed Hashmi'
msg.attach(MIMEText(body,'plain'))

filename='cv.pdf'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
