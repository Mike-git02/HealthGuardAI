# HealthGuardAI: Your Intelligent Wellness Watchdog

> **Theme:** "Tech for Good – Empowering Health with AI"  
> **Aligned to:** UN Sustainable Development Goal 3: *Good Health and Well-being*

---

## 🚀 Project Overview

The **AI-Powered Health Monitoring System** is a rule-based and ML-enhanced chatbot that simulates and monitors patient health data, detects anomalies, and provides basic advisory support. It is tailored for low-resource environments and focuses on proactive health alerts.

This project was created as part of the *Vibe and Code Challenge*.

---

## 🎯 Objectives

- ✅ Simulate health data (e.g., temperature, heart rate, blood pressure)
- ✅ Apply rule-based logic and anomaly detection
- ✅ Offer health advice based on trends and critical thresholds
- ✅ Align the solution with SDG 3 – "Ensure healthy lives and promote well-being for all"

---

## 🔧 Tech Stack

- **Language:** Python  
- **Libraries:** `sklearn`, `pandas`, `numpy`, `datetime`  
- **ML Algorithm:** Isolation Forest (for anomaly detection)

---

## 🧠 System Architecture

```plaintext
User Input
   ↓
Simulated Health Data (Real-Time or Batched)
   ↓
Rule-Based Engine + Anomaly Detection (Isolation Forest)
   ↓
AI-Powered Feedback (Advisory/Alert)
   ↓
[Optional] Future API/Web Dashboard
```

---

## 📂 File Structure

- `health_monitor.py` – Main script for simulating data and running analysis  
- `README.md` – Project summary and guide  
- `requirements.txt` – Required libraries (to be created)

---

## 📌 Example Features

- **Normal Health Advice:**
  ```
  Your vitals look good today. Stay hydrated and get enough sleep. 😊
  ```
- **Critical Alert:**
  ```
  🚨 Your heart rate is abnormally high. Please seek medical attention immediately!
  ```

---

## 🌍 SDG Alignment: Good Health and Well-being (SDG 3)

| Target | Description |
|--------|-------------|
| 3.8    | Achieve universal health coverage, access to quality essential health-care services |
| 3.d    | Strengthen capacity for early warning, risk reduction and management of health risks |

---

## ⚖️ Ethical Considerations

- The tool does **not replace professional diagnosis**.
- Includes disclaimers like:
  > *“This is not medical advice. Always consult a healthcare professional.”*

---

## 🧪 How to Run

1. Clone the repo or copy the `.py` file.
2. Install dependencies:
    ```bash
    pip install pandas scikit-learn
    ```
3. Run the script:
    ```bash
    python health_monitor.py
    ```

---

## 🚧 Future Enhancements

- Add web dashboard using Flask
- Real-time data via wearable integrations
- SMS alerts or WhatsApp bot
- Deploy via Docker or mobile integration

---

## 📝 License

MIT License  
(c) 2025 Onyimbo Michael