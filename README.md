# Deming Animal Guardians (DAG) Adoption Assistant 🐾

An AI-powered conversational adoption assistant built for **Deming Animal Guardians (DAG)**, a non-profit, volunteer-run animal rescue based in Deming, New Mexico (Luna County).

This web application helps potential adopters find companion animals, answers questions about adoption fees and requirements, and guides community members on how to foster, volunteer, or support rescue efforts.

---

## 🌟 Mission & Real-World Impact

Deming Animal Guardians rescues dogs, cats, and animals from local shelters and surrounding rural areas in New Mexico, placing them into foster homes and providing veterinary care (spay/neuter, vaccinations, microchipping, and heartworm testing) before finding them forever homes.

### Why This Tool Was Built:
- **Reduces Admin Overhead for Volunteers**: Answers recurring questions about adoption fees, eligibility, out-of-state adoption, and application steps so volunteer staff can focus on animal care.
- **Anti-Hallucination Guardrails**: Prompts are specifically engineered so the agent **never fabricates fake animals** or unavailable pets—always directing adopters to official live listings for real-time availability.
- **Low-Barrier Accessibility**: A lightweight, single-page web app built with zero build step requirements, designed for high accessibility on mobile and desktop.

---

## ✨ Key Features

- 🐶 **Intelligent Adoption Guidance**: Answers questions about adoption criteria, fees ($100–$200 for dogs, $50–$100 for cats), and out-of-state adoption pathways.
- 🏡 **Foster & Volunteer Onboarding**: Explains foster support programs (DAG covers medical costs) and volunteer opportunities.
- 💡 **One-Tap Quick Suggestions**: Pre-built prompt chips for common adopter inquiries (*"What animals are available?"*, *"Do you have dogs good with kids?"*, *"What are the adoption fees?"*).
- 🔒 **Client-Side Privacy**: API keys stay in the browser session and are never logged or stored externally.

---

## 💡 Key Design Decisions for Interview Reviewers

1. **System Prompt Guardrails & Triage**: The system prompt explicitly restricts the LLM from inventing current shelter inventory. It provides factual background on rescue policies while delegating live pet verification to official Facebook and website channels.
2. **Zero-Build Dependency Footprint**: Implemented in clean, modern vanilla JavaScript and CSS, requiring no heavy node modules or build toolchain to run.
3. **Session-Scoped Memory & State**: Maintains conversational state in lightweight client-side memory with auto-resizing text inputs and responsive mobile UI.

---

## 🛠️ Tech Stack

- **Frontend**: Vanilla HTML5, CSS3 (Custom Properties & Flexbox), Modern JavaScript (ES6+)
- **AI Model**: Anthropic API (`claude-3-5-sonnet`)
- **Typography & Styling**: Clean mobile-responsive UI with teal and warm orange palette

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/amandahervol-alt/DAG-Animal-Rescue-Adoption-Assistant-.git
cd DAG-Animal-Rescue-Adoption-Assistant-
```

### 2. Run the App
Simply open `index.html` in any web browser!
```bash
# On Windows
start index.html

# Or run a local HTTP server
python -m http.server 8000
```

### 3. Start Chatting
Enter your Anthropic API key (`sk-ant-...`) when prompted on the setup screen to launch the conversational assistant.

---

## 👩‍💻 About the Developer

Built by **Amanda Hervol**, an AI Software Engineer & Workflow Architect dedicated to leveraging technology for non-profit impact, health equity, and animal welfare.

- 🔗 [LinkedIn](https://www.linkedin.com/in/amandaa-hervol/)
- 📧 [amandahervol@gmail.com](mailto:amandahervol@gmail.com)
