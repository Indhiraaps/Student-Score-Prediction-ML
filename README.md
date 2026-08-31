## Project Structure

# Student Score Prediction using Machine Learning 🎓📊

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Scikit-Learn](<https://img.shields.io/badge/Scikit--Learn-Linear%20Regression-orange.svg>)
![Pandas](<https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg>)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

* `student_scores.csv` - Raw dataset file containing study hours and score records.
* `student_score_prediction.ipynb` - Core Jupyter Notebook containing data processing, exploratory analysis, and modeling.

## 📌 Project Overview

This project is an end-to-end Machine Learning application built during the 14-Day AI & ML Internship with **Codomax Digital Solutions**.

The goal of this system is to predict a student's final exam score percentage based on the number of hours spent studying per day using Supervised Machine Learning (Linear Regression).

---

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
* **Day 12** : Refactored project directory structure into `data/`, `models/`, and `scripts/`, updated relative file paths, added `.gitignore`, and polished notebook formatting.
* **Day 13** : Created comprehensive README documentation, organized screenshots into `assets/`, added tech badges, and published complete GitHub showcase.
* **Day 14**: Recorded 2-3 minute project demo video, completed final audit of repository assets, and submitted final internship deliverables.

## 📂 Project Structure

```text
Student-Score-Prediction-ML/
│
├── assets/                  # Project screenshots and visual evidence
│   ├── notebook_eda.png
│   ├── metrics.png
│   └── cli_app.png
├── data/                    # Dataset directory
│   └── student_scores.csv
├── models/                  # Serialized trained models
│   └── student_score_model.pkl
├── scripts/                 # Executable Python scripts
│   └── predict_app.py
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
└── student_score_prediction.ipynb # EDA, training, and evaluation notebook
```
