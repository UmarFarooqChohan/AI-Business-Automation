import PyPDF2
import docx
from PIL import Image
from typing import Optional
import io

# Make pytesseract optional
try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

class DocumentProcessor:
    """Handles document reading and text extraction"""
    
    @staticmethod
    def extract_text(file_content: bytes, filename: str) -> Optional[str]:
        """Extract text from various file formats"""
        try:
            if filename.lower().endswith('.pdf'):
                return DocumentProcessor._extract_from_pdf(file_content)
            elif filename.lower().endswith('.docx'):
                return DocumentProcessor._extract_from_docx(file_content)
            elif filename.lower().endswith('.txt'):
                return file_content.decode('utf-8')
            elif filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                return DocumentProcessor._extract_from_image(file_content)
            else:
                return None
        except Exception as e:
            print(f"Error extracting text: {e}")
            return None
    
    @staticmethod
    def _extract_from_pdf(file_content: bytes) -> str:
        """Extract text from PDF"""
        pdf_file = io.BytesIO(file_content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text.strip()
    
    @staticmethod
    def _extract_from_docx(file_content: bytes) -> str:
        """Extract text from Word document"""
        doc_file = io.BytesIO(file_content)
        doc = docx.Document(doc_file)
        
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        return text.strip()
    
    @staticmethod
    def _extract_from_image(file_content: bytes) -> str:
        """Extract text from image using OCR"""
        if not TESSERACT_AVAILABLE:
            return "OCR not available. Please upload PDF or DOCX files for text extraction."
        
        try:
            image = Image.open(io.BytesIO(file_content))
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            return f"OCR error: {str(e)}. Please try a different file format."
    
    @staticmethod
    def validate_file(filename: str, file_size: int, max_size: int = 10*1024*1024) -> tuple[bool, str]:
        """Validate uploaded file"""
        allowed_extensions = {'.pdf', '.docx', '.txt', '.png', '.jpg', '.jpeg'}
        
        # Check file size
        if file_size > max_size:
            return False, f"File too large. Maximum size: {max_size // (1024*1024)}MB"
        
        # Check file extension
        file_ext = '.' + filename.lower().split('.')[-1] if '.' in filename else ''
        if file_ext not in allowed_extensions:
            return False, f"Unsupported file type. Allowed: {', '.join(allowed_extensions)}"
        
        return True, "Valid file"