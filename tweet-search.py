import tweepy

consumer_key = 'RlRFeaKo8QBlq7DtNxG0Wqsyl'
consumer_secret = '01IKJ4Ods7LeiKdo73ofuAkisXTwnP5EZLiLgnIP2BuzmsqPqq'
access_token = '236189518-lvYKGmDBhD4hAmZtXMeTGuYE6wGlBxODLMyKlzOW'
access_secret = 'QPLFeMaZnbboiFrOmP9Kt1PoQnVAJiqC2P9lJLbJVLaYA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)  

"""You want: all recent tweets done in Portuguese, near
Maracanã soccer stadium in Rio de Janeiro Your search URL is: https://api.twitte
r.com/1.1/search/tweets.json?q=&geocode=-22.912214,-43.230182,1km&lang=pt&result
_type=recent"""

"""https://twitter.com/search?f=tweets&vertical=default&q=weather%20near%3A%22Is
lington%2C%20London%22%20within%3A15mi&src=typd"""
