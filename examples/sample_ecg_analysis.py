"""
KaliSense AI — Sample ECG Analysis
===================================
This example demonstrates how to submit an ECG recording
to the KaliSense AI API and retrieve a potassium risk report.

Note: Uses anonymized/synthetic ECG data for demonstration.
"""

import requests
import base64
import json

API_BASE = "https://api.kalisense.ai/v1"
API_TOKEN = "your_api_token_here"  # Replace with your token

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


def load_ecg_as_base64(filepath: str) -> str:
    """Load an ECG file and encode it as base64."""
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_ecg(ecg_b64: str, patient_id: str = "demo_patient") -> dict:
    """Submit ECG for potassium risk analysis."""
    payload = {
        "ecg_format": "csv",
        "leads": 12,
        "patient_id": patient_id,
        "ecg_data": ecg_b64,
        "sampling_rate": 500
    }

    response = requests.post(
        f"{API_BASE}/analyze",
        headers=HEADERS,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def get_report(report_url: str) -> None:
    """Fetch and display the AIGC-generated clinical report."""
    response = requests.get(report_url, headers=HEADERS)
    response.raise_for_status()
    report = response.json()
    print("\n=== Clinical Report ===")
    print(json.dumps(report, indent=2, ensure_ascii=False))


# ── Example usage ─────────────────────────────────────
if __name__ == "__main__":

    # In real usage, load from an actual ECG file:
    # ecg_b64 = load_ecg_as_base64("patient_ecg.csv")

    # For demo: use a placeholder
    ecg_b64 = base64.b64encode(b"<synthetic_ecg_data>").decode()

    print("Submitting ECG for analysis...")
    result = analyze_ecg(ecg_b64, patient_id="demo_001")

    print(f"\nPotassium Risk:    {result['potassium_risk'].upper()}")
    print(f"Risk Score:        {result['risk_score']:.2f}")
    print(f"Est. K⁺ Range:    {result['estimated_k_range']}")
    print(f"Confidence:        {result['confidence']:.1%}")
    print(f"ECG Findings:      {', '.join(result['ecg_findings'])}")
    print(f"Processing Time:   {result['processing_time_ms']} ms")

    # Fetch full AIGC report
    if result.get("report_url"):
        get_report(result["report_url"])
