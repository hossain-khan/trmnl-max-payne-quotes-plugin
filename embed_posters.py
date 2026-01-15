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
    
    # Use regex to replace existing base64 data or placeholders
    import re
    
    # Pattern to match base64 data in each capture block
    pattern_1 = r'({%- capture poster_max_payne_1 -%}\s*data:image/jpeg;base64,)[^\s]+(\s*{%- endcapture -%})'
    pattern_2 = r'({%- capture poster_max_payne_2 -%}\s*data:image/jpeg;base64,)[^\s]+(\s*{%- endcapture -%})'
    pattern_3 = r'({%- capture poster_max_payne_3 -%}\s*data:image/jpeg;base64,)[^\s]+(\s*{%- endcapture -%})'
    
    # Replace with new base64 data
    content = re.sub(pattern_1, r'\g<1>' + posters[1] + r'\g<2>', content)
    content = re.sub(pattern_2, r'\g<1>' + posters[2] + r'\g<2>', content)
    content = re.sub(pattern_3, r'\g<1>' + posters[3] + r'\g<2>', content)
    
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
