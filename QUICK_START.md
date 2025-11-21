# 🚀 Quick Start Guide - Authentication System

## Run Your App

```bash
streamlit run app.py
```

## First Time Setup

### Option 1: Create an Account (Recommended)
1. Click **"Sign Up"** tab
2. Enter:
   - Username: `myusername` (min 3 chars)
   - Email: `me@example.com`
   - Full Name: `My Name` (optional)
   - Password: `mypassword` (min 6 chars)
   - Confirm Password: `mypassword`
3. Click **"✨ Create Account"**
4. Switch to **"Login"** tab
5. Enter your username and password
6. Click **"🚀 Login"**

### Option 2: Use Guest Mode (Quick Demo)
1. Click **"Guest Mode"** tab
2. Click **"🚀 Continue as Guest"**
3. Start using immediately!

## What You'll See

### After Login/Guest Mode
- Your username in the top-right corner
- Personal dashboard with your stats (if logged in)
- Recent documents (your own if logged in)
- Upload & Analyze tab ready to use
- Logout button to sign out

### Using the App
1. Go to **"Upload & Analyze"** tab
2. Upload a document (PDF, DOCX, TXT, or image)
3. Click **"🚀 Analyze Document"**
4. View results in **"Results"** tab
5. Download reports as needed

## Key Differences

### Logged In Users
- ✅ Documents saved to your account
- ✅ Access history anytime
- ✅ Personal stats tracking
- ✅ Data persists across sessions

### Guest Users
- ✅ Full app functionality
- ✅ No registration needed
- ⚠️ Data not permanently saved to account
- ⚠️ History cleared on logout

## Testing the Authentication

### Test User Creation
```python
# The system will:
# 1. Validate username (min 3 chars)
# 2. Validate email format
# 3. Validate password (min 6 chars)
# 4. Check for duplicates
# 5. Hash password securely
# 6. Create user account
```

### Test Login
```python
# The system will:
# 1. Find user by username or email
# 2. Verify password hash
# 3. Update last login time
# 4. Create session
# 5. Load user dashboard
```

## Troubleshooting

### Can't Create Account?
- Check username is at least 3 characters
- Check password is at least 6 characters
- Make sure email has @ symbol
- Try different username/email if taken

### Can't Login?
- Verify username/email is correct
- Check password (case-sensitive)
- Make sure you created an account first

### Want to Start Fresh?
```bash
# Delete database and restart
del auto_ceo.db
python migrate_database.py
streamlit run app.py
```

## Demo Scenario

### For Hackathon/Presentation
1. **Start**: Open app → Guest Mode
2. **Demo**: Upload sample document → Analyze
3. **Show Results**: Display all analysis tabs
4. **Highlight**: "You can also create an account to save your work!"
5. **Quick Signup**: Show signup process (30 seconds)
6. **Login**: Show personalized dashboard

## File Structure

```
your-project/
├── app.py                 # Main app with authentication
├── auth.py               # Authentication manager
├── database.py           # Database with user support
├── style.css             # Enhanced styling
├── migrate_database.py   # Database migration
├── auto_ceo.db          # SQLite database
├── AUTH_GUIDE.md        # Detailed auth guide
├── FEATURES_SUMMARY.md  # Features overview
└── QUICK_START.md       # This file
```

## Next Steps

1. ✅ Run the app
2. ✅ Test signup/login
3. ✅ Test guest mode
4. ✅ Upload a document
5. ✅ Check user isolation (create 2 accounts)
6. ✅ Verify logout works
7. ✅ Ready for demo! 🎉

## Support

- Check `AUTH_GUIDE.md` for detailed documentation
- Check `FEATURES_SUMMARY.md` for feature overview
- All styling matches your existing theme
- Database automatically migrated

---

**You're all set! Enjoy your authenticated AI Business Automation Agent!** 🚀
