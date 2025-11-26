
# Phishing Website Detection using Machine Learning

A Machine Learning-based system that detects phishing websites using URL-level lexical, structural, and domain-based features. The project trains multiple ML models and deploys the best one using a Flask-based web application for real-time URL classification.


## Project Overview

Phishing attacks are widely used to trick users into revealing personal information such as passwords or financial details. Attackers usually create fake pages that look similar to trusted websites.  
This project identifies phishing links using URL-based features without loading full web content, making it fast and lightweight.

The project includes:
- Dataset preprocessing  
- URL feature extraction  
- Model training and comparison  
- Deployment using Flask  
- Logging of predictions

## 🎯Features of the Project

- Detects phishing URLs using URL-based characteristics  
- Extracts lexical, structural, and domain features  
- Models used: Logistic Regression, Random Forest, XGBoost  
- XGBoost selected as the final model  
- Real-time detection using a Flask web app  
- Simple and user-friendly interface  
- Logs stored for future reference

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
- Phishing URLs collected from PhishTank and Kaggle  
- Legitimate URLs collected from Alexa Top Sites  
- Dataset balanced and cleaned  

### 2. Preprocessing
- Removed duplicate URLs  
- Handled corrupted and blank entries  
- Standardized labels  
- Normalized URL text  

### 3. Feature Engineering
- Lexical features: length, digits, symbols, number of dots  
- Structural features: URL depth, redirections, parameters  
- Domain features: IP usage, domain age, DNS records  
- Security indicators: HTTPS or HTTP  

### 4. Model Training
Models tested:
- Logistic Regression  
- Random Forest  
- XGBoost  

Metrics used:
- Accuracy  
- Precision  
- Recall  
- F1-score  

### 5. Deployment
- Flask was used to build the interface  
- Model integrated for real-time prediction  
- Logging mechanism implemented  

## 💡Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- XGBoost
- NumPy & Pandas
- BeautifulSoup / urllib
- HTML / CSS / javascript

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

- Phishing URLs
- Legitimate URLs
- Cleaned & balanced
- 30+ URL-based features extracted
- Stored in `.csv` format

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

- PhishTank – Phishing URL Dataset
- Kaggle – Phishing Websites Dataset
- Alexa – Legitimate Top Sites
- scikit-learn Documentation
- XGBoost Documentation
- Flask Documentation

---

## 👨‍💻 Developer

Ashish Kumar
Cybersecurity Student & ML Enthusiast
GitHub: https://github.com/Ashishkumar-208


