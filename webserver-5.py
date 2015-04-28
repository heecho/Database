'''

Phase Five: DB Support

1) Using "sqlite3 blog.db"
   
    - create a table called posts, which has an id, post_name, post_text
    - add a row to this table, with a post name and post text

2) add the line below 

import blogmodel

3) Update blog_page(id) to use BlogModel read
   
   - passing the data from the db into the context.
   - to get an instance of blogmodel use blogmodel.BlogModel(DB_FILE)


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


