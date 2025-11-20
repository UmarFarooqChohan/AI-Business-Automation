"""
Demo version of AI Agent with mock responses for hackathon presentation
Use this when OpenAI API quota is exceeded
"""

from typing import Dict

class AIAgentDemo:
    """Demo AI agent with pre-generated responses"""
    
    def __init__(self):
        self.demo_mode = True
    
    def analyze_document(self, content: str, filename: str) -> Dict[str, str]:
        """Analyze document using mock AI responses"""
        
        # Detect document type for better mock responses
        content_lower = content.lower()
        
        if "proposal" in content_lower or "investment" in filename.lower():
            return self._business_proposal_response(content)
        elif "meeting" in content_lower or "notes" in filename.lower():
            return self._meeting_notes_response(content)
        elif "financial" in content_lower or "revenue" in content_lower:
            return self._financial_report_response(content)
        else:
            return self._generic_response(content)
    
    def _business_proposal_response(self, content: str) -> Dict[str, str]:
        summary = """
This business proposal outlines an AI automation implementation strategy with significant ROI potential. 
Key highlights include:

• 60% reduction in manual tasks through intelligent automation
• Annual cost savings of $50,000 with 6-month ROI timeline
• 85% reduction in manual errors and 3x document processing capacity
• Initial investment of $15,000 with $2,000 monthly operational costs
• Phased rollout from Q1 pilot to Q2 full implementation

The proposal addresses integration challenges, staff training needs, and data security considerations 
while emphasizing the competitive advantage of immediate implementation.
        """
        
        insights = """
**Key Business Implications:**
• Strong ROI: 6-month payback period indicates excellent investment efficiency
• Scalability: 3x capacity increase positions company for growth without proportional cost increases
• Risk mitigation: 85% error reduction significantly reduces operational and compliance risks

**Strategic Opportunities:**
• First-mover advantage in automation could differentiate from competitors
• Freed resources (20 hours/week) can be redirected to strategic initiatives
• Foundation for future AI/ML implementations across other departments

**Potential Risks:**
• Legacy system integration may require additional technical resources
• Change management and staff adoption critical to success
• Security considerations need thorough vetting before implementation

**Recommendations:**
1. Approve budget immediately to capture Q1 implementation window
2. Establish cross-functional steering committee for oversight
3. Develop comprehensive change management and training program
4. Conduct security audit before pilot launch
5. Define clear KPIs to measure success against projected benefits

**Next Steps for Leadership:**
• CFO: Approve $15K initial budget and $2K/month operational costs
• CTO: Evaluate and select implementation partner within 2 weeks
• CHRO: Design training program for affected staff
• CEO: Communicate strategic vision to organization
        """
        
        email = """
Subject: Re: AI Automation Implementation Proposal - Recommendation to Proceed

Dear Leadership Team,

Thank you for the comprehensive AI automation implementation proposal. After thorough review, 
I'm pleased to recommend moving forward with this initiative.

**Key Takeaways:**
The proposal presents a compelling business case with $50,000 in annual savings, 60% reduction 
in manual tasks, and a 6-month ROI. The phased approach from Q1 pilot to Q2 rollout demonstrates 
thoughtful planning and risk management.

**Strategic Value:**
Beyond cost savings, this positions us for scalable growth and competitive differentiation. 
The 3x capacity increase without proportional cost growth is particularly attractive as we 
expand operations.

**Recommended Actions:**
1. Approve the $15,000 initial investment and $2,000 monthly budget
2. Fast-track vendor selection to meet Q1 pilot timeline
3. Establish steering committee with representatives from IT, Operations, and Finance
4. Prioritize security audit and change management planning

**Next Steps:**
I suggest we schedule a 30-minute executive session this week to finalize approval and assign 
ownership. The competitive advantage of early implementation makes timing critical.

Please confirm your availability for Thursday or Friday this week.

Best regards,
[Business Automation Team]
        """
        
        tasks = """
**Priority 1 - Immediate (This Week):**
1. **Budget Approval** (CFO)
   - Review and approve $15K initial + $2K/month operational budget
   - Secure board approval if required
   - Timeline: By end of week

2. **Steering Committee Formation** (CEO)
   - Assign executive sponsor
   - Select cross-functional team members (IT, Ops, Finance, HR)
   - Schedule kickoff meeting
   - Timeline: Within 5 business days

**Priority 2 - Short Term (Next 2 Weeks):**
3. **Vendor Selection** (CTO)
   - Evaluate 3-5 implementation partners
   - Conduct technical assessments and reference checks
   - Negotiate contracts and SLAs
   - Timeline: Complete by Nov 30

4. **Security Assessment** (CISO/IT Security)
   - Conduct comprehensive security audit
   - Review data privacy and compliance requirements
   - Document security protocols and controls
   - Timeline: Complete before pilot launch

**Priority 3 - Medium Term (Next 30 Days):**
5. **Change Management Plan** (CHRO/HR)
   - Develop staff communication strategy
   - Design training curriculum for affected teams
   - Create support resources and documentation
   - Timeline: Ready before Q1 pilot launch
        """
        
        return {
            'summary': summary.strip(),
            'insights': insights.strip(),
            'email': email.strip(),
            'tasks': tasks.strip()
        }
    
    def _meeting_notes_response(self, content: str) -> Dict[str, str]:
        summary = """
Quarterly Business Review highlighted strong Q3 performance with $2.3M revenue (15% above target) 
and 450 new client acquisitions. Key Q4 priorities include new product launch, European expansion, 
and AI automation implementation with 25 new hires planned.

Budget allocations approved: $500K marketing increase, $300K for AI initiatives, $200K for 
automation tools. Critical action items assigned across departments with deadlines through 
mid-December. Leadership approved $1M investment in AI and automation for 2025, while noting 
concerns about Q1 supply chain risks and competitive pressures.
        """
        
        insights = """
**Key Business Implications:**
• Strong momentum: 15% revenue overperformance and improved churn (3.2% vs 4.1%) indicate healthy growth
• Aggressive expansion: European market entry and new product line show confidence in market position
• Strategic investment: $1M AI/automation commitment signals digital transformation priority

**Strategic Opportunities:**
• Market expansion timing aligns with strong financial performance
• AI automation investment can support scaling without proportional headcount growth
• Improved churn rate suggests product-market fit strengthening

**Potential Risks:**
• Q1 supply chain disruptions could impact new product launch timing
• Simultaneous initiatives (expansion + new product + automation) may strain resources
• Competitive pressure requires differentiation strategy

**Recommendations:**
1. Prioritize AI automation to support expansion efficiency
2. Develop contingency plans for Q1 supply chain issues
3. Ensure adequate project management for parallel initiatives
4. Accelerate recruitment to support growth plans
        """
        
        email = """
Subject: Q3 Business Review - Action Items and Next Steps

Team,

Excellent Q3 performance! The 15% revenue beat and improved retention metrics demonstrate 
strong execution across the organization.

**Key Decisions:**
- Approved $1M investment in AI/automation for 2025
- Green light for European expansion and new product launch
- Budget increases: Marketing +$500K, R&D +$300K, Operations +$200K

**Your Action Items:**
Please review the assigned tasks and deadlines from the meeting. All department heads should 
confirm resource allocation and timeline feasibility by end of week.

**Upcoming Milestones:**
- Nov 25: Finance - Q4 budget adjustments
- Nov 30: IT - AI automation vendor evaluation
- Dec 1: Marketing - European launch strategy
- Dec 15: HR - Key position recruitment plan

Let's maintain this momentum into Q4. Please flag any blockers or resource constraints immediately.

Best regards,
[Executive Team]
        """
        
        tasks = """
1. **Marketing Team - European Launch Strategy** (Due: Dec 1)
   - Conduct market research for target European countries
   - Develop localization and go-to-market strategy
   - Prepare budget allocation for regional marketing
   - Responsible: VP Marketing

2. **IT Team - AI Automation Vendor Evaluation** (Due: Nov 30)
   - Research and evaluate AI automation platforms
   - Conduct vendor demos and technical assessments
   - Prepare recommendation with cost-benefit analysis
   - Responsible: CTO

3. **HR Team - Key Position Recruitment** (Due: Dec 15)
   - Define job descriptions for 25 new positions
   - Launch recruitment campaigns
   - Begin candidate screening process
   - Responsible: VP HR

4. **Finance Team - Q4 Budget Adjustments** (Due: Nov 25)
   - Incorporate approved budget increases ($1M total)
   - Revise Q4 and 2025 financial projections
   - Prepare board presentation materials
   - Responsible: CFO

5. **Operations Team - Supply Chain Contingency Planning** (Due: Dec 10)
   - Assess Q1 supply chain risks
   - Develop mitigation strategies and backup suppliers
   - Create risk monitoring dashboard
   - Responsible: VP Operations
        """
        
        return {
            'summary': summary.strip(),
            'insights': insights.strip(),
            'email': email.strip(),
            'tasks': tasks.strip()
        }
    
    def _financial_report_response(self, content: str) -> Dict[str, str]:
        summary = """
October 2024 financial performance shows strong results with $850K total revenue (12% MoM, 28% YoY growth) 
and healthy 27% profit margin. Revenue mix: Product Sales 76% ($650K), Services 18% ($150K), Licensing 6% ($50K).

Total expenses of $620K dominated by salaries (56%) and marketing (19%). Key metrics demonstrate 
business health: CAC $150, LTV $2,400 (16:1 ratio), MRR $320K, positive cash flow +$180K.

Recommendations focus on capitalizing on growth momentum through increased marketing spend, automation 
investments, sales team expansion, and improved financial tracking. Risks include seasonal Q1 decline, 
competitive margin pressure, and rising operational costs.
        """
        
        insights = """
**Key Business Implications:**
• Exceptional unit economics: $150 CAC vs $2,400 LTV (16:1 ratio) indicates highly efficient growth model
• Strong cash generation: +$180K monthly cash flow provides runway for strategic investments
• Healthy growth trajectory: 28% YoY growth with 27% margins shows scalable business model

**Strategic Opportunities:**
• Increase marketing investment: Strong unit economics justify aggressive customer acquisition
• Subscription model expansion: Current MRR base provides foundation for recurring revenue growth
• Partnership opportunities: Tech company partnerships could accelerate market penetration

**Potential Risks:**
• Seasonal vulnerability: Q1 revenue decline expected - need revenue diversification
• Margin pressure: Competition affecting pricing power - differentiation critical
• Cost inflation: Rising operational costs threaten profitability - automation urgent

**Recommendations:**
1. **Immediate:** Increase marketing spend 20% to capitalize on strong CAC/LTV ratio
2. **Short-term:** Implement automation to offset rising operational costs
3. **Medium-term:** Expand sales team to capture market opportunities
4. **Ongoing:** Develop subscription model to increase MRR and revenue predictability

**Financial Health Score: 8.5/10**
Strong fundamentals with clear growth path, manageable risks with proactive mitigation strategies.
        """
        
        email = """
Subject: October Financial Results - Strong Performance & Strategic Recommendations

Leadership Team,

October delivered excellent results across all key metrics. Here's what you need to know:

**Financial Highlights:**
• Revenue: $850K (↑12% MoM, ↑28% YoY)
• Net Profit: $230K (27% margin)
• Cash Flow: +$180K positive
• MRR: $320K recurring revenue base

**What This Means:**
Our unit economics are exceptional - $150 to acquire customers worth $2,400 lifetime value. 
This 16:1 ratio is best-in-class and justifies aggressive growth investment.

**Strategic Recommendations:**
1. Approve 20% marketing budget increase to accelerate customer acquisition
2. Fast-track automation initiatives to control rising operational costs
3. Expand sales team to capture identified market opportunities
4. Invest in financial analytics for better forecasting

**Risk Mitigation:**
We're preparing for seasonal Q1 softness through revenue diversification and subscription 
model expansion. Competitive pressure requires continued product differentiation.

**Action Required:**
Please review detailed recommendations and confirm budget approvals for Q4 initiatives 
by November 30th.

The momentum is strong - let's capitalize on it.

Best regards,
[Finance Team]
        """
        
        tasks = """
1. **CFO - Marketing Budget Increase Approval** (Due: Nov 25)
   - Review 20% marketing spend increase proposal ($120K → $144K)
   - Analyze ROI projections based on current CAC/LTV metrics
   - Approve budget reallocation for Q4 and 2025
   - Timeline: Immediate priority

2. **VP Marketing - Customer Acquisition Acceleration** (Due: Dec 15)
   - Deploy additional $24K monthly marketing budget
   - Focus on highest-performing channels
   - Target 15% increase in new customer acquisition
   - Track and report weekly performance metrics

3. **CTO - Automation Implementation** (Due: Jan 15)
   - Prioritize automation projects to reduce operational costs
   - Target 15-20% efficiency improvement in operations
   - Implement financial tracking and analytics systems
   - Prepare ROI analysis for board presentation

4. **VP Sales - Team Expansion Plan** (Due: Dec 1)
   - Define sales team expansion requirements (roles, headcount)
   - Develop hiring timeline and onboarding process
   - Create sales enablement materials and training program
   - Set Q1 2025 revenue targets for expanded team

5. **Finance Team - Q1 Contingency Planning** (Due: Dec 10)
   - Model Q1 seasonal revenue scenarios
   - Develop cost management strategies
   - Create subscription model expansion roadmap
   - Prepare monthly cash flow monitoring dashboard
        """
        
        return {
            'summary': summary.strip(),
            'insights': insights.strip(),
            'email': email.strip(),
            'tasks': tasks.strip()
        }
    
    def _generic_response(self, content: str) -> Dict[str, str]:
        summary = """
This document contains important business information requiring analysis and action. 
Key themes include strategic planning, operational efficiency, and organizational alignment. 
The content suggests multiple stakeholders and cross-functional coordination needs.

Recommended next steps include stakeholder review, action item assignment, and timeline 
establishment for implementation.
        """
        
        insights = """
**Key Business Implications:**
• Document indicates strategic initiative requiring executive attention
• Cross-functional coordination necessary for successful implementation
• Timeline and resource allocation decisions needed

**Recommendations:**
1. Distribute to relevant stakeholders for review
2. Schedule alignment meeting to discuss next steps
3. Assign clear ownership and accountability
4. Establish success metrics and tracking mechanisms
        """
        
        email = """
Subject: Document Review - Action Required

Team,

I've reviewed the submitted document and identified several action items requiring attention.

**Next Steps:**
1. Please review the attached analysis
2. Provide feedback by end of week
3. We'll schedule a follow-up meeting to align on priorities

Let me know if you have questions or need additional context.

Best regards,
[Business Automation Agent]
        """
        
        tasks = """
1. **Stakeholder Review** (Due: Within 3 days)
   - Distribute document to relevant team members
   - Collect feedback and questions
   - Responsible: Project Lead

2. **Alignment Meeting** (Due: Within 1 week)
   - Schedule cross-functional discussion
   - Review priorities and resource needs
   - Responsible: Department Head

3. **Action Plan Development** (Due: Within 2 weeks)
   - Define specific next steps
   - Assign ownership and timelines
   - Responsible: Project Manager
        """
        
        return {
            'summary': summary.strip(),
            'insights': insights.strip(),
            'email': email.strip(),
            'tasks': tasks.strip()
        }