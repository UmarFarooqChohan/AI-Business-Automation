"""
Demo setup script for hackathon presentation
Creates sample documents for demonstration
"""

import os
from pathlib import Path

def create_demo_files():
    """Create sample business documents for demo"""
    
    # Create demo folder
    demo_dir = Path("demo_files")
    demo_dir.mkdir(exist_ok=True)
    
    # Sample business proposal
    proposal = """
BUSINESS PROPOSAL: AI AUTOMATION IMPLEMENTATION

Executive Summary:
Our company should implement AI automation to reduce manual tasks by 60% and increase productivity. 
The proposed solution includes document processing, email automation, and intelligent task management.

Key Benefits:
- Cost savings: $50,000 annually
- Time savings: 20 hours per week
- Error reduction: 85% fewer manual errors
- Scalability: Handle 3x more documents

Investment Required:
- Initial setup: $15,000
- Monthly costs: $2,000
- ROI timeline: 6 months

Next Steps:
1. Approve budget by end of month
2. Select implementation partner
3. Begin pilot program in Q1
4. Full rollout by Q2

Risks:
- Integration challenges with legacy systems
- Staff training requirements
- Data security considerations

Recommendation: Proceed with implementation immediately to capture competitive advantage.
    """
    
    # Sample meeting notes
    meeting_notes = """
QUARTERLY BUSINESS REVIEW MEETING NOTES
Date: November 20, 2024
Attendees: CEO, CFO, CTO, VP Sales, VP Marketing

Key Discussion Points:

1. Q3 Performance Review
   - Revenue: $2.3M (15% above target)
   - Customer acquisition: 450 new clients
   - Churn rate: 3.2% (improved from 4.1%)

2. Q4 Priorities
   - Launch new product line
   - Expand to European markets
   - Implement AI automation systems
   - Hire 25 additional staff members

3. Budget Allocation
   - Marketing: $500K increase
   - R&D: $300K for AI initiatives
   - Operations: $200K for automation tools

4. Action Items
   - Marketing team: Prepare European launch strategy (Due: Dec 1)
   - IT team: Evaluate AI automation vendors (Due: Nov 30)
   - HR: Begin recruitment for key positions (Due: Dec 15)
   - Finance: Prepare Q4 budget adjustments (Due: Nov 25)

5. Concerns Raised
   - Supply chain disruptions in Q1
   - Increased competition in core markets
   - Need for better data analytics capabilities

Decision: Approve $1M investment in AI and automation initiatives for 2025.
    """
    
    # Sample financial report
    financial_report = """
MONTHLY FINANCIAL REPORT - OCTOBER 2024

REVENUE ANALYSIS
Total Revenue: $850,000
- Product Sales: $650,000 (76%)
- Service Revenue: $150,000 (18%)
- Licensing: $50,000 (6%)

Month-over-Month Growth: +12%
Year-over-Year Growth: +28%

EXPENSE BREAKDOWN
Total Expenses: $620,000
- Salaries & Benefits: $350,000 (56%)
- Marketing: $120,000 (19%)
- Operations: $80,000 (13%)
- Technology: $70,000 (12%)

Net Profit: $230,000
Profit Margin: 27%

KEY METRICS
- Customer Acquisition Cost: $150
- Customer Lifetime Value: $2,400
- Monthly Recurring Revenue: $320,000
- Cash Flow: +$180,000

RECOMMENDATIONS
1. Increase marketing spend by 20% to capitalize on growth momentum
2. Invest in automation to reduce operational costs
3. Expand sales team to capture market opportunities
4. Implement better financial tracking systems

RISKS & OPPORTUNITIES
Risks:
- Seasonal revenue decline expected in Q1
- Increased competition affecting margins
- Rising operational costs

Opportunities:
- New market segments showing interest
- Partnership opportunities with tech companies
- Potential for subscription model expansion

Next Review: November 30, 2024
    """
    
    # Write demo files
    with open(demo_dir / "business_proposal.txt", "w") as f:
        f.write(proposal)
    
    with open(demo_dir / "meeting_notes.txt", "w") as f:
        f.write(meeting_notes)
    
    with open(demo_dir / "financial_report.txt", "w") as f:
        f.write(financial_report)
    
    print("✅ Demo files created in 'demo_files' folder:")
    print("   - business_proposal.txt")
    print("   - meeting_notes.txt") 
    print("   - financial_report.txt")
    print("\nUse these files to demonstrate the AI automation capabilities!")

if __name__ == "__main__":
    create_demo_files()