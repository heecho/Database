
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

    def open(self):
        "open sqlite3 db connection"
        pass

    def close(self):
        "close the connection to sqlite3"
        pass

    def create_table(self):
        #create the table
        pass

    def create(self, post_name, post_text):
        #create a new row with data that you pass in
        pass

    def read(self,id):
        # "search for id, and return post_name and post_text as a string"
        pass

    def update(self, id, post_name, post_text):
        pass
        # "search for id, and set a new post_name and post_text"

    def destroy(self,id):
        #"search for id, and delete that row"
        pass