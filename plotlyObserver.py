import plotly.plotly as py # plotly library
import json # used to parse config.json
import time # timer functions
import datetime # log and plot current time
import random
from observer import Observer,Observable


class plotlyObserver(Observer):
	'''observer class that publishes as a stream on plotly'''

	def __init__(self,subject,plotly_config,name):
		# call parent init
		super(plotlyObserver,self).__init__(subject)

		# load config
		with open('./%s' % plotly_config) as config_file:
		    self.plotly_user_config = json.load(config_file)
		    py.sign_in(self.plotly_user_config["plotly_username"], self.plotly_user_config["plotly_api_key"])

		# set up
		self.url = py.plot([
		    {
		        'x': [], 'y': [], 'type': 'scatter',
		        'stream': {
		            'token': self.plotly_user_config['plotly_streaming_tokens'][0],
		            'maxpoints': 1000
		        }
		    }], filename=name)

		# print "View your streaming graph here: ", url

		# open stream
		self.stream = py.Stream(self.plotly_user_config['plotly_streaming_tokens'][0])
		self.stream.open()

	def notify(self,observable, *args, **kwargs):
		# write to plotly
		if 'value' in kwargs:
			self.stream.write({'x': datetime.datetime.now(), 'y': kwargs['value']})




# import plotly.plotly as py
# from plotly.graph_objs import *

# trace0 = Scatter(
#     x=[1, 2, 3, 4],
#     y=[10, 15, 13, 17]
# )
# trace1 = Scatter(
#     x=[1, 2, 3, 4],
#     y=[16, 5, 11, 9]
# )
# data = Data([trace0, trace1])

# unique_url = py.plot(data, filename = 'basic-line')

if __name__ == '__main__':
	subject = Observable()
	plyobs = plotlyObserver(subject,'config.json','test stream plot')
	subject.notify_observers(value=45)
	subject.notify_observers(value=55)


