Last edited by Stephen Kercher, 3/2/15 at 8:36PM



For our project, we have run into a few snags using the most updated version of Apache,
so we have reverted to a version that we know is stable.  This version is 2.2.17.  In order to get this on your
CS directory, follow the directions in this readme.

(If working in the CS linux(not windows) lab, ignore step 1)

1.SSH(Putty or Cyberduck or WinSCP or whatever) into data.cs.purdue.edu
and log in with your Purdue Career Account and Password.

2. Open a web browser and go to https://www.cs.purdue.edu/homes/cs390lang/python/

3.  Click on "Lab Handouts" on the left side of the screen

4.  Click the link "Lab1:Pete Twitt"

5.  Follow the directions(starting with step 1) up through step 4(the "Write your first CGI scipt" step)

6.  In your home directory(<username>/...) create a folder/directory named "PUNetwork".

7.  In the httpd.conf in "~/apache/conf/", look for the line that looks like:


	#
	# DocumentRoot: The directory out of which you will serve your
	# documents. By default, all requests are taken from this directory, but
	# symbolic links and aliases may be used to point to other locations.
	#
	DocumentRoot "/homes/skercher/apache/htdocs"

	^^^^^^^^^^^^


  Change that line to:

	DocumentRoot "/homes/<username>/PUNetwork/cgi"

  where <username> is your username without the "<>".

This is where you will put all of your .cgi files for now until we figure out a better organization strategy.



8.  In the httpd.conf, find the line that looks like:


	#
	# Note that from this point forward you must specifically allow
	# particular features to be enabled - so if something's not working as
	# you might expect, make sure that you have specifically enabled it
	# below.
	#
	
	#
	# This should be changed to whatever you set DocumentRoot to.
	#
	<Directory "/homes/skercher/apache/htdocs">
	
	^^^^^^^^^^^^^^
	
    Change this line to be:

	<Directory "/homes/<username>/PUNetwork/cgi">

    where <username> is your username without the "<>"



9.  Move the index.html from "/homes/<username>/apache/htdocs" to "/homes/<username>/PUNetwork/cgi"


For the port number in step 2 of apache setup, use a port number that is large and not easily guessed.  So don't use something like 1111 or 1234.
Instead, use something like 2957 so that someone doesn't accidentally use the same port as you.

Any extra files that you write with the .cgi extension will need to have its permissions changed(as done in step 4 of 
installing apache) so that it is executable by everyone.  Make sure to do this or that script wont run at all.
