import flask
import tensorflow as tf
#Define the server object and stop it from caching for dev purposes
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Set up a redirect destination for our root
@app.route('/')
@app.route('/index.html')
def root():
    return flask.redirect("index.html", code=302)

def trainML():

    #Could *potentially* optimize these tuning params using k-fold cross validation.
    learning_rate= .5
    epochs = 10
    neurons = 50

    #Change this once we can connect to the DB
    features = 0
    sample_size = 0
    output_size = 0

    # import data from DB here
    x = None
    y = None

    # Define NN Model - X is the set of predictors for each job applicant, and y is the job they eventually selected
    weight1 = tf.Variable(tf.random_normal[features, neurons], stddev = 0.03, name="W1")
    bias1 = tf.Variable(tf.random_normal([neurons]), name="b1")
    weight2 = tf.Variable(tf.random_normal([neurons, output_size], stddev=.03), name="W2")
    bias2 = tf.Variable(tf.random_normal([output_size]), name="b2")

    hidden_out = tf.add(tf.matmul(x, weight1), bias1)
    hidden_out = tf.nn.relu(hidden_out)

    # Sigmoid activation function so we can get a probability
    output_layer=tf.math.sigmoid(tf.add(tf.matmul(hidden_out, weight2), bias2))

    output_clipped = tf.clip_by_value(output_layer, 1e-10, 0.9999999)
    cross_entropy= -tf.reduce_mean(tf.reduce_sum(y*tf.log(output_clipped)+(1-y)*tf.log()))


    # Predictor set will include - all of the details about a job applicant, as well as all of the details about a given job.
    # Put all of these into a NN, and see where it goes.
    # Save the model in a .pckl file

    return

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