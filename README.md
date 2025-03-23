# Trump Tweet Sentiment Analysis

This project analyzes the sentiment of tweets about Donald Trump using natural language processing.

## Features

- Fetches tweets about Trump using the Twitter API
- Analyzes sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Generates visualizations of sentiment distribution
- Provides detailed sentiment analysis results

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd trump-tweet-analysis
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

2. Run the sample tweet analysis:
```bash
python analyze_sample_tweets.py
```

## Output

The script generates:
- Sentiment analysis results in CSV format
- Visualization plots showing sentiment distribution
- Console output with summary statistics and sample tweets

## Note

Make sure to:
- Keep your `.env` file secure and never commit it to version control
- Follow Twitter's API rate limits and terms of service
- Use appropriate query parameters to get relevant tweets

## License

[Your chosen license] 