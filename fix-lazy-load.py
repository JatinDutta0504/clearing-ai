import os, re

added, skipped = 0, 0
for fname in sorted(os.listdir('.')):
    if not fname.endswith('.html'):
        continue
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all img tags without loading="lazy"
    # Pattern: <img ... src="..." ...> or <img src="..." ...>
    # We want to add loading="lazy" before src if not present
    
    def add_lazy(m):
        img = m.group(0)
        if 'loading=' in img:
            return img  # already has it
        # Add loading="lazy" after the <img part (before src or alt or >)
        # Find where to insert — after <img, before src/alt/title
        tag_start = img[:5]  # <img
        rest = img[5:]
        return tag_start + ' loading="lazy"' + rest

    new_content = re.sub(r'<img\s+[^>]*>', add_lazy, content)
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        added += 1
    else:
        skipped += 1

print(f"Updated: {added} pages | No change: {skipped} pages")
