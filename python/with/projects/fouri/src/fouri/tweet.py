from os import getenv
from tweepy import Client

"""
We use twitter api for the latest tweet of 5dizipal5 user.

note: Make sure that your .env file contains TWITTER_BEARER_TOKEN
ex: get_last_tweet(prompt="Explain how to use ai")
"""


def get_last_tweet(username: str = "acanisik"):
    token = getenv("TWITTER_BEARER_TOKEN")

    if token:
        xClient = Client(token, wait_on_rate_limit=True)
        user = xClient.get_user(username=username)

        if user.data:
            user_id = user.data.id
            tweets = xClient.get_users_tweets(user_id, max_results=5)

            if tweets.data:
                return tweets.data[0].text
            else:
                print(f"{username} hasn't tweet on the Twitter!")
        else:
            print(f"No user found!")
