#!/usr/bin/env python3
"""Fix all <button> elements missing type="button" across all HTML pages."""
import os
import re

clearing_dir = os.path.expanduser("~/Desktop/TheClearing")
html_files = [f for f in os.listdir(clearing_dir) if f.endswith(".html")]

total_fixed = 0
files_changed = 0

# Pattern: <button that is NOT already type="button" or type="submit" etc
button_pattern = re.compile(r'<button(?![^>]*\btype=")(?![^>]*\btype=\')(?![^>]*\btype=\")', re.IGNORECASE)

for filename in sorted(html_files):
    filepath = os.path.join(clearing_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = button_pattern.findall(content)
        if matches:
            # Replace <button (without type) with <button type="button"
            new_content = button_pattern.sub('button type="button"', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_count = len(matches)
                total_fixed += fixed_count
                files_changed += 1
                print(f"  ✓ {filename}: {fixed_count} button(s) fixed")
    except Exception as e:
        print(f"  ✗ Error in {filename}: {e}")

print(f"\n✅ Fixed {total_fixed} buttons across {files_changed} files.")
