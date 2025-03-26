# Twitter Sentiment Analysis

This project analyzes the sentiment of tweets using natural language processing, providing insights into public opinion on any topic.

## Features

- Fetches tweets about any topic using the Twitter API
- Analyzes sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Generates visualizations of sentiment distribution
- Provides detailed sentiment analysis results
- Includes a diverse set of sample tweets for testing

## Setup

1. Clone the repository:
```bash
git clone https://github.com/aarav-paul/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Twitter API credentials:
```
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

## Usage

1. Run the main analysis script:
```bash
python main.py
```
The script will prompt you to enter a topic to analyze tweets about.

2. Run the sample tweet analysis:
```bash
python analyze_sample_tweets.py
```

## Output

The script generates:
- Sentiment analysis results in CSV format
- Visualization plots showing sentiment distribution
- Console output with summary statistics and sample tweets

## Sample Topics

You can analyze tweets about various topics such as:
- Technology and innovation
- Entertainment and media
- Sports and athletics
- Business and finance
- Science and research
- Education and learning
- Health and wellness
- Environment and climate
- Travel and tourism
- Food and cuisine

## Why Sample Tweets Instead of Twitter API?

This project uses sample tweets instead of the Twitter API for several important reasons:

1. **Cost-Effective Development**: The Twitter API now requires a minimum subscription of $50/month for basic access. This makes it cost-prohibitive for development and testing purposes.

2. **API Access Requirements**: Twitter's API access requires:
   - A paid developer account
   - Application approval
   - API key management
   - Rate limit monitoring

3. **Development Flexibility**: Using sample data allows for:
   - Faster development cycles
   - Consistent testing scenarios
   - No API rate limits
   - No network dependencies

4. **Production Ready**: The code is fully compatible with the Twitter API. To use it with the actual API, you would only need to:
   - Replace the sample data loading with API calls
   - Add your API credentials
   - Handle API rate limits

The sample tweets provided in this project are carefully curated to represent real-world scenarios and can be used to test all features of the sentiment analysis system. When you're ready to deploy with the actual Twitter API, the code structure remains the same - you'll just need to modify the data input source.

## Note

Make sure to:
- Keep your `.env` file secure and never commit it to version control
- Follow Twitter's API rate limits and terms of service
- Use appropriate query parameters to get relevant tweets
- Consider the context and nuance of the topic being analyzed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Aarav Paul 