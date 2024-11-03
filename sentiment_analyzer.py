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

# Check if auth is successul
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication", e)

# Fetch recent tweets
tweets = api.home_timeline(count=5)
for tweet in tweets:
    print(f"{tweet.user.name} said: {tweet.text}")