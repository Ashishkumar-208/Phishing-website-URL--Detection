import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import pickle, os

# 1) CSV load karo
df = pd.read_csv("phishing.csv")

# Label column
y = df["class"]

# 2) Features: Index + class hata do, BAAKI 30 columns hi features rahenge
X = df.drop(columns=["class", "Index"])

print("X shape:", X.shape)      # yaha (N, 30) aana chahiye
print("Unique labels:", y.unique())

# 3) Model train karo
gbc = GradientBoostingClassifier()
gbc.fit(X, y)

# 4) Model save karo
os.makedirs("pickle", exist_ok=True)
with open("pickle/model.pkl", "wb") as f:
    pickle.dump(gbc, f)

print("✅ Model trained & saved to pickle/model.pkl")

