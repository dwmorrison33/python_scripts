'''
	This is a script that will allow you to query data from a
	database and use inside of a message to emails.
	One method uses text only, and the other is for sending emails
	with a html file.
	Its pretty cool, you should try it for yourself
	I have changed alot of wording in this script so that it is not known
	who I sent this mass emailer out too.
'''
import MySQLdb
import smtplib
from pprint import pprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

db = MySQLdb.connect('localhost',
					'email_user',
					'YouWillNeverKnow',
					'emailer')
c = db.cursor()

def send_email_with_text_only(fromaddr, password, table_name):
	c.execute("SELECT * FROM {0} WHERE unsubscribed<>1;".format(table_name))
	emails_in_db = c.fetchall()
	for emailer in emails_in_db:
		if emailer[0]:
			#check to see if a particular user_type is in db
			if 'special_user' in emailer[4]:
				whole_name = emailer[2]
				whole_toaddr = emailer[3]
				message_name = emailer[5]
				msg = MIMEMultipart('alternative')
				msg['Subject'] = "This is the subject"
				msg['From'] = fromaddr
				msg['To'] = toaddr
				text = "Hi %s,\n\nMy name is David and I am emailing you find out if this " \
				       "will work? And I know it does cause I already tested it. YAY " \
				       "\n\nI wanted to see how this formatted with new lines added in " \
				       "for %s, specifically if it works. " \
				       "\n\nNew paragraphs are a great to split up this email  " \
				       "If you have any questions, please contact me." \
				       "\n\nThank You," \
				       "\n\nDavid Morrison" % (whole_name, message_name)			
				msg.attach(MIMEText(text, 'plain'))			
				server = smtplib.SMTP('smtp.office365.com', 587)
				server.ehlo()
				server.starttls()
				server.login(fromaddr, password)
				server.sendmail(fromaddr, toaddr, msg.as_string())
				server.close()
				print "Yay the email sent to " + toaddr

send_email_with_text_only("dmorris@gmail.com", "LikeISaidUwillNeverKnow", "saved_emails")

def send_email_with_html(fromaddr, password):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "This is the subject"
	msg['From'] = fromaddr
	msg['To'] = 'daveyboy@gmail.com'
	message = open('/home/david/email_location/email_templates/email.html','rb').read()
	msg.attach(MIMEText(message, 'html'))		
	server = smtplib.SMTP('smtp.office365.com', 587)
	server.ehlo()
	server.starttls()
	server.login(fromaddr, password)
	server.sendmail(fromaddr, 'daveyboy@gmail.com', msg.as_string())
	server.close()
	print "The email was sent to: " + toaddr

send_email_with_html("dmorris@gmail.com", "LikeISaidUwillNeverKnow")