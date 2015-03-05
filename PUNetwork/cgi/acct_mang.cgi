#!/usr/bin/python

import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session
from os.path import expanduser

#Get Databasedir
HOMEDIR= expanduser("~")
DATABASE=HOMEDIR+"/PUNetwork/purdue_network.db"


############################################################
def generate_password_form(user,session):
    html="""
<HTML>
<HEAD>
<TITLE>PictureShare</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>PictureShare Account Management Page</H2></center>

<H3>Type Old Password and Confirm New Password:</H3>

<TABLE BORDER = 0>
<FORM METHOD=post ACTION="acct_mang.cgi">
<TR><TH>Old Password:</TH><TD><INPUT TYPE=password NAME="oldPassword"></TD><TR>
<TR><TH>New Password:</TH><TD><INPUT TYPE=password NAME="newPassword"></TD></TR>
<TR><TH>Confirm New Password:</TH><TD><INPUT TYPE=password NAME="newPasswordConfirm"></TD></TR>
</TABLE>

<INPUT TYPE=hidden NAME="action" VALUE="change">
<INPUT TYPE=submit VALUE="Change Password">

<a href="login.cgi?action=back&username={user}&session={session}">Back to Admin Options</a>
</FORM>
</BODY>
</HTML>
"""
    print_html_content_type()
    print(html.format(user=user,session=session))
#############################################################
def generate_delete_user_form(user, session):
    html="""
<HTML>
<HEAD>
<TITLE>PictureShare</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>PictureShare Account Management Page</H2></center>

<H3>Type your password and confirm it to delete your account</H3>

<TABLE BORDER = 0>
<FORM METHOD=post ACTION="acct_mang.cgi">
<TR><TH>Type Password:</TH><TD><INPUT TYPE=password NAME="changePassword"></TD></TR>
<TR><TH>Confirm Password:</TH><TD><INPUT TYPE=password NAME="changePasswordConfirm"></TD></TR>
</TABLE>

<INPUT TYPE=hidden NAME="action" VALUE="delete_user">
<INPUT TYPE=submit VALUE="Delete Account">

<a href="login.cgi?action=back&username={user}&session={session}">Back to Admin Options</a>
</FORM>
</BODY>
</HTML>
"""
    print_html_content_type()
    print(html.format(user=user,session=session))
#############################################################
def print_html_content_type():
    # Required header that tells the browser how to render the HTML.
    print("Content-Type: text/html\n\n")

######################################################
def change_password(form):
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()
    sessions=form["session"].value
    users=form["user"].value
    oldPass=form["oldPassword"].value
    newPass=form["newPassword"].value
    newPassConf=form["newPasswordConfirm"].value
    c.execute('SELECT password FROM users WHERE user=?', users)
    passw = c.fetchone()
    if (passw[0] == oldPass):
        if (newPass == newPassConf):
            c.execute('UPDATE users SET password = ? WHERE email = ?', (newPass,users))

    else:
        generate_password_form(users,sessions)
        print("<H3><font color=\"red\">Passwords do not match</font></H3>")
            

###################################################################
# Define function to test the password.
def check_password(user, passwd):

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    t = (user,)
    c.execute('SELECT * FROM users WHERE email=?', t)

    row = stored_password=c.fetchone()
    conn.close();

    if row != None: 
        stored_password=row[1]
    if (stored_password==passwd):
        return "passed"

    return "failed"
######################################################
#def delete_user(form):

######################################################
def check_sessions(form):
    return session.check_session(form)
##########################################################
def main():
    mangform=cgi.FieldStorage()
    isTrue=check_sessions(mangform)
    if isTrue == "passed":
        usera=mangform["user"].value
        sessiona=mangform["session"].value
        if "action" in mangform:
            action=mangform["action"].value
            if action == "delete_account":
                generate_delete_user_form(usera,sessiona)
            elif action == "change_password":
                generate_password_form(usera,sessiona)
            elif action == "change":
                change_password(mangform)
#            elif action == "delete_user":
#                delete_user(mangform)
        else:
            generate_password_form(usera,sessiona)
    else:
        goBack="""
<center><H1>Please Log in to use this Feature</H1></center>
<a href="login.cgi?action=login">Return to Login Screen</a>
"""
        print_html_content_type()
        print(goBack)




######################################################
# Call Main Function
main()