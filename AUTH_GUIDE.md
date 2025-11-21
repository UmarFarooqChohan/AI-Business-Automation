# 🔐 Authentication System Guide

## Overview
Your AI Business Automation Agent now includes a complete authentication system with user accounts and guest mode!

## Features

### 🔑 User Authentication
- **Sign Up**: Create a new account with username, email, and password
- **Login**: Access your personal workspace with your credentials
- **Secure**: Passwords are hashed using PBKDF2 with SHA-256
- **User Isolation**: Each user's documents are kept separate

### 👤 Guest Mode
- **No Registration Required**: Use the app without creating an account
- **Quick Access**: Perfect for trying out the features
- **Temporary Data**: Guest data is stored but not permanently associated with a user

### 📊 User Dashboard
- **Personal Stats**: View your document count and activity
- **Recent Documents**: Quick access to your last 5 documents
- **User Profile**: See your username displayed in the header

## How to Use

### For New Users
1. Open the app
2. Click on the **"Sign Up"** tab
3. Fill in:
   - Username (minimum 3 characters)
   - Email address
   - Full Name (optional)
   - Password (minimum 6 characters)
   - Confirm Password
4. Click **"Create Account"**
5. Switch to **"Login"** tab and sign in

### For Existing Users
1. Open the app
2. On the **"Login"** tab, enter:
   - Your username or email
   - Your password
3. Click **"Login"**

### For Guest Users
1. Open the app
2. Click on the **"Guest Mode"** tab
3. Click **"Continue as Guest"**
4. Start using the app immediately!

## Security Features

- ✅ Password hashing with salt
- ✅ Secure password verification
- ✅ User data isolation
- ✅ Session management
- ✅ Input validation

## Database Schema

### Users Table
- `id`: Unique user identifier
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Securely hashed password
- `full_name`: Optional full name
- `created_at`: Account creation timestamp
- `last_login`: Last login timestamp

### Documents Table (Updated)
- `user_id`: Links document to user (NULL for guests)
- All existing fields remain the same

## Technical Details

### Files Added/Modified
1. **auth.py** - New authentication manager
2. **app.py** - Updated with authentication flow
3. **database.py** - Modified to support user-specific data
4. **style.css** - Enhanced with authentication page styles

### Password Security
- Uses PBKDF2-HMAC-SHA256
- 100,000 iterations
- Random 16-byte salt per password
- Format: `salt$hash`

## Logout
Click the **"Logout"** button in the top-right corner to sign out and return to the login page.

## Data Privacy
- Each user can only see their own documents
- Guest data is isolated from user accounts
- No cross-user data access

## Troubleshooting

### "Username or email already exists"
- Try a different username or email
- Make sure you haven't already registered

### "Invalid username or password"
- Check your credentials
- Username/email and password are case-sensitive

### "Password must be at least 6 characters"
- Use a longer password for better security

## Future Enhancements
- Password reset functionality
- Email verification
- Profile editing
- Two-factor authentication
- Social login options

---

Enjoy your secure AI Business Automation Agent! 🚀
