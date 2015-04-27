
'''

Blog Model

Create a class to interface with sqlite3.  This type of object is typically called a Model.

The table in sqlite3 will have two columns: post_name and post_text

Discuss with your neighbour on how to solve this challenge.

To connect Python to SQL, reference the following:
http://www.pythoncentral.io/introduction-to-sqlite-in-python/

Your model should be able to:

1) Open a sqlite3 db connection
2) Close the connection
3) Create a new table with the correct fields
4) Perform CRUD actions on the database table

C - Create
R - Read
U - Update
D - Destroy

'''

import sqlite3


class BlogModel():
    def __init__(self,db_file):
        self.db_file = db_file
        self.post_name = None
        self.post_text = None
        self.db = self.open()
        
    def open(self):
        #open sqlite3 db connection
        return sqlite3.connect(self.db_file)

    def close(self):
        #close the connection to sqlite3
        self.db.close()

    def create_table(self):
        #create the table
        cursor = self.db.cursor()
        cursor.execute('''CREATE TABLE blog(blogid INTEGER PRIMARY KEY, post_name TEXT, post_text TEXT)''')
        self.db.commit()

    def create(self, post_name, post_text):
        #create a new row with data that you pass in
        cursor = self.db.cursor()
        cursor.execute('''INSERT INTO blog(post_name,post_text) VALUES(?,?)''',(post_name,post_text))
        print "posted"
        self.db.commit()

    def read(self,post_id):
        # "search for id, and return post_name and post_text as a string"
        cursor = self.db.cursor()
        cursor.execute('''SELECT post_name,post_text FROM blog WHERE blogid=?''', (post_id,))
        post = cursor.fetchone()
        print post
        self.db.commit()

    def update(self, post_id, post_name, post_text):
        # "search for id, and set a new post_name and post_text"
        cursor = self.db.cursor()
        newname = post_name
        newtext = post_text
        cursor.execute('''UPDATE blog SET post_name = ?, post_text = ? WHERE blogid = ? ''', (newname, newtext, post_id))
        self.db.commit()

    def destroy(self,post_id):
        #"search for id, and delete that row"
        cursor = self.db.cursor()
        cursor.execute('''DELETE FROM blog WHERE blogid = ? ''', (post_id,))
        self.db.commit()

blog = BlogModel('blogdb')
#blog.create_table()
#blog.create('hannah','first post!')
#blog.create('anabelle', 'second post!')
#blog.read(10)
#blog.update(2,"anna","herro")
#blog.read(2)
#blog.read(3)
#blog.destroy(3)
#blog.read(3)
#blog.close()

