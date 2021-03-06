import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
 
 
client = None
browser = None
 
class Client(tornado.websocket.WebSocketHandler):
    def open(self):        
        global client
        if client == None:
            client = self       
#        print client
#        print "Client is set"

    def on_message(self, message):
        global browser
        if browser != None:
            browser.write_message(message) 
#        print browser
#        print message[:100]
                
    def on_close(self):
	global client
	client = None
#        print client
#        print "Client is out"

class Browser(tornado.websocket.WebSocketHandler):
    def open(self):        
        global browser
        if browser == None:
            browser = self   
#        print browser
#        print "Browser is set"
      
    def on_message(self, message):
        global client
        if client != None:
            client.write_message(message)
#        print client
#        print message[:100]
       
               
    def on_close(self):
	global browser
	browser = None
#        print browser
#        print "Browser is out"
        
application = tornado.web.Application([
    (r'/client', Client),
    (r'/browser', Browser)
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
