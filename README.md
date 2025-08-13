# 🤖 AI Resume Optimizer

A simple and clean AI-powered resume optimizer that uses Google Gemini to tailor your resume to specific job descriptions.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Key
1. Get your Gemini API key from: https://makersuite.google.com/app/apikey
2. Rename `env_template.txt` to `.env`
3. Replace `your_gemini_api_key_here` with your actual API key

### 3. Run the Application
```bash
streamlit run app.py
```

## 📁 Project Structure
```
resume/
├── app.py                    # Main Streamlit application
├── resume_parser.py          # PDF/DOCX parsing
├── resume_optimizer.py       # AI optimization logic
├── requirements.txt          # Dependencies
├── env_template.txt          # Environment template
└── README.md                 # This file
```

## ✨ Features
- **PDF/DOCX Support**: Upload your resume in PDF or DOCX format
- **AI Optimization**: Uses Google Gemini to optimize content
- **Keyword Matching**: Extracts and incorporates relevant keywords
- **ATS Optimization**: Ensures compatibility with Applicant Tracking Systems
- **Clean Interface**: Simple and intuitive Streamlit frontend
- **Download Results**: Save your optimized resume as text file

## 🎯 How to Use
1. Upload your resume (PDF/DOCX)
2. Paste or edit the job description
3. Click "Optimize Resume"
4. Review the optimized version and explanation
5. Download the result

## 🔧 Requirements
- Python 3.8+
- Google Gemini API key
- Internet connection

## 📝 Sample Job Description
The app includes a sample job description for a Python Developer position that you can use for testing or as a template.

## License

