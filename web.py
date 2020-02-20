## TECHNIQUES FOR ACCESSING SERVICES VIA HTTP

#a get request

from urllib import request, parse
#base url to access
url= 'http:httpbin.org/get'
#dictionary of query parameters
parms= {
    'name1': 'value1',
    'name2': 'value2'
    }

#encode the query string
querystring=parse.urlencode(parms)
#make a GET request and read the response

u = request.urlopen(url +'?'+ querystring)
resp=u.read()
##VARIATION
## to make a post request

u=request.urlopen(url, querystring.encode('ascii'))
resp=u.read
# FOR MORE COMPLICATED THINGS USE REQUESTS

import requests
#base url to access
url= 'http:httpbin.org/get'
#dictionary of query parameters
parms= {
    'name1': 'value1',
    'name2': 'value2'
    }
# extra header
headers= {
    'user-agent': 'none/ofyourbusiness',
    'spam': 'eggs'
}

resp = requests.post(url, data=parms, headers=headers)
#decoded text
text=resp.text 
#provides many options.  for example, the response.txt call can by returned in various formats
resp.content #returns raw binary file
response.json #returns json file

## HOW TO IMPLEMENT A SERVER USING TCP protocol
# the easiest way to do this is to use the socketserver library

#a simple echo server
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('got connection from', self.client_address)
        while True:
            msg= self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv=TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

# the only problem with this is that it can only server one thread at a time.  to implement multi process threads use the ThreadingTCPServer

from socketserver import ThreadingTCPServer

## NOTE" most of pythons higher level network libraries are built on top of socketserver

## BUILD A SIMPLE RESTR BASED INTERFACE 
# if yo don't want to install a full fledged lramework, the easiest way to do this is to create small library based on the WSGI standard

import cgi

def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b 'not found']

class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH INFO']
        params= cgi.FieldStorage(environ['wsgi.input'],
                                    environ=environ)
        method= environ['REQUEST_METHOD'].lower()
        envorn['params'] = {key:params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(enviro, start_response)

    def register(self, mthod, path, function):
        self.pathmap[mathod.lower(), path] = function
        return function
# to  use this, you simply write different handlers such as the following

import time
_hello_resp = '''\
<html>
pass
# html body response
</html>'''

def hello_world(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    params=environ['params']
    resp= _hello_resp.format(name=params.get('name'))
    yield response.encode('utf-8')
    
