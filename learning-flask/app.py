import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html', name = "world")

@app.route('/profile/<string:username>')
def profile(username):
    return f"{username}'s page is working as expected"

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        return f"Hello, {name}!"

    return '''
        <form method = "POST">
            Name: <input type = "text" name = "name">
            <input type = "submit">
        </form>  
    '''

if __name__ == '__main__':
    app.run(debug=True)