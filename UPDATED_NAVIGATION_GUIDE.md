# Updated Navigation Setup Guide

## ✅ What Changed

Your existing **"Main Menu"** is now used as the **BOTTOM navigation bar** (for ISO Standards).

You NO LONGER need to create a separate "Bottom Navigation Menu" - your existing Main Menu items will appear in the bottom nav bar.

---

## 3-Tier Navigation Structure

1. **Top Nav** → New "Top Navigation Menu" (Why Choose Us, Resources, etc.)
2. **Middle Nav** → New "Middle Navigation Menu" (ISO Certification, etc.)
3. **Bottom Nav** → Your existing "Main Menu" (ISO Standards) ✨

---

## Setup Instructions

### Step 1: Create Top Navigation Menu

1. Go to **Admin** → **Snippets** → **Top Navigation Menus**
2. Click **Add Top Navigation Menu**
3. Fill in:
   ```
   Title: Main Top Nav
   Phone Number: 0330 058 5551
   Show Price: ✓ checked
   Price Text: £0.00
   ```
4. Add items:
   - Why Choose Us?
   - Resources
   - What is ISO?
   - About Us
   - Contact
5. **Save**

### Step 2: Create Middle Navigation Menu

1. Go to **Snippets** → **Middle Navigation Menus**
2. Click **Add Middle Navigation Menu**
3. Fill in:
   ```
   Title: Main Middle Nav
   Show Request Quote: ✓ checked
   Request Quote Text: Request a quote
   Request Quote Link: /contact/
   Show Client Portal: ✓ checked
   Client Portal Text: Client Portal
   Client Portal Link: /admin/
   ```
4. Add items:
   - ISO Certification
   - ISO Consultancy
   - ISO Training
5. **Save**

### Step 3: Keep Your Existing Main Menu

✅ **You already have this!**

Your existing **Main Menu** with items like:
- ISO 9001
- ISO 927001
- ISO 90013
- ISO 900133

Will now appear as the **bottom navigation bar**.

### Step 4: Assign Menus in Settings

1. Go to **Settings** → **Site Menu Settings**
2. You'll see THREE fields:
   - **Top Nav Menu**: Select "Main Top Nav" (the one you just created)
   - **Middle Nav Menu**: Select "Main Middle Nav" (the one you just created)
   - **Main Menu**: Select your existing Main Menu (already selected)
3. **Save**

### Step 5: Refresh Browser

**Hard refresh** to clear cache:
- **Mac**: `Cmd + Shift + R`
- **Windows/Linux**: `Ctrl + Shift + R`

---

## What Each Nav Bar Shows

```
┌─────────────────────────────────────────────────────────┐
│ TOP NAV: Why Choose Us | Resources | What is ISO?       │ ← Top Navigation Menu
│          About Us | Contact         📞 0330... | £0.00   │
├─────────────────────────────────────────────────────────┤
│ [LOGO]  ISO Certification | ISO Consultancy | ISO       │ ← Middle Navigation Menu
│         Training    [Request Quote] [Client Portal]     │
├─────────────────────────────────────────────────────────┤
│ ISO 9001 | ISO 14001 | ISO 27001 | ISO 22301 | BS EN... │ ← Main Menu (Bottom)
└─────────────────────────────────────────────────────────┘
```

---

## Summary

✅ **Keep**: Your existing "Main Menu" in Snippets (it's the bottom nav now)
✅ **Create**: Top Navigation Menu (new)
✅ **Create**: Middle Navigation Menu (new)
❌ **Ignore**: Bottom Navigation Menu (not needed)

Your existing menu items are already set up and will display in the bottom nav bar!
