from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# load dataset
data = pd.read_csv("cleaned_data.csv")

# clean location column
data['location'] = data['location'].str.strip()

# get all unique locations for dropdown
locations = sorted(data['location'].unique())

# load trained model
model = pickle.load(open("RidgeModel.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html", locations=locations)


@app.route('/predict', methods=['POST'])
def predict():

    location = request.form['location']
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    # create input vector
    input_df = pd.DataFrame({
        "location": [location],
        "total_sqft": [sqft],
        "bath": [bath],
        "bhk": [bhk]
    })

    prediction = round(model.predict(input_df)[0],2)
    return render_template(
        "index.html",
        locations=locations,
        prediction_text=f"Estimated Price: {prediction} Lakhs"
    )


if __name__ == "__main__":
    app.run(debug=True)