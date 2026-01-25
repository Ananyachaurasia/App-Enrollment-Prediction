from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Binary screen features list
binary_screens = [
    'location', 'Institutions', 'VerifyPhone', 'BankVerification', 'VerifyDateOfBirth',
    'ProfilePage', 'VerifyCountry', 'Cycle', 'idscreen', 'Splash', 'RewardsContainer',
    'EditProfile', 'Finances', 'Alerts', 'Leaderboard', 'VerifyMobile', 'VerifyHousing',
    'RewardDetail', 'VerifyHousingAmount', 'ProfileMaritalStatus', 'ProfileChildren',
    'ProfileEducation', 'ProfileEducationMajor', 'Rewards', 'AccountView',
    'VerifyAnnualIncome', 'VerifyIncomeType', 'ProfileJobTitle', 'Login',
    'ProfileEmploymentLength', 'WebView', 'SecurityModal', 'ResendToken',
    'TransactionList', 'NetworkFailure', 'ListPicker', 'other'
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html', binary_screens=binary_screens)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = int(request.form.get('age'))
        dayofweek = int(request.form.get('dayofweek'))
        hour = int(request.form.get('hour'))

        savings_count = int(request.form.get('savings_count'))
        cm_count = int(request.form.get('cm_count'))
        cc_count = int(request.form.get('cc_count'))
        loans_count = int(request.form.get('loans_count'))

        numscreens = int(request.form.get('numscreens'))
        minigame = int(request.form.get('minigame'))
        used_premium = int(request.form.get('used_premium'))
        liked = int(request.form.get('liked'))

        # Get binary screen values
        screen_values = []
        for screen in binary_screens:
            val = 1 if request.form.get(screen) == 'on' else 0
            screen_values.append(val)

        # Prepare data row in exact order
        data_row = [
            dayofweek, hour, age, numscreens, minigame, used_premium, liked,
            *screen_values,
            savings_count, cm_count, cc_count, loans_count
        ]

        # Convert to array and scale
        input_array = np.array([data_row])
        input_scaled = scaler.transform(input_array)

        # Predict
        prediction = model.predict(input_scaled)
        prob = model.predict_proba(input_scaled)[0][1]

        result = {
            'enrolled': int(prediction[0]),
            'probability': float(prob)
        }

        return render_template('predict.html', result=result)

    except Exception as e:
        return render_template('predict.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)

