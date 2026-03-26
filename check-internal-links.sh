#!/bin/bash

echo "📊 INTERNAL LINKING AUDIT"
echo "Scanning all 43 pages for link density..."
echo ""

for html in *.html; do
  # Count internal links (href="#" or href="/")
  links=$(grep -o 'href="[^"]*"' "$html" | grep -E '(href="#|href="\/')' | wc -l)
  
  # Skip if very low
  if [ "$links" -lt 5 ]; then
    echo "⚠️  LOW LINKS: $html ($links internal links)"
  fi
done

echo ""
echo "✅ Audit complete."
