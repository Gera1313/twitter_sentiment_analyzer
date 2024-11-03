from dotenv import load_dotenv
import os

# Get the API keys from environment variables
load_dotenv()

api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('access_token_here')
access_token_secret = os.getenv('secret_access_token_here')

# Check if all variables were loaded correctly
if not all([api_key, api_secret, access_token, access_token_secret]):
    raise ValueError("One or more environment variables for Twitter API keys are missing.")