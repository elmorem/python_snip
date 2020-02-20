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
