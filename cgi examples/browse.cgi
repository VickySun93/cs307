import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session

#Get Databasedir
MYLOGIN="skercher"
DATABASE="/homes/"+MYLOGIN+"/PictureShareDB/picture_share.db"
IMAGEPATH="/homes/"+MYLOGIN+"/PictureShareDB/images"

######################################################

##############################################################
def show_image(form):
    #Check session
    if session.check_session(form) != "passed":
        login_form()
        return

    # Your code should get the user album and picture and verify that the image belongs to this
    # user and this album before loading it

    #username=form["username"].value

    # Read image
    with open(IMAGEPATH+'/user1/test.jpg', 'rb') as content_file:
        content = content_file.read()

    # Send header and image content
    hdr = "Content-Type: image/jpeg\nContent-Length: %d\n\n" % len(content)
    print hdr+content
