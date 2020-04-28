# coding = utf-8

from flask import Flask, render_template, redirect, url_for, request

# In Google Cloud Platform
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

TUTORIAL_FLASK_PATH = '/tutorial_flask'

# Main Home Page
@app.route('/')
def index():
    error = None
    return render_template('index.html', error=error)

# Tutorial-1
@app.route(TUTORIAL_FLASK_PATH + '/tutorial1')
def hello():
    # return "Tutorial: Flask Web Application - Hello World!"
    error = None
    return render_template('tutorial1.html', error=error)

# Tutorial-2
@app.route(TUTORIAL_FLASK_PATH + '/tutorial2', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'guest' and request.form['password'] == 'guest':
            # redirect to success page: call tutorial2_welcome() function
            return redirect(url_for('tutorial2_welcome'))
        else:
            error = 'try again with username=guest and password=guest'
    return render_template('tutorial2.html', error=error)

@app.route(TUTORIAL_FLASK_PATH + '/tutorial2/welcome')
def tutorial2_welcome():
    # return "Welcome! Your login is successful."
    error = None
    return render_template('tutorial2_welcome.html', error=error)


if __name__ == "__main__":
    app.run()