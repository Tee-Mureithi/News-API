from flask import render_template

from main import app

@app.route('/')

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review website'
    return render_template('index.html', title = title)