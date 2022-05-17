import tweepy
import time
import pandas as pd

client = tweepy.Client(bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOQBcgEAAAAAt4mjcF4T1l0Z8G%2BSYtmT%2FYqouoQ%3DiIlwUDeSVMThwr6taT1kuJb5odbelhHvcCrn5Yhjclxxwa32ce', wait_on_rate_limit=True)

proj_tweets = []
for tweety in tweepy.Paginator(client.search_recent_tweets,
                                 query = 'Russian Ukrainian War',
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 expansions = 'author_id',
                              max_results=100):
    time.sleep(1)
    proj_tweets.append(tweety)

result = []
user_dict = {}
# Loop through each response object
for tweety in proj_tweets:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
    for user in tweety.includes['users']:
        user_dict[user.id] = {'username': user.username,
                              'followers': user.public_metrics['followers_count'],
                              'tweets': user.public_metrics['tweet_count'],
                              'description': user.description,
                              'location': user.location
                             }
    for tweet in tweety.data:
        # For each tweet, find the author's information
        author_info = user_dict[tweet.author_id]
        # Put all of the information we want to keep in a single dictionary for each tweet
        result.append({'author_id': tweet.author_id,
                       'username': author_info['username'],
                       'author_followers': author_info['followers'],
                       'author_tweets': author_info['tweets'],
                       'author_description': author_info['description'],
                       'author_location': author_info['location'],
                       'text': tweet.text,
                       'created_at': tweet.created_at,
                       'retweets': tweet.public_metrics['retweet_count'],
                       'replies': tweet.public_metrics['reply_count'],
                       'likes': tweet.public_metrics['like_count'],
                       'quote_count': tweet.public_metrics['quote_count']
                      })

# Change this list of dictionaries into a dataframe
df = pd.DataFrame(result)

df.to_csv("tweets.csv")