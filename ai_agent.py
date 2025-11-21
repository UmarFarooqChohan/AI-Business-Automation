import google.generativeai as genai
from typing import Dict, List
from config import Config

class AIAgent:
    def __init__(self):
        if not Config.GOOGLE_API_KEY:
            raise ValueError("Google API key not found. Using demo mode.")
        
        try:
            genai.configure(api_key=Config.GOOGLE_API_KEY)
            self.model = genai.GenerativeModel(Config.DEFAULT_MODEL)
            self.use_demo_fallback = False
        except Exception as e:
            raise ValueError(f"API configuration failed: {str(e)}")
    
    def analyze_document(self, content: str, filename: str) -> Dict[str, str]:
        # If we've detected quota issues, use demo fallback
        if self.use_demo_fallback:
            from ai_agent_demo import AIAgentDemo
            demo_agent = AIAgentDemo()
            return demo_agent.analyze_document(content, filename)
        
        summary = self._generate_summary(content)
        
        # Check if we got an error (quota exceeded)
        if "QUOTA_EXCEEDED" in summary or "Error code: 429" in summary or "insufficient_quota" in summary:
            self.use_demo_fallback = True
            from ai_agent_demo import AIAgentDemo
            demo_agent = AIAgentDemo()
            return demo_agent.analyze_document(content, filename)
        
        insights = self._generate_insights(content, summary)
        
        # Check if insights failed
        if "QUOTA_EXCEEDED" in insights:
            self.use_demo_fallback = True
            from ai_agent_demo import AIAgentDemo
            demo_agent = AIAgentDemo()
            return demo_agent.analyze_document(content, filename)
        
        email = self._generate_email(content, summary)
        tasks = self._generate_tasks(content, summary, insights)
        
        return {
            'summary': summary,
            'insights': insights,
            'email': email,
            'tasks': tasks
        }
    
    def _generate_summary(self, content: str) -> str:
        prompt = f"""
        Analyze this business document and provide a concise summary (max 150 words):
        
        Document Content:
        {content[:1500]}
        
        Include:
        - Key points and main topics
        - Important decisions or recommendations
        - Critical metrics
        - Action items
        """
        
        return self._call_gpt(prompt) 
   
    def _generate_insights(self, content: str, summary: str) -> str:
        prompt = f"""
        Based on this summary, provide strategic insights (max 200 words):
        
        Summary: {summary[:500]}
        
        Provide bullet points for:
        1. Key business implications
        2. Risks or opportunities
        3. Strategic recommendations
        4. Next steps
        """
        
        return self._call_gpt(prompt)
    
    def _generate_email(self, content: str, summary: str) -> str:
        prompt = f"""
        Generate a professional email (max 150 words):
        
        Summary: {summary[:400]}
        
        Include:
        - Subject line
        - Acknowledgement
        - Key points summary
        - Next steps
        """
        
        return self._call_gpt(prompt)
    
    def _generate_tasks(self, content: str, summary: str, insights: str) -> str:
        prompt = f"""
        Create 5 actionable follow-up tasks (max 150 words):
        
        Summary: {summary[:300]}
        Insights: {insights[:300]}
        
        For each task include:
        - Action item
        - Responsible role
        - Timeline
        
        Format as numbered list.
        """
        
        return self._call_gpt(prompt)
    
    def _call_gpt(self, prompt: str) -> str:
        try:
            full_prompt = f"""You are an expert business analyst and automation assistant. Provide clear, actionable, and professional responses.

{prompt}"""
            
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=2000,  # Increased token limit
                    temperature=Config.TEMPERATURE,
                ),
                safety_settings=[
                    {
                        "category": "HARM_CATEGORY_HARASSMENT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_HATE_SPEECH",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                        "threshold": "BLOCK_NONE",
                    },
                ]
            )
            
            # Check if response has valid content
            if not response.candidates:
                self.use_demo_fallback = True
                return "QUOTA_EXCEEDED"
            
            candidate = response.candidates[0]
            
            # Check finish reason
            if candidate.finish_reason != 1:  # 1 = STOP (normal completion)
                # Try to get partial content if available
                if candidate.content and candidate.content.parts:
                    return candidate.content.parts[0].text.strip()
                else:
                    # Fall back to demo mode
                    self.use_demo_fallback = True
                    return "QUOTA_EXCEEDED"
            
            return response.text.strip()
        
        except Exception as e:
            error_msg = str(e)
            # Check for quota, API errors, or leaked key
            if any(keyword in error_msg.lower() for keyword in ["quota", "429", "limit", "finish_reason", "leaked", "403", "invalid"]):
                self.use_demo_fallback = True
                return "QUOTA_EXCEEDED"
            return f"Error generating response: {error_msg}"