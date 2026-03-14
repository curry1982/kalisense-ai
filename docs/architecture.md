# KaliSense AI — System Architecture

## Overview

KaliSense AI is a cloud-native SaaS platform that predicts serum potassium (K⁺) anomalies from ECG waveforms using a CNN-Transformer deep learning model.

## Data Flow

```
ECG Device / Wearable
        │
        ▼
  [Input Adapter]
  Supports: .CSV, .EDF, HL7, proprietary device formats
        │
        ▼
  [Preprocessing Pipeline]
  • Noise filtering (bandpass 0.5–40 Hz)
  • Baseline wander correction
  • Beat segmentation (R-peak detection)
  • Feature normalization
        │
        ▼
  [CNN-Transformer Model]
  • CNN layers: local waveform feature extraction
    (T-wave amplitude, QRS width, PR interval, QTc)
  • Transformer encoder: global temporal context
  • Output head: 3-class classification
    (Normal / Hypokalemia / Hyperkalemia)
        │
        ▼
  [AIGC Report Generator]
  • LLM-based structured clinical report
  • Multilingual output (ZH / EN)
  • Risk explanation + suggested clinical action
        │
        ▼
  [Cloud Delivery]
  • REST API response (< 5 sec)
  • Push notification to nursing station
  • EHR / HIS integration via HL7 FHIR
```

## Security Architecture

- All data encrypted in transit (TLS 1.3) and at rest (AES-256)
- Role-based access control (RBAC)
- Audit logging for all API calls
- Compliant with ISO 27001 and TFDA SaMD requirements
- Patient data never stored beyond session unless explicitly consented

## Deployment Options

| Mode | Description |
|------|-------------|
| **Public Cloud** | AWS / Azure / 台智雲 managed SaaS |
| **Private Cloud** | On-premise deployment for hospitals with strict data residency |
| **Hybrid** | Model inference on-premise, reporting via cloud |

## Compliance

> Core model training data, patient records, and proprietary algorithm weights
> are maintained exclusively in our private GitLab repository under
> TFDA SaMD regulatory controls. This public repository documents
> architecture and interfaces only.
