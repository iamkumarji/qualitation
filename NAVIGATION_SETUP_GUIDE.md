# Navigation Setup Guide

## Setting Up the 3-Tier Navigation System

### Step 1: Create Top Navigation Menu

1. Go to Wagtail Admin (http://localhost:8000/admin/)
2. Navigate to **Snippets** → **Top Navigation Menus**
3. Click **Add Top Navigation Menu**
4. Fill in:
   - **Title**: Main Top Nav
   - **Phone Number**: 0330 058 5551 (or your number)
   - **Show Price**: ✓ (checked)
   - **Price Text**: £0.00

5. Add Top Nav Items (click "Add Top Nav Item"):
   - Why Choose Us?
   - Resources (with dropdown arrow if needed)
   - What is ISO?
   - About Us
   - Contact

6. Save

### Step 2: Create Middle Navigation Menu

1. Navigate to **Snippets** → **Middle Navigation Menus**
2. Click **Add Middle Navigation Menu**
3. Fill in:
   - **Title**: Main Middle Nav
   - **Show Request Quote**: ✓ (checked)
   - **Request Quote Text**: Request a quote
   - **Request Quote Link**: /contact/ (or your link)
   - **Show Client Portal**: ✓ (checked)
   - **Client Portal Text**: Client Portal
   - **Client Portal Link**: /admin/

4. Add Middle Nav Items:
   - ISO Certification
   - ISO Consultancy
   - ISO Training

5. Save

### Step 3: Create Bottom Navigation Menu

1. Navigate to **Snippets** → **Bottom Navigation Menus**
2. Click **Add Bottom Navigation Menu**
3. Fill in:
   - **Title**: ISO Standards Nav

4. Add Bottom Nav Items:
   - ISO 9001 (with dropdown if needed)
   - ISO 14001
   - ISO 27001
   - ISO 22301
   - ISO 17100
   - BS EN 15713

5. Save

### Step 4: Assign Menus in Site Settings

1. Go to **Settings** → **Site Menu Settings**
2. Assign the menus you just created:
   - **Top Nav Menu**: Select "Main Top Nav"
   - **Middle Nav Menu**: Select "Main Middle Nav"
   - **Bottom Nav Menu**: Select "ISO Standards Nav"
3. Save

### Step 5: Hard Refresh Browser

- **Windows/Linux**: Ctrl + Shift + R
- **Mac**: Cmd + Shift + R

Your navigation should now display properly with all three tiers!

## Troubleshooting

If navigation still looks unstyled:

1. **Clear browser cache completely**
2. **Restart Django dev server**:
   ```bash
   # Stop server (Ctrl+C)
   # Then restart:
   python manage.py runserver
   ```
3. **Check browser console** (F12) for any CSS loading errors
