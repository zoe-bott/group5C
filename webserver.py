from tornado.ncss import Server



def index_handler(request):
  request.write("Hello world")



server = Server(port=80)
server.register(r'/', index_handler)
server.run()
