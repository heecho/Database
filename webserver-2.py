'''

Phase two: Routing + Controllers

On Modern web sites we drop the .html for things, and it is more action based.

In your browser a user would request <your site.com> + 

/ 
/about
/blog
/blog/1

1) Add two new functions index_page and about_page

2) Create a hash called urls that maps between a http request like "/" and call index_page(), 
   "/about" calls about_page()

3) Move your file reading code into both of those functions, so index_page reads index.html and
   returns that data, about_page() the same but for about.html


'''
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

        if request_page != '/favicon.ico':
            if request_page == '/':
                page_file = VIEWS_DIR + '/index.html'
            elif request_page == '/about':
                page_file = VIEWS_DIR + '/about.html'

        http_response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"""

        if page_file:
            with open(page_file, 'r') as f:
                http_response += f.read()

        if not request:
            continue

        client_connection.sendall(http_response)
        client_connection.close()


run_server()


