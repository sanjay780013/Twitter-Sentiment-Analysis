import jsonlines
import pandas as pd
import matplotlib.pyplot as plt
import pylab


def readTwitterData(twitterDataFile):
    tweets = []
    with jsonlines.open(twitterDataFile) as infile:
        reader = jsonlines.Reader(infile)
        for line in reader:
            tweets.append(line)
    print(type(tweets[0]))
    return tweets


if __name__ == '__main__':
    tweets_data = []
    tweets = pd.DataFrame()
    tweets_data = readTwitterData('output.json')


    tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
    tweets['location'] = list(map(lambda tweet: tweet['user']['location'] if 'user' in tweet else None, tweets_data))
    tweets_by_loc = tweets['location'].value_counts()
    print (tweets_by_loc[:10]) #outputs top 10 locations

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('locations', fontsize=15)
    ax.set_ylabel('Number of Tweets' , fontsize=15)
    ax.set_title('Top 10 locations', fontsize=15, fontweight='bold')
    tweets_by_loc[:10].plot(ax=ax, kind='bar', color='green')

    pylab.show()
