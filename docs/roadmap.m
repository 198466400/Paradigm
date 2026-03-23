# paradigm roadmap

This roadmap outlines the planned development phases for **paradigm**, a local‑first, audio‑only AI companion designed to provide grounding, reflection, and clarity.

The goal is to build a simple, safe, intentional tool that works offline, respects privacy, and supports the user without replacing human connection.

---

## ✅ Phase 1 — Foundation (complete)

- Create initial repository structure  
- Add README with philosophy and purpose  
- Add system behavior contract  
- Add architecture overview  
- Add placeholder code for:
  - app entry point  
  - audio pipeline  
  - companion core  
- Establish clean `.gitignore` and MIT license  
- Add contributing guidelines and code of conduct  

**Status:** Complete

---

## 🚧 Phase 2 — Local Audio Pipeline (in progress)

- Implement microphone capture  
- Add local Whisper or Whisper.cpp for speech‑to‑text  
- Ensure audio is deleted immediately after processing  
- Add clear mic indicator logic (software‑level)  
- Build a simple CLI interface for testing  

**Goal:** Audio → text working fully offline

---

## 🔜 Phase 3 — Companion Core

- Load system_companion.txt dynamically  
- Integrate a small local LLM (Llama.cpp, Phi, or similar)  
- Add safety layer enforcing boundaries  
- Generate grounding, reflective responses  
- Ensure no long‑term memory unless explicitly added  

**Goal:** Text → safe, supportive response

---

## 🔮 Phase 4 — Output Layer

- Optional text‑to‑speech (local)  
- Configurable voice settings  
- CLI and/or minimal desktop UI  
- “Quiet mode” (text‑only)  

**Goal:** Response → spoken output (optional)

---

## 🧭 Phase 5 — User Experience

- Add journaling mode (opt‑in only)  
- Add reflection summaries (local‑only)  
- Add grounding prompts  
- Add “connection nudges” encouraging real human contact  

**Goal:** A tool that supports clarity without replacing people

---

## 🛠️ Phase 6 — Hardware Exploration

- Single‑button wearable concept  
- Bluetooth connection to mobile device  
- Hardware mic indicator  
- Hardware kill switch  
- Offline‑first companion device prototype  

**Goal:** A physical interface that respects autonomy and privacy

---

## 🌱 Phase 7 — Community & Extensions

- Contribution guidelines  
- Plugin architecture (local‑only)  
- Optional integrations (calendar, reminders, journaling)  
- Community‑driven safety improvements  

---

## 🏁 Long‑Term Vision

A small, intentional, local‑first companion that:

- listens without storing  
- reflects without judging  
- supports without replacing  
- grounds without controlling  

A moment of clarity, on demand.
