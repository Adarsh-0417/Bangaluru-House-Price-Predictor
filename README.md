🏠 Bengaluru House Price Prediction

A machine learning web application that predicts house prices in Bengaluru based on location, square footage, number of bedrooms (BHK), and bathrooms.

The project demonstrates an end-to-end ML workflow, including data preprocessing, feature engineering, model training, and deployment using Flask and Bootstrap.

🚀 Features

Predict house prices in real time

Dynamic location dropdown generated from dataset

Clean Bootstrap UI

Trained Regression model

Flask backend serving predictions

🧠 Machine Learning Pipeline

The model was built using the following workflow:

Data Cleaning

Removed irrelevant columns

Handled missing values

Feature Engineering

Extracted BHK from size

Converted total_sqft ranges to numeric values

Created price_per_sqft

Outlier Removal

Removed unrealistic sqft values

Removed illogical BHK pricing

Model Training

Linear Regression

Lasso Regression

Ridge Regression

Model Selection

Cross-validation

Performance comparison

🛠 Tech Stack

Backend

Python

Flask

Scikit-learn

Pandas

NumPy

Frontend

HTML

Bootstrap

Jinja Templates
