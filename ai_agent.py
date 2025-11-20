import openai
from typing import Dict, List
from config import Config

class AIAgent:
    def __init__(self):
        if not Config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable.")
        
        openai.api_key = Config.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.use_demo_fallback = False
    
    def analyze_document(self, content: str, filename: str) -> Dict[str, str]:
        # If we've detected quota issues, use demo fallback
        if self.use_demo_fallback:
            from ai_agent_demo import AIAgentDemo
            demo_agent = AIAgentDemo()
            return demo_agent.analyze_document(content, filename)
        
        summary = self._generate_summary(content)
        
        # Check if we got an error (quota exceeded)
        if "Error code: 429" in summary or "insufficient_quota" in summary:
            self.use_demo_fallback = True
            from ai_agent_demo import AIAgentDemo
            demo_agent = AIAgentDemo()
            return demo_agent.analyze_document(content, filename)
        
        insights = self._generate_insights(content, summary)
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
        Analyze this business document and provide a concise summary:
        
        Document Content:
        {content[:2000]}...
        
        Provide a professional summary highlighting:
        - Key points and main topics
        - Important decisions or recommendations
        - Critical data or metrics
        - Action items mentioned
        
        Keep it under 200 words and business-focused.
        """
        
        return self._call_gpt(prompt) 
   
    def _generate_insights(self, content: str, summary: str) -> str:
        prompt = f"""
        Based on this business document, provide strategic insights and recommendations:
        
        Summary: {summary}
        
        Provide:
        1. Key business implications
        2. Potential risks or opportunities
        3. Strategic recommendations
        4. Next steps for leadership
        
        Be specific and actionable. Format as bullet points.
        """
        
        return self._call_gpt(prompt)
    
    def _generate_email(self, content: str, summary: str) -> str:
        prompt = f"""
        Generate a professional email response based on this document:
        
        Summary: {summary}
        
        Create an email that:
        - Acknowledges receipt of the document
        - Summarizes key points
        - Suggests next steps
        - Maintains professional tone
        
        Include subject line and full email body.
        """
        
        return self._call_gpt(prompt)
    
    def _generate_tasks(self, content: str, summary: str, insights: str) -> str:
        prompt = f"""
        Based on this analysis, create a list of follow-up tasks:
        
        Summary: {summary}
        Insights: {insights}
        
        Generate 3-5 specific, actionable tasks that should be completed:
        - Include responsible parties (roles, not names)
        - Set realistic timelines
        - Prioritize by importance
        
        Format as numbered list with details.
        """
        
        return self._call_gpt(prompt)
    
    def _call_gpt(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert business analyst and automation assistant. Provide clear, actionable, and professional responses."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error generating response: {str(e)}"