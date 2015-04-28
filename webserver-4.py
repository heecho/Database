'''

Phase four: Refactor urls

1) Add this,


urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page)]

def blog_index_page():
    pass

def blog_page(id):
    pass

   - create a blog_index.html with some basic html
  
   - create a blog.html with basic html

2) Write a function url_dispatch(url) where url is the http file name request

   - this function loops through urlpatterns using re.match and urlpatterns[0]

   - if a match is found it calls the matching function

   - if a pattern has a grouping like /blog/(\d+) you pass the first group item to the function

   Ex: if a request for /blog comes in the regular expressions matches the third url patter, so blog_index_page is called

'''

import re
import socket

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    #urls = {'/': index_page(), '/about': about_page()}
    
 
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
        #print page_html
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
    #return read_file('/blog_index.html')
    pass

def blog_page(pageid):
    #return read_file('/blog/%s.html' %(pageid))
    pass

urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page)]

def url_dispatch(url):
    for regex,fn in urlpatterns:
        match = re.match(regex, url) 
            if match:
                if len(match.groups()):
                    return fn(match.group(1))
                else:
                    return fn()
                

run_server()

