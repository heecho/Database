'''

Phase three: Templating

Templating allows a program to replace data dynamically in an html file. 

Ex: A blog page, we wouldn't write a whole new html file for every blog page. We want to write
the html part, and styling just once, then just inject the different blog data into that page. 


1) Add the following line to index.html in the body

<h2>###Title###</h2>

2) When a request come in for index (/)
   
   - read the file data for index.html 

   - change the ###Title### string to the string "This is templating"
  
   - return the changed html 

3) Write a function render_template to take an html template, and a hash context

   Ex: render_template("<html>...",{"Title":"This is templating"})

   - Render will then try to replace all the fields in that hash

   Ex: context = {"Title":"This is the title","BlogText":"this is blog data"}

   In the html template replace ###Title### and ###BlogText### with corresponding key values.

   - Test by using this context {"Title":"This is the title","BlogText":"this is blog data"}

4) Add render_template to index_page with the sample context above

'''
import socket

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    urls = {'/': index_page(), '/about': about_page()}
 
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

        if request_page in urls.keys():
        	http_response += urls[request_page]

        if not request:
            continue

        client_connection.sendall(http_response)
        client_connection.close()

#def read_file():

def index_page():
	page_file = VIEWS_DIR + '/index.html'
	filehash = {"Title":"This is a Title"}
	with open(page_file,'r') as f:
		filedata = f.read()
		return render_template(filedata,filehash)
		
def about_page():
	page_file = VIEWS_DIR + '/about.html'
	with open(page_file,'r') as f:
		return f.read()	


def render_template(file_data, data_hash):
	for k,v in data_hash.iteritems():
		file_data = file_data.replace('###%s###' %k, v)
		return file_data

run_server()

