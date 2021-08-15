#---------------------------------------------------------------------------#
#  Flask based microservice to get statics about languages usage on github  #
#  Author : Abdelhamid BOUSSABOUNE                                          #     
#  Licence: Open Source                                                     #
#---------------------------------------------------------------------------#

import requests
from flask import Flask, render_template

app = Flask(__name__)

# Our Home page where statistics will be generated 
@app.route('/')
def home():
    # Calling github api to get the top 100 trending repos into json output
    GitRepos = requests.get("https://api.github.com/search/repositories?q=created:%3E2021-08-01&sort=stars&order=desc&page=1&&per_page=100").json()
    items = GitRepos['items']

    # Rendering our view
    return render_template('layout.html',
        heading='GitHub Languages Statistics',
        body_text='Find out a list of most used languages for top 100 trending repositories<br/><hr /><br />',
        langs = get_stats(items)
    )

# Method that actually get the statistics from api returned content
def get_stats(items):
    langs = {}
    
    # We loop the api returned content, count languaged and generate repos lists
    for item in items:
        if(item['language'] not in langs):
            langs[item['language']] = { 'count': 0, 'repos': [] } 
        langs[item['language']]['count'] += 1
        langs[item['language']]['repos'].append(item['name'])

    return langs
    
