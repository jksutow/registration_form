from flask import Flask, render_template, redirect, request, session, flash, url_for
#perform regex
import re
#create regex object
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NUM = re.compile('[0-9]')
app = Flask(__name__)
app.secret_key = "shhhThisIsSecret"

@app.route('/', methods=['GET'])
def index():
    if ('flash' not in session):
        session['flash'] = 0
    return render_template("form.html")

@app.route('/submitted', methods=['POST'])
def submit():
    session['flash'] = 0
    validate_name(request.form)
    validate_email(request.form)
    validate_pw(request.form)

    if(session['flash'] == 0):
        flash("Thank you for submitting your information!", 'success')
    return redirect ('/')
def validate_name(form):
    first_name = form['first_name']
    last_name = form['last_name']

    if(len(first_name) == 0):
        flash("First name can't be empty.", 'first_name')
        session['flash'] +=1
    else:
        if(NUM.search(first_name) != None):
            flash("Name cannot contain numbers",'first_name')
        session['flash'] +=1
    if(len(last_name) == 0):
        flash("Last name cannot be empty.", 'last_name')
        session['flash'] +=1
    else:
        if(NUM.search(last_name) != None):
            flash("Name cannot contain numbers", 'last_name')
        session['flash'] +=1
    return

def validate_email(form):
    email = form['email']

    if(len(email) == 0):
        flash("Email cannot be empty", 'email')
        session['flash'] += 1
    else:
        if(EMAIL_REGEX.match(email)== None):
            flash("Invalid Email", 'email')
            session['flash'] += 1
    return

def validate_pw(form):
    password = form['password']
    confirm_pw = form['confirm_pw']

    if (len(password)<=8):
        flash("Password must contain at least 9 characters", 'password')
        session['flash'] += 1
    if(password != confirm_pw):
        flash("Passwords do not match. Please re-type both passwords and submit again", 'password')
        session['flash'] += 1
    return
    # return redirect('/')
app.run(debug=True)
