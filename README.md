# Used Car Price Prediction

A machine learning web app that predicts the resale price of a used car based on details like [brand, year, fuel type, kilometers driven, etc.].

## Features

- Simple web form to enter car details
- Instant price prediction using a trained ML model
- Clean, responsive UI built with HTML and CSS

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **ML:** scikit-learn, pandas, NumPy
- **Frontend:** HTML, CSS

## Project Structure

```
used-car-price-prediction/
├── data/            # Dataset (car_data.csv)
├── models/          # Trained model (car_model_small.pkl)
├── notebooks/       # Model training notebook
├── static/          # CSS files
├── templates/       # HTML pages
├── app.py           # Flask application
├── requirements.txt # Dependencies
└── README.md
```

## Model Details

- **Algorithm:** Random Forest Regressor
- **R² Score:**  0.95
- **Dataset:** `data/car_data.csv`

The full training process is in `notebooks/model_traning.ipynb`.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/rahulverma-cse/used-car-price-prediction.git
   cd used-car-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`


## Future Improvements

- Add more car brands and features
- Try other models (XGBoost, Gradient Boosting)
- Deploy the app online

## Author

**Rahul Verma**
GitHub: [rahulverma-cse](https://github.com/rahulverma-cse)
