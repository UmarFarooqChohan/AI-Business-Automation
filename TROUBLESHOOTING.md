# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### ❌ "Module not found" errors

**Problem:** Missing Python packages

**Solution:**
```bash
pip install -r requirements.txt
```

If that fails, try:
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

---

### ❌ OpenAI API quota exceeded

**Problem:** API key has no credits or exceeded quota

**Solution:** 
✅ **App automatically switches to Demo Mode!**

You'll see: "🎭 Demo Mode Active" banner

Demo Mode provides high-quality pre-generated responses - perfect for hackathon presentations!

---

### ❌ Streamlit won't start

**Problem:** Port 8501 already in use

**Solution:**
```bash
# Kill existing Streamlit process
taskkill /F /IM streamlit.exe

# Or use different port
streamlit run app.py --server.port 8502
```

---

### ❌ OCR not working (images)

**Problem:** Tesseract not installed

**Solution:**
1. Download Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
2. Install it
3. Add to PATH or set in code:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

**For Demo:** Use PDF or text files instead - they work without Tesseract!

---

### ❌ Database errors

**Problem:** Corrupted database file

**Solution:**
```bash
# Delete and recreate database
del auto_ceo.db
python -c "from database import Database; Database()"
```

---

### ❌ Slow performance

**Problem:** Large documents taking too long

**Solution:**
- Demo mode is instant (no API calls)
- For live mode: Use GPT-3.5-turbo instead of GPT-4
- Limit document size to first 2000 characters (already implemented)

---

### ❌ App crashes on file upload

**Problem:** File too large or unsupported format

**Solution:**
- Check file size < 10MB
- Supported formats: PDF, DOCX, TXT, PNG, JPG, JPEG
- Use demo files for guaranteed compatibility

---

### ❌ Demo mode not activating

**Problem:** App still trying to use API

**Solution:**
1. Remove or rename `.env` file temporarily
2. Restart app
3. Demo mode will activate automatically

---

## 🎭 Demo Mode Advantages

If you encounter ANY API issues during hackathon:

✅ **Instant responses** - No API latency
✅ **No costs** - Zero API charges
✅ **Consistent quality** - Same results every time
✅ **Offline capable** - No internet needed
✅ **Professional output** - Impresses judges

Demo mode is actually BETTER for presentations!

---

## 🚀 Quick Fixes

### Reset Everything
```bash
# Stop app
Ctrl+C

# Clean up
del auto_ceo.db
del .env

# Reinstall
pip install -r requirements.txt

# Restart
streamlit run app.py
```

### Fresh Start
```bash
# Create new virtual environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📞 During Hackathon Presentation

### If something breaks:

1. **Stay calm** - Judges understand tech demos can glitch
2. **Switch to backup** - Have screenshots or video ready
3. **Explain the concept** - Your idea matters more than perfect execution
4. **Use demo files** - They're tested and guaranteed to work
5. **Highlight demo mode** - "This is actually better for demo - instant results!"

### Emergency Backup Plan:

1. Take screenshots of successful analysis results NOW
2. Save them in a `screenshots` folder
3. If app fails, show screenshots and explain the flow
4. Judges care about your solution, not perfect execution

---

## ✅ Pre-Presentation Checklist

Run this 30 minutes before presenting:

```bash
# Test the app
streamlit run app.py

# Upload each demo file
# - business_proposal.txt
# - meeting_notes.txt  
# - financial_report.txt

# Verify all features work:
# - Summary generation ✓
# - Insights generation ✓
# - Email generation ✓
# - Task generation ✓
# - Download reports ✓
```

If everything works → Great!
If anything fails → Demo mode has your back!

---

## 💡 Pro Tips

1. **Demo mode is your friend** - Don't fight it, embrace it
2. **Test before presenting** - Run through demo 2-3 times
3. **Have backup files** - Keep demo files on desktop too
4. **Close other apps** - Free up system resources
5. **Restart if needed** - Fresh start often fixes issues

---

## 🎯 Remember

The judges are evaluating:
- Your idea and innovation ⭐
- Business value and impact ⭐
- Technical implementation ⭐
- Presentation quality ⭐

A small technical glitch won't hurt if you handle it professionally!

**You've got this! 🚀**