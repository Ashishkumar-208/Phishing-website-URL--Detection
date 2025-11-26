
# Phishing Website Detection using Machine Learning

A Machine Learning-based system that detects phishing websites using URL-level lexical, structural, and domain-based features. The project trains multiple ML models and deploys the best one using a Flask-based web application for real-time URL classification.


## Project Overview

Phishing is a major cybersecurity threat where attackers create fake websites to steal sensitive user information such as login credentials, credit card details, and banking passwords.
This project uses **Machine Learning (XGBoost)** to classify URLs as **Phishing** or **Legitimate** based only on URL features—making it fast, lightweight, and real-time.

This project includes:

* Dataset preprocessing
* Feature engineering
* Multiple ML model training
* Evaluation & selection
* Flask deployment
* Logging & result interpretation

## 🎯Features of the Project

* ✔ URL-based phishing detection
* ✔ Lexical, structural, and domain-based feature extraction
* ✔ Models trained: Logistic Regression, Random Forest, XGBoost
* ✔ Highest accuracy model (XGBoost) deployed
* ✔ Real-time URL prediction through Flask
* ✔ Logs stored for monitoring
* ✔ Simple and clean UI for user

## Project Architecture

User → Flask Web App → Feature Extraction → XGBoost Model → Prediction → Result Page


## 📂 Project Structure

├── app.py                 # Flask application
├── model.pkl              # Trained XGBoost model (joblib/pickle)
├── feature_extractor.py   # Feature engineering module
├── utils.py               # URL parsing and helper functions
├── static/                # CSS & assets
├── templates/             # HTML templates (index.html, result.html)
├── dataset/               # Raw & processed datasets
├── logs/                  # URL analysis logs
└── README.md              # Project documentation

## 🔍How It Works

1. User enters a URL
2. URL is validated and cleaned
3. Feature extractor generates feature vector
4. Trained model (XGBoost) predicts phishing or legitimate
5. Result is displayed on web interface
6. URL + prediction is saved in logs

## 📊Detailed Methodology

### 1. Data Collection

* Phishing URLs → PhishTank, Kaggle
* Legitimate URLs → Alexa Top Sites
* Dataset balanced and cleaned

### 2. Preprocessing

* Removes duplicates
* Standardizes labels
* Normalizes URL strings
* Handles empty/corrupted URLs

### 3. Feature Engineering

* Lexical features (length, digits, dots, symbols…)
* Domain features (IP usage, domain age, DNS availability)
* Structural features (depth, redirections, queries)
* HTTPS & certificate features

### 4. Model Training

* Logistic Regression
* Random Forest
* XGBoost (best performance)
* Evaluation metrics → Accuracy, Precision, Recall, F1-score

### 5. Deployment

* Flask web app
* URL input form
* Real-time prediction output
* Logs generated for analysis

## 💡Technologies Used

* Python 3.x
* Flask
* Scikit-learn
* XGBoost
* NumPy & Pandas
* BeautifulSoup / urllib
* HTML / CSS / javascript

## 🔍 How It Works

1. User enters a URL  
2. URL is cleaned & validated  
3. Features are extracted:
   - Lexical  
   - Structural  
   - Domain-based  
4. XGBoost model predicts the URL type  
5. User sees result on web UI  
6. The system logs all predictions  

---

## 📊 Detailed Methodology

### 1. Data Collection
- PhishTank → Verified phishing URLs  
- Kaggle → Phishing datasets  
- Alexa Top Sites → Legitimate URLs  

### 2. Preprocessing
- Removed duplicates  
- Cleaned malformed URLs  
- Standardized labels  
- Normalized URL strings  

### 3. Feature Engineering
Extracts multiple features:
- URL length  
- Number of dots & digits  
- Number of special characters  
- Prefix/suffix (`-`) usage  
- IP address usage  
- HTTPS presence  
- Domain age  
- URL depth  
- Redirection patterns  

### 4. Model Training
Models tested:
- Logistic Regression  
- Random Forest  
- XGBoost (BEST)

Evaluation metrics:
- Accuracy  
- Precision  
- Recall  
- F1-score  

### 5. Deployment
- Flask interface  
- Real-time predictions  
- Logs generated for monitoring  

---

## 🛠️ Installation & Setup

### 1. Clone repository

git clone https://github.com/yourusername/phishing-website-url-detection.git
cd phishing-website-url-detection

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the Flask app

python app.py

### 4. Open the browser

http://127.0.0.1:5000/

---
### 🧪Dataset

Dataset includes:

* Phishing URLs
* Legitimate URLs
* Cleaned & balanced
* 30+ URL-based features extracted
* Stored in `.csv` format

---
## 📈 Results

* XGBoost achieved highest accuracy
* Fast real-time prediction
* Low false positives
* Effective against unknown phishing URLs

---

## 📝Conclusion

This project shows how Machine Learning can be used to detect phishing websites quickly and accurately using URL-based features. The system is lightweight, scalable, and practical for real-world use. It can be integrated into browsers, SOC tools, and email filters for enhanced security.

---

## 📚References

* PhishTank – Phishing URL Dataset
* Kaggle – Phishing Websites Dataset
* Alexa – Legitimate Top Sites
* scikit-learn Documentation
* XGBoost Documentation
* Flask Documentation

---

## 👨‍💻 Developer

Ashish Kumar
Cybersecurity Student & ML Enthusiast
GitHub: https://github.com/Ashishkumar-208


