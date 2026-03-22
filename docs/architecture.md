# paradigm architecture

This document describes the high-level architecture of **paradigm**, a local-first, audio-only AI companion designed to provide grounding, reflection, and clarity.

---

## 1. Core Principles

- **Local-first:** All processing happens on the user’s device.
- **Audio-only:** No camera, no visual sensors.
- **Ephemeral input:** Audio is processed in real time and then discarded.
- **No cloud dependency:** The system must function offline.
- **Strict safety boundaries:** No medical advice, no diagnosis, no emotional dependency.
- **User privacy:** No logs, no recordings, no stored transcripts.

---

## 2. System Overview

Paradigm consists of three main components:

### **A. Audio Pipeline**
- Microphone input  
- Local speech-to-text  
- Immediate deletion of raw audio  
- Text passed to the companion core  

### **B. Companion Core**
- System prompt defines behavior  
- Model generates grounding, reflective responses  
- No long-term memory unless explicitly added later  
- Safety layer enforces boundaries  

### **C. Output Layer**
- Text response  
- Optional text-to-speech  
- No storage of output unless user chooses  

---

## 3. Data Flow
