# Max Payne Quotes - TRMNL Plugin

A TRMNL plugin that displays dark, noir quotes from the Max Payne trilogy on your e-ink display.

> "They were all dead. The final gunshot was an exclamation mark to everything that had led to this point."

## 📋 Features

- **39 authentic quotes** verified from Wikiquote (35 Max Payne, 4 Mona Sax)
- **Multiple layouts** - Full, Half Horizontal, Half Vertical, and Quadrant
- **Dynamic text sizing** - Quotes auto-adjust to fit available space with proper padding
- **Embedded poster images** - Base64-encoded game-specific posters for offline functionality
- **GitHub Pages hosting** - Free, reliable quote delivery
- **E-ink optimized** - Uses TRMNL Framework with pixel-perfect rendering
- **Daily automatic updates** - GitHub Actions cron job refreshes quote at 2am UTC
- **Random rotation** - Fresh quotes on each refresh

## 📸 Demo

| Layout | Preview |
|--------|---------|
| **Full** | <img src="assets/demo/plugin-demo-max-payne-full.png" alt="Full Layout" width="400"/> |
| **Half Horizontal** | <img src="assets/demo/plugin-demo-max-payne-half-horizontal.png" alt="Half Horizontal Layout" width="400"/> |
| **Half Vertical** | <img src="assets/demo/plugin-demo-max-payne-half-vertical.png" alt="Half Vertical Layout" width="400"/> |
| **Quadrant** | <img src="assets/demo/plugin-demo-max-payne-quadrant.png" alt="Quadrant Layout" width="400"/> |

## 🚀 Quick Start

This plugin is available as a public Recipe on TRMNL. Just install and add to your playlist!

### Installation (3 Steps)

1. **Install the Recipe**
   - Visit [TRMNL Plugins](https://usetrmnl.com/plugins)
   - Scroll to **Recipes** section
   - Search for "Max Payne Quotes"
   - Click **Install**

2. **Add to Playlist**
   - Go to [Playlists](https://usetrmnl.com/playlists)
   - Click **Edit** on your playlist
   - Add "Max Payne Quotes"
   - Select your preferred layout (Full, Half Horizontal, Half Vertical, or Quadrant)
   - Save

3. **Enjoy!**
   - Your TRMNL will automatically display a new quote every 24 hours

### Install vs Fork

- **Install** (recommended): Get automatic updates when new quotes or improvements are added
- **Fork** (requires Developer Edition): Customize the markup, quotes, or styling to your preference

Learn more about [Plugin Recipes](https://help.usetrmnl.com/en/articles/10122094-plugin-recipes)

## 🛠️ For Developers

Want to customize or self-host this plugin? See [SETUP.md](SETUP.md) for detailed instructions on:
- Forking and customizing the plugin
- Setting up your own GitHub Pages deployment
- Adding custom quotes
- Modifying layouts and styling

## 🎨 How It Works

The plugin displays quotes in the following format:

```json
{
  "text": "Quote text here",
  "character": "Max Payne",
  "game": "Max Payne"
}
```

**Features:**
- Game-specific poster artwork (Max Payne 1, 2, or 3) embedded as base64
- Dynamic text sizing that adapts to quote length
- Noir-style Courier New typography
- Optimized for e-ink displays with pixel-perfect rendering

### Quote Rotation

The plugin automatically fetches a new random quote every 24 hours via:
`https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`

A GitHub Actions workflow updates this endpoint daily at 2am UTC.

## 📁 Project Structure

```
trmnl-max-payne-quotes-plugin/
├── .github/
│   └── workflows/
│       ├── static.yml              # GitHub Actions for Pages deployment
│       └── update-random-quote.yml # Daily random quote updates
├── api/
│   └── random-quote.json       # Single quote endpoint (for TRMNL polling)
├── assets/
│   ├── poster/                 # Game poster images
│   └── raw/                    # Raw/source assets
├── templates/                  # Liquid template files
│   ├── full.liquid             # Full screen layout template
│   ├── half_horizontal.liquid  # Half horizontal layout
│   ├── half_vertical.liquid    # Half vertical layout
│   ├── quadrant.liquid         # Quadrant/quarter screen layout
│   └── shared.liquid           # Shared variables (posters, icons)
├── settings.yml                # TRMNL plugin configuration
├── quotes.json                 # All quotes database
├── index.html                  # GitHub Pages landing page
└── README.md                   # This file
```

## 🔗 API Endpoints

Once deployed to GitHub Pages:

- **All Quotes**: `https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/quotes.json`
- **Random Quote**: `https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`

## 📚 Resources

- [Plugin Recipe on TRMNL](https://usetrmnl.com/recipes) - Install this plugin
- [Plugin Recipes Guide](https://help.usetrmnl.com/en/articles/10122094-plugin-recipes) - Learn about Recipes
- [TRMNL Framework Docs](https://usetrmnl.com/framework) - Styling reference
- [Setup Guide](SETUP.md) - For developers who want to fork/customize

## 🎮 About Max Payne

Max Payne is a neo-noir third-person shooter video game series developed by Remedy Entertainment (Max Payne 1 & 2) and Rockstar Studios (Max Payne 3). Known for its dark, gritty atmosphere, innovative bullet-time mechanics, and film noir narrative style with memorable quotes and internal monologues.

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! You can:
- Submit new authentic quotes from the Max Payne trilogy
- Report issues or suggest improvements
- Fork the Recipe to create your own variation

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

*"The past is a gaping hole. You try to run from it, but the more you run, the deeper it grows behind you."* — Max Payne
