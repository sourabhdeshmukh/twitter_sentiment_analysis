import pickle
import tweepy as tw 
import pandas as pd
import re
from nltk.stem import WordNetLemmatizer
import streamlit as st
from pathlib import Path
import tarfile
import requests
from streamlit_lottie import st_lottie
import plotly.express as px
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

consumer_key = st.secrets["consumer_key"]
consumer_key_secret = st.secrets["consumer_key_secret"]
access_token = st.secrets["access_token"]
access_token_secret = st.secrets["access_token_secret"]

auth = tw.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
    
def load_models():
    # Load the vectoriser.
    file = open('vectoriser-ngram.pickle', 'rb')
    vectoriser = pickle.load(file)
    file.close()
    # Load the LR Model.
    file = open('Sentiment-LR.pickle', 'rb')
    LRmodel = pickle.load(file)
    file.close()
    return vectoriser, LRmodel

def predict(LRmodel, model, text):
    # Predict the sentiment
    textdata = LRmodel.transform(preprocess(text))
    sentiment = model.predict(textdata)
    # Make a list of text with sentiment.
    data = []
    for text, pred in zip(text, sentiment):
        data.append((text,pred))
        print(text, " \n ")
        print(len(data), " \n")
        
    # Convert the list into a Pandas DataFrame.
    df = pd.DataFrame(data, columns = ['text','sentiment'])
    df = df.replace([0,1], ["Negative","Positive"])
    return df

emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

## Defining set containing all stopwords in english.
stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from', 
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're',
             's', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']

def preprocess(textdata):
    processedText = []
    
    # Create Lemmatizer and Stemmer.
    wordLemm = WordNetLemmatizer()
    
    # Defining regex patterns.
    urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern       = '@[^\s]+'
    alphaPattern      = "[^a-zA-Z0-9]"
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    
    for tweet in textdata:
        tweet = tweet.lower()
        
        # Replace all URls with 'URL'
        tweet = re.sub(urlPattern,' URL',tweet)
        # Replace all emojis.
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])        
        # Replace @USERNAME to 'USER'.
        tweet = re.sub(userPattern,' USER', tweet)        
        # Replace all non alphabets.
        tweet = re.sub(alphaPattern, " ", tweet)
        # Replace 3 or more consecutive letters by 2 letter.
        tweet = re.sub(sequencePattern, seqReplacePattern, tweet)

        tweetwords = ''
        for word in tweet.split():
            # Checking if the word is a stopword.
            #if word not in stopwordlist:
            if len(word)>1:
                # Lemmatizing the word.
                word = wordLemm.lemmatize(word)
                tweetwords += (word+' ')
            
        processedText.append(tweetwords)
        
    return processedText

