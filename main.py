from flask import Flask, render_template, request
from api.urls import app_add_urls

app = Flask(__name__)
app = app_add_urls(app)


@app.route('/')
def index():
    return render_template('index.html')


# To be deleted later
@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
