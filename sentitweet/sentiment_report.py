import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

consumer_key = 'VxbfpCcFIh3Kj0XIXiFV1VLl9'
consumer_secret = 'zAIpoj8OeSCrM95fr12BIbCWWoQMOnTGxkyFTMzmmNuo41lMPv'

access_token = '2902660219-5Dsnob4fPvzLopFvvRagv24XvP9eJ1LmT8KNCf9'
access_token_secret = 'VlOis4uH3COPw4k3GFU9rLrWd5YxqHxEYdqc3Fi8CD52t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Duterte')
sid = SentimentIntensityAnalyzer()
#for tweet in public_tweets:
#    print(tweet.text)
    #analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
#    ss = sid.polarity_scores(tweet.text)
#    for k in sorted(ss):
#        print('{0}: {1}, '.format(k, ss[k]), end='')
#    print()



def get_tweets(topic):
    public_tweets = api.search(topic)
    return public_tweets

def get_analyzer():
    return sid
