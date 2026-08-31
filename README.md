# Student Score Prediction using Machine Learning

A 14-day internship project with Codomax Digital Solutions focused on predicting a student's final exam score based on their daily study hours using Linear Regression.

## Project Structure

* `student_scores.csv` - Raw dataset file containing study hours and score records.
* `student_score_prediction.ipynb` - Core Jupyter Notebook containing data processing, exploratory analysis, and modeling.

## Progress Log

* **Day 1**: Environment setup complete with Python, VS Code, Jupyter, and Git.
* **Day 2**: Practiced Python fundamentals: variables, lists, loops, and custom functions.
* **Day 3**: Explored NumPy arrays, vectorized math operations, and array statistics.
* **Day 4**: Created `student_scores.csv`, loaded dataset using Pandas, and inspected structure.
* **Day 5**: Conducted data cleaning procedures, checked for missing values/duplicates, and analyzed statistics.
* **Day 6**: Built scatter plots, bar charts, and line charts using Matplotlib to visualize feature correlations.
* **Day 7**: Understood Supervised Learning concepts, isolated feature X and target y, and implemented train-test data splitting.
* **Day 8**: Initialized and trained a Linear Regression model using Scikit-learn and extracted learned slope and intercept parameters.
* **Day 9**: Generated predictions on test dataset using `.predict()` and built actual vs. predicted comparison tables.
* **Day 10**: Evaluated model performance metrics (MAE, MSE, RMSE, R² Score) and plotted best-fitting regression line.
* **Day 11**: Exported trained Linear Regression model to `.pkl` format using `joblib` and created an interactive Python CLI prediction application with input validation.
  10. LinkedIn Post Template.
* **Day 12** : Refactored project directory structure into `data/`, `models/`, and `scripts/`, updated relative file paths, added `.gitignore`, and polished notebook formatting^^.

## Project Structure

```text
Student-Score-Prediction-ML/
│
├── data/
│   └── student_scores.csv
├── models/
│   └── student_score_model.pkl
├── scripts/
│   └── predict_app.py
├── .gitignore
├── README.md
└── student_score_prediction.ipynb
```
