#!/usr/bin/python

# Import the CGI, string, sys modules
import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session

#Get Databasedir
HOMEDIR= expanduser("~")
DATABASE=HOMEDIR+"/PUNetwork/purdue_network.db"

##############################################################
# Define function to generate login HTML form.
def login_form():
    html="""
<HTML>
<HEAD>
<TITLE>PictureShare</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>PictureShare Login Page</H2></center>

<H3>Type Username and Password:</H3>

<TABLE BORDER = 0>
<FORM METHOD=post ACTION="login.cgi">
<TR><TH>Username:</TH><TD><INPUT TYPE=text NAME="username"></TD><TR>
<TR><TH>Password:</TH><TD><INPUT TYPE=password NAME="password"></TD></TR>
</TABLE>

<INPUT TYPE=hidden NAME="action" VALUE="login">
<INPUT TYPE=submit VALUE="Enter">
<a href="new_account.cgi">Create a New Account</a>
</FORM>
</BODY>
</HTML>
"""
    print_html_content_type()
    print(html)
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


#################################################################
def create_new_session(user):
    return session.create_session(user)

######################################################
# Diplay the options of admin
def display_admin_options(user, session):
    html="""
<HTML>
<HEAD>
<TITLE>Admin Options</TITLE>
</HEAD>

<BODY BGCOLOR = white>

<center><H2>Select what you would like to do</H2></center>

<TABLE BORDER = 0>
<H1>Picture Share Admin Options</H1>
<ul>
<H2>Account Management</H2>

<li> <a href="acct_mang.cgi?action=delete_account&user={user}&session={session}">Delete Your Account</a>
<li> <a href="acct_mang.cgi?action=change_password&user={user}&session={session}">Change Password</a>
<hr>
<H2>Manage Pictures and Albums</H2>

<li> <a href="manage_pics.cgi?action=new_album&user={user}&session={session}">Create new album</a>
<li> <a href="manage_pics.cgi?action=upload&user={user}&session={session}">Upload Picture</a>
<li> <a href="manage_pics.cgi?action=delete_album&user={user}&session={session}">Delete Album</a>
<li> <a href="manage_pics.cgi?action=make_album_public&user={user}&session={session}">Make Album Public or Private</a>
<hr>
<a href="browse.cgi?action=browse_albums&user={user}&session={session}">Browse Public Albums</a>

</ul>
"""
        #Also set a session number in a hidden field so the
        #cgi can check that the user has been authenticated

    print("Content-Type: text/html\n\n")
    print(html.format(user=user,session=session))
#############################################################
def print_html_content_type():
	# Required header that tells the browser how to render the HTML.
	print("Content-Type: text/html\n\n")

##########################################################
# Define main function.
def main():
    loginform = cgi.FieldStorage()
    if "action" in loginform:
        action=loginform["action"].value
        #print("action=",action)
        if action == "login":
            if "username" in loginform and "password" in loginform:
                #Test password
                username=loginform["username"].value
                password=loginform["password"].value
                if check_password(username, password)=="passed":
                    session=create_new_session(username)
                    display_admin_options(username,session)
                    
                else:
                    login_form()
                    print("<H3><font color=\"red\">Incorrect user/password</font></H3>")
            else:
                login_form()
                print("<H3><font color=\"red\">Incorrect user/password</font></H3>")
        elif action == "back":
            user=loginform["username"].value
            session=loginform["session"].value
            display_admin_options(user,session)
        else:
            login_form()
    else:
        login_form()

###############################################################
# Call main function.
main()