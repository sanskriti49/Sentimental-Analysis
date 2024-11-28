# Sentiment Analysis Project

## Overview
This project implements a text classification machine learning model that analyses the customer's sentiments based on their reviews about a restaurant.  The dataset is preprocessed, cleaned, and used to train a Naive Bayes classifier to classify reviews as either Positive or Negative.

##Project Structure
This project is focused on building a sentiment analysis model for restaurant reviews. It consists of the following major components:

- **`model.py`**: Code to train the sentiment analysis model. It uses a dataset of restaurant reviews and saves the trained model (`model.pkl`) and the CountVectorizer (`cv-model.pkl`).
- **`app.py`**: Flask app that serves as the main application. It provides:
  - A web interface to input reviews and get predictions.
  - A REST API to send reviews programmatically and get responses.
- **`request.py`**: A script to demonstrate how to call the Flask API using Python's `requests` library.
- **`templates/`**: Contains the HTML template for the web interface.
- **`static/`**: Contains static files like JavaScript and CSS.


## How to Clone and Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Sentiment-Analysis.git
   cd Sentiment-Analysis
   
## Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
```python app.py```

By default, flask will run on port 5000. Navigate to url http://localhost:5000

## Model Training
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
