import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    GhitRepos = requests.get("https://api.github.com/search/repositories?q=created:%3E2021-08-01&sort=stars&order=desc&page=1&&per_page=100").json()
    return render_template('layout.html',
        heading='Sample section',
        body_text='Very important<br/>message here!',
        pages=[
            dict(title='Home', href='/'),
            dict(title='About', href='/about')
        ],
        GhitRepos = GhitRepos
    )
