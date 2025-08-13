import google.generativeai as genai
import os
from typing import Dict, Any, Tuple
from dotenv import load_dotenv

load_dotenv()

class ResumeOptimizer:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def optimize_resume(self, resume_data: Dict[str, Any], job_description: str) -> Tuple[str, str]:
        try:
            keywords = self._extract_keywords(job_description)
            
            optimized_resume = self._generate_optimized_resume(
                resume_data['raw_text'], 
                job_description, 
                keywords
            )
            
            explanation = self._generate_explanation(
                resume_data['raw_text'], 
                optimized_resume, 
                keywords
            )
            
            return optimized_resume, explanation
            
        except Exception as e:
            error_msg = f"Error during optimization: {str(e)}"
            return error_msg, error_msg
    
    def _extract_keywords(self, job_description: str) -> str:
        prompt = f"""
        Extract the most important keywords and skills from this job description.
        Focus on technical skills, tools, technologies, and industry-specific terms.
        Return only the keywords separated by commas, no explanations.
        
        Job Description:
        {job_description}
        """
        
        response = self.model.generate_content(prompt)
        return response.text.strip()
    
    def _generate_optimized_resume(self, original_resume: str, job_description: str, keywords: str) -> str:
        prompt = f"""
        Create an optimized version of this resume tailored to the job description.
        
        Original Resume:
        {original_resume}
        
        Job Description:
        {job_description}
        
        Important Keywords to Include:
        {keywords}
        
        Requirements:
        1. Optimize for ATS (Applicant Tracking Systems)
        2. Include relevant keywords naturally
        3. Improve formatting and structure
        4. Keep it professional and concise
        5. Maintain the original information but enhance it
        
        Return only the optimized resume text, no explanations.
        """
        
        response = self.model.generate_content(prompt)
        return response.text.strip()
    
    def _generate_explanation(self, original_resume: str, optimized_resume: str, keywords: str) -> str:
        prompt = f"""
        Explain the key changes made to optimize this resume.
        
        Keywords Added/Emphasized:
        {keywords}
        
        Focus on:
        1. Keywords that were added or emphasized
        2. Formatting improvements for ATS
        3. Content enhancements
        4. Overall optimization strategy
        
        Keep the explanation concise and professional.
        """
        
        response = self.model.generate_content(prompt)
        return response.text.strip()
