#!/usr/bin/env python3
"""
Embed base64-encoded poster images into shared.liquid template
This script reads the .base64.txt files and inserts them into shared.liquid
"""

import os
from pathlib import Path

def embed_posters():
    """Read base64 files and embed them into shared.liquid"""
    
    # Paths
    project_root = Path(__file__).parent
    poster_dir = project_root / 'assets' / 'poster'
    shared_file = project_root / 'shared.liquid'
    
    # Read base64 files
    posters = {}
    for i in range(1, 4):
        base64_file = poster_dir / f'max-payne-{i}.base64.txt'
        if base64_file.exists():
            with open(base64_file, 'r') as f:
                posters[i] = f.read().strip()
            print(f"✅ Read max-payne-{i}.base64.txt ({len(posters[i])} chars)")
        else:
            print(f"❌ File not found: {base64_file}")
            return False
    
    # Read shared.liquid template
    if not shared_file.exists():
        print(f"❌ shared.liquid not found at {shared_file}")
        return False
    
    with open(shared_file, 'r') as f:
        content = f.read()
    
    # Replace placeholders
    content = content.replace('REPLACE_WITH_MAX_PAYNE_1_BASE64', posters[1])
    content = content.replace('REPLACE_WITH_MAX_PAYNE_2_BASE64', posters[2])
    content = content.replace('REPLACE_WITH_MAX_PAYNE_3_BASE64', posters[3])
    
    # Write updated file
    with open(shared_file, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Successfully embedded all posters into shared.liquid")
    print(f"📄 File size: {os.path.getsize(shared_file):,} bytes")
    print(f"\n📋 Usage in your .liquid templates:")
    print(f"   <img src=\"{{{{ poster_max_payne_1 }}}}\" />")
    print(f"   <img src=\"{{{{ poster_max_payne_2 }}}}\" />")
    print(f"   <img src=\"{{{{ poster_max_payne_3 }}}}\" />")
    
    return True

if __name__ == '__main__':
    success = embed_posters()
    if not success:
        print("\n❌ Failed to embed posters. Please check the error messages above.")
        exit(1)
