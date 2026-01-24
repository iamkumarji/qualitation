# Article Management System - User Guide

**Date:** January 24, 2026
**Status:** ✅ Fully Implemented and Operational

---

## Overview

The Qualitation website now has a complete Article Management System integrated into Wagtail CMS. You can create, edit, and manage articles directly from the admin panel without writing any code!

---

## Key Features

### Automatic Article Display
- ✅ Articles automatically appear on the Resources page (http://localhost:8000/resources/)
- ✅ Sorted by publication date (newest first)
- ✅ Beautiful gradient card design
- ✅ Automatic article counter badge
- ✅ Responsive grid layout

### Customizable for Each Article
- **Title**: Article headline
- **Date**: Publication date (automatically sorted)
- **Intro/Summary**: Brief description (max 500 characters) - shows on article cards
- **Body**: Full article content (rich text editor)
- **Author**: Author name (defaults to "Qualitation Team")
- **Featured Image**: Optional header image for articles
- **Card Gradient Colors**: Customize the gradient colors for each article card

### Professional Design
- 🎨 Customizable gradient colors for each article card
- 📱 Fully responsive design
- ✨ Hover animations and effects
- 💬 Social sharing buttons (Twitter, LinkedIn)
- 📰 Related articles section
- 🎯 Call-to-action sections

---

## How to Create a New Article

### Step 1: Access Wagtail Admin

1. Open your browser and go to: **http://localhost:8000/admin/**
2. Login with your admin credentials

### Step 2: Navigate to Resources

1. Click on **"Pages"** in the left sidebar
2. Find and click on **"Resources"** page
3. Click the **"Add child page"** button
4. Select **"Article"** from the page types

### Step 3: Fill in Article Details

**Required Fields:**
- **Title**: Your article title (e.g., "Why ISO 9001 Matters for Small Businesses")
- **Published date**: Select the publication date
- **Introduction/Summary**: Write a brief summary (shows on article cards, max 500 characters)
- **Body**: Write your full article content using the rich text editor

**Optional Fields:**
- **Author**: Author name (defaults to "Qualitation Team")
- **Featured image**: Upload a header image for the article
- **Card Appearance**:
  - **Card gradient start**: Starting color for the card (e.g., `#667eea`)
  - **Card gradient end**: Ending color for the card (e.g., `#764ba2`)

### Step 4: Publish

1. Click **"Save draft"** to save without publishing
2. Or click **"Publish"** to make it live immediately
3. The article will automatically appear on the Resources page!

---

## URL Structure

- **Resources Page**: `http://localhost:8000/resources/`
- **Individual Articles**: `http://localhost:8000/resources/[article-slug]/`

Example:
- `http://localhost:8000/resources/dont-use-templates-to-achieve-an-iso-standard/`
- `http://localhost:8000/resources/automation-is-the-future-for-iso-standards/`

---

## Current Articles

The system has been set up with 2 existing articles:

| # | Title | Date | URL |
|---|-------|------|-----|
| 1 | Don't use templates to achieve an ISO Standard | Oct 27, 2020 | `/resources/dont-use-templates-to-achieve-an-iso-standard/` |
| 2 | Automation is the future for ISO Standards! | Oct 24, 2019 | `/resources/automation-is-the-future-for-iso-standards/` |

---

## Customizing Article Card Colors

Each article can have unique gradient colors for its card on the Resources page. Here are some suggested color combinations:

### Professional Blues
- Start: `#667eea` End: `#764ba2` (Purple-Blue)
- Start: `#4facfe` End: `#00f2fe` (Cyan-Blue)
- Start: `#43e97b` End: `#38f9d7` (Green-Cyan)

### Warm Tones
- Start: `#fa709a` End: `#fee140` (Pink-Yellow)
- Start: `#f093fb` End: `#f5576c` (Pink-Red)
- Start: `#ffecd2` End: `#fcb69f` (Peach)

### Cool Tones
- Start: `#a8edea` End: `#fed6e3` (Mint-Pink)
- Start: `#c471f5` End: `#fa71cd` (Purple-Pink)
- Start: `#f5576c` End: `#feda75` (Red-Yellow)

You can use online tools like [https://cssgradient.io/](https://cssgradient.io/) to create custom gradients and copy the hex codes.

---

## Managing Existing Articles

### Edit an Article
1. Go to **Admin → Pages → Resources**
2. Click on the article you want to edit
3. Make your changes
4. Click **"Publish"** to update

### Delete an Article
1. Go to **Admin → Pages → Resources**
2. Click on the article you want to delete
3. Click **"More" → "Delete"**
4. Confirm deletion

### Unpublish an Article (Hide Temporarily)
1. Go to **Admin → Pages → Resources**
2. Click on the article
3. Click **"More" → "Unpublish"**
4. The article will be hidden from the site but not deleted

---

## Resources Page Customization

The Resources page itself can be customized:

1. Go to **Admin → Pages → Resources**
2. Click **"Edit"**
3. You can modify:
   - **Hero Section**: Title, subtitle, show/hide
   - **Introduction**: Optional intro text above articles
   - **Call-to-Action Section**: Title, text, button text/link, show/hide

---

## Technical Details

### Models Created
1. **ArticlePage**: Individual article page model
   - Fields: title, date, intro, body, author, featured_image, card_gradient_start, card_gradient_end
   - Parent: ArticleIndexPage or HomePage
   - Template: `home/templates/home/article_page.html`

2. **ArticleIndexPage**: Index/listing page for articles
   - Automatically queries and displays all child ArticlePage instances
   - Sorted by date (newest first)
   - Includes hero and CTA sections
   - Template: `home/templates/home/article_index_page.html`

### Templates
- **article_index_page.html**: Displays all articles in a beautiful grid
- **article_page.html**: Individual article display with social sharing

### Migrations
- `0019_articleindexpage_articlepage.py`: Created Article models
- `0020_alter_articleindexpage_cta_button_link.py`: Fixed CTA link field

---

## Features Included

### Article Index Page (Resources)
- 🎨 Beautiful gradient hero section with floating animations
- 📊 Dynamic article counter badge
- 🗂️ Automatic grid layout of article cards
- 🎯 Configurable call-to-action section
- 📱 Fully responsive design

### Individual Article Pages
- 📅 Publication date and author display
- 🖼️ Optional featured image
- 📝 Rich text content with proper formatting
- 🔗 Social sharing buttons (Twitter, LinkedIn)
- 📰 Related articles section (shows 3 most recent other articles)
- 💬 Call-to-action for contact

### Article Cards
- 🌈 Customizable gradient headers
- 📅 Publication date badge
- 📖 Article summary preview
- ➡️ Smooth hover animations
- 🎨 Unique colors for each article

---

## Best Practices

### Writing Articles

1. **Title**: Keep it clear and descriptive (50-70 characters ideal)
2. **Intro**: Write a compelling summary that encourages clicks (250-400 characters)
3. **Body**: Use headings (H2, H3) to break up content
4. **Length**: Aim for 800-2000 words for good SEO
5. **Images**: Use featured images for better engagement
6. **Date**: Use the actual publication date (articles sort by this)

### SEO Tips

- Use descriptive, keyword-rich titles
- Write clear meta descriptions (intro field)
- Use proper heading hierarchy (H2 → H3 → H4)
- Include internal links to other pages
- Add relevant images with alt text

### Color Selection

- Choose colors that reflect the article topic
- Use contrast for readability (light start, darker end or vice versa)
- Maintain brand consistency (blues, purples for professional topics)
- Use warmer colors for success stories or positive news
- Keep it professional (avoid very bright or neon colors)

---

## Troubleshooting

### Article not showing on Resources page
- Check if the article is published (not just saved as draft)
- Verify the article is a child of the Resources page
- Clear browser cache and refresh

### Article URL not working
- Articles are accessed via: `/resources/[slug]/`
- Check the slug in admin (Pages → Article → Promote tab)
- Slugs are auto-generated from the title

### Gradient colors not showing
- Ensure you've entered valid hex colors (e.g., `#667eea`)
- Include the `#` symbol before the color code
- Use 6-character hex codes (not 3-character shorthand)

---

## Future Enhancements (Optional)

You can further enhance the article system by:

- Adding categories/tags for article filtering
- Implementing search functionality
- Adding comment system
- Including article reading time estimates
- Adding pagination for large numbers of articles
- Implementing article view counters
- Adding RSS feed for articles
- Creating featured article promotion
- Adding article series/collections

---

## Summary

✅ **Complete article management system implemented**
✅ **2 articles migrated and published**
✅ **Fully automated - articles appear automatically on Resources page**
✅ **Admin-friendly - no coding required**
✅ **Beautiful, professional design**
✅ **Customizable colors for each article**
✅ **Responsive and mobile-friendly**

**Admin URL**: http://localhost:8000/admin/
**Resources Page**: http://localhost:8000/resources/

You can now create unlimited articles through the admin panel!

---

*This system was created on January 24, 2026*
