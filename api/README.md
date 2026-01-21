# API Directory

This directory contains the random quote endpoint used by the TRMNL plugin.

## Files

### `random-quote.json`

A single random quote selected from [`quotes.json`](../quotes.json) in the root directory.

**Format:**
```json
{
  "text": "Quote text here",
  "character": "Max Payne",
  "game": "Max Payne",
  "updated_on": "2026-01-21T02:45:21.153936Z"
}
```

**Endpoint:**
```
https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json
```

## Automatic Updates

This file is automatically updated daily by a GitHub Actions workflow.

### How It Works

1. **Workflow**: [`.github/workflows/update-random-quote.yml`](../.github/workflows/update-random-quote.yml)
2. **Schedule**: Runs every day at 2:00 AM UTC
3. **Process**:
   - Loads all quotes from [`quotes.json`](../quotes.json) (39 quotes)
   - Randomly selects one quote
   - Adds `updated_on` timestamp in ISO 8601 UTC format
   - Saves to `api/random-quote.json`
   - Commits and pushes changes automatically
4. **GitHub Pages**: Deploys the updated file within minutes

### Script

The [`generate_random_quote.py`](../generate_random_quote.py) script handles the random selection:

```bash
# Generate new random quote
python3 generate_random_quote.py

# View all available quotes
python3 generate_random_quote.py --list
```

### Manual Trigger

You can manually trigger a quote update:

1. Go to **Actions** tab in GitHub
2. Select **Update Random Quote** workflow
3. Click **Run workflow**
4. Wait ~1-2 minutes for GitHub Pages to deploy

## Source Data

All quotes come from [`quotes.json`](../quotes.json):
- **39 total quotes** verified from Wikiquote
- **35 Max Payne quotes** across the trilogy
- **4 Mona Sax quotes** from Max Payne 2

Each quote has:
- `text`: The actual quote
- `character`: Who said it (Max Payne or Mona Sax)
- `game`: Which game it's from (Max Payne, Max Payne 2, or Max Payne 3)

## TRMNL Integration

The TRMNL plugin polls this endpoint:
- **Polling URL**: `https://hossain-khan.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json`
- **Refresh Interval**: 1440 minutes (24 hours)
- **Strategy**: Polling (TRMNL fetches data on schedule)

Since the file updates daily at 2am UTC and TRMNL polls every 24 hours, users see a fresh quote each day.

## Workflow Configuration

Key settings from the workflow file:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2:00 AM UTC
  workflow_dispatch:      # Allow manual trigger

permissions:
  contents: write         # Required to commit changes
```

## Monitoring

Check if the automation is working:

1. **Recent commits**: Look for commits with message `"chore: update random quote [automated]"`
2. **Actions tab**: View workflow run history and logs
3. **Updated timestamp**: Check `updated_on` field in `random-quote.json`
4. **GitHub Pages**: Verify deployment status in Settings → Pages

## Troubleshooting

### Quote not updating
- Check GitHub Actions tab for failed workflows
- Verify `contents: write` permission is set
- Ensure `quotes.json` is valid JSON

### TRMNL not showing new quote
- Click "Force Refresh" in TRMNL plugin settings
- Verify polling URL is correct
- Check GitHub Pages is deployed and accessible

### Manual update needed
- Run workflow manually from Actions tab
- Or run script locally: `python3 generate_random_quote.py`
- Commit and push: `git add api/random-quote.json && git commit -m "chore: update random quote" && git push`

---

**Related Documentation:**
- [Main README](../README.md)
- [Setup Guide](../docs/SETUP.md)
- [Contributing Guide](../docs/CONTRIBUTING.md)
