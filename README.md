# Sentiment Analysis Project

## Overview
This project implements a text classification machine learning model that analyses the customer's sentiments based on their reviews about a restaurant.  The dataset is preprocessed, cleaned, and used to train a Naive Bayes classifier to classify reviews as either Positive or Negative.

##Project Structure
This project is focused on building a sentiment analysis model for restaurant reviews. It consists of the following major components:

1. model.py

This script contains the code for training the sentiment analysis machine learning model.
The model is trained using a dataset of restaurant reviews to classify them as Positive or Negative.
Once trained, the model and the CountVectorizer (used for text preprocessing) are saved as pickle files (model.pkl and cv-model.pkl).

2. app.py- This script is the main Flask application that powers the project. It provides two functionalities:
A GUI to input restaurant reviews via an HTML form and display the sentiment prediction and a RESTful api to accept reviews in JSON format and return predictions programmatically.
The app preprocesses the reviews, transforms them using the saved CountVectorizer, and predicts sentiment using the trained model.

3. request.py- This script demonstrates how to make API calls to the Flask app endpoints using Python's requests library. It sends sample review data to the API and displays the predicted sentiment returned by the server.

4. templates/- This folder contains HTML templates used to render the web interface for the application.

5. static/- This folder contains any static files such as CSS and JavaScript that enhance the functionality and styling of the web application.


## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
2. Open the Colab notebook::
   - [Prediction Notebook](https://colab.research.google.com/github/sanskriti49/Sentimental-Analysis/blob/main/Sentiment_Predictor.ipynb)
  
## Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000

## Usage
1. Run the script to train the model and display performance metrics:
   ```python sentiment_analysis.py```
   
2. View the final_df DataFrame to see the original reviews with their classified sentiments.
3. Use the saved model.pkl and cv-model.pkl files for predictions on new data.

The script generates:
1. Accuracy score and confusion matrix for the trained model.
2. A DataFrame (final_df) mapping original reviews to their classified sentiments.

## Example of final_df:

| Review  | Second Header |
| ------------- | ------------- |
|The food was amazing! | Positive  |
| Terrible service and cold food | Negative  |
