from Constants import directories
from files import saveJSONObject
from lib.sentiment import extractSentiment, getSentimentCount, getSentimentVector

sentiment = extractSentiment(directories.SENTIMENT_FILE)
saveJSONObject(sentiment, directories.SENTIMENT)
print sentiment
