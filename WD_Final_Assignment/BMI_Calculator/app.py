from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            bmi = round(weight / ((height / 100) ** 2), 2)

            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 24.9:
                category = 'Normal'
            elif 25 <= bmi < 29.9:
                category = 'Overweight'
            else:
                category = 'Obese'
        except Exception as e:
            print("Error:", e)
            bmi = None
            category = "Invalid input"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
