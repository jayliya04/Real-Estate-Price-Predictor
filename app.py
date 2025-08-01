from flask import Flask, request, jsonify, render_template
import joblib
import json
import numpy as np

app = Flask(__name__)

# Load model
model=joblib.load('prediction_model')

# Load column data
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

# Extract location names (ignore first 3 features: sqft, bath, bhk)
locations = [col for col in data_columns[3:]]

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form['location'].lower()
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])

        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        prediction = model.predict([x])[0]
        return render_template('index.html', locations=locations,
                               prediction_text=f'Estimated Price: ₹ {round(prediction, 2)} lakhs')

    except Exception as e:
        return render_template('index.html', locations=locations,
                               prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)