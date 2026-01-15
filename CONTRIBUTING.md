# Contributing to Max Payne Quotes TRMNL Plugin

Thank you for your interest in contributing! This plugin is designed to showcase quotes from the Max Payne trilogy on TRMNL e-ink displays.

## 🛠️ For Developers

Want to customize or self-host this plugin? See [SETUP.md](SETUP.md) for detailed instructions on:
- Forking and customizing the plugin
- Setting up your own GitHub Pages deployment
- Adding custom quotes
- Modifying layouts and styling

Once you have your development environment set up, come back here for contribution guidelines.

## 🎯 How to Contribute

### Adding Quotes

The most valuable contribution is adding more authentic quotes from the games!

1. **Find quotes** from Max Payne games (1, 2, or 3)
2. **Edit** [quotes.json](quotes.json)
3. **Add entry** following this format:

```json
{
  "text": "The exact quote text",
  "character": "Character name (Max Payne, Mona Sax, etc.)",
  "game": "Max Payne | Max Payne 2 | Max Payne 3",
  "image": "https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-max-payne-quotes-plugin/main/assets/poster/max-payne-1.jpg"
}
```

4. **Verify accuracy** - Ensure quotes are accurate to the games
5. **Test** - Run `python3 generate_random_quote.py` to verify JSON validity
6. **Submit PR** with a clear description

### Improving Layouts

If you want to enhance the visual design:

1. **Test locally** with TRMNL's markup editor
2. **Edit** the appropriate `.liquid` file (full, half_horizontal, half_vertical, quadrant)
3. **Follow TRMNL Framework** guidelines: https://usetrmnl.com/framework
4. **Optimize for e-ink** - High contrast, clear typography
5. **Test on actual device** if possible
6. **Submit PR** with screenshots/photos

### Adding Images

To contribute game poster images:

1. **Create/find** high-quality images (400x400px or larger, square)
2. **Optimize** for e-ink displays (high contrast, dithered)
3. **Name appropriately**: `max-payne-1.jpg`, `max-payne-2.jpg`, `max-payne-3.jpg`
4. **Place in** `assets/poster/`
5. **Keep file size** reasonable (< 500KB each)
6. **Test rendering** on TRMNL preview
7. **Submit PR** with source attribution

### Bug Fixes

Found a bug? Please:

1. **Check existing issues** to avoid duplicates
2. **Open an issue** describing the problem
3. **Include details**: 
   - What you expected to happen
   - What actually happened
   - Steps to reproduce
   - TRMNL display model (if relevant)
4. **Submit PR** with fix if you can

## 📋 Contribution Guidelines

### Code Style

- **Liquid templates**: Use proper indentation (2 spaces)
- **JSON**: Use 2-space indentation, ensure valid syntax
- **YAML**: Follow existing formatting in settings.yml
- **Python**: Follow PEP 8 style guide

### Commit Messages

Use clear, descriptive commit messages:

```
✅ Good:
- "Add 5 new quotes from Max Payne 3"
- "Fix typography overflow in quadrant layout"
- "Optimize poster images for e-ink display"

❌ Bad:
- "Update stuff"
- "Fix"
- "Changes"
```

### Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your feature/fix
3. **Make changes** following guidelines above
4. **Test thoroughly**:
   - Validate JSON syntax
   - Test liquid templates in TRMNL
   - Run generate_random_quote.py
5. **Update documentation** if needed (README, SETUP, etc.)
6. **Submit PR** with:
   - Clear title
   - Description of changes
   - Screenshots/examples (for visual changes)
   - Testing notes

## 🎨 Design Principles

When contributing, keep these in mind:

1. **Noir Aesthetic** - Dark, moody, film noir style
2. **Typography** - Courier New monospace for authenticity
3. **Readability** - High contrast for e-ink displays
4. **Simplicity** - Clean layouts that work at all sizes
5. **Authenticity** - Stay true to Max Payne's tone and style

## 🚫 What NOT to Contribute

- Quotes from sources other than Max Payne games
- Copyrighted artwork without permission
- Excessive file sizes (>500KB per image)
- Breaking changes without discussion
- Unrelated features or plugins

## 📚 Resources

- [TRMNL Framework Docs](https://usetrmnl.com/framework)
- [Liquid Documentation](https://shopify.github.io/liquid/)
- [Max Payne Wiki](https://maxpayne.fandom.com/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

## 💡 Ideas for Contributions

Not sure where to start? Try:

- [ ] Add more quotes (current: 39, target: 50+ total)
- [ ] Create custom game poster artwork
- [ ] Improve mobile responsiveness of index.html
- [ ] Add quote categories/filtering
- [ ] Create alternative color schemes
- [ ] Add comic book panel styling
- [ ] Implement quote of the day feature
- [ ] Add character-specific themes

## ❓ Questions?

Open an issue with the "question" label or reach out via:
- GitHub Issues
- TRMNL Developer Discord (if applicable)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this project (see LICENSE file).

---

**"The pain kept my feelings sharp and my purpose clear."** — Max Payne

Thank you for helping make this plugin better! 🔫
