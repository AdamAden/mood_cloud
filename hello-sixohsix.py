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

world_woe_id = 1
uk_woe_id = 23424975


wold_trends = twit_api.trends.place(_id=world_woe_id)
uk_trends = twit_api.trends.place(_id=uk_woe_id)


#print wold_trends
#print usa_trends

#print json.dumps(wold_trends, indent =1)

world_trends_set = set([trend['name']for trend in wold_trends[0]['trends']])
uk_trends_set = set([trend['name']for trend in uk_trends[0]['trends']])
common_trends = world_trends_set.intersection(uk_trends_set)

print common_trends