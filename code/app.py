from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('marriage_age_predict_model.ml')  # Ensure the path to your model file is correct.

# Full mappings based on the model's training data
gender_map = {'female': 0, 'male': 1}
religion_map = {'jain': 0, 'hindu': 1, 'christian': 2, 'muslim': 3, 'sikh': 4, 'other': 5}
caste_map = {'shwetamber': 0, 'brahmin': 1, 'thakur': 2, 'born again': 3, 'valmiki': 4, 'rajput': 5, 'bhatia': 6, 'billava': 7, 'vanniyar': 8, 'agri': 9, 'marthoma': 10, 'ahom': 11, 'baishnab': 12, 'roman catholic': 13, 'kalita': 14, 'goud': 15, 'bhandari': 16, 'kshatriya': 17, 'patel': 18, 'scheduled caste (sc)': 19, 'viswabrahmin': 20, 'obc': 21, 'sahu': 22, 'panchal': 23, 'arora': 24, 'baishya': 25, 'lingayath': 26, 'kaibarta': 27, 'gursikh': 28}
mother_tongue_map = {'telugu': 0, 'gujarati': 1, 'hindi': 2, 'malayalam': 3, 'punjabi': 4, 'tulu': 5, 'tamil': 6, 'bengali': 7, 'marathi': 8, 'marwari': 9, 'assamese': 10, 'kannada': 11, 'sindhi': 12, 'english': 13, 'odia': 14, 'konkani': 15, 'chattisgarhi': 16, 'kutchi': 17, 'bhojpuri': 18, 'urdu': 19, 'nepali': 20, 'haryanavi': 21, 'rajasthani': 22, 'manipuri': 23, 'aka': 24, 'kashmiri': 25, 'other': 26}
country_map = {'india': 0, 'usa': 1, 'uk': 2, 'australia': 3, 'united arab emirates': 4, 'canada': 5, 'malaysia': 6, 'netherlands': 7, 'sweden': 8, 'qatar': 9, 'pakistan': 10, 'denmark': 11, 'new zealand': 12, 'myanmar': 13, 'hong kong sar': 14, 'bangladesh': 15, 'italy': 16, 'kuwait': 17, 'japan': 18, 'bahrain': 19, 'nigeria': 20, 'ireland': 21, 'singapore': 22, 'armenia': 23, 'oman': 24, 'philippines': 25, 'norway': 26, 'germany': 27, 'south africa': 28}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data and convert to lowercase for consistent mapping
    gender = gender_map.get(request.form['gender'].lower(), -1)
    religion = religion_map.get(request.form['religion'].lower(), -1)
    caste = caste_map.get(request.form['caste'].lower(), -1)
    mother_tongue = mother_tongue_map.get(request.form['mother_tongue'].lower(), -1)
    country = country_map.get(request.form['country'].lower(), -1)
    # Convert height from feet'inches" to cm
    height = convert_height_to_cm(request.form['height'])

    # Ensure all inputs are valid before making a prediction
    if -1 in [gender, religion, caste, mother_tongue, country]:
        return render_template('index.html', error="Please fill in all fields correctly.")

    features = [gender, religion, caste, mother_tongue, country, height]
    prediction = model.predict([features])[0]
    return render_template('predict.html', prediction=prediction)

def convert_height_to_cm(height_str):
    try:
        feet, inches = height_str.split("'")
        feet = int(feet)
        inches = int(inches.replace('"', ''))
        return (feet * 30.48) + (inches * 2.54)
    except ValueError:
        # Handle the case where height is not entered in the expected format
        return -1
'''
if __name__ == '__main__':
    app.run(debug=True)
    
    '''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

