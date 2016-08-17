from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kenju'} #fake user
    return'''
    <html>
        <head>
            <title> Run With ''' + user['nickname'] + ''' </title>
        </head>
        <body>
            <h1>Hello, ''' + user['nickname']  + '''</h1>
        </body>
    </html>
'''
