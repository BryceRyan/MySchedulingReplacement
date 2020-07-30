import flask
from tensorflow.keras import Model
from tensorflow.keras import Input
from tensorflow.keras.layers import Dense
import tensorflow.keras as keras
import mysql.connector
from mysql.connector import Error
from sklearn.model_selection import train_test_split
#Define the server object and stop it from caching for dev purposes
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Set up a redirect destination for our root
@app.route('/')
@app.route('/index.html')
def root():
    return flask.redirect("index.html", code=302)

def trainML():

    # Get data from DB
    # The result of this should be as follows: 
        # XData holds the information about the applicants, as well as the information about the job
        # YData holds the job that the individuals actually took
        # Each row corresponds to a customer-job match
    try:
        connection = mysql.connector.connect(host = "", database="", user="", password="")
        sql_query = ""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        Xdata=cursor.fetchall()
        sql_query = ""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        Ydata=cursor.fetchall()
    except Error as e:
        print("Error reading data", e)

    x_train, x_test, y_train, y_test = train_test_split(Xdata, Ydata, test_size=.4)
    features = len(Xdata[1])

    x_in = Input(shape=(features,))
    x = Dense(50, activation="relu")(x_in)
    x_out = Dense(10, activation="sigmoid")(x)

    model = Model(inputs=x_in, outputs=x_out)

    model.compile(
        loss= "binary_crossentropy",
        optimizer = "adam",
        metrics=["accuracy"],
    )

    history = model.fit(x_train, y_train, batch_size=60, epochs=4, validation_split=.4)

    test_scores = model.evaluate(x_test, y_test, verbose=2)

    print("Loss: ", test_scores[0])
    print("Accuracy: ", test_scores[1])
    # We must fix the file path
    model.save("/MySchedulingReplacement")
    return

def runML():
    # We must fix the file path
    model = keras.models.load_model("/MySchedulingReplacement")

    # Load in the data we need from the DB - The actual applicants we want to evaluate
    try:
        connection = mysql.connector.connect(host = "", database="", user="", password="")
        sql_query = ""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        Xdata=cursor.fetchall()
    except Error as e:
        print("Error reading data", e)


    predictions = model.predict(Xdata)


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