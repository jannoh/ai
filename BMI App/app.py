# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # BMI Calculation
        bmi = weight / (height ** 2)

        # Interpretation
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 25:
            category = 'Normal weight'
        elif 25 <= bmi < 30:
            category = 'Overweight'
        else:
            category = 'Obese'

        return render_template('result.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
