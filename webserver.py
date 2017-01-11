import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from tornado.ncss import Server


env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def index_handler(request):
  template = env.get_template('index.html')
  response = template.render()
  request.write(response)


PORT = int(os.environ.get("PORT", "8888"))
server = Server(port=PORT)
server.register(r'/', index_handler)
server.run()
