import streamlit as st
import praw
from psaw import PushshiftAPI
import pandas as pd
import datetime as dt
import time
import datetime
from datetime import datetime, timedelta

# email = "samuellawrenceJSE@gmail.com"
# password = "JSEStocksGoUp"

# Praw API login

username = "SamTheIceCreamMan"
password = "Samernator1"
id = "U9EagV0j3qUSbw"
secret = "Su_o5xTzvs4RKygGOBakQFutxw49-A"
user_agent = "scrapermaster"

reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=password, user_agent=user_agent,
                     username=username)


def submissionsWithin24hours(subreddit):
    subreddit = reddit.subreddit(subreddit)

    submissionsLast24 = []
    for submission in subreddit.new(limit=100):
        utcPostTime = submission.created
        submissionDate = datetime.utcfromtimestamp(utcPostTime)
        submissionDateTuple = submissionDate.timetuple()

        currentTime = datetime.utcnow()

        # How long ago it was posted.
        submissionDelta = currentTime - submissionDate

        title = submission.title
        link = 'www.reddit.com' + submission.permalink
        submissionDelta = str(submissionDelta)

        if 'day' not in submissionDelta:
            submissionsLast24.append((title, link, submissionDelta))

    return submissionsLast24

# subred = reddit.subreddit("investing")

# top = subred.top(limit = 10)

# for i in top:
#   print(i.title, i.url)

def app():
    selection = ["r/wallstreetbets", "r/stocks", "r/investing", "r/CyptoCurrency", "r/StockMarket", "r/pennystocks",
                 "r/WallStreetbetsELITE", "Multi-select"]  # Selections
    choice = st.sidebar.selectbox("Dashboard Selection", selection)
    if choice == 'r/wallstreetbets':
        choice_search = 'wallstreetbets'
        st.title("r/Wallstreetbets")

        subreddit = choice_search
        validSubmissions = submissionsWithin24hours(subreddit)
        # st.write((validSubmissions[1:])[0:])
        df = pd.DataFrame(validSubmissions)
        st.write(df)




                # About subreddit
        # Collect top 25 posts from x days
        # Take all comments from posts and put into list
        # - top stocks listed
        # - ideas / themes

    if choice == 'r/stocks':
        st.title("r/Stocks subreddit")
        subred = reddit.subreddit("investing")
        st.write(subred.title)

    if choice == 'r/investing':
        st.title("r/investing subreddit")
        subred = reddit.subreddit("investing")
        st.write(subred.description)

    if choice == 'r/CyptoCurrency':
        st.title("r/CyptoCurrency subreddit")
        subred = reddit.subreddit("CyptoCurrency")
        st.write(subred.description)

    if choice == 'r/StockMarket':
        st.title("r/StockMarket subreddit")
        subred = reddit.subreddit("StockMarket")
        st.write(subred.description)

    if choice == 'r/pennystocks':
        st.title("r/pennystocks subreddit")
        subred = reddit.subreddit("pennystocks")
        st.write(subred.description)

    if choice == 'r/WallStreetbetsELITE':
        st.title("r/WallStreetbetsELITE subreddit")
        subred = reddit.subreddit("WallStreetbetsELITE")
        st.write(subred.description)

    # if choice == '"Multi-select"':
    #     st.title("r/Multi-select subreddit")
    #     subred = reddit.subreddit("investing")
    #     st.write(subred.description)


if __name__ == "__main__":
    app()
