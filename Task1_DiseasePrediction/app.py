from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("heart_model.pkl")
features = joblib.load("features.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    probability = None

    if request.method == "POST":
        data = {
            "age": float(request.form["age"]),
            "sex": int(request.form["sex"]),
            "cp": int(request.form["cp"]),
            "trestbps": float(request.form["trestbps"]),
            "chol": float(request.form["chol"]),
            "fbs": int(request.form["fbs"]),
            "restecg": int(request.form["restecg"]),
            "thalach": float(request.form["thalach"]),
            "exang": int(request.form["exang"]),
            "oldpeak": float(request.form["oldpeak"]),
            "slope": int(request.form["slope"]),
            "ca": float(request.form["ca"]),
            "thal": float(request.form["thal"]),
        }
        input_df = pd.DataFrame([data])[features]
        result = int(model.predict(input_df)[0])
        probability = round(model.predict_proba(input_df)[0][1] * 100)

    return render_template("index.html", result=result, probability=probability)


if __name__ == "__main__":
    app.run(debug=True)