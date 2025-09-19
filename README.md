# 🎉 Hacktoberfest Registration App  

A simple **Streamlit web app** for managing Hacktoberfest registrations.  
This app allows users to register with their details and stores the data directly in **Google Sheets**.  

---
## 🔔IMPORTANT NOTE 
- The project is live! You can check it out directly by visiting this link in any browser: https://gdgoc-gu-task2.streamlit.app/
---

## 🚀 Features
- ✅ Streamlit-based registration form  
- ✅ Data stored securely in Google Sheets  
- ✅ Works with Google Service Account credentials  
- ✅ Deployment-ready (Streamlit Cloud or local)  
- ✅ Hacktoberfest-themed logo integration  

---

## 🛠️ Requirements
- Python 3.9+  
- Google Cloud Service Account (JSON credentials)  
- A Google Sheet named **"Hacktoberfest Registrations"** (shared with the service account email)  

---

## 📂 Project Structure
```
hacktoberfest-registration/
│── Task2.py                 # Main Streamlit app
│── requirements.txt          # Dependencies
│── logo.png                  # Hacktoberfest logo (used in app + README)
│── README.md                 # Documentation
│
└── .streamlit/
    └── secrets.toml          # Google Service Account credentials (DO NOT COMMIT)
```

---

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/<your-username>/hacktoberfest-registration.git
cd hacktoberfest-registration
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Google Credentials
1. Go to **Google Cloud Console** → create a **Service Account**.  
2. Download the JSON key file.  
3. Share your Google Sheet with the **service account email** (e.g., `xxxx@project.iam.gserviceaccount.com`).  

---

## ⚙️ Local Setup with Streamlit Secrets
Create a `.streamlit/secrets.toml` file in your project root:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "xxxx"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@project.iam.gserviceaccount.com"
client_id = "xxxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "..."
```

---

## ▶️ Run the App Locally
```bash
streamlit run Task2.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.  

---

## 🌍 Deploy to Streamlit Cloud
1. Push your project to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Connect your GitHub repo.  
4. Add the same `[gcp_service_account]` block to **Secrets Manager**.  
5. Deploy 🚀  

---

## 🙌 Acknowledgements
- [Streamlit](https://streamlit.io/)  
- [gspread](https://github.com/burnash/gspread)  
- [Google Cloud Service Accounts](https://cloud.google.com/iam/docs/service-accounts)  
