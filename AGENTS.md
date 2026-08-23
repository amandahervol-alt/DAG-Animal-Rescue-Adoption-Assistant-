# Deming Animal Guardians (DAG) Adoption Assistant — AI Orchestration Guide
AGENTS.md — Antigravity Orchestration Architecture

This repository delivers an accessible, zero-cost adoption assistant, compatibility quiz, and community triage portal for **Deming Animal Guardians (DAG)**, an all-volunteer non-profit animal rescue in Luna County, New Mexico.

## Architecture

### 1. Dual-Mode Conversational Agent (`index.html`)
- **Live AI Mode**: Direct Anthropic Claude (`claude-3-7-sonnet-20250219` / `claude-3-5-sonnet-20241022`) integration with strict anti-hallucination guardrails.
- **Instant Demo Mode**: Zero-config offline rule engine providing instant responses to adoption fees, foster policies, and veterinary care without requiring an API key.

### 2. Interactive Pet Compatibility Matcher
- 4-step interactive lifestyle questionnaire (Housing, Activity Level, Household Members, Existing Pets).
- Deterministic heuristic matching engine generating personalized adopter profiles and recommended animal categories.

### 3. Rescue Information & Triage Hub
- Visual fee breakdown ($100–$200 for dogs, $50–$100 for cats) detailing included veterinary services (spay/neuter, vaccinations, microchip, heartworm test).
- Foster sponsorship pathways highlighting DAG's 100% veterinary cost coverage.

## Operating Principles & Guardrails
- **Anti-Hallucination**: The agent explicitly never invents specific shelter animals. It answers policy questions factually and routes live inventory lookups to verified social/web listings.
- **Civic Zero-Cost Hosting**: Runs 100% free on GitHub Pages with zero backend server dependencies.
