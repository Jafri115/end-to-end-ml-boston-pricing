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
```
## Deployement on Heroku for Live Demo
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Jafri115/end-to-end-ml-california-pricing)

## Deploy and Setup Instructions

Follow the [Heroku Devcenter Instructions](https://devcenter.heroku.com/articles/app-webhooks-tutorial)


## CI/CD Heroku Deployment Workflow
This project uses GitHub Actions to automate the deployment process to Heroku. The workflow performs the following steps:

Build: Creates a Docker container using the Dockerfile.
Push: Uploads the container to the Heroku Container Registry.
Deploy: Releases the container, making the application live on Heroku.
Simply push changes to the main branch, and the workflow will handle the deployment automatically.