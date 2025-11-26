import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from feature import FeatureExtraction
import pickle, os

# 1) CSV load karo
df = pd.read_csv("phishing.csv")

# URL column ka naam guess karte hain
if "URL" in df.columns:
    url_col = "URL"
elif "url" in df.columns:
    url_col = "url"
else:
    # maan lete hain pehla column URL hai
    url_col = df.columns[0]

# Label column ka naam guess karo (last column)
label_col = df.columns[-1]

print("Using URL column:", url_col)
print("Using label column:", label_col)

urls = df[url_col].tolist()
labels = df[label_col].tolist()

X = []
y = []

print("Extracting features from URLs... (thoda time lag sakta hai)")

for u, lab in zip(urls, labels):
    try:
        obj = FeatureExtraction(u)
        feats = obj.getFeaturesList()   # yahi 30 features hain
        if len(feats) != 30:
            print("WARNING: feature length != 30 for URL:", u, "len =", len(feats))
            continue
        X.append(feats)
        y.append(lab)
    except Exception as e:
        print("Failed for URL:", u, "Error:", e)

X = np.array(X)
y = np.array(y)

print("Final X shape:", X.shape)   # should be (N, 30)
print("Label values:", set(y))

# 2) Model train karo
gbc = GradientBoostingClassifier()
gbc.fit(X, y)

# 3) Model save karo
os.makedirs("pickle", exist_ok=True)
with open("pickle/model.pkl", "wb") as f:
    pickle.dump(gbc, f)

print("✅ New model trained and saved to pickle/model.pkl")
