import PyPDF2
import docx
import os
from typing import Dict, Any, Optional

class ResumeParser:
    def __init__(self):
        pass
    
    def parse_resume(self, file_path: str) -> Optional[Dict[str, Any]]:
        try:
            if file_path.lower().endswith('.pdf'):
                text = self._extract_pdf_text(file_path)
            elif file_path.lower().endswith(('.docx', '.doc')):
                text = self._extract_docx_text(file_path)
            else:
                raise ValueError("Unsupported file format. Please use PDF or DOCX.")
            
            if not text.strip():
                raise ValueError("No text content found in the file.")
            
            return {
                'raw_text': text,
                'file_path': file_path,
                'file_size': os.path.getsize(file_path)
            }
            
        except Exception as e:
            print(f"Error parsing resume: {str(e)}")
            return None
    
    def _extract_pdf_text(self, file_path: str) -> str:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def _extract_docx_text(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
