# Phishing-Website-Detection-Tool
ML-based desktop tool to detect phishing websites via URL analysis

A smart desktop application that detects phishing websites based on URL structure using a trained machine learning model. Developed as part of a Cybersecurity & Ethical Hacking Internship, this project demonstrates real-world ML integration in cybersecurity for identifying malicious web links.

---

## 📘 Overview

Phishing websites mimic trusted platforms to deceive users into disclosing sensitive information. This tool leverages machine learning (Random Forest Classifier) to analyze URL patterns and classify them as either *phishing* or *legitimate*. It features a Python-Tkinter GUI, operates offline, and is packaged into a `.exe` for standalone execution.

---

## 🚀 Features

- ✔️ Feature-rich URL analysis (length, symbols, structure, keywords)
- ✔️ Trained ML model (Random Forest Classifier)
- ✔️ Desktop GUI built with Tkinter
- ✔️ Instant prediction results
- ✔️ Packaged `.exe` for offline use

---

## 🧠 Machine Learning Approach

**Model Used:** Random Forest Classifier  
**Dataset:** `advanced_phishing_dataset.csv`  
**Learning Type:** Supervised  

### 🔍 Features Extracted:
- URL length
- Hostname and domain length
- Number of dots/subdomains
- IP address presence
- `@`, `-`, `//` usage
- Keywords like `login`, `verify`, `secure`
- Use of HTTPS

### 📊 Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🖥️ How the App Works

1. User launches the application (Python script or `.exe` file).
2. A URL is entered into the GUI input field.
3. The app extracts meaningful features from the URL.
4. The model predicts whether it is **phishing** or **legitimate**.
5. Output is displayed in real time via the GUI.

---

## 🛠️ Technologies Used

| Purpose                 | Tools / Libraries Used            |
|--------------------------|----------------------------------|
| Programming              | Python 3.12                      |
| Machine Learning         | Scikit-learn                     |
| Data Processing          | Pandas                           |
| Feature Parsing          | urllib, TLDExtract               |
| GUI Development          | Tkinter                          |
| Application Packaging    | PyInstaller                      |

---

## 📁 Folder Structure

Phishing_Website_Detection/ ├── phishing_gui_advanced.py            # GUI + ML Integration ├── phishing_model_advanced.joblib      # Trained ML model ├── advanced_phishing_dataset.csv       # Dataset used for training ├── phishing_gui_advanced.exe           # Executable for Windows ├── Project_Report_PWDT_SaiSrinivas.pdf # PDF documentation └── README.md                           # GitHub documentation

---

## 📄 Project Documentation

📘 Full report with methodology, evaluation, and architecture:  
👉 [Download Project Report (PDF)]
(https://drive.google.com/file/d/1c0HGQuI1lV5iNLBYkHhoB13a6GNK-Psl/view?usp=sharing)

---

## 👨‍💻 Author

**D. Sai Srinivas Reddy**  
B.Tech – Computer Science and Engineering  
Vignan’s LARA Institute of Technology and Science

---

## 📬 Contact
•Email:saisrinivasreddy456@gmail.com

- LinkedIn: www.linkedin.com/in/sai-srinivas-reddy 
- GitHub: https://github.com/Reddy-02
---

## 📌 Notes

- Ensure `phishing_model_advanced.joblib` is in the same folder as `.exe`.
- To retrain the model, use the `train_phishing_model.py` script with your dataset.
- For demo/testing, use synthetic phishing and legitimate URLs.

---
## 🖥️ Download Executable (.exe)

To run the phishing detection tool offline:

👉 [Download phishing_gui_advanced.exe](https://drive.google.com/file/d/1PTA629tPbyhy9-faddI6OEp4pkAKj3hE/view?usp=sharing)

📌 Note: Place the file `phishing_model_advanced.joblib` in the same folder as the `.exe`.

> 🔒 This project was created as part of a cybersecurity internship to demonstrate applied machine learning in phishing URL detection.
