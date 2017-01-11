import os
import random
from jinja2 import Environment, FileSystemLoader, select_autoescape

from tornado.ncss import Server

scores = {'group1': 15, 'group2': 1, 'group3': 5, 'group4':90 }

sorted_scores = []

for score in scores:
	sorted_scores.append(scores[score])

sorted_scores.sort()

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def index_handler(request):
	template = env.get_template('index.html')
  
	response = template.render(score = sorted_scores[0])
	request.write(response)
  

def score_handler(request, group_name, score):
	# stores the score thing
	request.write("Score saved")
		
PORT = int(os.environ.get("PORT", "8888"))
server = Server(port=PORT)
server.register(r'/', index_handler)
server.register(r'/add_score', score_handler)
server.run()
