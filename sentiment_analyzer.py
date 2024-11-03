from dotenv import load_dotenv
import os
import tweepy

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

