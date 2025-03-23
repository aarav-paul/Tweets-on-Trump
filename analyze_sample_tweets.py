import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import logging
from datetime import datetime
import ssl

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Handle SSL certificate issues for NLTK download
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Initialize VADER sentiment analyzer
try:
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    logger.error(f"Error initializing VADER: {e}")
    raise

def analyze_sample_tweets():
    """Analyze sentiment of sample tweets from CSV file"""
    try:
        # Read the CSV file
        logger.info("Reading sample tweets from CSV file...")
        df = pd.read_csv('sample_tweets.csv')
        
        # Analyze sentiment of tweets
        sentiments = []
        detailed_results = []
        
        for tweet in df['tweet_text']:
            try:
                # Get full sentiment scores
                scores = sia.polarity_scores(tweet)
                compound_score = scores['compound']
                sentiments.append(compound_score)
                
                # Determine sentiment category
                if compound_score >= 0.05:
                    sentiment = 'Positive'
                elif compound_score <= -0.05:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'
                
                # Store detailed results
                detailed_results.append({
                    'tweet': tweet,
                    'compound_score': compound_score,
                    'pos_score': scores['pos'],
                    'neg_score': scores['neg'],
                    'neu_score': scores['neu'],
                    'sentiment': sentiment
                })
                
                logger.debug(f"Tweet analyzed: {tweet[:50]}... Score: {compound_score}")
            except Exception as e:
                logger.warning(f"Error analyzing tweet: {e}")
                continue
        
        if not sentiments:
            logger.error("No tweets were successfully analyzed")
            return None
            
        # Calculate statistics
        avg_sentiment = sum(sentiments) / len(sentiments)
        positive_tweets = sum(1 for s in sentiments if s >= 0.05)
        negative_tweets = sum(1 for s in sentiments if s <= -0.05)
        neutral_tweets = sum(1 for s in sentiments if -0.05 < s < 0.05)
        
        # Create results DataFrame
        results_df = pd.DataFrame(detailed_results)
        
        # Save detailed results to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_filename = f'sentiment_analysis_results_{timestamp}.csv'
        results_df.to_csv(results_filename, index=False)
        logger.info(f"Detailed results saved to {results_filename}")
        
        # Create visualizations
        plt.figure(figsize=(15, 10))
        
        # Sentiment distribution histogram
        plt.subplot(2, 1, 1)
        plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
        plt.title("Sentiment Distribution of Sample Tweets")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Frequency")
        
        # Sentiment categories pie chart
        plt.subplot(2, 1, 2)
        plt.pie([positive_tweets, neutral_tweets, negative_tweets], 
                labels=['Positive', 'Neutral', 'Negative'],
                colors=['green', 'gray', 'red'],
                autopct='%1.1f%%')
        plt.title("Distribution of Sentiment Categories")
        
        # Save the plots
        plot_filename = f'sentiment_analysis_plots_{timestamp}.png'
        plt.tight_layout()
        plt.savefig(plot_filename)
        plt.close()
        logger.info(f"Plots saved as {plot_filename}")
        
        # Print summary results
        print("\nAnalysis Results:")
        print(f"Total tweets analyzed: {len(sentiments)}")
        print(f"Average sentiment score: {avg_sentiment:.3f}")
        print(f"\nSentiment Distribution:")
        print(f"Positive tweets: {positive_tweets} ({positive_tweets/len(sentiments)*100:.1f}%)")
        print(f"Neutral tweets: {neutral_tweets} ({neutral_tweets/len(sentiments)*100:.1f}%)")
        print(f"Negative tweets: {negative_tweets} ({negative_tweets/len(sentiments)*100:.1f}%)")
        
        print("\nTop 5 Most Positive Tweets:")
        for tweet in sorted(detailed_results, key=lambda x: x['compound_score'], reverse=True)[:5]:
            print(f"\nTweet: {tweet['tweet']}")
            print(f"Sentiment Score: {tweet['compound_score']:.3f}")
        
        print("\nTop 5 Most Negative Tweets:")
        for tweet in sorted(detailed_results, key=lambda x: x['compound_score'])[:5]:
            print(f"\nTweet: {tweet['tweet']}")
            print(f"Sentiment Score: {tweet['compound_score']:.3f}")
        
        return {
            'average_sentiment': avg_sentiment,
            'total_tweets': len(sentiments),
            'sentiments': sentiments,
            'detailed_results': detailed_results
        }
        
    except Exception as e:
        logger.error(f"Error in analyze_sample_tweets: {e}")
        raise

if __name__ == "__main__":
    try:
        analyze_sample_tweets()
    except Exception as e:
        logger.error(f"Main execution error: {e}") 