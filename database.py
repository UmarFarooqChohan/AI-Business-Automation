import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional

class Database:
    def __init__(self, db_path: str = "auto_ceo.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Documents table with user_id
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                filename TEXT NOT NULL,
                content TEXT,
                summary TEXT,
                insights TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Check if user_id column exists, add it if not (migration)
        cursor.execute("PRAGMA table_info(documents)")
        columns = [column[1] for column in cursor.fetchall()]
        if 'user_id' not in columns:
            try:
                cursor.execute("ALTER TABLE documents ADD COLUMN user_id INTEGER")
                conn.commit()
            except sqlite3.OperationalError as e:
                # If we can't add the column, we need to recreate the table
                print(f"Warning: Could not add user_id column: {e}")
                pass
        
        # Tasks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id INTEGER,
                task_type TEXT,
                content TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (document_id) REFERENCES documents (id)
            )
        ''')
        
        # Users table for authentication
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
        conn.close()
    
    def check_user_id_column_exists(self) -> bool:
        """Check if user_id column exists in documents table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(documents)")
        columns = [column[1] for column in cursor.fetchall()]
        conn.close()
        return 'user_id' in columns
    
    def save_document(self, filename: str, content: str, summary: str, insights: str, user_id: Optional[int] = None) -> int:
        """Save processed document"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        has_user_id = self.check_user_id_column_exists()
        
        try:
            if has_user_id:
                cursor.execute('''
                    INSERT INTO documents (user_id, filename, content, summary, insights)
                    VALUES (?, ?, ?, ?, ?)
                ''', (user_id, filename, content, summary, insights))
            else:
                cursor.execute('''
                    INSERT INTO documents (filename, content, summary, insights)
                    VALUES (?, ?, ?, ?)
                ''', (filename, content, summary, insights))
        except sqlite3.OperationalError:
            # Fallback if user_id column doesn't exist
            cursor.execute('''
                INSERT INTO documents (filename, content, summary, insights)
                VALUES (?, ?, ?, ?)
            ''', (filename, content, summary, insights))
        
        doc_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return doc_id
    
    def save_task(self, document_id: int, task_type: str, content: str):
        """Save generated task"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tasks (document_id, task_type, content)
            VALUES (?, ?, ?)
        ''', (document_id, task_type, content))
        
        conn.commit()
        conn.close()
    
    def get_recent_documents(self, limit: int = 10, user_id: Optional[int] = None) -> List[Dict]:
        """Get recent documents for a specific user or all if guest"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if user_id column exists
        has_user_id = self.check_user_id_column_exists()
        
        try:
            if has_user_id and user_id is not None:
                cursor.execute('''
                    SELECT id, filename, summary, created_at
                    FROM documents
                    WHERE user_id = ?
                    ORDER BY created_at DESC
                    LIMIT ?
                ''', (user_id, limit))
            elif has_user_id and user_id is None:
                cursor.execute('''
                    SELECT id, filename, summary, created_at
                    FROM documents
                    WHERE user_id IS NULL
                    ORDER BY created_at DESC
                    LIMIT ?
                ''', (limit,))
            else:
                # Fallback if user_id column doesn't exist
                cursor.execute('''
                    SELECT id, filename, summary, created_at
                    FROM documents
                    ORDER BY created_at DESC
                    LIMIT ?
                ''', (limit,))
            
            results = cursor.fetchall()
        except sqlite3.OperationalError:
            # Final fallback
            cursor.execute('''
                SELECT id, filename, summary, created_at
                FROM documents
                ORDER BY created_at DESC
                LIMIT ?
            ''', (limit,))
            results = cursor.fetchall()
        
        conn.close()
        
        return [
            {
                'id': row[0],
                'filename': row[1],
                'summary': row[2],
                'created_at': row[3]
            }
            for row in results
        ]