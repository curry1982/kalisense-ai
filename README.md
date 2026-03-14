# KaliSense AI 🩺
### Non-Invasive Serum Potassium Anomaly Detection SaaS Platform
**非侵入式血鉀異常偵測 SaaS 智慧判讀平台**

> 🏆 **2025 SelectUSA Investment Summit — Global 2nd Place**  
> 🏥 Invited for evaluation by world top-10 medical institutions

---

## 📌 Overview | 平台簡介

**KaliSense AI** detects serum potassium (K⁺) anomalies — hyperkalemia and hypokalemia — directly from ECG waveforms using deep learning, **without any blood draw**.

Traditional potassium testing requires venous blood sampling and lab processing (30 min – several hours). KaliSense AI enables:
- ✅ Zero-invasive, real-time potassium risk assessment
- ✅ Continuous monitoring for dialysis patients
- ✅ Remote deployment for rural clinics and home care
- ✅ AIGC-generated structured clinical reports

---

## 🏗️ System Architecture | 系統架構

```
┌─────────────────────────────────────────────────────┐
│                   KaliSense AI Platform              │
├──────────────┬──────────────────┬───────────────────┤
│  ECG Input   │   AI Engine      │  Cloud SaaS       │
│              │                  │                   │
│ • 12-lead    │ • CNN-Transformer│ • AWS / Azure     │
│ • Wearable   │ • K⁺ Predictor  │ • 台智雲           │
│ • .CSV/.EDF  │ • AIGC Report    │ • Private Cloud   │
│ • HL7        │   Generator      │ • REST API        │
└──────────────┴──────────────────┴───────────────────┘
         ↓                ↓                ↓
   Web Dashboard    Mobile App       HIS Integration
   (iOS / Android)               (Hospital Systems)
```

---

## 🧠 AI Model Overview | 模型架構說明

| Component | Description |
|-----------|-------------|
| **Feature Extraction** | T-wave amplitude, PR interval, QRS width, QTc |
| **Model Architecture** | CNN-Transformer hybrid (local + global temporal features) |
| **Output** | K⁺ risk level: Normal / Hypokalemia / Hyperkalemia |
| **Accuracy** | 91%+ classification accuracy |
| **Sensitivity** | 88% for hyperkalemia detection |
| **Input Formats** | 12-lead ECG, .CSV, .EDF, HL7 |

> ⚠️ **Note:** Core model weights and training pipeline are maintained in our private repository in compliance with **TFDA SaMD regulations** and patient data privacy requirements (醫療資安合規). Only architecture documentation and evaluation benchmarks are published here.

---

## 📊 Clinical Validation | 臨床驗證結果

Validated in collaboration with nephrology and hemodialysis centers:

```
Metric                        Value
─────────────────────────────────────
Overall Classification Acc.   92.2%
Hyperkalemia Sensitivity       92.0%
Hyperkalemia Specificity       93.5%
Hypokalemia Sensitivity        92.4%
AUC (Hyperkalemia)             0.947
AUC (Hypokalemia)              0.921
Avg. Assessment Time           < 5 min
```

> IRB ethics approval obtained from partner medical institutions.

---

## 🗂️ Repository Structure | 目錄說明

```
kalisense-ai/
├── README.md                  # This file
├── docs/
│   ├── architecture.md        # System architecture details
│   ├── api_spec.yaml          # OpenAPI 3.0 specification
│   └── clinical_validation.md # Validation methodology
├── examples/
│   ├── sample_ecg_analysis.py # Example API call (anonymized)
│   └── report_output_sample.json # Sample AIGC report output
└── evaluation/
    └── benchmark_metrics.md   # Public benchmark results
```

> 🔒 **Core model training code, patient data, and proprietary algorithms** are stored in our private GitLab instance under TFDA SaMD compliance controls.

---

## 🔌 API Quick Start | API 快速開始

```python
import requests

# Submit ECG for potassium risk analysis
response = requests.post(
    "https://api.kalisense.ai/v1/analyze",
    headers={"Authorization": "Bearer <your_token>"},
    json={
        "ecg_format": "csv",
        "leads": 12,
        "patient_id": "anonymized_id",
        "ecg_data": "<base64_encoded_ecg>"
    }
)

result = response.json()
print(result["potassium_risk"])   # "normal" / "hypokalemia" / "hyperkalemia"
print(result["report_url"])       # AIGC-generated clinical report link
```

Full API documentation: [`docs/api_spec.yaml`](docs/api_spec.yaml)

---

## 🌐 Tech Stack | 技術架構

| Layer | Technology |
|-------|-----------|
| **Frontend** | React.js + Tailwind CSS + Chart.js |
| **Backend** | FastAPI + PostgreSQL + Redis |
| **AI Training** | PyTorch + scikit-learn + XGBoost |
| **Cloud** | AWS / Azure / 台智雲 (multi-cloud) |
| **DevOps** | Docker + GitHub Actions / GitLab CI |
| **Security** | ISO 27001, data encryption, RBAC |

---

## 🏆 Awards & Recognition | 獲獎與認可

- 🥈 **2025 SelectUSA Investment Summit** — Global 2nd Place (representing Taiwan)
- 🏥 Formal evaluation invitation from **world top-10 medical institutions**
- 📋 **TFDA SaMD** medical device software certification in progress
- 🌏 Active expansion into Southeast Asia, Japan, and European dialysis markets

---

## 🤝 Collaboration & Contact | 合作洽詢

We welcome collaborations with:
- Hospitals and dialysis centers
- Medical device manufacturers
- Healthcare IT integrators
- International distributors

📧 **contact@precisebiotech.ai**  
🌐 **www.precisebiotech.ai**  
🏢 **精準智能生技股份有限公司 | Precise Intelligent Biotech Co., Ltd.**

---

## 📄 License | 授權

This repository contains **documentation and examples only**.  
All proprietary algorithms, model weights, and clinical data remain confidential under TFDA SaMD compliance requirements.

© 2025 PreCiseBD　股份有限公司. All rights reserved.
