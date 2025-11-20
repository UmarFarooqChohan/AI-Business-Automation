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
    st.title("🤖 AI Business Automation Agent")
    st.markdown("*Your intelligent assistant for document analysis and business automation*")
    
    # Initialize
    db, processor, agent, error, demo_mode = init_components()
    
    if demo_mode:
        st.info("🎭 **Demo Mode Active** - Using pre-generated AI responses for demonstration purposes")
    
    if error and not demo_mode:
        st.error(f"⚠️ {error}")
        st.info("Please set your OpenAI API key in the environment variable OPENAI_API_KEY")
        return
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Dashboard")
        
        # Recent documents
        recent_docs = db.get_recent_documents(5)
        if recent_docs:
            st.subheader("Recent Documents")
            for doc in recent_docs:
                with st.expander(f"📄 {doc['filename'][:30]}..."):
                    st.write(f"**Date:** {doc['created_at']}")
                    st.write(f"**Summary:** {doc['summary'][:100]}...")
        
        st.markdown("---")
        st.markdown("**Features:**")
        st.markdown("✅ Document Analysis")
        st.markdown("✅ AI Summarization") 
        st.markdown("✅ Email Generation")
        st.markdown("✅ Task Automation")
        st.markdown("✅ Business Insights")
    
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
            st.subheader("📝 Executive Summary")
            st.write(results['summary'])
            
            # Insights
            st.subheader("💡 Business Insights")
            st.write(results['insights'])
            
            # Email
            st.subheader("📧 Generated Email")
            st.code(results['email'], language="text")
            
            # Tasks
            st.subheader("✅ Follow-up Tasks")
            st.write(results['tasks'])
            
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