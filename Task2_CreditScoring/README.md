# Task 2: Credit Scoring Model (CodeAlpha ML Internship)

Predicts whether a person is creditworthy (good or bad credit) from their financial history, with a simple website to try it.

## Dataset
German Credit Data, UCI Machine Learning Repository (1,000 applicants, 20 features).

## Feature Engineering
- `monthly_payment` = loan amount / duration
- `long_loan` = 1 if the loan is longer than 24 months
- `young_borrower` = 1 if age is under 25
- Dropped `personal_status` because it contains gender information, which should not be used in credit decisions
- Text columns converted to numbers with one-hot encoding

## Models Compared (test split)
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.665 | 0.829 | 0.657 | 0.733 | 0.741 |
| Decision Tree | 0.620 | 0.840 | 0.564 | 0.675 | 0.685 |
| Random Forest | 0.735 | 0.764 | 0.900 | 0.826 | 0.776 |

5-fold cross-validation ROC-AUC: Logistic Regression 0.783, Decision Tree 0.732, **Random Forest 0.793**.

Final model: **Random Forest** (class weights balanced), ROC-AUC about 0.78.

## Limitations
- The model finds good-credit applicants well (recall 0.90) but catches only about 35% of bad-credit applicants.
- The dataset is small (1,000 rows), so results are approximate.
- The website asks for 8 key details; the other details use typical default values.
- This is a student project, not real financial advice.

## Project Files
- `CreditScoring.ipynb`: data cleaning, feature engineering, training and evaluation
- `app.py`: Flask website backend
- `templates/index.html`: website page
- `credit_model.pkl`, `features.pkl`: saved model and feature list
- `requirements.txt`: required libraries

## How to Run the Website on Your Laptop
1. Install Python 3.9 or higher.
2. Download this repository (Code, then Download ZIP) and extract it, or clone it:
   ```
   git clone https://github.com/shaguftanoor8618/codealpha_tasks.git
   cd codealpha_tasks/Task2_CreditScoring
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
   python -m pip install -r requirements.txt
   ```
5. Start the website:
   ```
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.
