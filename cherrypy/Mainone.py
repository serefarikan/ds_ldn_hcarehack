__author__ = 'sarikan'
import random
import string
from ML import *
import cherrypy
import json

class StringGeneratorWebService(object):
 exposed = True

 @cherrypy.tools.accept(media='application/json')
 def GET(self,age , gcsmotor , daysicu , normalscan):
     #return cherrypy.session['mystring']
     #get_probs(age , gcsmotor , daysicu , normalscan)
     cherrypy.response.headers['Content-Type'] = 'application/json'
     return json.dumps(get_probs(age,gcsmotor,daysicu,normalscan))

 def POST(self, length=8):
     some_string = ''.join(random.sample(string.hexdigits, int(length)))
     cherrypy.session['mystring'] = some_string
     return some_string

 def PUT(self, another_string):
     cherrypy.session['mystring'] = another_string

 def DELETE(self):
     cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
 conf = {
     '/': {
         'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
         'tools.sessions.on': True,
         'tools.response_headers.on': True,
         'tools.response_headers.headers': [('Content-Type', 'text/plain')],
     }
 }
 cherrypy.server.socket_host = '0.0.0.0'
 cherrypy.quickstart(StringGeneratorWebService(), '/', conf)