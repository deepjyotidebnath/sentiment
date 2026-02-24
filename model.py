from textblob import TextBlob

def predict_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive 😊 "
    elif polarity <0:
        return "Negative 😞"
    else: 
        return"Neutral 😐"