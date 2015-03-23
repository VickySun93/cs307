#!/usr/bin/python

import sqlite3, os

if os.path.exists("purdue_network.db"):
	os.remove("purdue_network.db")

tmp = open("purdue_network.db", "w")
tmp.close()
conn = sqlite3.connect('purdue_network.db')

c = conn.cursor()

# Turn on foreign key support
c.execute("PRAGMA foreign_keys = ON")

# Create users table; path for each user class list
c.execute('''CREATE TABLE users
	     (name TEXT NOT NULL,
	      user_name TEXT NOT NULL,
	      user_id INTEGER NOT NULL,
	      password TEXT NOT NULL,
	      email TEXT NOT NULL,
	      path TEXT NOT NULL,
	      PRIMARY KEY(user_name, user_id))''')

# Create QA_Thread table
c.execute('''CREATE TABLE qathreads
	     (thread_id INTEGER NOT NULL,
	      thread_title TEXT NOT NULL,
	      orig_time INTEGER NOT NULL,
	      thread_owner TEXT NOT NULL,
	      path TEXT NOT NULL,
	      FOREIGN KEY (thread_owner) REFERENCES users(user_name),
	      PRIMARY KEY(thread_id))''')

# Create Courses table
# What is the course major(MATH,CS,etc)
c.execute('''CREATE TABLE courses
	     (path TEXT NOT NULL,
	      course_major TEXT NOT NULL,
	      course_id INTEGER NOT NULL,
	      course_title TEXT NOT NULL,
	      course_desc TEXT NOT NULL,
	      course_term INTEGER NOT NULL,
	      PRIMARY KEY(course_major,course_id))''')

# Create sessions table
c.execute('''CREATE TABLE sessions
	     (user TEXT NOT NULL,
	      session TEXT NOT NULL,
	      FOREIGN KEY(user) REFERENCES users(user_name),
	      PRIMARY KEY(session))''')

# Create inbox table
c.execute('''CREATE TABLE inbox
	     (msg_thread_id INTEGER NOT NULL,
	      path TEXT NOT NULL,
	      owner_list TEXT NOT NULL,
	      PRIMARY KEY(msg_thread_id))''')


# Save the changes
conn.commit()

# Close the connection
conn.close()
