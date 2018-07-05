import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#gotta remove the keys and tokens for security purposes
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

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
