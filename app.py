
#import necessary packages
from flask import Flask, render_template, request, redirect, url_for, make_response
#from datetime import date
import db

# instantiate the app
app = Flask(__name__)

'''
# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mode
'''



#login page
@app.route("/login")
def login():
    """
    Route for GET request to login page
    Displays form for user
    """
    title = 'Login'
    return render_template('login.html', title = title)

#validate login
@app.route('/login', methods=['POST'])
def validate_login():
    """
    Route for POST requests to the login page
    Validates login attempt
    """
    global username
    username = request.form['username']
    password = request.form['password']

    # check if username and password are in the users table
    if db.login_data.count_documents({'username': username, 'password': password}) != 0:
        #allow login and redirect
        return redirect(url_for('home')) # tell the browser to make a request for the /home route
        #but logged in version
    else:
        #return error message in login page
        error = "Invalid username or password. Please try again."
        return render_template('login.html', error=error)

#index
@app.route("/index")
def index():
    """
    Route for GET request to index page
    Displays form for user
    """
    return render_template('index.html')

#sign_up_athletecoach
@app.route("/sign_up_athlete")
def sign_up_athlete():
    """
    Route for GET request to sign_up_athlete page
    Displays form for user
    """
    return render_template('sign_up_athletecoach.html')

#sign_up_athletecoach
@app.route("/sign_up_coach")
def sign_up_coach():
    """
    Route for GET request to sign_up_coach page
    Displays form for user
    """
    return render_template('sign_up_athletecoach.html')

@app.route('/sign_up_coach', methods=['POST'])
def add_coach():
    """
    Route for POST requests to the sign up pages.
    Accepts the form submission data for a new document and saves the document to the database.
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_type = 'coach'

    #return error if their account already exists
    if db.login_data.count_documents({'email': email}) != 0:
        error = "An account with this email already exists."
        return render_template('sign_up_coach.html', error = error)
     
    
    # create a new document with the data the user entered
    doc = {
        "username": username,
        "password": password,
        "email": email, 
        "user_type": user_type,
        #"created_at": date.today()
    }
    db.login_data.insert_one(doc) # insert a new document for user
    return redirect(url_for('home')) # tell the browser to make a request for the /home route


#sign_up_sponsor
@app.route("/sign_up_sponsor")
def sign_up_sponsor():
    """
    Route for GET request to sign_up_sponsor page
    Displays form for user
    """
    return render_template('sign_up_sponsor.html')

@app.route('/sign_up_sponsor', methods=['POST'])
def add_sponsor():
    """
    Route for POST requests to the sign up pages.
    Accepts the form submission data for a new document and saves the document to the database.
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_type = 'sponsor'

    #return error if their account already exists
    if db.login_data.count_documents({'email': email}) != 0:
        error = "An account with this email already exists."
        return render_template('sign_up_sponsor.html', error = error)
    
    # create a new document with the data the user entered
    doc = {
        "username": username,
        "password": password,
        "email": email, 
        "user_type": user_type,
        #"created_at": date.today()
    }
    db.login_data.insert_one(doc) # insert a new document for user
    return redirect(url_for('home')) # tell the browser to make a request for the /home route

@app.route('/sign_up_athlete', methods=['POST'])
def add_athlete():
    """
    Route for POST requests to the sign up pages.
    Accepts the form submission data for a new document and saves the document to the database.
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_type = 'athlete'

    #return error if their account already exists
    if db.login_data.count_documents({'email': email}) != 0:
        error = "An account with this email already exists."
        return render_template('sign_up_athletecoach.html', error = error)
    
    # create a new document with the data the user entered
    doc = {
        "username": username,
        "password": password,
        "email": email, 
        "user_type": user_type,
        #"created_at": date.today()
    }
    db.login_data.insert_one(doc) # insert a new document for user
    return redirect(url_for('home')) # tell the browser to make a request for the /home route

#athleteprofile
@app.route("/athleteprofile")
def athleteprofile():
    """
    Route for GET request to athleteprofile page
    Displays form for user
    """
    return render_template('athleteprofile.html')

#athleteprofileedit
@app.route("/athleteprofileedit")
def athleteprofileedit():
    """
    Route for GET request to athleteprofileedit page
    Displays form for user
    """
    return render_template('athleteprofileedit.html')

#sponsorprofile
@app.route("/sponsorprofile")
def sponsorprofile():
    """
    Route for GET request to sponsorprofile page
    Displays form for user
    """
    return render_template('sponsorprofile.html')

#sponsorprofileedit
@app.route("/sponsorprofileedit")
def sponsorprofileedit():
    """
    Route for GET request to sponsorprofileedit page
    Displays form for user
    """
    return render_template('sponsorprofileedit.html')

#home
@app.route("/home")
def home():
    """
    Route for GET request to home page
    Displays form for user
    """
    return render_template('home.html')

#coach views players list
@app.route("/viewathletes")
def view_athletes():
    """
    Route for GET request to viewathletes page
    Displays page where coach can view all athletes under them; only coach can access
    """
    #docs = db.athletes_data.find({"coach_id":username}).sort("athlete_name", -1)
    return render_template('viewplayers.html')

@app.route("/createrequest")
def create_request():
    """
    Route for GET request to createrequest page
    Displays page where coach/athlete can create request
    """
    return render_template('requestform.html')

if __name__ == '__main__':
    app.run(debug = True, port=8000)