# Developer Setup Guide

> **Note:** This guide is for developers who want to fork and customize this plugin. If you just want to use the plugin, simply install it as a Recipe from [TRMNL Plugins](https://usetrmnl.com/plugins) - no setup required! See the [README](../README.md) for installation instructions.

Follow these steps to fork and customize your Max Payne Quotes plugin.

## ✅ Pre-requisites

- [ ] GitHub account
- [ ] TRMNL account with Developer Edition
- [ ] Git installed on your computer

## 📝 Setup Steps

### 1. Repository Setup

- [ ] Fork or clone this repository
- [ ] Navigate to the project directory

```bash
cd trmnl-max-payne-quotes-plugin
```

### 2. Update Configuration Files

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username in:

- [ ] `settings.yml` (line 7)
- [ ] `index.html` (line 79)

Also update:
- [ ] `settings.yml` - Replace `YOUR_EMAIL@example.com` with your email (line 14)

**Quick Find & Replace:**
```bash
# macOS/Linux
find . -type f \( -name "*.yml" -o -name "*.html" \) -exec sed -i '' 's/YOUR_GITHUB_USERNAME/your-actual-username/g' {} +

# Or manually with your editor's find & replace feature
```

> **Note:** Template files (`templates/*.liquid`) and data files (`quotes.json`, `api/random-quote.json`) no longer require username updates — poster images are embedded directly in `templates/shared.liquid`.

### 3. Generate Random Quote

Run the Python script to generate a random quote for testing:

```bash
python3 generate_random_quote.py
```

Or list all quotes:
```bash
python3 generate_random_quote.py --list
```

### 4. Add Images (Optional but Recommended)

- [ ] Add game poster images to `assets/poster/`
  - `max-payne-1.jpg`
  - `max-payne-2.jpg`
  - `max-payne-3.jpg`
- [ ] Add plugin icon to `assets/icon.png`

See [assets/README.md](assets/README.md) for image guidelines.

### 5. Commit and Push

```bash
git add .
git commit -m "Configure Max Payne Quotes plugin"
git push origin main
```

### 6. Enable GitHub Pages

1. [ ] Go to your repository on GitHub
2. [ ] Navigate to **Settings** → **Pages**
3. [ ] Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main** / **(root)**
4. [ ] Click **Save**
5. [ ] Wait 2-5 minutes for deployment
6. [ ] Visit `https://your-username.github.io/trmnl-max-payne-quotes-plugin/`

### 7. Create TRMNL Private Plugin

1. [ ] Log into https://usetrmnl.com
2. [ ] Go to **Plugins** → Search "Private Plugin"
3. [ ] Click **Create a Private Plugin**
4. [ ] Fill in:
   - **Name**: Max Payne Quotes
   - **Strategy**: Polling
   - **Polling URL**: `https://your-username.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`
   - **Polling Verb**: GET
   - **Refresh Interval**: 1440 (daily)
5. [ ] Click **Save**

### 7a. Add Plugin Information (Optional - For Recipe Publishing)

If you plan to publish this as a TRMNL Recipe, add the `author_bio` field:

```yaml
- keyname: author_bio
  name: About This Plugin
  field_type: author_bio
  category: entertainment,games
  description: |
    Max Payne Quotes brings the iconic noir dialogue from the legendary Max Payne trilogy directly to your TRMNL device.
    <br><br>
    <strong>Features:</strong><br>
    🎮 50 authentic quotes from Max Payne, Max Payne 2, and Max Payne 3<br>
    🗨️ Noir-style typography with Courier New monospace font<br>
    📱 Optimized layouts for all TRMNL view sizes<br>
    🎨 Game-specific poster artwork for visual atmosphere<br>
    🎲 Random quote selection with daily automatic updates
    <br><br>
    <strong>Setup:</strong><br>
    1. Install or Fork this recipe<br>
    2. The plugin automatically polls for a new quote every 24 hours<br>
    3. Add to your playlist and enjoy noir wisdom on your e-ink display
    <br><br>
    All quotes are verified authentic from Wikiquote and capture the philosophical, dark, and action-packed moments that made Max Payne an iconic character in gaming.
    <br><br>
    <strong>Quote Database:</strong> 50 quotes verified from Wikiquote (45 Max Payne across trilogy, 5 Mona Sax)
  github_url: https://github.com/hossain-khan/trmnl-max-payne-quotes-plugin
  learn_more_url: https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/
  email_address: trmnl@hossain.dev
```

**Important Notes:**
- The `author_bio` field is **required** when publishing as a Recipe
- Categories (`entertainment,gaming`) help users discover your plugin
- Special properties render as clickable icons on the recipe page

### 8. Add Markup Templates

1. [ ] Click **Edit Markup** button
2. [ ] Copy content from each file to corresponding tab:
   - `templates/full.liquid` → **Full** tab
   - `templates/half_horizontal.liquid` → **Half Horizontal** tab
   - `templates/half_vertical.liquid` → **Half Vertical** tab
   - `templates/quadrant.liquid` → **Quadrant** tab
3. [ ] Click **Save** after each template
4. [ ] Click **Force Refresh** to test

### 9. Test the Plugin

1. [ ] Check the preview in TRMNL's markup editor
2. [ ] Verify quote text displays correctly
3. [ ] Verify character and game name display
4. [ ] Check image rendering (if you added images)
5. [ ] Test different layouts (full, half, quadrant)

### 10. Add to Playlist

1. [ ] Go to **Playlists** in TRMNL
2. [ ] Create new or edit existing playlist
3. [ ] Add "Max Payne Quotes" plugin
4. [ ] Select preferred layout
5. [ ] Set rotation timing
6. [ ] Save playlist
7. [ ] Assign to your device

## 🎉 You're Done!

Your TRMNL should now display Max Payne quotes. The plugin will:
- Fetch a new quote every 24 hours (or your configured interval)
- Automatically update with GitHub Actions daily at 2am UTC
- Display quotes in noir-style Courier New typography
- Rotate through all 50 quotes randomly
- Show character attribution (Max Payne or Mona Sax)

## 🐛 Troubleshooting

### Plugin not showing data
- [ ] Verify GitHub Pages is deployed and accessible
- [ ] Check the polling URL is correct
- [ ] Click "Force Refresh" in TRMNL plugin settings
- [ ] Verify JSON syntax in `api/random-quote.json`

### Images not displaying
- [ ] Ensure images are committed to repository
- [ ] Verify image URLs use `raw.githubusercontent.com`
- [ ] Check image file extensions match (case-sensitive)
- [ ] Wait a few minutes for GitHub CDN to update

### Layout issues
- [ ] Check that all liquid tags are properly closed
- [ ] Verify TRMNL framework classes are correct
- [ ] Test in different view sizes
- [ ] Review TRMNL framework docs: https://usetrmnl.com/framework

### Quotes not changing
- [ ] Run `python3 generate_random_quote.py` locally
- [ ] Commit and push the updated `api/random-quote.json`
- [ ] Wait for GitHub Pages to redeploy (~2 minutes)
- [ ] Force refresh on TRMNL

## 📚 Next Steps

- Add more quotes from the games
- Customize the typography and styling
- Create custom game poster artwork
- Share your plugin as a TRMNL Recipe
- Contribute improvements back to this repository

## 🔗 Resources

- [TRMNL Documentation](https://help.usetrmnl.com)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [Liquid Templating](https://shopify.github.io/liquid/)
