import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Interview Preparation Assistant")

st.title("AI Interview Preparation Assistant")

st.write("Upload your resume and prepare for interviews intelligently.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type="pdf"
)

role = st.selectbox(
    "Select Target Role",
    [
        "Data Scientist",
        "Machine Learning Engineer",
        "Data Analyst",
        "Software Engineer"
    ]
)

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    return text

role_questions = {
    "Data Scientist": [
        "Explain overfitting and underfitting.",
        "What is feature engineering?",
        "Difference between supervised and unsupervised learning?",
        "Explain bias-variance tradeoff."
    ],
    "Machine Learning Engineer": [
        "What is cross-validation?",
        "Explain gradient descent.",
        "Difference between Random Forest and XGBoost?",
        "What is model deployment?"
    ],
    "Data Analyst": [
        "Explain SQL joins.",
        "Difference between Power BI and Tableau?",
        "How do you handle missing data?",
        "What is data visualization?"
    ],
    "Software Engineer": [
        "Explain OOP concepts.",
        "Difference between stack and queue?",
        "What is time complexity?",
        "Explain REST APIs."
    ]
}

skills_database = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "tensorflow",
    "tableau",
    "power bi",
    "data analysis"
]

role_required_skills = {
    "Data Scientist": [
        "python",
        "machine learning",
        "sql",
        "pandas"
    ],
    "Machine Learning Engineer": [
        "python",
        "tensorflow",
        "deep learning",
        "numpy"
    ],
    "Data Analyst": [
        "sql",
        "power bi",
        "tableau",
        "pandas"
    ],
    "Software Engineer": [
        "python",
        "sql"
    ]
}

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    # FIX 1: Use a set for O(1) lookups instead of a list
    found_skills = set()

    for skill in skills_database:
        if skill.lower() in resume_text.lower():
            found_skills.add(skill)

    # FIX 2: Cap score BEFORE passing to st.progress()
    score = min(len(found_skills) * 10, 100)

    st.subheader("Resume Strength Score")

    # FIX 3: st.progress() requires a float between 0.0 and 1.0
    st.progress(score / 100)
    st.write(f"{score}/100")

    st.subheader("Detected Skills")
    if found_skills:
        for skill in sorted(found_skills):
            st.write(f"- {skill}")
    else:
        st.write("No major skills detected.")

    st.subheader("Missing Skills")
    # FIX 4: Compare against set (fast lookup) instead of list
    missing_skills = [
        skill for skill in role_required_skills[role]
        if skill not in found_skills
    ]

    if missing_skills:
        for skill in missing_skills:
            st.write(f"- {skill}")
    else:
        st.success("No major missing skills detected.")

    st.subheader("Suggested Interview Questions")
    for question in role_questions[role]:
        st.write(f"- {question}")

    st.subheader("Preparation Suggestions")
    suggestions = []

    if "sql" not in found_skills:
        suggestions.append("Improve SQL skills.")
    if "machine learning" not in found_skills:
        suggestions.append("Learn machine learning fundamentals.")
    if "python" not in found_skills:
        suggestions.append("Strengthen Python programming.")

    # FIX 5: Show a success message when no suggestions are needed
    if suggestions:
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.success("Great! No major preparation gaps found.")

    if len(found_skills) >= 5:
        st.success("Your resume shows a strong technical foundation.")

    st.subheader("Suggested Learning Roadmap")
    if role == "Data Scientist":
        st.write("- Learn statistics and probability")
        st.write("- Practice machine learning projects")
        st.write("- Improve SQL and data visualization")
    elif role == "Machine Learning Engineer":
        st.write("- Learn deep learning")
        st.write("- Study model deployment")
        st.write("- Practice TensorFlow and PyTorch")
    elif role == "Data Analyst":
        st.write("- Strengthen SQL")
        st.write("- Build dashboard projects")
        st.write("- Learn business analytics")
    elif role == "Software Engineer":
        st.write("- Practice DSA problems")
        st.write("- Learn system design")
        st.write("- Build backend projects")

else:
    # FIX 6: Guide the user when no file is uploaded
    st.info("Please upload your resume PDF to get started.")