import flask

#Define the server object and stop it from caching for dev purposes
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Set up a redirect destination for our root
@app.route('/')
@app.route('/index.html')
def root():
    return flask.redirect("index.html", code=302)

def trainML():
    # import data from DB
    return
    # Train NN Model - X is the set of predictors for each job applicant, and y is the job they eventually selected
    # Predictor set will include - all of the details about a job applicant, as well as all of the details about a given job.
    # Put all of these into a NN, and see where it goes.

    # Save the model in a .pckl file


def runML():
    return
    # import model from .pckl file
    # import data from db about applicant
    # SQL query DB for jobs that meet non-negotiable criteria
    # Run the model on each job, making sure to add in the job predictors when we run the model - make a sorted list
    # Present models with the highest matches

#Run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


# ML:
    # 1. Establish non-negotiables - these are so we can filter out initially what we want to search, thereby reducing overall computation needed
    # 2. Run the algo on each of the jobs and gather a list of best fits