# Book Catalog — Project Overview

## 🔍 Project Purpose

Book Catalog is an intelligent automation system designed for the cataloging, evaluation, and sale of used and rare books. It is being developed with three core objectives:

1. **Automated Personal Tool**: To streamline and optimize the workflow of book intake, metadata extraction, and sales preparation.
2. **Open Source Framework**: To create a modular, replicable system accessible to non-technical users.
3. **Educational Asset**: To document every step and decision for future guides, tutorials, and potential course content.

---

## 🤖 The Automatic Mode

This project is being developed under a unique framework called **Automatic Mode**, powered by GPT-4o.

### What is Automatic Mode?

It is a structured collaboration where the assistant acts as a **step-by-step guide**, memory engine, and development planner. The assistant tracks progress, breaks the project into actionable milestones, and synchronizes documentation in real time.

### How it was built

The user defined the prompting logic that enables this mode. Key features include:
- Memory-based tracking of project phases and context
- GitHub synchronization reminders
- Decision logging embedded in project files
- User-controlled tempo and branching of development

---

## 🏗️ Project Architecture

book-catalog/
├── backend/
│ ├── acquisition/
│ ├── db/
│ ├── extraction/
│ ├── intelligence/
│ └── utils/
├── data/
│ ├── raw/
│ └── processed/
├── models/
├── notebooks/
├── ui/
├── docs/
├── guide/
├── content/
└── library.db

---

## ✅ Completed Phases

- Repository initialized and pushed to GitHub
- Legacy code moved and refactored into modular backend/
- Folder structure aligned with scalable architecture
- Insert script updated for extended schema
- Intelligence modules (classifier, pricer, evaluator) created
- API cost logging system planned
- Vision API integration defined

---

## 🔄 Current Phase

> **Integrating OpenAI Vision API** to extract title/author/ISBN from cover images and store results in the database with cost logging.

---

## 🔜 Next Steps

- Implement API call module `vision_openai.py`
- Add cost tracking system to database or log
- Create UI mask for data verification
- Begin training logic for intelligent pricing and rarity assessment
