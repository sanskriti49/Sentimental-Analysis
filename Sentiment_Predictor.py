# importing libraries
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from nltk.corpus import stopwords   
from nltk.stem.porter import PorterStemmer
import re
import nltk

nltk.download('stopwords')

# importing dataset
url = "https://raw.githubusercontent.com/sanskriti49/Sentimental-Analysis/refs/heads/main/Restaurant%20reviews.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")
df = df.drop(columns=["Restaurant","Reviewer","Metadata","Time","Pictures"])

# tokenizing, cleaning and stemming data
y = df["Rating"]
X = df.drop(columns=["Rating"])
y = y.replace({'Like':3})
y = y.fillna(y.median())
y = pd.to_numeric(y)

y = y.astype(object)
for i in range(0,len(y)):
    y.iloc[i] = round(y.iloc[i],0)

for i in range(0,len(y)):
    if (y[i]>=3):
        y[i] = "Positive"
    else:
        y[i] = "Negative"

ps = PorterStemmer()
corpus = []
for i in range(0, len(X)):
    review = re.sub('[^a-zA-Z]',' ', str(X['Review'][i]))
    review = review.lower()
    review = review.split()

    review = [ps.stem(word) for word in review if not word in stopwords.words('english')] #stemming
    review = ' '.join(review)
    corpus.append(review)

# creating matrix of CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=9000)
X = cv.fit_transform(corpus).toarray()

# Train-Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# applying MultinomialNB
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(X_train, y_train)

# making predictions
y_pred = classifier.predict(X_test)

# creating confusion matrix
from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(y_test, y_pred)
print(confusion_m)

# getting the accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# saving models
import pickle
pickle.dump(classifier,open('model.pkl','wb'))
pickle.dump(cv,open('cv-model.pkl','wb'))

# create a DataFrame with cleaned reviews and their corresponding sentiments
final_df = pd.DataFrame({'Review': df['Review'], 'Sentiment': y})

# display the first few rows of the new DataFrame
print(final_df.head())