def app():
    st.title("Twitter Sentiment Analyzer")
    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_twitter = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_ayl5c9tf.json')
    st_lottie(lottie_twitter, speed=1, height=180, key="initial")

    st.subheader("Analyze Sentiments on Twitter in Real Time!")
	
    st.markdown("Hey there! Welcome to Twitter Sentiment Analysis App. This app scrapes (and never keeps or stores!) the tweets you want to classfiy and analyzes the sentiments as positive, negative or neutral and visualises their distribution.")
    st.markdown("**To begin, please enter the number of tweets you want to analyse.** 👇")

    notweet = st.slider('Select a number between 1-100')
    if notweet == 0:
        notweet = 1
    st.write(notweet, 'tweets are being fetched.')
    st.write("__________________________________________________________________________________")

		# Radio Buttons
    st.markdown(" Great! Now, let's select the type of search you want to conduct. You can either search a twitter handle (e.g. @elonmusk) which will analyse the recent tweets of that user or search a trending hashtag (e.g. #WorkFromHome) to classify sentiments of the tweets regarding it. ")
    st.write("")

    stauses = st.radio('Select the mode of fetching',("Fetch the most recent tweets from the given twitter handle","Fetch the most recent tweets from the given twitter hashtag"))

    if stauses == 'Fetch the most recent tweets from the given twitter handle':
        st.success("Enter User Handle")
    elif stauses == 'Fetch the most recent tweets from the given twitter hashtag':
        st.success("Enter Hashtag")
    else:
        st.warning("Choose an option")
    
    raw_text = st.text_input("Enter the twitter handle of the personality (without @) or enter the hashtag (without #)")
    need_help = st.expander('Need help? 👉')
    with need_help:
        st.markdown("Having trouble finding the Twitter profile or Hashtag? Head to the [Twitter website](https://twitter.com/home) and click on the search bar in the top right corner.")
        
    st.markdown(" ### Almost done! Finally, let's choose what we want to do with the tweets ")
    Analyzer_choice = st.selectbox("Choose the action to be performed 👇",  ["Show Recent Tweets","Classify Sentiment"])

    if st.button("Analyze"):
        if Analyzer_choice == "Show Recent Tweets":
            st.success("Fetching latest Tweets")
            def Show_Recent_Tweets(raw_text):
                if stauses == 'Fetch the most recent tweets from the given twitter handle': 
                    posts = [status for status in tw.Cursor(api.user_timeline, screen_name=raw_text).items(notweet)]
                else:
                    posts = [status for status in tw.Cursor(api.search_tweets, q=raw_text).items(100)]
                
                def get_tweets():
                    tweet_list = []
                    itr = 1
                    for tweet in posts[:10]:
                        tweet_list.append(tweet.text)
                        itr += 1
                    return tweet_list
                
                recent_tweets = get_tweets()
                return recent_tweets
            recent_tweets = Show_Recent_Tweets(raw_text)
            st.write(recent_tweets)
        else:
            st.success("Analysing latest tweets")
            m = []
            def Analyse_Recent_Tweets(raw_text):
                if stauses == 'Fetch the most recent tweets from the given twitter handle': 
                    posts = [status for status in tw.Cursor(api.user_timeline, screen_name=raw_text).items(notweet)]
                else:
                    posts=[status for status in tw.Cursor(api.search_tweets, q=raw_text).items(100)]

                def fetch_tweets():
                    l2 = []
                    for tweet in posts[:notweet]:
                        l2.append(tweet.text)
                        #st.write(tweet.text)
                    
                    df = predict(vectoriser, LRmodel, l2)

                    for i in range(len(df)):
                        m.append(df.iloc[i]["sentiment"])
                   
                    for j in range(0, notweet):
                        st.write(l2[j])
                        st.write("The predicted sentiment is", m[j])
                        st.write("")
                        st.write("__________________________________________________________________________________")

                rec_tweets = fetch_tweets()
                return rec_tweets

            rec_tweets= Analyse_Recent_Tweets(raw_text)
            df = pd.DataFrame(m, columns = ['Sentiment'])
        st.markdown("**Whoa! Those are some strong opinions alright. Outta the {0} tweets that we analysed, the positive, negative and neutral sentiment distribution is summed up in the followed visualisation and table.**".format(notweet)) 
        st.write("")
        fig = px.pie(df,names=df['Sentiment'], title ='Pie chart of different sentiments of tweets')
        st.plotly_chart(fig)
        pos = df[df['Sentiment'] == 'Positive']
        neg = df[df['Sentiment'] == 'Negative']
        total_rows = df.count()
        rowsp = pos.count()
        rowsn = neg.count()
        result = pd.concat([rowsp, rowsn], axis=1)
        result.columns = ['Positive', 'Negative']
        result.index = ['No. of Tweets']
        st.subheader('Sentiment Distribution')
        st.write(result)
        st.markdown('***')
        st.markdown("Thanks for going through this mini-analysis with us. Cheers!")

def filesCheck():
    path = './vectoriser-ngram.pickle'
    obj = Path(path)
    if obj.exists() == False:
        file = tarfile.open('vectoriser.tar.gz')
        file.extractall('./')
        file.close()
        

if __name__=="__main__":
    filesCheck()
    # Loading the models.
    vectoriser, LRmodel = load_models()
    app()
    
    
