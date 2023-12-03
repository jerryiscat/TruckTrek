from collections import Counter
from flask import Flask, render_template, jsonify, request
from app.utils.auth_utils import get_token
from flask_cors import CORS
import requests
import json

# Create the Flask app with the template folder specified that will contain your index.html and static folder which will contain your JavaScript files
app = Flask(__name__, template_folder='app/templates', static_url_path='/static')
# By adding CORS(app), you are telling Flask to include CORS headers in responses. The flask_cors extension will add headers such as Access-Control-Allow-Origin: *, allowing requests from any origin.
# This way, when your frontend makes requests to your Flask server, the server will respond with the appropriate CORS headers, and the browser will permit the requests. Since the frontend and backend are on the same origin (domain), you won't encounter CORS issues.
# For more info on CORS goto: https://www.bannerbear.com/blog/what-is-a-cors-error-and-how-to-fix-it-3-ways/
CORS(app)

# This is the route that will serve your index.html template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/getToken', methods=['GET'])
def display_token():
    # This makes the call to the get_token function in the auth_utils.py file
    response, status_code = get_token()
    # If the request is successful, return the token
    if status_code == 200:
        api_token = response
        return jsonify({'message': api_token})
    #If the request fails, return the error message
    else:
        return jsonify({'message': response})
    
@app.route('/accidents', methods=['GET'])
def count_accidents():
    response, status_code = get_token()
    # If the request is successful, return the token
    if status_code == 200:
        api_token = response
        headers = {
            'Authorization': f'Bearer {api_token}'
        }

        start1 = 47.66350964362737
        start2 =  -122.31656051285994
        end1 = 37.773345964182795
        end2 = -122.48529082191631

        api_url = f"https://api.iq.inrix.com/v1/incidents?box=37.757386%7C-122.490667%2C37.746138%7C-122.395481&incidentoutputfields=Core&incidenttype=&locale=en"

        response = requests.get(api_url, headers=headers)
        accidents = response.json()

        accidents_data = accidents["result"]["incidents"]
        accidents_num = len(accidents_data)
        severities = [incident['severity'] for incident in accidents_data]
        severity_counts = Counter(severities)
        most_common_severity = severity_counts.most_common(1)[0][0]
        
        print(accidents_num)
        print(most_common_severity)

        return jsonify({
        'accidents_num': accidents_num,
        'most_common_severity': most_common_severity
    })
        
    #If the request fails, return the error message
    else:
        return jsonify({'message': response})
    
    

if __name__ == '__main__':
    app.run(debug=False, port=5000)
