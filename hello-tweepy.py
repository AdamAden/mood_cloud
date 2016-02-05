import tweepy

consumer_key = 'RlRFeaKo8QBlq7DtNxG0Wqsyl'
consumer_secret = '01IKJ4Ods7LeiKdo73ofuAkisXTwnP5EZLiLgnIP2BuzmsqPqq'
access_token = '236189518-lvYKGmDBhD4hAmZtXMeTGuYE6wGlBxODLMyKlzOW'
access_secret = 'QPLFeMaZnbboiFrOmP9Kt1PoQnVAJiqC2P9lJLbJVLaYA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text

