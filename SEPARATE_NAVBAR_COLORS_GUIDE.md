# Separate Navigation Bar Colors Guide

## 🎨 Now Each Navigation Bar Can Have Different Colors!

You can now customize the **Top**, **Middle**, and **Bottom** navigation bars with completely different color schemes.

---

## How It Works

### Go to: Admin → Settings → Color Theme Settings

You'll now see these sections:

1. **Navbar Colors (Global Defaults)** - Fallback colors if specific nav colors aren't set
2. **Top Navigation Bar Colors** ⭐ NEW!
3. **Middle Navigation Bar Colors** ⭐ NEW!
4. **Bottom Navigation Bar Colors** ⭐ NEW!

---

## Example Configuration

### For a QSL-Style Layout:

#### **Top Navigation Bar** (Why Choose Us, Resources, etc.)
```
Background: #f5f5f5 (light gray)
Text Color: #333333 (dark gray)
Hover Color: #3B3885 (purple-blue)
```

#### **Middle Navigation Bar** (Logo + ISO Certification, etc.)
```
Background: #ffffff (white)
Text Color: #333333 (dark gray)
Hover Color: #0066cc (blue)
```

#### **Bottom Navigation Bar** (ISO Standards)
```
Background: #f8f9fa (very light gray)
Text Color: #555555 (medium gray)
Hover Color: #28a745 (green)
```

---

## Color Fields Explained

### Each Navigation Bar Has 3 Color Options:

| Field | What It Controls |
|-------|------------------|
| **Background** | Background color of the navbar |
| **Text Color** | Color of links and text |
| **Hover Color** | Color when you hover over links |

### How Fallback Works:

If you **don't set** a specific nav bar color, it uses the **Global Default** from "Navbar Colors (Global Defaults)".

**Example:**
- Top Nav Background = `#f5f5f5` (set)
- Middle Nav Background = `(empty)` → Uses Global Default `#ffffff`
- Bottom Nav Background = `#f8f9fa` (set)

---

## Step-by-Step Setup

### 1. Access Color Settings
```
Admin Panel → Settings → Color Theme Settings
```

### 2. Set Global Defaults (Optional)
Scroll to **"Navbar Colors (Global Defaults)"**:
- These apply to ALL nav bars if specific ones aren't set
- Good for quick setup

### 3. Customize Individual Nav Bars
Scroll to each section:

**Top Navigation Bar Colors:**
- Set background, text, and hover colors
- Leave blank to use global defaults

**Middle Navigation Bar Colors:**
- Set background, text, and hover colors
- This is your main nav with the logo

**Bottom Navigation Bar Colors:**
- Set background, text, and hover colors
- This shows your ISO standards

### 4. Save and Refresh
1. Click **Save**
2. **Hard refresh** browser:
   - Mac: `Cmd + Shift + R`
   - Windows: `Ctrl + Shift + R`

---

## Visual Example

```
┌─────────────────────────────────────────────────────┐
│ TOP NAV (Light Gray Background)                     │ ← Top Nav Colors
│ Why Choose Us | Resources | Contact   📞 0330...    │
├─────────────────────────────────────────────────────┤
│ [LOGO] ISO Certification | ISO Consultancy          │ ← Middle Nav Colors
│        (White Background)    [Buttons]              │
├─────────────────────────────────────────────────────┤
│ ISO 9001 | ISO 14001 | ISO 27001 | BS EN 15713      │ ← Bottom Nav Colors
│ (Very Light Gray Background)                        │
└─────────────────────────────────────────────────────┘
```

---

## Quick Color Suggestions

### Professional Look:
```
Top:    BG=#f0f0f0, Text=#444, Hover=#0066cc
Middle: BG=#ffffff, Text=#333, Hover=#0066cc
Bottom: BG=#fafafa, Text=#555, Hover=#0066cc
```

### Modern Dark Accent:
```
Top:    BG=#2c3e50, Text=#ecf0f1, Hover=#3498db
Middle: BG=#ffffff, Text=#2c3e50, Hover=#e74c3c
Bottom: BG=#34495e, Text=#ecf0f1, Hover=#1abc9c
```

### Minimalist:
```
Top:    BG=#ffffff, Text=#666, Hover=#000
Middle: BG=#ffffff, Text=#333, Hover=#000
Bottom: BG=#f9f9f9, Text=#666, Hover=#000
```

---

## What Affects What?

### Top Nav Colors Affect:
- ✓ Top navigation background
- ✓ Menu items (Why Choose Us, Resources, etc.)
- ✓ Phone number link
- ✓ Price badge (uses primary color)

### Middle Nav Colors Affect:
- ✓ Middle navigation background
- ✓ Logo text color
- ✓ Menu items (ISO Certification, etc.)
- ✓ Mobile menu toggle icon

### Bottom Nav Colors Affect:
- ✓ Bottom navigation background
- ✓ ISO standard links
- ✓ Border colors between items

---

## Tips

1. **Contrast is Key**: Make sure text color contrasts well with background
2. **Consistency**: Use similar hover colors for a cohesive look
3. **Test on Mobile**: Colors look different on different screens
4. **Use Hex Codes**: Always use `#` format (e.g., `#0066cc`)

---

## Troubleshooting

**Q: Colors aren't changing?**
- Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R)
- Make sure you clicked Save
- Check you're editing the right setting

**Q: Want all navs the same color?**
- Just set the "Navbar Colors (Global Defaults)"
- Leave specific nav colors blank

**Q: Want to reset to defaults?**
- Clear the specific nav color fields
- They'll use global defaults

---

Now you have full control over each navigation bar's appearance! 🎨
