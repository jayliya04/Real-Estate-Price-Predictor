# Real Estate Price Predictor

A machine learning web application that predicts real estate prices in Bangalore, India based on location, area, number of bedrooms (BHK), and bathrooms.

## Features

- **Price Prediction**: Predict house prices in Bangalore using machine learning
- **Location-based**: Supports multiple locations across Bangalore
- **User-friendly Interface**: Clean and intuitive web interface
- **Real-time Predictions**: Instant price estimates based on input parameters

## Project Structure

```
Real Estate Price Predictor/
├── app.py                          # Flask web application
├── bengaluru_house_prices.csv      # Dataset containing house prices
├── columns.json                    # Feature columns configuration
├── prediction_model                # Trained machine learning model
├── real_estate_price_prediction.ipynb  # Jupyter notebook for model development
├── static/
│   └── style.css                   # CSS styling for the web interface
└── templates/
    └── index.html                  # HTML template for the web interface
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Data Visualization**: matplotlib, seaborn
- **Frontend**: HTML, CSS
- **Model Persistence**: joblib

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Real-Estate-Price-Predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## Usage

1. **Select Location**: Choose a location from the dropdown menu
2. **Enter Area**: Input the area in square feet
3. **Specify BHK**: Enter the number of bedrooms (BHK)
4. **Add Bathrooms**: Specify the number of bathrooms
5. **Predict**: Click "Predict Price" to get the estimated price

The application will display the predicted price in Indian Rupees (lakhs).

## Model Information

The machine learning model is trained on the Bangalore house prices dataset and uses the following features:
- **Location**: One-hot encoded location features
- **Area**: Square footage of the property
- **BHK**: Number of bedrooms
- **Bathrooms**: Number of bathrooms

## Dataset

The model is trained on the `bengaluru_house_prices.csv` dataset, which contains:
- House prices in Bangalore
- Location information
- Property details (area, BHK, bathrooms)
- Additional features like area type, society, balcony, availability
- **Dataset link**: https://www.kaggle.com/code/tanushagupta/bangaluru-house-price-analysis/input

## Development

The model development process is documented in the Jupyter notebook `real_estate_price_prediction.ipynb`, which includes:
- Data loading and exploration
- Data cleaning and preprocessing
- Feature engineering
- Model training and evaluation
- Model persistence

## API Endpoints

- `GET /`: Home page with the prediction form
- `POST /predict`: Predicts house price based on form inputs

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy
- joblib
- matplotlib
- seaborn

## Acknowledgments

- Dataset: Bangalore house prices dataset
- Flask framework for web development
- scikit-learn for machine learning capabilities 
