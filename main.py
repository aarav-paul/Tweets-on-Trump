import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize VADER sentiment analyzer
try:
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    logger.error(f"Error initializing VADER: {e}")
    raise

# Get Twitter API credentials from environment variables
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

def analyze_tweets(query, count=100):
    try:
        # Check if credentials are available
        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            logger.error("Twitter API credentials not found in environment variables")
            raise ValueError("Missing Twitter API credentials")

        # Authenticate with Tweepy
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        
        logger.info(f"Fetching {count} tweets about '{query}'")
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
        
        # Analyze sentiment of tweets
        sentiments = []
        tweet_texts = []
        
        for tweet in tweets:
            try:
                score = sia.polarity_scores(tweet.text)['compound']
                sentiments.append(score)
                tweet_texts.append(tweet.text)
                logger.debug(f"Tweet: {tweet.text[:50]}... Score: {score}")
            except Exception as e:
                logger.warning(f"Error analyzing tweet: {e}")
                continue
        
        if not sentiments:
            logger.error("No tweets were successfully analyzed")
            return None
            
        # Calculate average sentiment score
        avg_sentiment = sum(sentiments) / len(sentiments)
        logger.info(f"Average Sentiment Score: {avg_sentiment}")
        
        # Plot sentiment distribution
        plt.figure(figsize=(10, 6))
        plt.hist(sentiments, bins=20)
        plt.title(f"Sentiment Distribution for Tweets about '{query}'")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Frequency")
        
        # Save the plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.savefig(f'sentiment_analysis_{timestamp}.png')
        plt.close()
        logger.info(f"Plot saved as sentiment_analysis_{timestamp}.png")
        
        return {
            'average_sentiment': avg_sentiment,
            'total_tweets': len(sentiments),
            'sentiments': sentiments,
            'tweet_texts': tweet_texts
        }
        
    except Exception as e:
        logger.error(f"Error in analyze_tweets: {e}")
        raise

if __name__ == "__main__":
    try:
        print("\nWelcome to Twitter Sentiment Analysis!")
        print("Enter a topic to analyze tweets about (e.g., 'artificial intelligence', 'climate change', 'sports'):")
        topic = input("> ").strip()
        
        if not topic:
            print("Error: Please enter a topic to analyze")
            exit(1)
            
        results = analyze_tweets(query=topic)
        if results:
            print("\nAnalysis Results:")
            print(f"Topic: {topic}")
            print(f"Total tweets analyzed: {results['total_tweets']}")
            print(f"Average sentiment score: {results['average_sentiment']:.3f}")
            print("\nSample tweets and their sentiments:")
            for i, (text, score) in enumerate(zip(results['tweet_texts'][:5], results['sentiments'][:5])):
                print(f"\nTweet {i+1}:")
                print(f"Text: {text[:100]}...")
                print(f"Sentiment: {score:.3f}")
    except Exception as e:
        logger.error(f"Main execution error: {e}")
