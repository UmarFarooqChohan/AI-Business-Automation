import streamlit as st
import os
from datetime import datetime
from document_processor import DocumentProcessor
from ai_agent import AIAgent
from ai_agent_demo import AIAgentDemo
from database import Database
from config import Config

# Page config
st.set_page_config(
    page_title=Config.APP_TITLE,
    page_icon="🤖",
    layout="wide"
)

# Load custom CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass  # CSS file optional

load_css()

# Initialize components
@st.cache_resource
def init_components():
    db = Database()
    processor = DocumentProcessor()
    try:
        agent = AIAgent()
        return db, processor, agent, None, False
    except ValueError as e:
        # Use demo mode if API key issues
        agent_demo = AIAgentDemo()
        return db, processor, agent_demo, None, True

def main():
    # Custom header with styling
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='color: #1e3a8a; font-size: 3rem; margin-bottom: 0.5rem;'>
                🤖 AI Business Automation Agent
            </h1>
            <p style='color: #64748b; font-size: 1.2rem; font-style: italic;'>
                Your intelligent assistant for document analysis and business automation
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Initialize
    db, processor, agent, error, demo_mode = init_components()
    
    if demo_mode:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                        color: white; padding: 1rem; border-radius: 10px; 
                        text-align: center; font-weight: 600; margin: 1rem 0;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
                🎭 <strong>Demo Mode Active</strong> - Using intelligent pre-generated responses based on your document content
            </div>
        """, unsafe_allow_html=True)
    
    if error and not demo_mode:
        st.error(f"⚠️ {error}")
        st.info("Please set your Google API key in the environment variable GOOGLE_API_KEY")
        return
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 10px; margin-bottom: 1rem;'>
                <h2 style='color: white; margin: 0;'>📊 Dashboard</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Recent documents
        recent_docs = db.get_recent_documents(5)
        if recent_docs:
            st.subheader("📁 Recent Documents")
            for doc in recent_docs:
                with st.expander(f"📄 {doc['filename'][:30]}..."):
                    st.write(f"**Date:** {doc['created_at']}")
                    st.write(f"**Summary:** {doc['summary'][:100]}...")
        
        st.markdown("---")
        st.markdown("""
            <div style='background-color: #f8fafc; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #1e3a8a; margin-top: 0;'>✨ Features</h4>
                <ul style='list-style: none; padding-left: 0;'>
                    <li> Document Analysis</li>
                    <li> AI Summarization</li>
                    <li> Email Generation</li>
                    <li> Task Automation</li>
                    <li> Business Insights</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Main content
    tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Results"])
    
    with tab1:
        st.header("Upload Business Document")
        
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'],
            help="Upload PDF, Word, text, or image files"
        )
        
        if uploaded_file is not None:
            # Validate file
            is_valid, message = processor.validate_file(
                uploaded_file.name, 
                uploaded_file.size
            )
            
            if not is_valid:
                st.error(message)
                return
            
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            if st.button("🚀 Analyze Document", type="primary"):
                with st.spinner("🤖 AI is analyzing your document..."):
                    # Extract text
                    file_content = uploaded_file.read()
                    text_content = processor.extract_text(file_content, uploaded_file.name)
                    
                    if not text_content:
                        st.error("Could not extract text from the document")
                        return
                    
                    # AI Analysis
                    results = agent.analyze_document(text_content, uploaded_file.name)
                    
                    # Check if we switched to demo mode due to API issues
                    if hasattr(agent, 'use_demo_fallback') and agent.use_demo_fallback:
                        st.warning("⚠️ API quota exceeded - automatically switched to Demo Mode for this analysis")
                    
                    # Save to database
                    doc_id = db.save_document(
                        uploaded_file.name,
                        text_content,
                        results['summary'],
                        results['insights']
                    )
                    
                    # Save tasks
                    db.save_task(doc_id, "email", results['email'])
                    db.save_task(doc_id, "tasks", results['tasks'])
                    
                    # Store in session state
                    st.session_state['analysis_results'] = results
                    st.session_state['filename'] = uploaded_file.name
                    
                    st.success("✅ Analysis complete!")
    
    with tab2:
        if 'analysis_results' in st.session_state:
            results = st.session_state['analysis_results']
            filename = st.session_state['filename']
            
            st.header(f"📊 Analysis Results: {filename}")
            
            # Summary
            st.markdown("### 📝 Executive Summary")
            st.markdown(f"""
                <div style='background-color: #f0f9ff; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #3b82f6;
                            margin: 1rem 0;'>
                    {results['summary'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            # Insights
            st.markdown("### 💡 Business Insights")
            st.markdown(f"""
                <div style='background-color: #fef3c7; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #f59e0b;
                            margin: 1rem 0;'>
                    {results['insights'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            # Email
            st.markdown("### 📧 Generated Email")
            st.markdown(f"""
                <div style='background-color: #f1f5f9; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #8b5cf6;
                            margin: 1rem 0; font-family: monospace; white-space: pre-wrap;'>
                    {results['email']}
                </div>
            """, unsafe_allow_html=True)
            
            # Tasks
            st.markdown("### ✅ Follow-up Tasks")
            st.markdown(f"""
                <div style='background-color: #d1fae5; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #10b981;
                            margin: 1rem 0;'>
                    {results['tasks'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            # Download options
            st.subheader("💾 Export Results")
            col1, col2 = st.columns(2)
            
            with col1:
                # Create report
                report = f"""
AI BUSINESS AUTOMATION REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Document: {filename}

EXECUTIVE SUMMARY
{results['summary']}

BUSINESS INSIGHTS
{results['insights']}

GENERATED EMAIL
{results['email']}

FOLLOW-UP TASKS
{results['tasks']}
                """
                
                st.download_button(
                    "📄 Download Report",
                    report,
                    file_name=f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            with col2:
                st.download_button(
                    "📧 Download Email",
                    results['email'],
                    file_name=f"generated_email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
        
        else:
            st.info("👆 Upload and analyze a document to see results here")

if __name__ == "__main__":
    main()