# Shared Posters - Max Payne Game Posters

This file contains base64-encoded poster images for all three Max Payne games that can be used in your TRMNL liquid templates without external dependencies.

## File Information

- **File**: `templates/shared.liquid`
- **Size**: ~63KB (all three posters combined, optimized)
- **Format**: Base64-encoded JPEG images
- **Purpose**: Inline poster images without requiring external URLs

## Poster Details

| Poster Variable | Game | Original File | JPEG Size | Base64 Size |
|----------------|------|---------------|-----------|-------------|
| `poster_max_payne_1` | Max Payne (2001) | max-payne-1.jpg | 21KB | ~29KB |
| `poster_max_payne_2` | Max Payne 2 (2003) | max-payne-2.jpg | 28KB | ~38KB |
| `poster_max_payne_3` | Max Payne 3 (2012) | max-payne-3.jpg | 19KB | ~26KB |

## Setup in TRMNL

1. Copy the entire contents of `templates/shared.liquid`
2. In TRMNL markup editor, go to the **"Shared"** tab
3. Paste the contents
4. Click **Save**

The poster variables will now be available in ALL your layout templates (full, half, quadrant).

## Usage in Templates

Instead of using the `image` property from JSON, use the shared poster variables:

### Before (using JSON property):
```liquid
<img src="{{ image }}" />
```

### After (using shared posters):
```liquid
{% if game == "Max Payne" %}
  <img src="{{ poster_max_payne_1 }}" />
{% elsif game == "Max Payne 2" %}
  <img src="{{ poster_max_payne_2 }}" />
{% elsif game == "Max Payne 3" %}
  <img src="{{ poster_max_payne_3 }}" />
{% endif %}
```

### Or with specific dimensions:
```liquid
<img src="{{ poster_max_payne_1 }}" height="200px" width="200px" />
```

## Example: Full Layout with Conditional Posters

```liquid
<div class="layout">
  <div class="grid">
    <div class="col--span-1 ml--1 mt--20">
      {% if game == "Max Payne" %}
        <img class="image" src="{{ poster_max_payne_1 }}" />
      {% elsif game == "Max Payne 2" %}
        <img class="image" src="{{ poster_max_payne_2 }}" />
      {% elsif game == "Max Payne 3" %}
        <img class="image" src="{{ poster_max_payne_3 }}" />
      {% endif %}
    </div>
    <div class="col--span-2 col col--center mt--10 text--black" data-pixel-perfect="true">
      <p style="font-family: 'Courier New', monospace; font-weight: bold;">
        {{ text }}
      </p>
      <p style="font-family: 'Courier New', monospace;">
        — {{ character }}, {{ game }}
      </p>
    </div>
  </div>
</div>
```

## Advantages

✅ **No external dependencies** - Images are embedded directly
✅ **Always available** - No need for GitHub Pages or external hosting
✅ **Faster loading** - No additional HTTP requests
✅ **Offline compatible** - Works even without internet
✅ **No CORS issues** - Everything is inline

## Disadvantages

⚠️ **Larger file size** - The templates/shared.liquid file is ~63KB (optimized)
⚠️ **Not cacheable** - Base64 images can't be cached separately
⚠️ **Harder to update** - Need to re-run embed script for changes

## Regenerating Shared Posters

If you add new poster images or want to update existing ones:

1. Add/update JPG files in `assets/poster/`
2. Convert to base64:
   ```bash
   cd assets/poster
   base64 -i max-payne-1.jpg > max-payne-1.base64.txt
   ```
3. Run the embed script:
   ```bash
   python3 embed_posters.py
   ```
4. Copy updated `templates/shared.liquid` to TRMNL Shared tab

## Updating After Image Optimization

If you've optimized the poster JPEG files to reduce file size:

### Step 1: Verify Optimized Image Sizes
```bash
cd assets/poster
ls -lh *.jpg
```

You should see the file sizes for each poster (e.g., 21KB, 28KB, 19KB).

### Step 2: Regenerate Base64 Files
```bash
for img in *.jpg; do base64 -i "$img" > "${img%.jpg}.base64.txt"; done
```

This converts all optimized JPEGs to base64-encoded text files.

### Step 3: Update shared.liquid
```bash
cd /Users/hossain/dev/repos/hk-projects/trmnl-max-payne-quotes-plugin
python3 embed_posters.py
```

The script will:
- Read all `.base64.txt` files
- Update the existing base64 data in `templates/shared.liquid`
- Report the new file size

### Step 4: Verify File Size Reduction
```bash
ls -lh templates/shared.liquid
```

You should see a smaller file size (e.g., ~63KB after optimization from ~200KB original).

### Step 5: Update TRMNL Plugin

1. Copy the updated `templates/shared.liquid` contents
2. Go to your TRMNL Private Plugin
3. Navigate to the **Shared** tab
4. Paste the new contents
5. Click **Save**
6. Force refresh your plugin to test

### Optimization Tips

- **Target file sizes**: Aim for 15-30KB per JPEG for optimal e-ink display
- **Tools**: Use ImageOptim, JPEGmini, or online tools like TinyJPG
- **Quality**: E-ink displays work well with 70-80% JPEG quality
- **Progressive optimization**: Run multiple passes, checking quality each time
- **Verify visually**: Open optimized JPEGs to ensure they still look good

### Example Optimization Workflow

```bash
# 1. Check current sizes
cd assets/poster
ls -lh *.jpg

# 2. Optimize images (using your preferred tool)
# ... optimize max-payne-1.jpg, max-payne-2.jpg, max-payne-3.jpg ...

# 3. Regenerate base64
for img in *.jpg; do base64 -i "$img" > "${img%.jpg}.base64.txt"; done

# 4. Update shared.liquid
cd ..
python3 embed_posters.py

# 5. Verify new size
ls -lh templates/shared.liquid
```

The `embed_posters.py` script uses regex to update existing base64 data, so you can run it multiple times as you optimize further.

## Alternative: Using JSON Image URLs

If you prefer smaller templates and don't mind external dependencies, you can keep using the `image` property from your JSON file:

```json
{
  "text": "Quote here",
  "game": "Max Payne",
  "image": "https://your-username.github.io/trmnl-max-payne-quotes-plugin/assets/poster/max-payne-1.jpg"
}
```

And in templates:
```liquid
<img src="{{ image }}" />
```

## Recommendation

**Use templates/shared.liquid posters if:**
- You want completely self-contained templates
- You're worried about GitHub Pages availability
- You don't plan to change images frequently

**Use JSON image URLs if:**
- You want smaller template files
- You want easier image updates
- File size is a concern

## Files in This Project

```
assets/poster/
├── max-payne-1.jpg              # Original poster image
├── max-payne-1.base64.txt       # Base64 encoded version
├── max-payne-2.jpg
├── max-payne-2.base64.txt
├── max-payne-3.jpg
└── max-payne-3.base64.txt

templates/
├── shared.liquid                 # Template with embedded posters
├── full.liquid                   # Full screen layout
├── half_horizontal.liquid        # Half horizontal layout
├── half_vertical.liquid          # Half vertical layout
└── quadrant.liquid               # Quadrant layout

embed_posters.py                  # Script to generate shared.liquid
SHARED_POSTERS.md                # This documentation file
```

## Questions?

See the main [README.md](../README.md) for full plugin documentation.
