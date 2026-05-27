# AI Interview Preparation Assistant

An AI-powered interview preparation assistant that analyzes resumes, detects technical skills, generates role-specific interview questions, and provides personalized preparation roadmaps.

## Features

- Resume PDF upload
- Resume strength scoring
- Skill extraction
- Missing skills analysis
- Role-based interview questions
- Personalized preparation suggestions
- Learning roadmap generation
- Interactive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- pdfplumber
- NLP
- Scikit-learn

---

## How It Works

1. User uploads resume PDF
2. System extracts resume text
3. Skills are identified dynamically
4. Resume strength score is calculated
5. Missing skills are detected based on target role
6. AI-generated interview questions are displayed
7. Personalized preparation roadmap is generated

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

LIVE DEMO:
https://ai-interview-preparation-assistant-ndzdwsxam8tbvnrjxrgvr6.streamlit.app/

Future Improvements:

LLM integration with Gemini/OpenAI
Speech-based mock interviews
AI answer evaluation
Behavioral interview simulation
Resume optimization suggestions