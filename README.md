# 🌿 Urban Mobility AI Agent (Commute Optimizer)

A context-aware reasoning engine built with **Gemini 2.0 Flash** that nudges users toward sustainable transport by calculating the true "friction" of urban travel.

## 📁 Repository Breakdown
- **`app.py`**: The core integration using the **Gemini 2.0 Flash SDK**.
- **`prompt.txt`**: The decoupled **AI Logic Policy**. By separating the "Brain" (logic) from the "Plumbing" (code), we can update mobility policies without a redeploy.
- **`commute_data.json`**: Real-world scenarios (The Morning Sync, The Grandma Trip, The Grocery Run).
- **`output_data.json`**: Cached AI reasoning results, serving as a high-availability fallback for API rate limits.

## 🚀 Key Features
- **Dynamic Car Utility Scoring:** Starts with an 80-point "driving tax" and adjusts for parking difficulty and traffic delays.
- **Thermal Comfort Analysis:** Calculates wind-chill and temperature friction specifically for scooters and walking.
- **Decoupled Logic Policy:** Reasoning logic is stored in `prompt.txt`, allowing for "No-Code" tuning of mobility policies.
- **Micro-Mobility Optimization:** Penalizes "Lazy Car" trips (<2km) and "Overkill Scooter" trips (<1.5km).

## 🛠 Tech Stack
- **SDK:** `google-genai` (2026 Modern Python Client)
- **Model:** `gemini-2.0-flash`
- **Logic:** Chain-of-Thought (CoT) Prompting with Structured JSON Output.

## 📊 Logic Example: "Should I leave the car?"
The agent evaluates the "Parking Pain" vs. "Weather Pain." If the viability of a scooter or walk exceeds the utility of the car (factoring in the need for groceries or distance), it issues a "YES" recommendation.
