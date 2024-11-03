from dotenv import load_dotenv
import os
import tweepy
from textblob import TextBlob

# Get the API keys from environment variables
load_dotenv()

api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Print a message indicating that the keys were loaded
print("Loaded environment variables.")

# Check if all variables were loaded correctly
if not all([api_key, api_secret, access_token, access_token_secret]):
    raise ValueError("One or more environment variables for Twitter API keys are missing.")
else:
    print("All environment variables loaded successfully.")

# Authenticate to Twitter/X
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Check if auth is successful
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication", e)

def fetch_tweets(keyword, count=10):
    try:
        tweets = api.search_tweets(q=keyword, count=count, lang='en', tweet_mode='extended')
        for tweet in tweets:
            print(f"{tweet.user.screen_name}: {tweet.full_text}\n")
    except Exception as e:  # Catch all exceptions
        print(f"Failed to fetch tweets: {e}")

# Example usage
fetch_tweets("#news", count=10)  # Change the keyword as needed