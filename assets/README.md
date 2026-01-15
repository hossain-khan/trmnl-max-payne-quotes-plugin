# Assets Directory

This directory contains images used by the Max Payne Quotes plugin.

## Directory Structure

```
assets/
├── poster/          # Game poster/cover art images
│   ├── max-payne-1.jpg
│   ├── max-payne-2.jpg
│   └── max-payne-3.jpg
├── raw/            # Original/source images before processing
└── icon.png        # Plugin icon (32x32 or 64x64 recommended)
```

## Adding Images

### Game Posters

1. Find or create square images (recommended: 400x400px or 800x800px)
2. Save them as:
   - `poster/max-payne-1.jpg` - Max Payne (2001)
   - `poster/max-payne-2.jpg` - Max Payne 2: The Fall of Max Payne (2003)
   - `poster/max-payne-3.jpg` - Max Payne 3 (2012)

### Plugin Icon

Create a simple icon representing the plugin:
- Size: 32x32, 64x64, or 128x128 pixels
- Format: PNG with transparency
- Theme: Gun, bullet, noir aesthetic, or Max Payne silhouette
- Save as: `assets/icon.png`

## Image Optimization for E-ink

TRMNL displays use e-ink screens (1-bit or grayscale). Images should be:

1. **High contrast** - Strong blacks and whites
2. **Dithered** - TRMNL framework handles this automatically
3. **Simple designs** - Complex gradients may not render well
4. **Properly sized** - Match the layout requirements

## Example Image Sources

- **Game Covers**: Search for "Max Payne cover art" or use screenshots
- **Icons**: Use Font Awesome, create custom, or use game logos
- **Dithering Tools**: 
  - Online: [ditherit.com](https://ditherit.com/)
  - GIMP: Filters → Blur → Pixelize → Dither
  - Photoshop: Image → Mode → Bitmap → Diffusion Dither

## Current Image URLs

Update these URLs in the `.liquid` files after adding your images:

```
Icon: https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin/main/assets/icon.png

Posters:
- Max Payne 1: https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin/main/assets/poster/max-payne-1.jpg
- Max Payne 2: https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin/main/assets/poster/max-payne-2.jpg
- Max Payne 3: https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin/main/assets/poster/max-payne-3.jpg
```

## Tips

- Keep file sizes reasonable (under 500KB each)
- Test on TRMNL's preview before deploying
- Consider using SVG for the icon for scalability
- Store original high-res versions in `raw/` directory
