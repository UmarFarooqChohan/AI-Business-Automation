# Quick Deployment Guide - Database Fix

## What Was Fixed
✅ Added automatic database schema migration on app startup
✅ Made all database queries defensive with fallback logic
✅ Added `user_id` column check before every query
✅ No data loss - existing documents are preserved

## Deploy to Streamlit Cloud

### Step 1: Commit and Push Changes
```bash
git add app.py database.py fix_database.py DATABASE_FIX_README.md
git commit -m "Fix: Add automatic database migration for user_id column"
git push origin main
```

### Step 2: Streamlit Cloud Will Auto-Deploy
- Streamlit Cloud will detect the changes
- The app will restart automatically
- On startup, `fix_database_schema()` will run
- The `user_id` column will be added to existing database
- App should work normally

### Step 3: Verify the Fix
1. Go to your Streamlit Cloud app URL
2. Check if the app loads without errors
3. Try logging in as a user
4. Try guest mode
5. Upload a document to test database writes

## If Issues Persist

### Option 1: Delete Database on Streamlit Cloud
If the automatic fix doesn't work, you can force a fresh database:
1. Go to Streamlit Cloud dashboard
2. Click "Manage app"
3. Go to "Settings" → "Secrets"
4. Add a temporary secret to trigger rebuild
5. Or manually delete `auto_ceo.db` if you have access

### Option 2: Run Manual Fix Script
Add this to your app temporarily at the very top of `app.py`:
```python
import subprocess
subprocess.run(["python", "fix_database.py"])
```

## Expected Behavior After Fix

✅ App loads without `OperationalError`
✅ Users can log in and see their documents
✅ Guest users can use the app
✅ New documents are saved with user_id
✅ Old documents (without user_id) are still accessible

## Files Changed
- `app.py` - Added startup database fix
- `database.py` - Added defensive checks and fallbacks
- `fix_database.py` - Manual fix script (optional)
- `DATABASE_FIX_README.md` - Detailed documentation
- `DEPLOY_FIX.md` - This deployment guide
