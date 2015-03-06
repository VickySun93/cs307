Last edited by Stephen Kercher, 3/2/15 at 9:01PM

As I am sure most of you know, we are using SourceTree to keep all of our file updated
 and so we all have very updated versions of what each other is doing.

Remember that all files must be saved in the directory that SourceTree is working out of(typically named cs307 for most of us)

The most common buttons we will use and their descriptions of use are below.

Outgoing:
 In order to use the commit button, you will need to first go to the tab at the bottom of SourceTree that says "File Status"
and click it.  Now, you will need to click the checkboxes next to the files you want to send to everyone and wait a couple
seconds for the program to do what it needs to.  After you have selected all the files you want to send, follow the buttons below.


   Commit(Top Left): Pressing this will permanently save the changed files on your computer, but not on other people's computers.
	Make sure that you leave a comment for your commit so that people know what you updated when you committed.
	To fully commit after typing your comment, the commit button to push will be in the bottom right of the program

   Push(Top Middle):  Only use this after committing something.  Pressing this will save the changes on other people's computers.
	Make sure you actually want to do this because there is no "undo" button if you push something that you didn't mean to.

Incoming:

   Fetch(Top Middle):  Brings in what other people have commited and pushed, basically as a preview.  Does not change the files on your
	computer, only gives a preview of what will change.

   Pull(Top Middle):  Pressing this will make changes to the files on your computer based on what other people have commited.  It makes
	permanent the changes that are previewed by "Fetch".  This button can be pressed without needing to press "Fetch",
	you just don't get a preview before it saves.



Unfortunately, given the circumstances, not everything is automated.

We will need to move the files to our data.cs.purdue.edu home directory by hand each time we make a "Pull" request so that our
personal local apache servers are all running the most up-to-date code that we have all written.

In order to make this easier, I have named the directories the same and have the same hierarchy.  In other words, in SourceTree,
I have a directory named "PUNetwork" which has the same setup as the "PUNetwork" on our CS Home Directories.

All you have to do is copy the "PUNetwork" folder from your laptop to your CS Home directory "/homes/<username>/" and
say "yes to all changes" if prompted when copying.