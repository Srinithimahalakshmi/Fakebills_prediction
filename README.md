# Fakebills_prediction
## Goal
The goal is to analyze the dimensions of Euro banknotes and determine whether a bill is a fake or a genuine one.
## Dataset
The dataset consists of 1500 banknotes, of which 1000 are genuine and 500 are fake. The data consists of six columns:
* is_genuine: This is the target variable. It is 1 for genuine banknotes and 0 for fake banknotes.
* length: The length of the banknote in mm.
* left: The length of the left edge of the banknote in mm.
* right: The length of the right edge of the banknote in mm.
* bottom: The length of the bottom edge of the banknote in mm.
* top: The length of the top edge of the banknote in mm.
* diagonal: The length of the diagonal of the banknote in mm.
## Steps Involved
1. Data Analysis
2. Model Training
3. Model Evaluation
4. Flask Deployment
## Model
I have built a Random Forest Classifier model to predict the genuineness of the banknotes.
## Accuracy
The model achieved an accuracy of 99.8%.

This repository demonstrates the following:
* Data preprocessing and analysis.
* Building a machine learning model using scikit-learn.
* Deploying the model using Flask.
* Creating a simple web interface to interact with the model.
