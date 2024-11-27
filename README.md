# Sentiment Analysis Project

## Overview
This project implements a text classification machine learning model that analyses the customer's sentiments based on their reviews about a restaurant.  The dataset is preprocessed, cleaned, and used to train a Naive Bayes classifier to classify reviews as either Positive or Negative.



## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
2. Open the Colab notebook::
   - [Prediction Notebook](https://colab.research.google.com/github/sanskriti49/Sentimental-Analysis/blob/main/Sentiment_Predictor.ipynb) 

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
