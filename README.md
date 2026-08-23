# Deming Animal Guardians (DAG) Adoption Assistant 🐾

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Hosting-GitHub%20Pages%20($0)-green.svg)](https://pages.github.com/)
[![Anthropic Claude](https://img.shields.io/badge/Claude-3.7%20%7C%203.5-purple.svg)](https://www.anthropic.com/)

An interactive, zero-cost AI Adoption Assistant, Pet Compatibility Matcher, and Community Rescue Portal built for **Deming Animal Guardians (DAG)**, an all-volunteer non-profit 501(c)(3) animal rescue in Deming, New Mexico (Luna County).

---

## 🌟 Mission & Real-World Impact

Deming Animal Guardians rescues dogs and cats from local shelters and surrounding rural areas in New Mexico, placing them into foster homes and providing complete veterinary care (spay/neuter surgery, core vaccines, microchipping, and heartworm testing) before finding them forever homes.

### Why This Tool Was Built:
- **Reduces Volunteer Admin Overhead**: Answers repetitive questions about adoption fees, eligibility, out-of-state transport, and foster programs so volunteers can focus on direct animal care.
- **Interactive Pet Compatibility Matcher**: Guides potential adopters through a 4-step lifestyle quiz to identify the best companion energy level for their household.
- **Strict Anti-Hallucination Guardrails**: The assistant never invents fake shelter animals—guiding adopters to verified live listings on Facebook while answering rescue policies accurately.
- **Zero-Cost Civic Hosting**: Runs 100% free on **GitHub Pages** with zero backend infrastructure or server bills.

---

## ✨ 4-Tab Interactive Portal Features

| Tab | Feature | Description |
| :--- | :--- | :--- |
| 💬 **AI Adoption Assistant** | Dual-Mode Conversational Agent | Instant Zero-Config Demo Mode + optional live Anthropic Claude (`claude-3-7-sonnet-20250219`) connectivity. |
| 🐶 **Pet Compatibility Matcher** | 4-Step Interactive Quiz | Evaluates housing, activity levels, household members, and existing pets to recommend customized rescue categories. |
| 📋 **Adoption Process & Fees** | Visual Fee Breakdown | Transparent fee schedule ($100–$200 dogs, $50–$100 cats) and details on veterinary care and out-of-state adoption. |
| 🏡 **Foster & Volunteer Hub** | Community Action Guide | Explains DAG's **100% veterinary cost coverage** for foster homes and details volunteer driver/event roles. |

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/amandahervol-alt/DAG-Animal-Rescue-Adoption-Assistant-.git
cd DAG-Animal-Rescue-Adoption-Assistant-
```

### 2. Run Locally
Open `index.html` in your browser, or launch with Python:
```bash
python app.py
```

### 3. Run Automated Tests
```bash
python -m pytest tests/
```

---

## 💡 Optional: Enabling Live Claude AI Key

By default, the portal runs in **Instant Demo Mode** (no API key required). To enable live Claude 3.7 / 3.5 AI reasoning:
1. Click the **(Settings)** button in the chat header.
2. Enter your Anthropic API key (`sk-ant-...`) and click **Save Live Key**.

---

## 📂 Repository Structure

```
DAG-Animal-Rescue-Adoption-Assistant-/
├── index.html                  # Main multi-tab interactive adoption portal
├── app.py                      # Local Python web server & runner
├── tests/
│   └── test_assistant.py       # Automated test suite for portal and guardrails
├── AGENTS.md                   # Antigravity AI Orchestration Architecture
├── LICENSE                     # MIT License
├── .env.example                # Environment configuration template
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
*Proudly developed in support of Deming Animal Guardians and rural animal welfare.*
