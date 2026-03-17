from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class SentimentResult:
    emoji: str
    sentiment: float


def analyze_sentiment(input_text: str, *, threshold: float) -> SentimentResult:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return SentimentResult(emoji="😊 looks happy", sentiment=sentiment)
    elif sentiment <= hostile_threshold:
        return SentimentResult(emoji="😠 looks angry", sentiment=sentiment)
    else:
        return SentimentResult(emoji="😐 looks neutral", sentiment=sentiment)


if __name__ == "__main__":
    while True:
        text: str = input("Enter text to analyze (or 'exit' to quit): ")

        if text.lower() == "exit":
            break

        mood: SentimentResult = analyze_sentiment(text, threshold=0.3)
        print(f"Sentiment: {mood.emoji} (Polarity: {mood.sentiment:.2f})")