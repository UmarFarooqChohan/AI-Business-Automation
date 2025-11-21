"""
Emergency Database Fix Script
Run this to fix the user_id column issue on Streamlit Cloud
"""

import sqlite3
import os

def fix_database(db_path="auto_ceo.db"):
    """Fix database schema by adding missing user_id column"""
    
    print(f"🔍 Checking database at: {db_path}")
    
    if not os.path.exists(db_path):
        print(f"✅ Database doesn't exist yet. Will be created with correct schema.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if user_id column exists
        cursor.execute("PRAGMA table_info(documents)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print(f"📋 Current columns in documents table: {columns}")
        
        if 'user_id' not in columns:
            print("⚠️  user_id column is missing. Adding it now...")
            cursor.execute("ALTER TABLE documents ADD COLUMN user_id INTEGER")
            conn.commit()
            print("✅ user_id column added successfully!")
        else:
            print("✅ user_id column already exists. No fix needed.")
        
        # Verify the fix
        cursor.execute("PRAGMA table_info(documents)")
        columns = [column[1] for column in cursor.fetchall()]
        print(f"📋 Updated columns: {columns}")
        
    except Exception as e:
        print(f"❌ Error during fix: {str(e)}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    print("🔧 Starting database fix...")
    fix_database()
    print("🎉 Database fix completed!")
