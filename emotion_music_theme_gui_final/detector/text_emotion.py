from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download required NLTK data
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

def detect_emotion(text):
    """
    Detect emotion from text using NLTK's VADER sentiment analyzer.
    Returns one of: happy, sad, angry, neutral
    """
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    
    # Map sentiment scores to emotions
    compound = scores['compound']
    
    if compound >= 0.5:
        return 'happy'
    elif compound <= -0.5:
        return 'sad'
    elif scores['neg'] > 0.5:
        return 'angry'
    else:
        return 'neutral'
