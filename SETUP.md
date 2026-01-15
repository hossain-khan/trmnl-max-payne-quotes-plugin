# Quick Setup Checklist

Follow these steps to get your Max Payne Quotes plugin running on TRMNL.

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
- [ ] `full.liquid` (line 17)
- [ ] `half_horizontal.liquid` (line 16)
- [ ] `half_vertical.liquid` (line 20)
- [ ] `quadrant.liquid` (line 13)
- [ ] `quotes.json` (all image URLs)
- [ ] `api/random-quote.json` (image URL)
- [ ] `index.html` (line 79)

Also update:
- [ ] `settings.yml` - Replace `YOUR_EMAIL@example.com` with your email (line 14)

**Quick Find & Replace:**
```bash
# macOS/Linux
find . -type f \( -name "*.yml" -o -name "*.liquid" -o -name "*.json" -o -name "*.html" \) -exec sed -i '' 's/YOUR_GITHUB_USERNAME/your-actual-username/g' {} +

# Or manually with your editor's find & replace feature
```

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
  - `maxpayne1.png`
  - `maxpayne2.png`
  - `maxpayne3.png`
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

### 8. Add Markup Templates

1. [ ] Click **Edit Markup** button
2. [ ] Copy content from each file to corresponding tab:
   - `full.liquid` → **Full** tab
   - `half_horizontal.liquid` → **Half Horizontal** tab
   - `half_vertical.liquid` → **Half Vertical** tab
   - `quadrant.liquid` → **Quadrant** tab
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
- Display quotes in noir-style typography
- Rotate through all 15+ quotes randomly

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
