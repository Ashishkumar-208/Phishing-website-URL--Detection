from flask import Flask, request, render_template 
import numpy as np
import warnings
import pickle
from feature import FeatureExtraction

warnings.filterwarnings("ignore")

# --------- MODEL LOAD ----------
with open("pickle/model.pkl", "rb") as f:
    gbc = pickle.load(f)

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"].strip()

        obj = FeatureExtraction(url)
        features = obj.getFeaturesList()
        x = np.array(features).reshape(1, -1)

        # ML prediction
        y_pred = gbc.predict(x)[0]   # 1 = safe, -1 = phishing (tumhare model ka assumption)

        # EXTRA RULES
        brand_flag = obj.brand_spoof_flag()      # -1 = brand spoof
        domain_flag = obj.domain_exists_flag()   # -1 = domain resolve nahi ho raha

        # Final decision:
        if brand_flag == -1 or domain_flag == -1:
            final_pred = -1
        else:
            final_pred = y_pred

        if final_pred == 1:
            verdict = "✅ Legitimate (Safe website)"
            is_safe = True
        else:
            verdict = "❌ Phishing / Fake website"
            is_safe = False

        return render_template(
            "index.html",
            url=url,
            verdict=verdict,
            is_safe=is_safe,
        )

    # GET (first load)
    return render_template("index.html", verdict=None, is_safe=None, url=None)

if __name__ == "__main__":
    app.run(debug=True)

