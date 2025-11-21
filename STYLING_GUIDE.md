# 🎨 Styling Guide

## CSS Location

Your app's custom styling is in:
- **`style.css`** - Main stylesheet with custom colors, gradients, and component styles
- **`app.py`** - Inline HTML/CSS for specific components

## Current Styling Features

### 🎨 Color Scheme

**Primary Colors:**
- Purple Gradient: `#667eea` → `#764ba2`
- Blue: `#1e3a8a` (headers)
- Gray: `#64748b` (text)

**Status Colors:**
- Success: `#10b981` (green)
- Info: `#3b82f6` (blue)
- Warning: `#f59e0b` (orange)
- Error: `#ef4444` (red)

### 📦 Styled Components

1. **Header**
   - Large centered title with gradient
   - Subtitle with italic styling
   - Custom font sizes and colors

2. **Demo Mode Banner**
   - Orange gradient background
   - Centered text with shadow
   - Prominent display

3. **Results Cards**
   - Executive Summary: Blue border, light blue background
   - Business Insights: Orange border, yellow background
   - Generated Email: Purple border, gray background
   - Follow-up Tasks: Green border, light green background

4. **Sidebar**
   - Purple gradient header
   - Feature list with checkmarks
   - Recent documents with expanders

5. **Buttons**
   - Primary: Purple gradient with hover effect
   - Download: Green with hover effect
   - Rounded corners and shadows

6. **File Uploader**
   - Dashed blue border
   - Light blue background
   - Rounded corners

## 🔧 How to Customize

### Change Primary Color

In `style.css`, find and replace:
```css
/* Current purple gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to blue gradient */
background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);

/* Change to green gradient */
background: linear-gradient(135deg, #10b981 0%, #059669 100%);
```

### Change Header Style

In `app.py`, find the header section:
```python
st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='color: #1e3a8a; font-size: 3rem; margin-bottom: 0.5rem;'>
            🤖 AI Business Automation Agent
        </h1>
        ...
    </div>
""", unsafe_allow_html=True)
```

### Add Custom Fonts

Add to `style.css`:
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body {
    font-family: 'Inter', sans-serif;
}
```

### Change Result Card Colors

In `app.py`, find the results section and modify:
```python
# Summary - currently blue
<div style='background-color: #f0f9ff; border-left: 4px solid #3b82f6;'>

# Change to purple
<div style='background-color: #f5f3ff; border-left: 4px solid #8b5cf6;'>
```

## 🎯 Streamlit Config

Additional styling in `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"        # Accent color
backgroundColor = "#FFFFFF"      # Main background
secondaryBackgroundColor = "#F0F2F6"  # Sidebar, cards
textColor = "#262730"           # Text color
font = "sans serif"             # Font family
```

## 📱 Responsive Design

The current CSS includes:
- Flexible layouts
- Responsive padding and margins
- Mobile-friendly components

## 🚀 Quick Style Changes

### Make it More Professional
```css
/* Add to style.css */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1, h2, h3 {
    letter-spacing: -0.5px;
}
```

### Make it More Colorful
```css
/* Add vibrant gradients */
.stButton > button {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}
```

### Make it Darker (Dark Mode)
```css
/* Add to style.css */
.main {
    background-color: #1a1a1a;
    color: #ffffff;
}

.stTabs [data-baseweb="tab-panel"] {
    background-color: #2d2d2d;
}
```

## 🎨 Pre-made Color Schemes

### Professional Blue
```css
--primary: #2563eb;
--secondary: #1e40af;
--accent: #3b82f6;
```

### Modern Purple (Current)
```css
--primary: #667eea;
--secondary: #764ba2;
--accent: #8b5cf6;
```

### Fresh Green
```css
--primary: #10b981;
--secondary: #059669;
--accent: #34d399;
```

### Bold Orange
```css
--primary: #f59e0b;
--secondary: #d97706;
--accent: #fbbf24;
```

## 🔍 Debugging Styles

### View Applied Styles
1. Open app in browser
2. Press F12 (Developer Tools)
3. Click "Elements" tab
4. Inspect any element
5. See applied CSS in "Styles" panel

### Override Streamlit Defaults
Use `!important` for stubborn styles:
```css
.stButton > button {
    background-color: #667eea !important;
}
```

## 📝 Best Practices

1. **Keep it consistent** - Use the same color scheme throughout
2. **Maintain contrast** - Ensure text is readable on backgrounds
3. **Test on different screens** - Check mobile and desktop views
4. **Use semantic colors** - Green for success, red for errors, etc.
5. **Don't overdo it** - Less is more with styling

## 🎬 For Hackathon Demo

Current styling is optimized for:
- ✅ Professional appearance
- ✅ Clear visual hierarchy
- ✅ Easy to read results
- ✅ Impressive first impression
- ✅ Brand consistency

## 🔄 Reload Styles

After changing CSS:
1. Save `style.css` or `app.py`
2. Refresh browser (Ctrl+R or Cmd+R)
3. Or click "Rerun" in Streamlit

If styles don't update:
1. Hard refresh: Ctrl+Shift+R (Cmd+Shift+R on Mac)
2. Clear browser cache
3. Restart Streamlit app

## 📚 Resources

- [Streamlit Theming](https://docs.streamlit.io/library/advanced-features/theming)
- [CSS Gradients](https://cssgradient.io/)
- [Color Palettes](https://coolors.co/)
- [Google Fonts](https://fonts.google.com/)

---

Your app now has professional, polished styling that will impress hackathon judges! 🎨✨