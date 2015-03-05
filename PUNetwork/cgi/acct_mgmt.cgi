#!/usr/bin/python

import cgi, string, sys, os, re, random
from os.path import expanduser
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
#import session

#Get Databasedir
HOMEDIR= expanduser("~")
DATABASE=HOMEDIR+"/PUNetwork/purdue_network.db"


############################################################
def generate_password_form(form):#add session parameter
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

<a href="login.cgi?action=back&username={user}">Back to Admin Options</a>
</FORM>
</BODY>
</HTML>
"""# add session to url above
    print_html_content_type()
    print(html.format(form["user"]=user))#add (session=session) to html.format parameter
#############################################################
def generate_delete_user_form(user): #add session to parameter
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

<a href="login.cgi?action=back&username={user}">Back to Admin Options</a>
</FORM>
</BODY>
</HTML>
"""#add session to url variables
    print_html_content_type()
    print(html.format(user=user)) #add session to html.format
#############################################################
def print_html_content_type():
    # Required header that tells the browser how to render the HTML.
    print("Content-Type: text/html\n\n")

######################################################
def change_password(form):
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()
    #sessions=form["session"].value
    users=form["user"].value
    oldPass=form["oldPassword"].value
    newPass=form["newPassword"].value
    newPassConf=form["newPasswordConfirm"].value
    c.execute('SELECT password FROM users WHERE user=?', users)
    passw = c.fetchone()
    if (passw[0] == oldPass):
        if (newPass == newPassConf):
            c.execute('UPDATE users SET password = ? WHERE user_name = ?', (newPass,users))

    else:
        generate_password_form(users)#add sessions to parameters
        print("<H3><font color=\"red\">Passwords do not match</font></H3>")
            

###################################################################
# Define function to test the password.
def check_password(user, passwd):

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    t = (user,)
    c.execute('SELECT password FROM users WHERE user_name=?', t)

    stored_password=c.fetchone()
    conn.close();

    if (stored_password[0]==passwd):
        return "passed"

    return "failed"
######################################################
#def delete_user(form):

######################################################
#def check_sessions(form):
    #return session.check_session(form)
########################################################
def generate_acct_mgmt_form(form):#add session to this?
    html="""
<HTML>
<HEAD>
<TITLE>PUNetwork</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>PUNetwork Account Management Page</H2></center>

<H3>Account Options</H3>

<TABLE BORDER = 0>
<FORM METHOD=post ACTION="acct_mang.cgi">
<TR><TH>Type Password:</TH><TD><INPUT TYPE=password NAME="changePassword"></TD></TR>
<TR><TH>Confirm Password:</TH><TD><INPUT TYPE=password NAME="changePasswordConfirm"></TD></TR>
</TABLE>

<INPUT TYPE=hidden NAME="action" VALUE="delete_user">
<INPUT TYPE=submit VALUE="Delete Account">

<a href="login.cgi?action=back&username={user}">Back to Admin Options</a>
</FORM>
</BODY>
</HTML>
"""#add session to url variables
    print_html_content_type()
    print(html.format(user=user)) #add session to html.format
##########################################################
def main():
    mangform=cgi.FieldStorage()
    generate_acct_mgmt_form(mangform)
    isTrue= "passed" #check_sessions(mangform)
    if isTrue == "passed":
        usera=mangform["user"].value
#       sessiona=mangform["session"].value
        if "action" in mangform:
            action=mangform["action"].value
            if action == "delete_account":
                generate_delete_user_form(usera)#add sessiona to parameter
            elif action == "change_password":
                generate_password_form(usera)#add sessiona to parameter
            elif action == "change":
                change_password(mangform)
#            elif action == "delete_user":
#                delete_user(mangform)
        else:
            generate_password_form(usera)#add sessiona to parameters
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