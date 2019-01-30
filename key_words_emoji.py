# -*- coding: utf-8 -*-		#sets the file encoding for emoji

__author__ = 'petermarozzi'
import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import re
import os, sys	#necessary for using UTF-8

reload(sys)  #fixes the errors otherwise with ASCII
sys.setdefaultencoding('utf8')	#fixes the errors otherwise with ASCII

tweets_data_path = 'output.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
     try:
             tweet = json.loads(line)
             tweets_data.append(tweet)
     except:
             continue


tweets = pd.DataFrame()

tweets['tweet'] = map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data)


if __name__ == '__main__':
     tweets_data_path = 'output.txt'
     tweets_data = []
     tweets_file = open(tweets_data_path, "r")
     for line in tweets_file:
             try:
                     tweet = json.loads(line)
                     tweets_data.append(tweet)
             except:
                     continue

tweets = pd.DataFrame()
texts = []

for line, tweet in enumerate(tweets_data):
	try:
		texts.append(tweet['text'])
	except:
		continue
		# print "Error line %d" % (line)
		
tweets['text'] = texts


def key_words(row):
	words = []
	text = row["text"].lower()
	if "😭" in text or "😪" in text or "😣" in text or "😒" in text or "☹️" in text:
		words.append("Sad")
	if "😋" in text or "😊" in text or "😃" in text or "😌" in text or "😝" in text or "😉" in text or "😙" in text or "🙂" in text or "😁" in text:
		words.append("Happy")
	if "😍" in text or "❤️" in text or "💝" in text or "💕" in text or "😘" in text or "💗" in text or "💞" in text or "💖" in text or "💛" in text:
		words.append("Loving")
	if "🎉" in text or "🎂" in text or "🎁" in text or "💐" in text or "👑" in text or "🌹" in text:
		words.append("Celebratory")
	if "👍" in text or "👌" in text or "🤙🏽" in text or "👏" in text:
		words.append("Ok")
	if "😅" in text or "😆" in text or "😂" in text:
		words.append("Funny")
	if "🙀" in text or "😳" in text or "😱" in text:
		words.append("Scared")
	if "😴" in text:
		words.append("Tired")
	if "😡" in text or "😠" in text:
		words.append("Angry")
	if "🙏🏻" in text or "🙇🏻" in text:
		words.append("Hopeful")
	if "😷" in text or "🤧" in text:
		words.append("Sick")
	if "🤔" in text:
		words.append("Thoughtful")
	if "😎" in text:
		words.append("Cool")
	return ",".join(words)

tweets["words"] = tweets.apply(key_words,axis=1)
counts = tweets["words"].value_counts()
print(counts)


fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Key Words', fontsize=15)
ax.set_ylabel('Number of Tweets' , fontsize=15)
ax.set_title('Key Words', fontsize=15, fontweight='bold')
counts[1:100].plot(ax=ax, kind='bar', color='purple')

pylab.show()