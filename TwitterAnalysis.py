
import numpy as np
import re
import tweepy
import textblob
import wordcloud
import pandas as pd

import numpy
import math

import matplotlib.pyplot as plt
consumerKey = 'XXXXXXXXXXXXXXXXXXXXXXXX'
consumerSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
accessToken = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
accessTokenSecret ='YYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(authenticate, wait_on_rate_limit= True)

posts = api.user_timeline(screen_name="elon", count=100,tweet_mode="extended")

print("the last 5 tweets")
i=1
for tweet in posts[0:5]:
  print(str(i)+')'+tweet.full_text + '\n')
i=i+1

#credate a dataframe
df = pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])
df.head()
#CLEAN THE TEXT
def cleanTxt(text):
  text = re.sub(r'@[A-Za-z0-9]+', text) #removes@
  text = re.sub(r'#','', text)
  text = re.sub(r'RT[\s]+','', text)
  text = re.sub(r'https?:\/\/\S+','', text)

  return text

def getSubjectivity(text):
  return textblob(text).sentiment.Subjectivity

def getPolarity(text):
  return textblob(text).sentiment.Polarity  
 

def getAnalysis(score):
  if score < 0:
    return 'Negative' 
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'
  
  
  
  
 #OUTPUT  

the last 5 tweets
1)RT @jimrossignol: Alternative theology: we have made the sun angry. We have falsely worshipped its enemies, coal and oil, who were imprison…

1)RT @webflow: Woah, we now have over 100,000 friends here on Twitter! 💙💙

You’re all so amazing, so we’re going to giveaway a very special s…

1)RT @SenWhitehouse: With legislative climate options now closed, it’s now time for executive Beast Mode.

1)RT @tedlieu: Our Constitutional Republic cannot tolerate Supreme Court Justices who lied in order to get confirmed. The legitimacy of the C…

1)RT @AOC: I will never understand the pearl clutching over these protests. Republicans send people to protest me all the time, sometimes dru…

  
  
  
  #credate a dataframe
df = pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])
df.head()

#OUTPUT




index	Tweets
0	RT @jimrossignol: Alternative theology: we have made the sun angry. We have falsely worshipped its enemies, coal and oil, who were imprison…
1	RT @webflow: Woah, we now have over 100,000 friends here on Twitter! 💙💙 You’re all so amazing, so we’re going to giveaway a very special s…
2	RT @SenWhitehouse: With legislative climate options now closed, it’s now time for executive Beast Mode.
3	RT @tedlieu: Our Constitutional Republic cannot tolerate Supreme Court Justices who lied in order to get confirmed. The legitimacy of the C…
4	RT @AOC: I will never understand the pearl clutching over these protests. Republicans send people to protest me all the time, sometimes dru…
