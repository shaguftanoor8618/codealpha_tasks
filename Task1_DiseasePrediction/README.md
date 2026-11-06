# CodeAlpha_HeartDiseasePrediction

Machine Learning Internship, Task 4: Disease Prediction from Medical Data (CodeAlpha)

A machine learning model that predicts heart disease from patient medical data, with a simple website to try it.

## Dataset
Heart Disease dataset, UCI Machine Learning Repository (303 patients, 13 features).

## Models Compared
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.869 | 0.812 | 0.929 | 0.867 | 0.951 |
| SVM | 0.852 | 0.806 | 0.893 | 0.847 | 0.944 |
| Random Forest | 0.902 | 0.844 | 0.964 | 0.900 | 0.955 |
| XGBoost | 0.852 | 0.788 | 0.929 | 0.852 | 0.919 |

Final model: **Logistic Regression** (best 5-fold cross-validation accuracy, 0.828).

## Project Files
- `HeartDisease_Prediction.ipynb`: data cleaning, model training and evaluation
- `app.py`: Flask website backend
- `templates/index.html`: website page
- `heart_model.pkl`, `features.pkl`: saved model and feature list
- `requirements.txt`: required libraries

## How to Run the Website on Your Laptop

1. Install Python 3.9 or higher.
2. Download this repository (Code, then Download ZIP) and extract it, or clone it:
   ```
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_HeartDiseasePrediction.git
   cd CodeAlpha_HeartDiseasePrediction
   ```
3. Create and activate a virtual environment.
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
4. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
5. Start the website:
   ```
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser, enter the patient details and click Predict.

To re-train the model, open the notebook:
```
jupyter notebook HeartDisease_Prediction.ipynb
```

## Disclaimer
Educational project. Not for medical use.


