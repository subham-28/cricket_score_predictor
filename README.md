# 🏏 Cricket Score Prediction ⚡

This project predicts the final score of a T20 cricket match based on current match conditions like teams, venue, score, overs, and wickets.  
It uses a **Stacking Regressor** (XGBoost + Gradient Boosting as base models, Extra Trees as meta model) wrapped inside a scikit-learn pipeline, and provides an intuitive **Streamlit** web app interface.

---
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  </p>

---

## 📖 Table of Contents

- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [📊 Model Overview](#-model-overview)
- [✅ Performance Metrics](#-performance-metrics)
- [🛠️ Installation](#️-installation)
- [💻 Tech Stack](#-tech-stack)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🚀 Features

- 🏏 Predict final T20 score based on:
  - Batting team, bowling team, venue
  - Current score, overs, wickets, recent runs
- 🧠 **Stacking Regressor** for better accuracy:
  - Base models: XGBoost, Gradient Boosting
  - Meta model: Extra Trees
- 🌙 Simple, elegant Streamlit UI
- 📊 MLflow tracking via DagsHub
- ⚠️ Validates overs & team selections
- 📦 Ready for deployment (Streamlit / cloud)
- 📊 MAE under ~1-2 runs on validation and 0.98 of r2_score

---

## 📁 Project Structure
```md
cricket_score_prediction/
├── Data/                # Raw, interim, and processed data
├── Models/
│   └── Pipe.pkl         # Trained stacking pipeline (tracked via Git LFS)
├── Notebooks/
│   └── EDA & model experiments
├── Streamlit/
│   └── app.py          # Streamlit web app
├── requirements.txt
└── README.md

```
---

## 📊 Model Overview

- Model: Stacking Regressor with:
  -Base models: XGBoost, GradientBoosting
  -Meta model: ExtraTrees
-Wrapped in scikit-learn Pipeline with:
-ColumnTransformer for categorical encoding
-Input features:
  -Batting team, bowling team, venue
  -Current score, balls left, wickets left, current run rate, last five overs runs
-Trained on historical T20 data

### ✅ Performance Metrics

| Metric       | Value     |
|--------------|-----------|
| Train MAE    | ~0.2 runs |
| Test MAE     | ~1.74 runs |
| Train R² Score  | ~0.99 runs |
| Test R² Score     | ~0.98 runs |

---

## 🛠️ Installation

```bash
# 1️⃣ Clone the repo
git clone https://github.com/subham-28/cricket_score_prediction.git
cd cricket_score_prediction

# 2️⃣ Set up environment
pip install -r requirements.txt

# 3️⃣ Pull model tracked with Git LFS
git lfs install
git lfs pull

# 4️⃣ Run the Streamlit app
streamlit run Streamlit/app.py

```

---

## 💻 Technologies Stack

| Layer            | Technology                               |
|------------------|------------------------------------------|
| **Backend**  | [FastAPI](https://fastapi.tiangolo.com/) – High-performance API framework |
| **Modeling** | Scikit-learn, LightGBM, RandomForest, StackingRegressor           |
| **Preprocessing** | PowerTransformer, ColumnTransformer, Pipelines, OneHotEncoder, OrdinalEncoder |
| **Experiment Tracking** | [MLflow](https://mlflow.org/) with [DagsHub](https://dagshub.com/) integration |
| **Data Visualization** | Matplotlib, Seaborn, Plotly, Missingno (for missing value visualizations)      |
| **Data Storage** | Pandas, CSV (for static data)|
| **Deployment** | Uvicorn (Local Dev)     |
| **Version Control** | Git, GitHub, Git LFS (for large model files)               |

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request!

---

## 📜 License
MIT License. Feel free to use, modify, and share!

---

## 🙌 Acknowledgements
*Streamlit for rapid prototyping
*scikit-learn & XGBoost for modeling
*Cricket fans everywhere 🏏✨

---

Made with ❤️ by Subham Mohanty
