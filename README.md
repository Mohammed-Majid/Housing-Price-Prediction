# Housing Price Prediction Using Kaggle Dataset
-------
This repository contains code for a regression model that predicts housing prices. The Project also contains code for a frontend (streamlit).
------
## Overview

The Project involves the following

- Pre-processing: EDA, Feature engineering and Outlier Removal.
- Modeling: K-Fold Cross-Validation, Grid Search (Multiple models) and building a predictive model.
- Evaluation: Testing the Model.
-------
## Usage

- Clone the Repository

- Install Dependencies: Make sure you have the necessary dependencies installed. You can install them using pip:
```
pip install numpy pandas matplotlib scikit-learn pickle
```
- Run app.py: Execute the script to launch a streamlit app on local host
-------
## Requirements

- Python 3.x
- numpy
- pandas
- Pickle
- Scikit-Learn
- matplotlib
--------
## Project Structure

- app.py: streamlit application
- model.ipynb: Regression Model
- model.pickle: Persisted Model used in streamlit application
- util.py: Main Functions used to import and run model
- house.csv: Dataset
- columns.json: Feature Vector
