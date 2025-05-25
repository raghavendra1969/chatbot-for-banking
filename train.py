import json
import nltk
import pickle
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nltk.download('punkt')

with open('intents.json') as f:
    data = json.load(f)

X = []
y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

model = Pipeline([
    ('vectorizer', CountVectorizer(tokenizer=nltk.word_tokenize, lowercase=True)),
    ('classifier', MultinomialNB())
])

model.fit(X, y)

with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as chatbot_model.pkl")
