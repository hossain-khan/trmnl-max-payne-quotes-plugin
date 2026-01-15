# 🎮 Max Payne Quotes TRMNL Plugin - Project Summary

## ✅ What's Been Created

Your TRMNL plugin for Max Payne quotes is now complete and ready to deploy!

### 📁 Project Structure

```
trmnl-max-payne-quotes-plugin/
├── 📄 Core Plugin Files
│   ├── settings.yml              # Plugin configuration for TRMNL
│   ├── templates/                # Liquid template files
│   │   ├── full.liquid           # Full screen layout template
│   │   ├── half_horizontal.liquid # Half horizontal layout
│   │   ├── half_vertical.liquid  # Half vertical layout
│   │   ├── quadrant.liquid       # Quadrant/quarter screen layout
│   │   └── shared.liquid         # Shared variables (posters, icons)
│
├── 📊 Data Files
│   ├── quotes.json               # All 15 Max Payne quotes
│   └── api/
│       └── random-quote.json     # Single random quote endpoint
│
├── 🌐 Web Files
│   └── index.html                # GitHub Pages landing page
│
├── 🖼️ Assets
│   ├── poster/                   # (Empty - add your game posters here)
│   ├── raw/                      # Source images
│   └── README.md                 # Image guidelines
│
├── 🛠️ Automation
│   ├── .github/workflows/
│   │   └── deploy.yml           # Auto-deploy to GitHub Pages
│   ├── generate_random_quote.py  # Generate random quotes
│   └── setup.sh                  # Quick setup script
│
└── 📚 Documentation
    ├── README.md                 # Main documentation
    ├── SETUP.md                  # Step-by-step setup guide
    └── CONTRIBUTING.md           # Contribution guidelines
```

## 🚀 Quick Start (Next Steps)

### 1. Configure Your Plugin

Run the setup script:
```bash
./setup.sh
```

Or manually replace in all files:
- `YOUR_GITHUB_USERNAME` → your GitHub username
- `YOUR_EMAIL@example.com` → your email

### 2. Test Locally

```bash
# Generate a random quote
python3 generate_random_quote.py

# View all quotes
python3 generate_random_quote.py --list
```

### 3. Deploy to GitHub

```bash
git add .
git commit -m "Configure Max Payne Quotes plugin"
git push origin main
```

### 4. Enable GitHub Pages

1. Go to your repo **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **(root)**
4. Click **Save**

Wait 2-5 minutes, then visit:
`https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/`

### 5. Create TRMNL Plugin

1. Login to https://usetrmnl.com
2. Plugins → Private Plugin → Create
3. Settings:
   - **Name**: Max Payne Quotes
   - **Strategy**: Polling
   - **URL**: `https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`
   - **Interval**: 1440 (daily)
4. Edit Markup → Copy each `.liquid` file to corresponding tab
5. Force Refresh to test

## ✨ Features

### 🎯 What It Does

- ✅ Displays random Max Payne quotes on TRMNL e-ink display
- ✅ 15+ authentic quotes from all 3 games
- ✅ 4 different layout sizes (full, half-h, half-v, quadrant)
- ✅ Noir-style typography with Courier New monospace
- ✅ Auto-refreshes daily (configurable)
- ✅ GitHub Pages hosting (free, reliable)
- ✅ Auto-deployment via GitHub Actions

### 🎨 Design Features

- **Courier New Font** - Authentic noir/typewriter aesthetic
- **Quote Marks** - Visual SVG icons for quotes
- **High Contrast** - Optimized for e-ink displays
- **Responsive** - Works in all TRMNL layout sizes
- **Game Attribution** - Shows character and game name

### 📊 Data Format

Each quote contains:
```json
{
  "text": "Quote text",
  "character": "Character name",
  "game": "Game title",
  "image": "Poster URL"
}
```

## 🔧 Customization Options

### Add More Quotes

Edit [quotes.json](quotes.json):
```json
{
  "quotes": [
    {
      "text": "Your new quote",
      "character": "Max Payne",
      "game": "Max Payne",
      "image": "https://..."
    }
  ]
}
```

### Change Refresh Rate

Edit [settings.yml](settings.yml):
```yaml
refresh_interval: 1440  # minutes (1440 = 24 hours)
```

Options:
- 60 = hourly
- 360 = every 6 hours
- 720 = twice daily
- 1440 = daily

### Modify Typography

Edit any `.liquid` file:
```html
<p style="font-family: 'Your Font', monospace; font-weight: bold;">
  {{ text }}
</p>
```

### Add Game Posters

1. Add images to `assets/poster/`:
   - `maxpayne1.png`
   - `maxpayne2.png`
   - `maxpayne3.png`
2. Update URLs in `quotes.json` and `.liquid` files
3. See [assets/README.md](assets/README.md) for guidelines

## 📖 Documentation

| File | Purpose |
|------|---------|
| [README.md](README.md) | Main project overview & instructions |
| [SETUP.md](SETUP.md) | Detailed step-by-step setup checklist |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guidelines for contributors |
| [assets/README.md](assets/README.md) | Image guidelines & optimization tips |

## 🛠️ Tools Included

### generate_random_quote.py

Generate random quotes for API endpoint:
```bash
# Generate random quote
python3 generate_random_quote.py

# List all quotes
python3 generate_random_quote.py --list
```

### setup.sh

Interactive setup wizard:
```bash
./setup.sh
```
Prompts for GitHub username and email, updates all files automatically.

## 📊 Sample Quotes Included

✅ 15 authentic quotes from:
- **Max Payne** (2001)
- **Max Payne 2: The Fall of Max Payne** (2003)
- **Max Payne 3** (2012)

Including classics like:
- "They were all dead..."
- "The past is a gaping hole..."
- "I don't know about angels, but it's fear that gives men wings."

## 🔗 API Endpoints

Once deployed:

| Endpoint | Purpose |
|----------|---------|
| `/quotes.json` | All quotes array |
| `/api/random-quote.json` | Single random quote |
| `/index.html` | Documentation page |

## 📚 Resources

- [TRMNL Plugin Docs](https://help.usetrmnl.com/en/articles/9510536-private-plugins)
- [TRMNL Framework](https://usetrmnl.com/framework)
- [Liquid Templating](https://help.usetrmnl.com/en/articles/10671186-liquid-101)
- [GitHub Pages](https://docs.github.com/en/pages)

## 🐛 Troubleshooting

### Common Issues

1. **Plugin not showing data**
   - Check GitHub Pages is deployed
   - Verify polling URL
   - Click "Force Refresh" in TRMNL

2. **Images not loading**
   - Add images to `assets/poster/`
   - Update URLs in all files
   - Commit and push changes

3. **Quotes not random**
   - Run `python3 generate_random_quote.py`
   - Commit updated `api/random-quote.json`
   - Wait for GitHub Pages to update

See [SETUP.md](SETUP.md#-troubleshooting) for more help.

## 🎉 You're Ready!

Your Max Payne Quotes plugin is complete and ready to deploy. Follow the Quick Start steps above to get it running on your TRMNL display.

**"The past is a gaping hole. You try to run from it, but the more you run, the deeper it grows behind you."** — Max Payne

Enjoy your noir quotes! 🔫
