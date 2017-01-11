import os
import random
from jinja2 import Environment, FileSystemLoader, select_autoescape

from tornado.ncss import Server

scores = {'group1': 15, 'group2': 1, 'group3': 5, 'group4':90 }



env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def index_handler(request):
	template = env.get_template('index.html')
	sorted_scores = []
	sorted_names = []
	print(scores)
	for name, score in scores.items():
		sorted_scores.append((score,name))
	
	
	sorted_scores.sort()
	
	response = template.render({'first': sorted_scores[0][1], 'first_score': sorted_scores[0][0],
	'second': sorted_scores[1][1], 'second_score': sorted_scores[1][0],
	'third': sorted_scores[2][1], 'third_score': sorted_scores[2][0],
	'fourth': sorted_scores[3][1], 'fourth_score': sorted_scores[3][0]
	})
	request.write(response)
	
  

def score_handler(request, group_name, score):
	# stores the score thing
	scores[group_name] = int(score)
	request.write("Score saved")
		
PORT = int(os.environ.get("PORT", "8888"))
server = Server(port=PORT)
server.register(r'/', index_handler)
server.register(r'/add_score/(\w+)/(\d+)', score_handler)
server.run()
