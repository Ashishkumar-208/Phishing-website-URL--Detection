
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

<img width="783" height="306" alt="Screenshot 2025-11-27 014139" src="https://github.com/user-attachments/assets/8a9f7ed5-2fe1-4281-a7f8-788647ac2180" />

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

## System Implementation & Output Screenshots

This section shows how the Phishing Website Detection System works in real life.
The following screenshots explain each stage—from running the backend server to checking URLs and getting the final prediction.
These outputs help to understand how the project behaves practically, beyond theory
http://127.0.0.1:5000/

<img width="1733" height="831" alt="Screenshot 2025-11-26 215630" src="https://github.com/user-attachments/assets/82bb98f1-db2c-4b77-8317-b4984929393c" />

In this step, the user enters a website link (e.g., https://google.com) into the input box.
When the user clicks on the Check URL button, the backend processes the URL, extracts features, and sends it to the ML model.

<img width="1801" height="546" alt="Screenshot 2025-11-26 215749 - Copy" src="https://github.com/user-attachments/assets/f09bae94-d4d1-4316-b689-f20c1240228d" />

After checking the URL, the model returns the result.
In this case, the system correctly identifies google.com as a safe and legitimate website.
The output clearly displays the scanned URL and the prediction result.

<img width="1808" height="647" alt="Screenshot 2025-11-26 220031" src="https://github.com/user-attachments/assets/660a71ef-513c-4077-b1c3-737f5400a4fa" />

This screenshot shows the system detecting a suspicious URL like https://paypa1.com,
which is a fake version of PayPal where "l" is replaced with "1".
The system correctly marks it as a phishing website and warns the user.

<img width="1288" height="482" alt="Screenshot 2025-11-27 010054" src="https://github.com/user-attachments/assets/051b7fcb-5ac1-4ffa-a6c9-75dadc7b6eb8" />

The system correctly identifies the URL https://paypa1.com as a Phishing / Fake website and warns the user before visiting the site.

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


