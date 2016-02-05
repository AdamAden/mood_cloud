from twitter import *
import json

t_ck = 'RlRFeaKo8QBlq7DtNxG0Wqsyl' #twitter consumer_key
t_cs = '01IKJ4Ods7LeiKdo73ofuAkisXTwnP5EZLiLgnIP2BuzmsqPqq' #twitter consumer_secret
t_ak = '236189518-lvYKGmDBhD4hAmZtXMeTGuYE6wGlBxODLMyKlzOW' #twitter access_key
t_as = 'QPLFeMaZnbboiFrOmP9Kt1PoQnVAJiqC2P9lJLbJVLaYA' #twitter access_secret

#y_ck = ''
#y_cs = '94a7e8745d9f2a588f3596439ee8f882c9213f54'



auth = OAuth(t_ak,t_as,t_ck,t_cs)

twit_api= Twitter(auth=auth)

print twit_api


q = '#FridayFeeling'
count = 5

search_results = twit_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']


for _ in range(5):
	print "Length of statuses", len(statuses)
	try:
		#import pdb; pdb.set_trace()
		next_results = search_results['search_metadata']['next_results']
	except KeyError, e:
		break

	kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
	search_results = twit_api.search.tweets(**kwargs)
	statuses += search_results['statuses']

#print json.dumps(statuses[0], indent=1)

status_texts = [ status['text'] for status in statuses]
print json.dumps(status_texts[0:5], indent=1)

screen_names = [  user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]
print json.dumps(screen_names[0:5], indent=1) 