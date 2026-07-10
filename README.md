# 🚗 Used Car Price Prediction

> An end-to-end Machine Learning web application that predicts the selling price of a used car based on its specifications using an **Extra Trees Regressor** model. The application features a responsive web interface, automatic vehicle specification filling, real-time prediction, and downloadable valuation reports in PDF format.

---

## 📸 Project Preview

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 🚘 Vehicle Details Form

![Autofill](screenshots/form.png)

---

### 💰 Prediction Report

![Prediction](screenshots/prediction.png)

---

### 📄 Downloadable PDF Report

![PDF](screenshots/pdf_report.png)

---

### 📊 Feature Importance

![Feature](screenshots/feature_importance.png)

---

### 📈 Actual vs Predicted Prices

![Actual_vs_Prediction](screenshots/actual_vs_predicted.png)

---

## 📌 Overview

The selling price of a used car depends on multiple factors including:

- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Fuel Type
- Transmission
- Engine Capacity
- Maximum Power
- Mileage
- Number of Seats
- Seller Type

This application predicts the estimated selling price using Machine Learning, helping buyers and sellers make informed pricing decisions.

---

# ✨ Features

### 🤖 Machine Learning

- Complete Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Model Comparison
- Hyperparameter Tuning
- Ensemble Learning
- Feature Importance Analysis

### 🌐 Web Application

- Responsive Bootstrap UI
- Dynamic Brand → Model Selection
- Automatic Vehicle Specification Filling
- Editable Auto-filled Fields
- Loading Animation
- Prediction without Page Reload (AJAX)
- Bootstrap Prediction Modal
- Indian Currency Formatting
- Download Valuation Report as PDF

---

# 📂 Dataset

The dataset contains information about **15,411** used cars.

### Features

| Feature      | Description                            |
| ------------ | -------------------------------------- |
| Brand        | Car Manufacturer                       |
| Model        | Vehicle Model                          |
| Vehicle Age  | Age of the Vehicle                     |
| KM Driven    | Total Distance Driven                  |
| Seller Type  | Dealer / Trustmark Dealer / Individual |
| Fuel Type    | Petrol / Diesel / CNG / LPG / Electric |
| Transmission | Manual / Automatic                     |
| Mileage      | Mileage (km/l)                         |
| Engine       | Engine Capacity (cc)                   |
| Max Power    | Maximum Power (bhp)                    |
| Seats        | Number of Seats                        |

**Target Variable**

- Selling Price

---

# 🧹 Data Preprocessing

### Numerical Features

- Median Imputation
- Standard Scaling

### Categorical Features

- Most Frequent Imputation
- One-Hot Encoding

### Pipeline Components

- ColumnTransformer
- Pipeline

---

# 📊 Exploratory Data Analysis

Performed:

- Missing Value Analysis
- Duplicate Detection
- Target Variable Analysis
- Univariate Analysis
- Bivariate Analysis
- Distribution Analysis
- Correlation Heatmap
- Outlier Detection
- Feature Importance Analysis

---

# 🤖 Machine Learning Models Compared

| Model                    |         MAE |         RMSE | R² Score |
| ------------------------ | ----------: | -----------: | -------: |
| Linear Regression        |    ₹177,655 |     ₹387,848 |     0.80 |
| Decision Tree            |    ₹121,933 |     ₹284,756 |     0.89 |
| Gradient Boosting        |    ₹126,845 |     ₹243,537 |     0.92 |
| Random Forest            |     ₹99,007 |     ₹214,278 |     0.94 |
| ⭐ Extra Trees Regressor | **₹96,823** | **₹212,231** | **0.94** |

---

# 🏆 Final Model

**Extra Trees Regressor**

### Performance

| Metric   |    Value |
| -------- | -------: |
| MAE      |  ₹96,823 |
| RMSE     | ₹212,231 |
| R² Score | **0.94** |

---

# 🧠 Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Train-Test Split
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Model Training
      │
      ▼
Model Comparison
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Final Extra Trees Model
      │
      ▼
Flask Deployment
```

---

# 🛠️ Technologies Used

## Programming

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Backend

- Flask

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Model Persistence

- Joblib

## PDF Generation

- ReportLab

---

# 📁 Project Structure

```text
Used-Car-Price-Prediction/
│
├── data/
│
├── models/
│   └── used_car_price_model.pkl
│
├── notebooks/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── json/
│   └── images/
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── home.png
│   ├── form.png
│   ├── prediction.png
│   ├── pdf_report.png
│   ├── feature_importance.png
│   └── actual_vs_predicted.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Used-Car-Price-Prediction.git
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 🔮 Future Improvements

- XGBoost
- LightGBM
- CatBoost
- Explainable AI (SHAP)
- User Authentication
- Database Integration
- Cloud Deployment
- Price Trend Dashboard
- Vehicle Image Upload
- VIN Decoder Integration

---

# 👨‍💻 Author

**Atharva Pawar**

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
