# 🔫 Max Payne Quotes - TRMNL Plugin

A TRMNL plugin that displays dark, noir quotes from the Max Payne trilogy on your e-ink display.

> "They were all dead. The final gunshot was an exclamation mark to everything that had led to this point."

## 📋 Features

- **15+ iconic quotes** from Max Payne, Max Payne 2, and Max Payne 3
- **Multiple layouts** - Full, Half Horizontal, Half Vertical, and Quadrant
- **GitHub Pages hosting** - Free, reliable quote delivery
- **E-ink optimized** - Uses TRMNL Framework for perfect rendering
- **Random rotation** - Fresh quotes on each refresh

## 🚀 Setup Instructions

### Step 1: Fork/Clone this Repository

```bash
git clone https://github.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin.git
cd trmnl-max-payne-quotes-plugin
```

### Step 2: Update Configuration

Replace `YOUR_GITHUB_USERNAME` in these files:
- [settings.yml](settings.yml)
- [full.liquid](full.liquid)
- [half_horizontal.liquid](half_horizontal.liquid)
- [half_vertical.liquid](half_vertical.liquid)
- [quadrant.liquid](quadrant.liquid)
- [quotes.json](quotes.json)
- [index.html](index.html)

Also update `YOUR_EMAIL@example.com` in [settings.yml](settings.yml)

### Step 3: Enable GitHub Pages

1. Go to your repository **Settings** → **Pages**
2. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main** / **(root)**
3. Click **Save**
4. Wait a few minutes for deployment

Your quotes will be available at: `https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/`

### Step 4: Create TRMNL Private Plugin

1. Log into [TRMNL](https://usetrmnl.com) (requires Developer Edition)
2. Navigate to **Plugins** → Search for "**Private Plugin**"
3. Click "Create a Private Plugin"
4. Configure:
   - **Name**: Max Payne Quotes
   - **Strategy**: Polling
   - **Polling URL**: `https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`
   - **Refresh Interval**: 1440 minutes (daily)
5. Click **Save**

### Step 5: Add Markup Templates

1. Click **Edit Markup** on your plugin
2. Copy content from each `.liquid` file to corresponding tab:
   - `full.liquid` → **Full** tab
   - `half_horizontal.liquid` → **Half Horizontal** tab
   - `half_vertical.liquid` → **Half Vertical** tab
   - `quadrant.liquid` → **Quadrant** tab
3. Click **Save** and **Force Refresh** to test

### Step 6: Add to Playlist

1. Go to **Playlists**
2. Add your "Max Payne Quotes" plugin
3. Choose your preferred layout
4. Save and enjoy!

## 📊 Data Structure

The plugin expects JSON in this format:

```json
{
  "text": "Quote text here",
  "character": "Max Payne",
  "game": "Max Payne",
  "image": "https://url-to-image.png"
}
```

## 🎨 Customization

### Adding More Quotes

Edit [quotes.json](quotes.json) and add new entries:

```json
{
  "text": "Your new quote here",
  "character": "Character name",
  "game": "Max Payne 3",
  "image": "https://your-image-url.png"
}
```

### Changing Refresh Rate

Edit [settings.yml](settings.yml):
```yaml
refresh_interval: 1440  # minutes (1440 = 24 hours)
```

### Styling

The liquid templates use:
- **Font**: `Courier New` monospace (noir/typewriter aesthetic)
- **TRMNL Framework**: Grid system, responsive utilities
- **Quote marks**: SVG icons for visual appeal

## 📁 Project Structure

```
trmnl-max-payne-quotes-plugin/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions for Pages deployment
├── api/
│   └── random-quote.json       # Single quote endpoint (for TRMNL polling)
├── assets/
│   ├── poster/                 # Game poster images
│   └── raw/                    # Raw/source assets
├── full.liquid                 # Full screen layout template
├── half_horizontal.liquid      # Half horizontal layout
├── half_vertical.liquid        # Half vertical layout
├── quadrant.liquid             # Quadrant/quarter screen layout
├── settings.yml                # TRMNL plugin configuration
├── quotes.json                 # All quotes database
├── index.html                  # GitHub Pages landing page
└── README.md                   # This file
```

## 🔗 API Endpoints

Once deployed to GitHub Pages:

- **All Quotes**: `https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/quotes.json`
- **Random Quote**: `https://YOUR_USERNAME.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`

## 📚 Documentation

- [TRMNL Private Plugins Guide](https://help.usetrmnl.com/en/articles/9510536-private-plugins)
- [TRMNL Framework Docs](https://usetrmnl.com/framework)
- [Liquid Templating 101](https://help.usetrmnl.com/en/articles/10671186-liquid-101)

## 🎮 About Max Payne

Max Payne is a neo-noir third-person shooter video game series developed by Remedy Entertainment (Max Payne 1 & 2) and Rockstar Studios (Max Payne 3). Known for its dark, gritty atmosphere, innovative bullet-time mechanics, and film noir narrative style with memorable quotes and internal monologues.

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to submit issues or pull requests to add more quotes, improve layouts, or enhance functionality!

---

*"The past is a gaping hole. You try to run from it, but the more you run, the deeper it grows behind you."* — Max Payne