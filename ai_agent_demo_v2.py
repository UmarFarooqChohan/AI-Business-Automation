"""
Improved Demo AI Agent with dynamic content analysis
"""

from typing import Dict
import re

class AIAgentDemoV2:
    """Enhanced demo AI agent with content-aware responses"""
    
    def __init__(self):
        self.demo_mode = True
    
    def analyze_document(self, content: str, filename: str) -> Dict[str, str]:
        """Analyze document with dynamic content-aware responses"""
        
        # Extract key information from content
        lines = [l.strip() for l in content.split('\n') if l.strip()]
        first_lines = '\n'.join(lines[:15])
        
        # Extract numbers and metrics
        numbers = re.findall(r'\$?[\d,]+\.?\d*%?', content)
        
        # Extract sentences
        sentences = [s.strip() for s in re.split(r'[.!?]', content) if len(s.strip()) > 30][:8]
        
        # Analyze content themes
        content_lower = content.lower()
        themes = {
            'financial': any(word in content_lower for word in ['revenue', 'profit', 'cost', 'budget', 'financial', 'investment', 'expense']),
            'strategic': any(word in content_lower for word in ['strategy', 'plan', 'goal', 'objective', 'vision', 'mission']),
            'operational': any(word in content_lower for word in ['process', 'operation', 'efficiency', 'workflow', 'implementation']),
            'meeting': any(word in content_lower for word in ['meeting', 'discussion', 'attendees', 'agenda', 'minutes']),
            'proposal': any(word in content_lower for word in ['proposal', 'recommend', 'suggest', 'propose']),
            'report': any(word in content_lower for word in ['report', 'analysis', 'findings', 'results', 'summary']),
        }
        
        active_themes = [theme for theme, present in themes.items() if present]
        if not active_themes:
            active_themes = ['business operations']
        
        # Generate dynamic responses
        summary = self._generate_summary(content, first_lines, sentences, numbers, active_themes, filename)
        insights = self._generate_insights(content, active_themes, numbers)
        email = self._generate_email(filename, active_themes, len(content))
        tasks = self._generate_tasks(active_themes, numbers)
        
        return {
            'summary': summary,
            'insights': insights,
            'email': email,
            'tasks': tasks
        }
    
    def _generate_summary(self, content, first_lines, sentences, numbers, themes, filename):
        """Generate dynamic summary based on content"""
        
        theme_text = ', '.join(themes) if themes else 'business operations'
        word_count = len(content.split())
        
        summary = f"""**Document: {filename}**

This document focuses on {theme_text} with {len(numbers)} quantitative metrics identified.

**Key Content Preview:**
{first_lines[:400]}...

**Document Characteristics:**
• Length: {len(content)} characters ({word_count} words approximately)
• Data Points: {len(numbers)} numerical values
• Key Statements: {len(sentences)} major points identified
• Primary Themes: {theme_text}

**Initial Assessment:**
The document contains substantive information requiring detailed analysis and stakeholder review. 
Multiple decision points and action items appear to be present based on the content structure."""
        
        return summary.strip()
    
    def _generate_insights(self, content, themes, numbers):
        """Generate insights based on content analysis"""
        
        complexity = 'High' if len(content) > 3000 else 'Medium' if len(content) > 1500 else 'Moderate'
        review_time = max(5, len(content) // 500)
        
        theme_bullets = '\n'.join([f'• {theme.title()}: Significant presence in document' for theme in themes[:3]])
        
        insights = f"""**Content Analysis:**

**Primary Focus Areas:**
{theme_bullets}

**Quantitative Assessment:**
• {len(numbers)} numerical data points identified
• Document complexity: {complexity}
• Estimated review time: {review_time} minutes

**Strategic Implications:**
• Document requires executive-level review and decision-making
• Multiple stakeholders likely involved based on content scope
• Cross-functional coordination appears necessary
• Timeline and resource allocation decisions needed

**Key Observations:**
• Content suggests strategic importance to organization
• Data-driven approach evident from metrics included
• Implementation planning appears to be a focus
• Risk assessment and mitigation may be required

**Recommendations:**
1. **Immediate:** Distribute to relevant stakeholders for review
2. **Short-term:** Schedule alignment meeting to discuss findings
3. **Medium-term:** Develop detailed action plan with clear ownership
4. **Ongoing:** Establish tracking mechanisms for implementation
5. **Follow-up:** Create feedback loop for continuous improvement

**Risk Considerations:**
• Ensure all stakeholders are aligned before proceeding
• Validate all numerical data and assumptions
• Consider resource constraints and competing priorities
• Plan for change management if implementation required"""
        
        return insights.strip()
    
    def _generate_email(self, filename, themes, content_length):
        """Generate professional email response"""
        
        theme_text = ', '.join(themes[:2]) if len(themes) >= 2 else themes[0] if themes else 'business operations'
        
        email = f"""Subject: Analysis Complete - {filename}

Dear Team,

I've completed the automated analysis of "{filename}" and wanted to share the key findings.

**Document Overview:**
The document primarily addresses {theme_text} and contains substantial information requiring your attention.

**Key Highlights:**
• Document has been processed and analyzed
• Multiple themes and data points identified
• Strategic implications noted for review
• Action items and next steps recommended

**What I've Prepared:**
1. Executive summary of key content
2. Strategic insights and recommendations  
3. Suggested action items with priorities
4. Risk considerations and mitigation strategies

**Recommended Next Steps:**
1. Review the detailed analysis provided
2. Validate key assumptions and data points
3. Schedule stakeholder alignment meeting
4. Develop implementation timeline
5. Assign ownership for action items

**Timeline:**
I recommend reviewing this within the next 2-3 business days to maintain momentum and ensure timely decision-making.

**Questions or Concerns:**
Please don't hesitate to reach out if you need clarification on any aspect of the analysis or if additional information would be helpful.

Looking forward to discussing this further.

Best regards,
AI Business Automation Agent

---
*This analysis was generated automatically. Please review all findings and validate against source documents.*"""
        
        return email.strip()
    
    def _generate_tasks(self, themes, numbers):
        """Generate actionable tasks"""
        
        tasks = f"""**PRIORITY 1 - IMMEDIATE (Next 24-48 Hours)**

1. **Initial Document Review**
   - Conduct thorough review of all content
   - Validate {len(numbers)} numerical data points identified
   - Highlight areas requiring clarification
   - Timeline: Complete within 2 days
   - Owner: Department Head / Project Lead

2. **Stakeholder Identification**
   - Identify all relevant stakeholders
   - Determine decision-makers and approvers
   - Create distribution list
   - Timeline: Complete within 1 day
   - Owner: Project Manager

**PRIORITY 2 - SHORT TERM (Next 3-5 Days)**

3. **Data Validation & Analysis**
   - Cross-reference all metrics with source data
   - Verify assumptions and calculations
   - Document any discrepancies or concerns
   - Timeline: Complete within 5 days
   - Owner: Finance/Analytics Team

4. **Stakeholder Alignment Meeting**
   - Schedule meeting with key stakeholders
   - Prepare presentation materials
   - Distribute pre-read materials 24 hours in advance
   - Timeline: Schedule within 3 days
   - Owner: Executive Sponsor

5. **Risk Assessment**
   - Identify potential risks and challenges
   - Develop mitigation strategies
   - Assess resource requirements
   - Timeline: Complete within 5 days
   - Owner: Risk Management / Operations

**PRIORITY 3 - MEDIUM TERM (Next 1-2 Weeks)**

6. **Action Plan Development**
   - Define specific next steps and milestones
   - Assign clear ownership for each action
   - Establish success metrics and KPIs
   - Create tracking and reporting mechanism
   - Timeline: Complete within 10 days
   - Owner: Program Manager

7. **Resource Planning**
   - Determine budget requirements
   - Identify staffing needs
   - Assess technology/tool requirements
   - Secure necessary approvals
   - Timeline: Complete within 14 days
   - Owner: Finance & HR Teams

8. **Communication Strategy**
   - Develop internal communication plan
   - Prepare stakeholder updates
   - Create feedback collection mechanism
   - Timeline: Complete within 14 days
   - Owner: Communications Team

**ONGOING ACTIVITIES**

9. **Progress Tracking**
   - Weekly status updates to stakeholders
   - Monthly review of milestones and KPIs
   - Quarterly strategic assessment
   - Owner: Project Management Office

10. **Continuous Improvement**
    - Collect feedback from all stakeholders
    - Identify optimization opportunities
    - Implement lessons learned
    - Owner: Quality Assurance Team"""
        
        return tasks.strip()
