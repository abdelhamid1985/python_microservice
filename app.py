import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    GhitRepos = requests.get("https://api.github.com/search/repositories?q=created:%3E2021-08-01&sort=stars&order=desc&page=1&&per_page=100").json()
    return render_template('layout.html',
        heading='GhitHub Languages Statistics',
        body_text='Find out a list of most used languages for top 100 trending repositories<br/><br /><hr /><br /><br />',
        pages=[
            dict(title='Home', href='/'), # List infos about the app
            dict(title='Stats', href='/stats') # Provide statistics for languages
        ],
        items = GhitRepos['items']
    )
