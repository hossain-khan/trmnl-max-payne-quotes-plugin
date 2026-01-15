#!/bin/bash

# Setup script for Max Payne Quotes TRMNL Plugin
# This script helps configure the plugin with your GitHub username and email

set -e

echo "🔫 Max Payne Quotes TRMNL Plugin Setup"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -f "settings.yml" ]; then
    echo "❌ Error: settings.yml not found. Please run this script from the project root directory."
    exit 1
fi

# Get GitHub username
echo "Please enter your GitHub username:"
read -r GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Error: GitHub username cannot be empty"
    exit 1
fi

# Get email address
echo ""
echo "Please enter your email address:"
read -r EMAIL_ADDRESS

if [ -z "$EMAIL_ADDRESS" ]; then
    echo "❌ Error: Email address cannot be empty"
    exit 1
fi

echo ""
echo "📝 Updating configuration files..."
echo ""

# Function to replace in file and show result
replace_in_file() {
    local file=$1
    local old=$2
    local new=$3
    
    if [ -f "$file" ]; then
        if grep -q "$old" "$file"; then
            sed -i.bak "s|$old|$new|g" "$file"
            rm "${file}.bak"
            echo "  ✅ Updated $file"
        else
            echo "  ⚠️  $file already configured or pattern not found"
        fi
    else
        echo "  ❌ $file not found"
    fi
}

# Replace GitHub username
echo "Replacing YOUR_GITHUB_USERNAME with $GITHUB_USERNAME..."
replace_in_file "settings.yml" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "full.liquid" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "half_horizontal.liquid" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "half_vertical.liquid" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "quadrant.liquid" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "quotes.json" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "api/random-quote.json" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"
replace_in_file "index.html" "YOUR_GITHUB_USERNAME" "$GITHUB_USERNAME"

echo ""
echo "Replacing YOUR_EMAIL@example.com with $EMAIL_ADDRESS..."
replace_in_file "settings.yml" "YOUR_EMAIL@example.com" "$EMAIL_ADDRESS"

echo ""
echo "✅ Configuration complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Generate a random quote: python3 generate_random_quote.py"
echo "  2. Add your images to assets/poster/ (optional)"
echo "  3. Commit changes: git add . && git commit -m 'Configure plugin'"
echo "  4. Push to GitHub: git push origin main"
echo "  5. Enable GitHub Pages in your repository settings"
echo "  6. Create Private Plugin in TRMNL with polling URL:"
echo "     https://$GITHUB_USERNAME.github.io/trmnl-max-payne-quotes-plugin/api/random-quote.json"
echo ""
echo "📖 See SETUP.md for detailed instructions"
echo ""
