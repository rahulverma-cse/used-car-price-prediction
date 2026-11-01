import numpy as np 
import pandas as pd 
from flask import Flask,render_template,request,jsonify
import joblib
import warnings
warnings.filterwarnings("ignore")

car_model = joblib.load("models/car_model_small.pkl")



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("predict.html")

    try:
        
        model_name = request.form["model"]
        vehicle_age = int(request.form["vehicle_age"])
        km_driven = int(request.form["km_driven"])
        seller_type = request.form["seller_type"]
        fuel_type = request.form["fuel_type"]
        transmission_type = request.form["transmission_type"]
        mileage = float(request.form["mileage"])
        engine = float(request.form["engine"])
        max_power = float(request.form["max_power"])
        seats = int(request.form["seats"])

        input_data = pd.DataFrame([{
            "model": model_name,
            "vehicle_age": vehicle_age,
            "km_driven": km_driven,
            "seller_type": seller_type,
            "fuel_type": fuel_type,
            "transmission_type": transmission_type,
            "mileage": mileage,
            "engine": engine,
            "max_power": max_power,
            "seats": seats
        }])

        prediction = car_model.predict(input_data)[0]

        return render_template(
            "result.html",
            prediction=round(float(prediction), 2)
        )



    except Exception as e:
        print("PREDICTION ERROR:", repr(e))
        raise





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

