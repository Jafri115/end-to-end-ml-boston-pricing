# California House Pricing Prediction

This project is an end-to-end implementation of a machine learning pipeline to predict house prices using the California Housing dataset. It includes data preprocessing, model training, evaluation, and deployment.

---

## Features

- **Data Preprocessing**: Handling missing values, scaling, and feature engineering.
- **Model Training**: Trained multiple models including Linear Regression, Random Forest, and Gradient Boosting.
- **Model Evaluation**: Compared models using performance metrics like R², MSE, and MAE.
- **Model Deployment**: Saved the trained model using pickle for deployment and new data predictions.
- **Web Application**: Creating Flask webapplication for prediction of prices.
- **Deployment**: Deployed Application using Heroku and Dockers

---

## Tools and Software Requirements
- **Python 3.8+**
- **Flask**
- **Docker**
- **Git**
- **Heroku CLI**


## Project Structure
```plaintext
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── Procfile             # Heroku configuration
├── static/              # Static files (CSS, JS, etc.)
├── templates/           # HTML templates
├── model.pkl            # Pickled machine learning model
├── dataset/             # Dataset files
└── README.md            # Project documentation
```
## Requirements

To run this project, ensure you have the following installed:
- Python 3.7 or above
- Required packages listed in `requirements.txt`

Install the packages using:
```bash
pip install -r requirements.txt
