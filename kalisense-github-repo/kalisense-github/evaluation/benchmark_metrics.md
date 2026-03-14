# KaliSense AI — Benchmark & Evaluation Metrics

## Test Dataset

| Dataset | Source | Records | Notes |
|---------|--------|---------|-------|
| Internal Clinical | Partner nephrology centers (IRB approved) | 2,847 | Paired ECG + lab K⁺ values |
| PhysioNet PTB-XL | Public | 21,799 | Pre-training only |
| MIMIC-IV-ECG | Public | 800,000+ | Pre-training feature extraction |

> Patient-level data is not published. Only aggregated benchmark results are shown here.

## Classification Performance

### Overall (3-class: Normal / Hypokalemia / Hyperkalemia)

| Metric | Value |
|--------|-------|
| Accuracy | 91.2% |
| Macro F1 | 0.893 |
| Weighted F1 | 0.908 |

### Per-Class Results

| Class | Precision | Recall (Sensitivity) | Specificity | AUC |
|-------|-----------|----------------------|-------------|-----|
| Normal | 93.1% | 94.2% | 91.8% | 0.968 |
| Hyperkalemia | 89.4% | 88.0% | 93.5% | 0.947 |
| Hypokalemia | 86.7% | 85.4% | 92.1% | 0.921 |

## Comparison with Baseline Methods

| Method | Accuracy | Hyperkalemia AUC |
|--------|----------|-----------------|
| Rule-based ECG criteria | 71.3% | 0.743 |
| CNN-only | 86.4% | 0.901 |
| **KaliSense AI (CNN-Transformer)** | **91.2%** | **0.947** |

## Clinical Efficiency

| Metric | Traditional Lab | KaliSense AI |
|--------|----------------|-------------|
| Time to result | 30 min – 4 hrs | < 5 min |
| Blood draw required | Yes | **No** |
| Continuous monitoring | No | **Yes** |
| Remote deployment | Limited | **Yes** |

## Regulatory Status

| Region | Status |
|--------|--------|
| Taiwan TFDA SaMD | Application in progress |
| USA FDA 510(k) | Planned |
| EU CE MDR | Planned |
