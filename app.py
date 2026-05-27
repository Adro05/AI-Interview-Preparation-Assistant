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

    found_skills = []

    score = 0

    for skill in skills_database:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

            score += 10

    st.subheader("Resume Strength Score")

    if score > 100:
        score = 100

    st.progress(score)

    st.write(f"{score}/100")

    st.subheader("Detected Skills")

    

    if found_skills:

        for skill in found_skills:

            st.write(f"- {skill}")

    else:

        st.write("No major skills detected.")
    
    st.subheader("Missing Skills")
    missing_skills = []

    for skill in role_required_skills[role]:

        if skill not in found_skills:

            missing_skills.append(skill)

    if missing_skills:

        for skill in missing_skills:

            st.write(f"- {skill}")

    else:

        st.success("No major missing skills detected.")

        
    st.subheader("Suggested Interview Questions")

    for question in role_questions[role]:

        st.write(f"- {question}")

    st.subheader("Preparation Suggestions")

    if "sql" not in found_skills:
        st.write("- Improve SQL skills.")

    if "machine learning" not in found_skills:
        st.write("- Learn machine learning fundamentals.")

    if "python" not in found_skills:
        st.write("- Strengthen Python programming.")

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