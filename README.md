💍 Cloud-Based Marriage Age Prediction System

A real-time, cloud-integrated prediction service that estimates the likely age of marriage based on user demographic data using machine learning.

---

 🧠 Overview

This application uses a trained ML model deployed via Flask and hosted on AWS EC2. It predicts marriage age using factors like gender, profession, and religion. It provides instant predictions without storing user data.

---

 ⚙️ Tech Stack

| Component         | Tech Used                       |
|------------------|---------------------------------|
| Frontend         | HTML, CSS                       |
| Backend          | Python Flask                    |
| ML Libraries     | Scikit-learn, Pandas             |
| Cloud Services   | AWS EC2, S3, SageMaker           |
| File Transfer    | WinSCP, PuTTY                   |

---

 🧩 Features

- Instant marriage age prediction based on demographic input
- Hosted in cloud for scalable access
- No database – user input is processed in real-time only
- Deployed using AWS EC2 + SageMaker + S3

---

 🧪 ML Models Evaluated

| Algorithm             | R² Score   | MAE        |
|-----------------------|------------|------------|
| Gradient Boosting ✅  | 70.77      | 1.02       |
| Random Forest         | 70.02      | 1.03       |
| KNN                   | 28.15      | 1.47       |
| Linear Regression     | 12.83      | 1.66       |
| SVR                   |  7.99      | 1.70       |

Final model: **Gradient Boosting Regressor**

---

 🚀 How to Run

```bash
cd app
pip install -r ../requirements.txt
python app.py
