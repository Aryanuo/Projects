<div align="center">

# 🌲 The Forest of Cursed Elves 🌲  
### A Psychological Command-Line Text Adventure

*A subtly hostile forest.  
A quiet erosion of will.  
A choice that may never appear.*

</div>

---

## 🧠 Game Overview

**The Forest of Cursed Elves** is a **psychological text adventure** played entirely in the command line.  
The forest is not openly violent — it is patient, observant, and persuasive.

The player navigates a living environment that reacts not just to actions, but to **mental state**.

---

## 🎮 Genre & Platform

- **Genre:** Psychological Text Adventure / Interactive Fiction  
- **Platform:** Command Line Interface (CLI)  
- **Language:** Python  

---

## 🌲 Core Concept

The game tracks **three hidden core stats** that define who the player becomes:

| Stat | Represents | Narrative Role |
|----|----|----|
| **Will** | Mental fortitude | The power to refuse comfort or submission |
| **Awareness** | Perception and insight | The power to notice deception and patterns |
| **Corruption** | Forest influence | The seductive pull of belonging |

The primary challenge is **maintaining Will and Awareness** while resisting the slow rise of **Corruption**.

You never see these values directly.  
You feel them through disappearing choices.

---

## 🚀 How to Run the Game

### 🔧 Prerequisites
- Python **3.x** (recommended)

### ▶️ Execution

Clone the repository:
```bash
git clone []
cd elf-forest

python main.py

🏁 Endings (4 Primary Outcomes)

The game has four possible endings, resolved at the final scene through weighted logic:

| Ending                 | Probability | Final Action   | Required Conditions                     |
| ---------------------- | ----------- | -------------- | --------------------------------------- |
| 🌿 **The True Ending** | 10%         | Refusal (2)    | Will ≥ 7, Awareness ≥ 7, Corruption < 5 |
| ❌ **Consumed Refusal** | 30%         | Refusal (2)    | Fails True Ending conditions            |
| 🌑 **Rooted Will**     | 30%         | Acceptance (1) | High Will + Awareness                   |
| 🌲 **The Embrace**     | 30%         | Acceptance (1) | Low Will + Awareness or high Corruption |
