from flask import Flask , render_template , request
import pandas as pd
import joblib
import numpy as np 

app = Flask(__name__)

model = joblib.load(filename="C:/vs code/vs programs/virtual fitting room/model/bodytypemodel.joblib" )


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about" )
def about():
    return render_template("about.html")


@app.route("/predict" , methods=["POST"])
def predict():
    types= ['Bottom Hourglass' ,'Hourglass' ,'Inverted triangle' ,'Rectangle' ,'Spoon','Top Hourglass' ,'Triangle']
    bust = float(request.form['bust'])
    waist = float(request.form['waist'])
    high_hips = float(request.form['highhips'])
    hips = float(request.form['hips'])
    arr = np.array([[bust ,waist , high_hips , hips]])
    y_pred = model.predict(arr)
    return render_template('home.html' ,btype = types[int(y_pred)])


if __name__ == "__main__":
    app.run(debug=True)