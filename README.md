# House Price Prediction Web App Documentation
### Welcome to the House Price Prediction Web App documentation! This document serves as a guide for users who are not familiar with Python and Django but wish to understand how to use and deploy this web application.

# Overview
The House Price Prediction Web App is a Django-based application designed to provide users with predictions for house rent and sales prices in Rwanda. It utilizes machine learning models trained on historical data to make predictions.

### Folder Structure
- **iris/**: The project folder.
- **predict/:** The app folder containing views and database schemas.
- **templates/:** Contains HTML templates for the web pages.
- **db.sqlite3:** SQLite database file for storing data.
- **manage.py:** Django management script for running administrative tasks.
- **rent_model.pickle:** Pickled machine learning model for predicting house rent prices.
- **sales_model.pickle:** Pickled machine learning model for predicting house sales prices.
- **requirements.txt:** List of Python dependencies required for the project.
- **runtime.txt:** Specifies the Python version used in the project.
- **Procfile:** Specifies the commands that are executed by the app on Render.
## Deployment
Hosting Platform
The web app is hosted on Render `https://ewawehpi.onrender.com/`, a cloud platform for deploying and scaling web applications but **not forever**.

# To run it locally. Steps:

Clone the repository to your local machine.
Install Python on your system if not already installed.
Create a virtual environment if you want and activate it
Install the required dependencies using `pip install -r requirements.txt`.
Run `python manage.py migrate`
finally, run `python manage.py runserver`

Head over to your local host `172.0.0.1:8000` and you find your app is running on the local machine.
