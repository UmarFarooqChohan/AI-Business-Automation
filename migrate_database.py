"""
Database Migration Script
Adds user_id column to existing documents table
"""

import sqlite3
import os

def migrate_database(db_path="auto_ceo.db"):
    """Add user_id column to documents table if it doesn't exist"""
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} does not exist. No migration needed.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if user_id column exists
        cursor.execute("PRAGMA table_info(documents)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'user_id' not in columns:
            print("Adding user_id column to documents table...")
            cursor.execute("ALTER TABLE documents ADD COLUMN user_id INTEGER")
            conn.commit()
            print("✅ Migration completed successfully!")
        else:
            print("✅ Database already up to date. No migration needed.")
        
        # Create auth tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        conn.commit()
        print("✅ Authentication tables verified/created!")
        
    except Exception as e:
        print(f"❌ Error during migration: {str(e)}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    print("🔄 Starting database migration...")
    migrate_database()
    print("🎉 Migration process completed!")
