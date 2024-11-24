# Sentiment Analysis Project

## Overview
This project performs sentiment analysis on restaurant reviews using a Naive Bayes classifier. 
It includes:
- Training a sentiment analysis model using historic data.
- Predicting sentiments for new reviews.

## Repository Structure
- `Sentiment_Training_Model.ipynb`: Notebook for training the model.
- `Sentiment_Predictor.ipynb`: Notebook for making predictions on new data.
- `/data`: Contains the datasets (`a1_RestaurantReviews_HistoricDump.tsv`, `a2_RestaurantReviews_FreshDump.tsv`).
- `/models`: Contains serialized models (`c1_BoW_Sentiment_Model.pkl`, `c2_Classifier_Sentiment_Model`).

## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/sanskriti49/Sentimental-Analysis.git
   ```
2. Open the Colab notebooks and follow the steps:
   - [Training Notebook](https://colab.research.google.com/github/sanskriti49/Sentimental-Analysis/blob/main/Sentiment_Training_Model.ipynb)
   - [Prediction Notebook](https://colab.research.google.com/github/sanskriti49/Sentimental-Analysis/blob/main/Sentiment_Predictor.ipynb)

## Requirements
Install dependencies using:
 ``` pip install -r requirements.txt ```
