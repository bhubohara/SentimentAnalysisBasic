Sentiment Analysis Project

This is a Sentiment Analysis project built in Python using TextBlob.
It analyzes text input and classifies the sentiment as Positive 😊, Negative 😠, or Neutral 😐.

Libraries Used:
- Python 3.x
- TextBlob – for natural language processing and sentiment analysis
- dataclasses – for structured result objects (built-in in Python 3.7+)

Setup Instructions:

1. Clone the repository (or download):
   git clone https://github.com/your-username/SentimentAnalysisBasic.git
   cd SentimentAnalysisBasic

2. Create and activate virtual environment (recommended)

   Windows:
   python -m venv venv
   venv\Scripts\activate

   Mac/Linux:
   python -m venv venv
   source venv/bin/activate

3. Install required library:
   pip install textblob

4. Download TextBlob corpora:
   python -m textblob.download_corpora

How to Run:

Run the program using Python:

   python sentiment.py

- The program will ask you to enter a sentence.
- It will return sentiment emoji and polarity score.
- Type 'exit' to quit.

Example:

Enter text to analyze (or 'exit' to quit): I love AI
Sentiment: 😊 looks happy (Polarity: 0.50)

Enter text to analyze (or 'exit' to quit): This is bad
Sentiment: 😠 looks angry (Polarity: -0.60)

Enter text to analyze (or 'exit' to quit): exit

Project Files:
- sentiment.py – main Python script
- README.txt – this file
- .gitignore – ignores virtual environment and cache files

Notes:
- Polarity ranges from -1 (negative) to +1 (positive)
- Threshold can be adjusted in analyze_sentiment function for stricter or looser sentiment detection

Author:
Bhupendra Bohara – GitHub: https://github.com/bhubohara