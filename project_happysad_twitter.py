#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twitterscraper import query_tweets
from twitterscraper import query_tweets_from_user
import datetime as dt
import pandas as pd
import nltk


begin_date = dt.date(2017, 1, 1)
end_date = dt.date(2020, 4, 25)

limit = 1000
#lang = 'english'
user = 'dril'

tweets = query_tweets_from_user(user = user)

df = pd.DataFrame(t.__dict__ for t in tweets)


# In[ ]:


#csv_data = df.to_csv (r'C:\Users\44759\Documents\Anaconda\twitter_shit\tweets.csv', index = None, header = True)


# In[2]:


df.head(60)
#df = df[]


# In[3]:


##for index, row in df.iterrows():
    ##found = re.findall(r"^\twentyonepilots"), str(row['screen_name'])
    ##if
    
    
    #dropping rows not containing username of 21pilots
df = df[df.screen_name.str.contains(user, case=False)]
df = df.reset_index(drop=True)


# In[4]:


df.head


# In[5]:


df = df['text']


# In[6]:


df.head


# In[7]:


#tokens = nltk.word_tokenize()

tweets = []
#appennding tweets into a list to use stopwords later on 

for _ in df:
    print(_)
    print('------------')   
    tweets.append(_)


# In[8]:


# from textblob import TextBlob
# t1 = ''.join(tweets)
# print(t1)

# blob_t1 = TextBlob(t1)

# print(blob_t1.sentiment)


# In[9]:


# # from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# #stop = stopwords.words('english')
# #making a list of stopwords
# from nltk.tokenize import TweetTokenizer
# tkznr = word_tokenize(tweets[0])
# # print(tkznr)
# # print('-----------------------------------')
# # print(tweets[0])
# # # print(type(word_tokenize))
# # # tkznr.tokenize(self, tweets[0])
# print(type(TweetTokenizer))
# # print(type(word_tokenize))


# In[26]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
#example_sent = tweets[0] # forget this line
  
stop_words = set(stopwords.words('english')) 
#rint(stop_words)
milestone = []
for elem in tweets:
    word_tokens = word_tokenize(elem) #returning [0] ?????
    milestone.append(word_tokens)

#print(milestone)
#milestone = [item for sublist in milestone for item in sublist]
#rint(milestone)
#result_of_stopwords = [w for w in milestone if not w in stop_words] 
#print(result_of_stopwords)
# result_of_stopwords = [] 
# for w in result_of_stopwords: 
#       if w not in stop_words: 
#         result_of_stopwords.append(w)

# print(milestone)
# #rint('-----------------')
# print(result_of_stopwords)
# # print(result_of_stopwords)
# # print(word_tokens)
# # print('------------------------------------------')
# # print(filtered_sentence) 


# In[27]:


#flatten list

milestone = [item for sublist in milestone for item in sublist]
print(milestone)


# In[28]:


len(milestone)
#print(stop_words)


# In[29]:


result_of_stopwords = [w for w in milestone if not w in stop_words]


# In[30]:


len(result_of_stopwords)
#print(result_of_stopwords)


# In[36]:


import re
x = []
for _ in result_of_stopwords:
    found = re.findall(r'([a-zA-Z]+)[^https]', str(_))
    if found:
        print(_)
        print(found[0])
        x.append(found[0])

# c = []
# for _ in result_of_stopwords:
#     #print(_)
#     if _ in x:
#         c.append(_)
        
# print(c)
# new_list = []
# for fruit in a:
#     if fruit not in b:
#         new_list.append(fruit)


# In[23]:


#len(c)
#len(x)
print(x)


# In[24]:


stop_words.add('[')

print(stop_words)


# In[34]:


from textblob import TextBlob

test_stop = ' '.join(c)
#print(result_of_stopwords)
#print(test_stop)

blob_test = TextBlob(test_stop)

print(blob_test.sentiment)
print(c)
print(test_stop)


# In[ ]:





# In[ ]:





# In[ ]:




