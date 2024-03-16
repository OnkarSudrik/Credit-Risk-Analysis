# Credit-Risk-Analysis
Credit Risk Analysis: Flask web app predicts credit card defaults. Includes EDA, model selection, model evaluation,   model training, MongoDB integration for data storage

# Credit Risk Analysis

## Overview
This project aims to predict credit card defaults using demographic factors and six months of behavioral data. It includes exploratory data analysis (EDA), model training, and deployment of a Flask web application for predictions.

## Dataset Information
The dataset contains information on default payments, demographic factors, credit data, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

## Technical Aspect
The project is divided into two main parts:
1. **Model Training**:
   - Utilizes RandomForestClassifier for prediction.
   - Preprocessing involves dataset cleaning and feature fixing.
2. **Flask Web Application**:
   - Development using Flask API.
   - GitHub project upload.
   - Integration with MongoDB for data storage.
   - Deployment on AWS and Local Server.

## User Interface
The web application provides a user-friendly interface for users to input their information and receive predictions. Below is a screenshot of the user interface:

![User Interface](https://github.com/OnkarSudrik/Credit-Risk-Analysis/raw/main/UI.png)

## Technologies Used

[<img target="_blank" src="https://www.python.org/static/img/python-logo.png" width=100 style="margin-right: 20px;">](https://www.python.org/)    [<img target="_blank" src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" width=100 style="margin-right: 20px;">](https://flask.palletsprojects.com/en/2.0.x/)    [<img target="_blank" src="https://www.mongodb.com/assets/images/global/favicon.ico" width=100 style="margin-right: 20px;">](https://www.mongodb.com/)    [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=100 style="margin-right: 20px;">](https://scikit-learn.org/stable/)    [<img target="_blank" src="https://pandas.pydata.org/static/img/pandas_mark.svg" width=100 style="margin-right: 20px;">](https://pandas.pydata.org/)    [<img target="_blank" src="https://numpy.org/images/logo.svg" width=100 style="margin-right: 20px;">](https://numpy.org/)    [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/38/HTML5_Badge.svg" width=100 style="margin-right: 20px;">](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)    [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" width=100 style="margin-right: 20px;">](https://developer.mozilla.org/en-US/docs/Web/CSS) <img target="_blank" src="https://user-images.githubusercontent.com/315810/92159303-30d41100-edfb-11ea-8107-1c5352202571.png" width=100 style="margin-right: 20px;">[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" width=100 style="margin-right: 20px;">](https://matplotlib.org/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width=100 style="margin-right: 20px;">](https://aws.amazon.com/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" width=100 style="margin-right: 20px;">](https://code.visualstudio.com/)


## Installation
Ensure you have Python 3.9 installed. Clone the repository and navigate to the project directory. Create a virtual environment and install the required packages using:
```bash
pip install -r requirements.txt
