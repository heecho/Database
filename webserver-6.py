'''

Phase Six: Form Support


1) Add a new html file into views called "create_post.html"

   - add a html form to the page

   - the form has inputs,  post_name and post_text

   - add a submit input

   - This doc has good guidlines for forms: http://learn.shayhowe.com/html-css/building-forms/

2) Add a new action for 'blog/new' tied to blog_new

   - renders the new_post.html

3) Update the form in create_post.html to <form action="/blog/create" method="post">

4) Add a new action for 'blog/create' tied to blog_create

   - have it return blog_index_page

5) Refactor the controller functions blog_index,blog_create... 

   - to accept the body of the http request

6) Write a new helper function called process_form 
 
   - it takes the body and take the form line from the end of body

   Ex: 'post_name=test&post_text=test'

   - and returns a hash {'post_name':'test','post_text':'test'}

7) Use proccess_form in blog_create to create a new row in the db using BlogModel

8) Last redirect to blog/<new id>

'''
import sqlite3
import blogmodel
import re
import socket

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        request_line = request.split('\r\n')
        request_first_part = request_line[0].split(' ')
        request_verb = request_first_part[0]
        request_page = request_first_part[1]
        print request_verb, request_page

        http_response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"""
        
        if request_page == '/favicon.ico':
         continue
        page_html = url_dispatch(request_page)
        print page_html
        http_response += str(page_html)

        if not request:
            continue

        client_connection.sendall(http_response)
        client_connection.close()

def read_file(page):
    page_file = VIEWS_DIR + page
    with open(page_file, 'r') as f:
        return f.read()

def index_page():
    return read_file('/index.html')
    
def about_page():
    return read_file('/about.html') 

def blog_index_page():
    return read_file('/blog_index.html')

def render_template(filedata, data_hash):
   for k,v in data_hash.iteritems():
      filedata = filedata.replace('###%s###' %k, v)
   return filedata

def blog_page(pageid):
   filedata = read_file('/blog.html')
   blog = blogmodel.BlogModel('blogdb')
   blog.read(pageid)
   return render_template(filedata, {"name":blog.post_name,"text":blog.post_text})

urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page)]

def url_dispatch(url):
   for regex,fn in urlpatterns:
      match = re.match(regex, url) 
      if match:
         print regex,fn
         if len(match.groups()):
            return fn(match.group(1))
         else:
            return fn()
          

run_server()
blog = blogmodel.BlogModel('blogdb')

