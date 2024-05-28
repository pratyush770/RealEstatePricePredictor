# The code related to backend server is written here
from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__, static_url_path='/client', static_folder='../client')  # creating the app
CORS(app)


@app.route('/')
def home():
    return app.send_static_file('app.html')
@app.route('/get_location_names')  # to call a function we create a routine
def get_location_names():
    print(util.get_location_names())
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_area_types')
def get_area_types():
    print(util.get_area_types())
    response = jsonify({
        'area_types': util.get_area_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_price', methods=['POST'])
def predict_price():
    location = request.form['location']
    area_type = request.form['area_type']
    size = int(request.form['size'])
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'predicted_price': util.get_estimated_price(location, area_type, size, total_sqft, bath, balcony)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server for Home Price Prediction")
    app.run()
