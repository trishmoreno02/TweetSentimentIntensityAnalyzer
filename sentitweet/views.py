from django.http import HttpResponse
from django.shortcuts import render
from . import sentiment_report


def tweets(request):
    topic = request.GET.get('search','Duterte')

    public_tweets = sentiment_report.get_tweets(topic)
    sid = sentiment_report.get_analyzer()
    analysis_list = []
    compounds = []
    for tweet in public_tweets:
        ss = sid.polarity_scores(tweet.text)
        analysis_list.append('compound: '+ str(ss['compound']) + ' pos: ' + str(ss['pos']) + ' neu: ' + str(ss['neu']) + ' neg: ' + str(ss['neg']))
        compounds.append(ss['compound'])
    tweet_list = zip(public_tweets, analysis_list, compounds)
    return render(request, 'tweets.html', {'tweet_list': tweet_list, 'topic': topic})
