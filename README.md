# Twitter Sentiment Analyzer

This is a small Python project for fetching and analyzing the sentiment of tweets. Using Tweepy to connect to the Twitter API and TextBlob for sentiment analysis, this tool helps determine the emotional tone (positive, negative, or neutral) of tweets based on keywords, hashtags, or usernames.

## Project Overview

The Twitter Sentiment Analyzer lets you:
- **Fetch Tweets by Keyword/Hashtag**: Retrieve tweets containing a specified keyword or hashtag.
- **Analyze Sentiment**: Classify the sentiment of each tweet using TextBlob.
- **Display Results**: Show tweets and their sentiment scores in the console.

## Requirements

- **Python 3.11** (or a compatible version)
- **Twitter API Access** (Free or elevated access may limit data retrieval)
- **Required Libraries**: Tweepy, TextBlob, dotenv

Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup and Usage

### Step 1: Set Up Environment Variables
Create a ```.env``` file in the root of your project with your Twitter API credentials:

```
TWITTER_API_KEY='your_api_key'
TWITTER_API_SECRET='your_api_secret'
TWITTER_ACCESS_TOKEN='your_access_token'
TWITTER_ACCESS_TOKEN_SECRET='your_access_token_secret'
```

### Step 2: Run the Sentiment Analyzer
Run the script to analyze tweets based on a specific keyword, hashtag, or username:

```
python sentiment_analyzer.py
```
The output will display each tweet alongside its sentiment (Positive, Negative, or Neutral).

### Example Output
```
User123: "This is an amazing day!" - Sentiment: Positive
User456: "Feeling frustrated with the traffic." - Sentiment: Negative
User789: "Just a regular day, nothing special." - Sentiment: Neutral
```

## Known Limitations
Twitter API Access Level: Free access may limit tweet retrieval. Certain Twitter API endpoints require a paid subscription.
Rate Limits: Twitter API limits the number of requests. Be mindful of these limits when testing.
Compatibility: This script uses Twitter API v1.1, which may be subject to changes or deprecation.


## Future Improvements
Add Visualization: Use libraries like Matplotlib or Seaborn to graph sentiment data.
Expand NLP Capabilities: Replace TextBlob with advanced NLP libraries for deeper analysis.