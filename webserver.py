import os

from tornado.ncss import Server



def index_handler(request):
  request.write("Hello world")


PORT = int(os.environ.get("PORT", "8888"))
server = Server(port=PORT)
server.register(r'/', index_handler)
server.run()
