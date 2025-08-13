import streamlit as st
import tempfile
import os
from pathlib import Path
from resume_parser import ResumeParser
from resume_optimizer import ResumeOptimizer

st.set_page_config(
    page_title="AI Resume Optimizer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00d4ff;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }
    
    .info-box {
        background-color: #262730;
        padding: 1.5rem;
        border-radius: 0.8rem;
        border-left: 4px solid #00d4ff;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .info-box strong {
        color: #00d4ff;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #00d4ff, #0099cc);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.75rem 2rem;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #0099cc, #00d4ff);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }
    
    .stFileUploader > div > div {
        background-color: #262730;
        border: 2px dashed #00d4ff;
        border-radius: 0.8rem;
        padding: 2rem;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #262730;
        color: #ffffff;
        border: 1px solid #4a4a4a;
        border-radius: 0.5rem;
    }
    
    .stSuccess {
        background-color: #1e3a2e;
        border-left: 4px solid #00ff88;
        color: #00ff88;
    }
    
    .stError {
        background-color: #3a1e1e;
        border-left: 4px solid #ff4444;
        color: #ff4444;
    }
    
    .stWarning {
        background-color: #3a2e1e;
        border-left: 4px solid #ffaa00;
        color: #ffaa00;
    }
    
    .stDownloadButton > button {
        background: linear-gradient(90deg, #00ff88, #00cc66);
        color: #000000;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #00cc66, #00ff88);
        transform: translateY(-1px);
    }
    
    h2 {
        color: #00d4ff !important;
        border-bottom: 2px solid #00d4ff;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #ffffff !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🤖 AI Resume Optimizer</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>How it works:</strong> Upload your resume (PDF/DOCX) and provide a job description. 
        Our AI will optimize your resume with relevant keywords, improved formatting, and ATS-friendly content.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📁 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose your resume file",
        type=['pdf', 'docx', 'doc'],
        help="Supported formats: PDF, DOCX, DOC"
    )
    
    st.subheader("🎯 Job Description")
    
    sample_job_description = """Software Engineer - Python Developer

We are looking for a talented Software Engineer with expertise in Python development to join our dynamic team.

Key Responsibilities:
• Develop and maintain Python-based applications and services
• Collaborate with cross-functional teams to design and implement new features
• Write clean, maintainable, and efficient code
• Participate in code reviews and technical discussions
• Troubleshoot and debug complex issues

Required Skills:
• Strong proficiency in Python programming
• Experience with web frameworks (Django, Flask, or FastAPI)
• Knowledge of databases (SQL, PostgreSQL, MongoDB)
• Familiarity with version control systems (Git)
• Understanding of RESTful APIs and microservices
• Experience with cloud platforms (AWS, Azure, or GCP)
• Knowledge of containerization (Docker, Kubernetes)

Preferred Skills:
• Experience with machine learning libraries (TensorFlow, PyTorch)
• Knowledge of frontend technologies (JavaScript, React)
• Experience with CI/CD pipelines
• Understanding of agile development methodologies

Education:
• Bachelor's degree in Computer Science, Engineering, or related field
• 3+ years of experience in software development

We offer competitive salary, flexible work arrangements, and opportunities for professional growth."""

    job_description = st.text_area(
        "Paste the job description here",
        value=sample_job_description,
        height=300,
        placeholder="Enter the job description you're applying for..."
    )
    
    if st.button("🚀 Optimize Resume", type="primary", use_container_width=True):
        if uploaded_file is not None and job_description.strip():
            with st.spinner("🤖 AI is optimizing your resume..."):
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name
                    
                    parser = ResumeParser()
                    resume_data = parser.parse_resume(tmp_file_path)
                    
                    if resume_data:
                        optimizer = ResumeOptimizer()
                        optimized_resume, explanation = optimizer.optimize_resume(resume_data, job_description)
                        
                        st.success("✅ Resume optimization completed!")
                        
                        st.subheader("📄 Optimized Resume")
                        st.text_area("Optimized Content", optimized_resume, height=400)
                        
                        st.download_button(
                            label="📥 Download Optimized Resume",
                            data=optimized_resume,
                            file_name=f"optimized_resume_{uploaded_file.name.split('.')[0]}.txt",
                            mime="text/plain"
                        )
                        
                        st.subheader("📝 Changes Explanation")
                        st.markdown(explanation)
                        
                    else:
                        st.error("Failed to parse resume. Please check the file format.")
                    
                    os.unlink(tmp_file_path)
                    
                except Exception as e:
                    st.error(f"Error during optimization: {str(e)}")
                    if "GEMINI_API_KEY" in str(e):
                        st.error("Please make sure you have set up your Gemini API key in the .env file.")
        else:
            st.warning("Please upload a resume and provide a job description.")

if __name__ == "__main__":
    main()
