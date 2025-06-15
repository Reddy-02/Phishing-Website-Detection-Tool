import pandas as pd
import tldextract
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# STEP 1: Define feature extractor
# ------------------------------
def extract_advanced_features(url):
    parsed = urlparse(url)
    ext = tldextract.extract(url)
    hostname = parsed.hostname or ""

    return {
        'url_length': len(url),
        'hostname_length': len(hostname),
        'has_ip': 1 if re.match(r'\d{1,3}(\.\d{1,3}){3}', hostname) else 0,
        'has_at': 1 if '@' in url else 0,
        'has_dash': 1 if '-' in hostname else 0,
        'subdomain_count': hostname.count('.') - 1,
        'is_https': 1 if parsed.scheme == 'https' else 0,
        'num_dots': url.count('.'),
        'has_double_slash': 1 if '//' in url[7:] else 0,
        'domain_length': len(ext.domain),
        'path_length': len(parsed.path),
        'query_length': len(parsed.query),
        'has_suspicious_word': int(any(word in url.lower() for word in ['login', 'secure', 'bank', 'verify', 'account', 'update']))
    }

# ------------------------------
# STEP 2: Load dataset
# ------------------------------
df = pd.read_csv("advanced_phishing_dataset.csv")

# ------------------------------
# STEP 3: Extract features
# ------------------------------
features_df = df['url'].apply(extract_advanced_features).apply(pd.Series)
features_df['label'] = df['label'].map({'phishing': 1, 'legitimate': 0})

# ------------------------------
# STEP 4: Split data
# ------------------------------
X = features_df.drop('label', axis=1)
y = features_df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# STEP 5: Train the model
# ------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ------------------------------
# STEP 6: Evaluate
# ------------------------------
y_pred = model.predict(X_test)
print("✅ Model Trained Successfully")
print(classification_report(y_test, y_pred))

# ------------------------------
# STEP 7: Save the model
# ------------------------------
dump(model, "phishing_model_advanced.joblib")
print("✅ Model saved as 'phishing_model_advanced.joblib'")

# ------------------------------
# STEP 8: Confusion Matrix
# ------------------------------
cm = confusion_matrix(y_test, y_pred)
labels = ["Legitimate", "Phishing"]

sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix - Phishing Website Detection")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.show()
