from dotenv import load_dotenv
import os

# Get the API keys from environment variables
api_key = os.getenv('api_key_here')
api_secret = os.getenv('secret_api_here')
access_token = os.getenv('access_token_here')
access_token_secret = os.getenv('secret_access_token_here')

# Check if all variables were loaded correctly
if not all([api_key, api_secret, access_token, access_token_secret]):
    raise ValueError("One or more environment variables for Twitter API keys are missing.")