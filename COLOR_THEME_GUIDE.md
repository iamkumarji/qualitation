# Color Theme Configuration Guide

## How to Change Navigation Bar Colors

The navigation bars now use the **Color Theme Settings** from your admin panel.

### Step 1: Access Color Theme Settings

1. Go to **Admin Panel** → **Settings** → **Color Theme Settings**

### Step 2: Configure Navbar Colors

The navigation bars use these color settings:

#### Navbar Colors Section:
- **Navbar Background** → Background color for ALL navigation bars (top, middle, bottom)
- **Navbar Text Color** → Color of text and links in navigation
- **Navbar Hover Color** → Color when you hover over links
- **Navbar Active Color** → Color for active/current page links

#### Button Colors Section:
- **Primary Button BG** → "Client Portal" button background
- **Primary Button Text** → "Client Portal" button text
- **Primary Button Hover** → "Client Portal" button hover color
- **Secondary Button BG** → "Request a quote" button background
- **Secondary Button Text** → "Request a quote" button text
- **Secondary Button Hover** → "Request a quote" button hover color

#### Background & Text Colors:
- **Border Color** → Borders between navigation items

### Step 3: Example Configuration

For the QSL style shown in your image:

```
Navbar Colors:
- Navbar Background: #ffffff (white)
- Navbar Text Color: #333333 (dark gray)
- Navbar Hover Color: #3B3885 (blue)
- Navbar Active Color: #3B3885 (blue)

Button Colors:
- Primary Button BG: #3B3885 (blue)
- Primary Button Text: #ffffff (white)
- Primary Button Hover: #2E2B6B (darker blue)
- Secondary Button BG: #f97316 (orange)
- Secondary Button Text: #ffffff (white)
- Secondary Button Hover: #ea580c (darker orange)

Background & Text:
- Border Color: #e0e0e0 (light gray)
```

### Step 4: Apply Changes

1. **Save** your Color Theme Settings
2. **Hard refresh** your browser:
   - Mac: `Cmd + Shift + R`
   - Windows: `Ctrl + Shift + R`

### Color Picker Tips

- Click on the color field to open a color picker
- Or enter hex codes directly (e.g., #3B3885)
- The changes apply to all navigation bars automatically

### What Changes with Each Setting

| Setting | Affects |
|---------|---------|
| Navbar Background | Background of all 3 nav bars |
| Navbar Text Color | All link text, logo text, phone number |
| Navbar Hover Color | Links when you hover over them |
| Border Color | Lines between nav items in bottom bar |
| Primary Color | Price badge, accent elements |

---

## Quick Fix for White Navigation

If your navigation bars look all white:

1. Go to **Settings** → **Color Theme Settings**
2. Make sure **Navbar Background** is NOT white (#ffffff) or leave it different from body background
3. Make sure **Navbar Text Color** has good contrast with background
4. Save and hard refresh browser

---

Now your navigation bars will use colors from the admin panel instead of hardcoded values!
