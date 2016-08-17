from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kenju'} #fake user
    posts = [
        {
            'author':{'nickname': 'Dennis'},
            'body': 'This is one good day in San Francisco'
        },
        {
            'author': {'nickname': 'Biggie'},
            'body': 'I enjoyed watching Will Smith on Suicide Squad'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
