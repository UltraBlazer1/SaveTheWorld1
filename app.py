from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study', methods=['GET', 'POST'])
def study():
    if request.method == 'POST':
        # handle form submission
        subject = request.form['subject']
        hours = request.form['hours']
        date = request.form['date']
        # save the study plan to a database or file
        return render_template('study.html', subject=subject, hours=hours, date=date)
    else:
        return render_template('study.html')

@app.route('/fitness', methods=['GET', 'POST'])
def fitness():
    if request.method == 'POST':
        # handle form submission
        exercise = request.form['exercise']
        duration = request.form['duration']
        date = request.form['date']
        # save the fitness plan to a database or file
        return render_template('fitness.html', exercise=exercise, duration=duration, date=date)
    else:
        return render_template('fitness.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        # handle form submission
        items = request.form.getlist('items')
        # save the shopping list to a database or file
        return render_template('food.html', items=items)
    else:
        return render_template('food.html')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        # handle form submission
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = format(weight / (height ** 2), '.1f')
        return render_template('bmi.html', bmi=bmi)
    else:
        return render_template('bmi.html')

@app.route('/health_survey', methods=['GET', 'POST'])
def health_survey():
    if request.method == 'POST':
        # handle form submission
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        exercise = request.form['exercise']
        diet = request.form['diet']
        # save the survey data to a database or file
        return render_template('health_survey.html')
    else:
        return render_template('health_survey.html')

@app.route('/gym_registration', methods=['GET', 'POST'])
def gym_registration():
    if request.method == 'POST':
        # handle form submission
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        membership_type = request.form['membership_type']
        # save the registration data to a database or file
        return render_template('gym_registration.html')
    else:
        return render_template('gym_registration.html')

if __name__ == '__main__':
    app.run(debug=True)

