import pandas as pd
import tldextract
import tkinter as tk
from tkinter import messagebox
from joblib import load
from urllib.parse import urlparse
import re

# ---------- Feature Extraction ----------
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

# ---------- Load Trained Model ----------
model = load("phishing_model_advanced.joblib")

# ---------- GUI Prediction ----------
def check_url():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    try:
        x = pd.DataFrame([extract_advanced_features(url)])
        prediction = model.predict(x)[0]
        result = "⚠️ Phishing Site!" if prediction == 1 else "✅ Legitimate Site"
        result_label.config(text=result, fg="red" if prediction == 1 else "green")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Advanced Phishing URL Detector")
root.geometry("460x240")
root.config(bg="#e6f2ff")

tk.Label(root, text="Enter URL to Check:", font=("Arial", 12), bg="#e6f2ff").pack(pady=12)
entry = tk.Entry(root, width=55)
entry.pack(pady=5)

tk.Button(root, text="Check URL", command=check_url, bg="#0066cc", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#e6f2ff")
result_label.pack(pady=10)

root.mainloop()