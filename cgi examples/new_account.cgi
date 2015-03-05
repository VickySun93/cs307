#!/usr/bin/python

import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session
import smtplib
from email.mime.text import MIMEText


#Get Databasedir
MYLOGIN="skercher"
DATABASE="/homes/"+MYLOGIN+"/PictureShareDB/picture_share.db"
IMAGEPATH="/homes/"+MYLOGIN+"/PictureShareDB/images"

######################################################
def new_acct_form():
	newacct="""
<HTML>
<HEAD>
<TITLE>Create a new Account</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>Please enter a valid email address and a password</H2></center>

<H3>Type Email and Password:</H3>

<TABLE BORDER = 0>
<FORM METHOD=post ACTION="new_account.cgi">
<TR><TH>Email:</TH><TD><INPUT TYPE=text NAME="username"></TD><TR>
<TR><TH>Password:</TH><TD><INPUT TYPE=password NAME="password"></TD></TR>
<TR><TH>Confirm Password:</TH><TD><INPUT TYPE=password NAME="passwordconf"></TD></TR>
</TABLE>

<INPUT TYPE=hidden NAME="action" VALUE="newaccount">
<INPUT TYPE=submit VALUE="Create">
<a href="login.cgi">Return to Login Screen</a>
</FORM>
</BODY>
</HTML>
"""
	print_html_content_type()
	print(newacct)
#############################################################
def print_html_content_type():
	# Required header that tells the browser how to render the HTML.
	print("Content-Type: text/html\n\n")
########################################################
def send_confirm(user):
	fromaddr = "skercher@cs.purdue.edu"
	body = """
Please copy and paste the link below into a web browser:
http://data.cs.purdue.edu:3431/PictureShareDB/login.cgi
****Do Not Reply to this Email***
"""
	msg = MIMEText(body)
	s = smtplib.SMTP("localhost")
	s.set_debuglevel(1)
	s.sendmail(fromaddr, user, msg.as_string())
	s.quit()

####################################################
def main():
	acctform=cgi.FieldStorage()
	conn = sqlite3.connect(DATABASE)
	c=conn.cursor()
	if "action" in acctform:
		action=acctform["action"].value
		if action == "newaccount":
			if "username" in acctform and "password" in acctform and "passwordconf" in acctform:
				username=acctform["username"].value
				password=acctform["password"].value
				passwordconf=acctform["passwordconf"].value
				c.execute('SELECT * FROM users')
				for newUser in c:
					if newUser[0] != username:
						isOkay = True
						continue
					else:
						isOkay = False
						break
				if password != passwordconf:
					new_acct_form()
					print("<H3><font color=\"red\">Passwords do not match</font></H3>")
				elif isOkay == False: 
					new_acct_form()
					print("<H3><font color=\"red\">Email already used</font></H3>")
					
				else:
					new_acct_form()
					print("<H3><font color=\"green\">Please check your email for a confirmation</font></H3>")
					send_confirm(username)
					path = "/home/u94/skercher/PictureShareDB/images/"+username
					os.mkdir(path, 755)
					c.execute('INSERT INTO users VALUES (?,?)',(username,password))
			else:
				new_acct_form()
				print("<H3><font color=\"red\">Please fill in all fields</font></H3>")
	else:
		new_acct_form()
	conn.commit()
	conn.close()
###########################################
#Call the main function
main()
