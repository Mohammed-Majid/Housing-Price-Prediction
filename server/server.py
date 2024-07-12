# from flask import Flask, request, jsonify
# # from flask_cors import CORS
# import util


# app = Flask(__name__)
# # CORS(app)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })

#     return response

# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     try:
#         location = request.form.get('location')
#         sqft = int(request.form.get('sqft'))
#         bedrooms = int(request.form.get('bedrooms'))
#         bath = int(request.form.get('bath'))
        
#         estimated_price = util.get_estimated_price(location, sqft, bedrooms, bath)
        
#         return jsonify({
#             'estimated_price': estimated_price
#         }), 200
#     except Exception as e:
#         return jsonify({
#             'error': str(e)
#         }), 500
    

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Home Price Prediction...")
#     util.load_saved_artifacts()
#     app.run('localhost', 5000, True)
