import os
import time
import requests as requests
import json

import flask

f = open("python_packages.txt", "r")
content = f.read()

content_list = content.splitlines()
f.close()

for content in content_list:
    print(content)
    response = requests.get('https://pypi.org/pypi/' + content + '/json')
    html_txt = response.text
    index = html_txt.index('github.com')
    print(html_txt[index:index+200])


# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

