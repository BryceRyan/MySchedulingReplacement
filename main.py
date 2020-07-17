import flask

#Define the server object and stop it from caching for dev purposes
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Set up a redirect destination for our root
@app.route('/')
@app.route('/index.html')
def root():
    return flask.redirect("index.html", code=302)

#Run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


# Thoughts:
    # We could probably do the ML in line here once we establish and connect to the DB