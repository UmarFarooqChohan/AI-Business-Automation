import sqlite3
import hashlib
import secrets
from datetime import datetime
from typing import Optional, Dict, Tuple

class AuthManager:
    def __init__(self, db_path: str = "auto_ceo.db"):
        self.db_path = db_path
        self.init_auth_tables()
    
    def init_auth_tables(self):
        """Initialize authentication tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
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

    def hash_password(self, password: str) -> str:
        """Hash password with salt"""
        salt = secrets.token_hex(16)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
        return f"{salt}${pwd_hash.hex()}"
    
    def verify_password(self, password: str, password_hash: str) -> bool:
        """Verify password against hash"""
        try:
            salt, pwd_hash = password_hash.split('$')
            new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
            return new_hash.hex() == pwd_hash
        except:
            return False
    
    def signup(self, username: str, email: str, password: str, full_name: str = "") -> Tuple[bool, str]:
        """Register new user"""
        try:
            if len(username) < 3:
                return False, "Username must be at least 3 characters"
            if len(password) < 6:
                return False, "Password must be at least 6 characters"
            if '@' not in email:
                return False, "Invalid email address"
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT id FROM users WHERE username = ? OR email = ?', (username, email))
            if cursor.fetchone():
                conn.close()
                return False, "Username or email already exists"
            
            password_hash = self.hash_password(password)
            cursor.execute('''
                INSERT INTO users (username, email, password_hash, full_name)
                VALUES (?, ?, ?, ?)
            ''', (username, email, password_hash, full_name))
            
            conn.commit()
            conn.close()
            return True, "Account created successfully!"
        
        except Exception as e:
            return False, f"Error creating account: {str(e)}"
    
    def login(self, username: str, password: str) -> Tuple[bool, Optional[Dict], str]:
        """Login user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, username, email, password_hash, full_name
                FROM users WHERE username = ? OR email = ?
            ''', (username, username))
            
            user = cursor.fetchone()
            
            if not user:
                conn.close()
                return False, None, "Invalid username or password"
            
            if not self.verify_password(password, user[3]):
                conn.close()
                return False, None, "Invalid username or password"
            
            cursor.execute('UPDATE users SET last_login = ? WHERE id = ?', 
                         (datetime.now(), user[0]))
            
            conn.commit()
            conn.close()
            
            user_data = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'full_name': user[4]
            }
            
            return True, user_data, "Login successful!"
        
        except Exception as e:
            return False, None, f"Error logging in: {str(e)}"
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        """Get user by ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, username, email, full_name, created_at
                FROM users WHERE id = ?
            ''', (user_id,))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'full_name': user[3],
                    'created_at': user[4]
                }
            return None
        
        except:
            return None
