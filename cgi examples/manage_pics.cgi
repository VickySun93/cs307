import cgi, string, sys, os, re, random
import cgitb; cgitb.enable()  # for troubleshooting
import sqlite3
import session

#Get Databasedir
MYLOGIN="skercher"
DATABASE="/homes/"+MYLOGIN+"/PictureShareDB/picture_share.db"
IMAGEPATH="/homes/"+MYLOGIN+"/PictureShareDB/images"

######################################################
def make_album_public(form):
    #Check session is correct
    if (session.check_session(form) != "passed"):
        login_form()
        return

##############################################################
def delete_album(form):
    #Check session is correct
    if (session.check_session(form) != "passed"):
        login_form()
        return

#######################################################

def upload_pic_data(form):
    #Check session is correct
    if (session.check_session(form) != "passed"):
        login_form()
        return

    #Get file info
    fileInfo = form['file']

    #Get user
    user=form["user"].value
    s=form["session"].value

    # Check if the file was uploaded
    if fileInfo.filename:
        # Remove directory path to extract name only
        fileName = os.path.basename(fileInfo.filename)
        open(IMAGEPATH+'/user1/test.jpg', 'wb').write(fileInfo.file.read())
        image_url="login.cgi?action=show_image&user={user}&session={session}".format(user=user,session=s)
        print_html_content_type()
	print ('<H2>The picture ' + fileName + ' was uploaded successfully</H2>')
        print('<image src="'+image_url+'">')
    else:
        message = 'No file was uploaded'
        
###############################################################################

def upload(form):
    if session.check_session(form) != "passed":
       login_form()
       return

    html="""
        <HTML>

        <FORM ACTION="login.cgi" METHOD="POST" enctype="multipart/form-data">
            <input type="hidden" name="user" value="{user}">
            <input type="hidden" name="session" value="{session}">
            <input type="hidden" name="action" value="upload-pic-data">
            <BR><I>Browse Picture:</I> <INPUT TYPE="FILE" NAME="file">
            <br>
            <input type="submit" value="Press"> to upload the picture!
            </form>
        </HTML>
    """

    user=form["user"].value
    s=form["session"].value
    print_html_content_type()
    print(html.format(user=user,session=s))

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

##############################################################
def new_album(form):
    #Check session
    if session.check_session(form) != "passed":
        return

    html="""
        <H1> New Album</H1>
        """
    print_html_content_type()
    print(html);
