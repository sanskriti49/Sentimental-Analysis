import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

app=Flask(__name__)

cv=pickle.load(open('cv-model.pkl','rb'))
classifier=pickle.load(open('model.pkl','rb'))

nltk_stopwords=stopwords.words('english')
nltk_stopwords.remove('not')

#pre-process user input
def preprocess_review(review):
    ps=PorterStemmer()
    review=re.sub('[^a-zA-Z]',' ',review)
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in set(nltk_stopwords)]    
    return ' '.join(review)

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None, original_review=None)

@app.route('/predict', methods=['POST'])
def predict():
    #for Rendering results on the HTML Page
    
    review=request.form['review']
    
    if review:
        processed_review=preprocess_review(review)
        transformed_review=cv.transform([processed_review]).toarray()
        prediction=classifier.predict(transformed_review)[0]
        
        sentiment="Positive" if prediction==1 else "Negative"
        return render_template('index.html', prediction_text=f"Sentiment of the review is: {prediction}", original_review=review)
    
    else:
        return render_template('index.html', prediction_text=None, original_review=None)
    # return jsonify({'review':review, 'sentiment':sentiment})

@app.route('/predict', methods=['POST'])
def predict_api():
    #for Rendering results on the HTML Page
    
    data=request.get_json()
    if 'review' not in data:
        return jsonify({'error':'No review provided in the request'})
    
    review=data['review']
    processed_review=preprocess_review(review)
    transformed_review=cv.transform([processed_review]).toarray()
    prediction=classifier.predict(transformed_review)[0]
    
    sentiment="Positive" if prediction==1 else "Negative"
    return jsonify({'original_review': review, 'sentiment': sentiment})

if __name__=='__main__':
    app.run(debug=True)