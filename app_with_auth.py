import streamlit as st
import os
from datetime import datetime
from document_processor import DocumentProcessor
from ai_agent import AIAgent
from ai_agent_demo import AIAgentDemo
from database import Database
from config import Config
from auth import AuthManager

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
        pass

load_css()

# Initialize components
@st.cache_resource
def init_components():
    db = Database()
    auth = AuthManager()
    processor = DocumentProcessor()
    try:
        agent = AIAgent()
        return db, auth, processor, agent, None, False
    except ValueError as e:
        agent_demo = AIAgentDemo()
        return db, auth, processor, agent_demo, None, True

def show_auth_page():
    """Display login/signup page"""
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='color: #1e3a8a; font-size: 3.5rem; margin-bottom: 0.5rem;'>
                🤖 AI Business Automation Agent
            </h1>
            <p style='color: #64748b; font-size: 1.3rem; font-style: italic;'>
                Your intelligent assistant for document analysis and business automation
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                        margin: 2rem 0;'>
                <h2 style='color: white; text-align: center; margin-bottom: 1.5rem;'>Welcome! 👋</h2>
            </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["🔐 Login", "📝 Sign Up", "👤 Guest Mode"])
        
        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("login_form"):
                username = st.text_input("Username or Email", placeholder="Enter your username or email")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                submit = st.form_submit_button("🚀 Login", use_container_width=True)
                
                if submit:
                    if username and password:
                        db, auth, _, _, _, _ = init_components()
                        success, user_data, message = auth.login(username, password)
                        
                        if success:
                            st.session_state['authenticated'] = True
                            st.session_state['user'] = user_data
                            st.session_state['is_guest'] = False
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.warning("Please fill in all fields")
        
        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("signup_form"):
                new_username = st.text_input("Username", placeholder="Choose a username (min 3 characters)")
                new_email = st.text_input("Email", placeholder="your.email@example.com")
                new_fullname = st.text_input("Full Name (Optional)", placeholder="Your full name")
                new_password = st.text_input("Password", type="password", placeholder="Choose a password (min 6 characters)")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
                submit = st.form_submit_button("✨ Create Account", use_container_width=True)
                
                if submit:
                    if new_username and new_email and new_password and confirm_password:
                        if new_password != confirm_password:
                            st.error("Passwords do not match!")
                        else:
                            db, auth, _, _, _, _ = init_components()
                            success, message = auth.signup(new_username, new_email, new_password, new_fullname)
                            
                            if success:
                                st.success(message)
                                st.info("Please login with your new account")
                            else:
                                st.error(message)
                    else:
                        st.warning("Please fill in all required fields")
        
        with tab3:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                <div style='background-color: #f0f9ff; padding: 1.5rem; border-radius: 10px; 
                            border-left: 4px solid #3b82f6; margin: 1rem 0;'>
                    <h4 style='color: #1e3a8a; margin-top: 0;'>🎭 Guest Mode</h4>
                    <p style='color: #64748b; margin-bottom: 0;'>
                        Continue without an account. Your data will be temporary and not saved permanently.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("🚀 Continue as Guest", use_container_width=True, type="primary"):
                st.session_state['authenticated'] = True
                st.session_state['is_guest'] = True
                st.session_state['user'] = {'username': 'Guest', 'id': None}
                st.rerun()

def show_main_app():
    """Display main application"""
    db, auth, processor, agent, error, demo_mode = init_components()
    
    # User info in header
    user = st.session_state.get('user', {})
    is_guest = st.session_state.get('is_guest', False)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
            <div style='text-align: center; padding: 1rem 0;'>
                <h1 style='color: #1e3a8a; font-size: 3rem; margin-bottom: 0.5rem;'>
                    🤖 AI Business Automation Agent
                </h1>
                <p style='color: #64748b; font-size: 1.2rem; font-style: italic;'>
                    Your intelligent assistant for document analysis and business automation
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        user_display = f"👤 {user.get('username', 'Guest')}"
        if is_guest:
            user_display += " (Guest)"
        
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white; padding: 0.8rem; border-radius: 10px; text-align: center;
                        font-weight: 600; margin-top: 1rem;'>
                {user_display}
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.clear()
            st.rerun()
    
    if demo_mode:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                        color: white; padding: 1rem; border-radius: 10px; 
                        text-align: center; font-weight: 600; margin: 1rem 0;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
                🎭 <strong>Demo Mode Active</strong> - Using intelligent pre-generated responses
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
        
        # User stats
        user_id = user.get('id') if not is_guest else None
        recent_docs = db.get_recent_documents(5, user_id)
        
        if not is_guest:
            st.markdown(f"""
                <div style='background-color: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'>
                    <h4 style='color: #1e3a8a; margin-top: 0;'>📈 Your Stats</h4>
                    <p style='margin: 0.5rem 0;'><strong>Total Documents:</strong> {len(recent_docs)}</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Recent documents
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
                    <li>📄 Document Analysis</li>
                    <li>🤖 AI Summarization</li>
                    <li>📧 Email Generation</li>
                    <li>✅ Task Automation</li>
                    <li>💡 Business Insights</li>
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
                    file_content = uploaded_file.read()
                    text_content = processor.extract_text(file_content, uploaded_file.name)
                    
                    if not text_content:
                        st.error("Could not extract text from the document")
                        return
                    
                    results = agent.analyze_document(text_content, uploaded_file.name)
                    
                    if hasattr(agent, 'use_demo_fallback') and agent.use_demo_fallback:
                        st.warning("⚠️ API quota exceeded - automatically switched to Demo Mode")
                    
                    user_id = user.get('id') if not is_guest else None
                    doc_id = db.save_document(
                        uploaded_file.name,
                        text_content,
                        results['summary'],
                        results['insights'],
                        user_id
                    )
                    
                    db.save_task(doc_id, "email", results['email'])
                    db.save_task(doc_id, "tasks", results['tasks'])
                    
                    st.session_state['analysis_results'] = results
                    st.session_state['filename'] = uploaded_file.name
                    
                    st.success("✅ Analysis complete!")
    
    with tab2:
        if 'analysis_results' in st.session_state:
            results = st.session_state['analysis_results']
            filename = st.session_state['filename']
            
            st.header(f"📊 Analysis Results: {filename}")
            
            st.markdown("### 📝 Executive Summary")
            st.markdown(f"""
                <div style='background-color: #f0f9ff; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #3b82f6;
                            margin: 1rem 0;'>
                    {results['summary'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 💡 Business Insights")
            st.markdown(f"""
                <div style='background-color: #fef3c7; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #f59e0b;
                            margin: 1rem 0;'>
                    {results['insights'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📧 Generated Email")
            st.markdown(f"""
                <div style='background-color: #f1f5f9; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #8b5cf6;
                            margin: 1rem 0; font-family: monospace; white-space: pre-wrap;'>
                    {results['email']}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### ✅ Follow-up Tasks")
            st.markdown(f"""
                <div style='background-color: #d1fae5; padding: 1.5rem; 
                            border-radius: 10px; border-left: 4px solid #10b981;
                            margin: 1rem 0;'>
                    {results['tasks'].replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            st.subheader("💾 Export Results")
            col1, col2 = st.columns(2)
            
            with col1:
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

def main():
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    # Show appropriate page
    if st.session_state['authenticated']:
        show_main_app()
    else:
        show_auth_page()

if __name__ == "__main__":
    main()
