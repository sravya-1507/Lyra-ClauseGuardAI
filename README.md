# ClauseGuard AI 📄⚖️

ClauseGuard AI is an intelligent contract analysis dashboard that helps users understand legal agreements by detecting risky clauses and explaining them in simple language.

The system analyzes uploaded contracts or pasted agreement text and highlights potential legal risks using a rule-based risk engine combined with AI-powered clause explanations.

---

## 🚀 Features

*  Upload PDF contracts or paste agreement text
*  Automatic clause risk detection (High / Medium / Low)
*  AI-powered clause explanations in simple language
*  Contract red flag identification
*  Overall contract risk scoring dashboard
*  Clean and interactive Streamlit interface
*  Privacy-first local document processing

---

## 🧠 How It Works

1. User uploads a contract or pastes agreement text
2. Text extraction and cleaning is performed
3. Contract is split into legal clauses
4. Risk Engine evaluates clauses using legal rule patterns
5. AI explains clause impact and risks
6. Dashboard displays risk score and warnings

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Plotly
* PDF Processing (PyPDF)
* Regex-based Risk Engine
* AI Clause Explanation Module

---

## 📂 Project Structure

```
Clause_guard/
│
├── app.py                 # Streamlit dashboard
├── risk_engine.py         # Risk detection logic
├── ai_engine.py           # AI clause explanation
├── clause_splitter.py     # Clause segmentation
├── pdf_reader.py          # PDF text extraction
├── text_cleaner.py        # Text preprocessing
├── requirements.txt
└── .streamlit/config.toml
```

---

## ▶️ Running Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 🎯 Use Cases

* Employment Agreements
* Internship Contracts
* SaaS Terms & Conditions
* Subscription Policies
* Business Agreements

---

## Future Improvements

* Semantic legal search
* Multi-document comparison
* Advanced AI risk prediction
* Contract summarization

---

## 👩‍💻 Author

Sravya C V S S
Electronics & Telecommunication Engineering Student
Interested in Software Development and Intelligent Systems.

---

⭐ If you found this project useful, consider giving it a star!
