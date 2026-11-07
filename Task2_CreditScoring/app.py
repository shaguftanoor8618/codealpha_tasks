from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("credit_model.pkl")
features = joblib.load("features.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    probability = None

    if request.method == "POST":
        f = request.form
        duration = int(f["duration_months"])
        amount = float(f["credit_amount"])
        age = int(f["age"])

        data = {
            "checking_account": f["checking_account"],
            "duration_months": duration,
            "credit_history": f["credit_history"],
            "purpose": f["purpose"],
            "credit_amount": amount,
            "savings_account": f["savings_account"],
            "employment_since": f["employment_since"],
            "installment_rate": int(f["installment_rate"]),
            "other_debtors": f["other_debtors"],
            "residence_since": int(f["residence_since"]),
            "property": f["property"],
            "age": age,
            "other_installments": f["other_installments"],
            "housing": f["housing"],
            "existing_credits": int(f["existing_credits"]),
            "job": f["job"],
            "dependents": int(f["dependents"]),
            "telephone": f["telephone"],
            "foreign_worker": f["foreign_worker"],
            # features created in the notebook
            "monthly_payment": amount / duration,
            "long_loan": int(duration > 24),
            "young_borrower": int(age < 25),
        }

        input_df = pd.DataFrame([data])[features]
        result = int(model.predict(input_df)[0])
        probability = round(model.predict_proba(input_df)[0][1] * 100)

    return render_template("index.html", result=result, probability=probability)


if __name__ == "__main__":
    app.run(debug=True)