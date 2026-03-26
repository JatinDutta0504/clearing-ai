#!/bin/bash

echo "=== SEO AUDIT AFTER FIXES ==="
echo ""

echo "📋 CANONICAL TAGS:"
grep -l 'rel="canonical"' *.html | wc -l | xargs echo "Pages with canonical:"
echo ""

echo "🔗 SCHEMA.ORG:"
grep -l 'schema.org' *.html | wc -l | xargs echo "Pages with schema.org:"

echo ""
echo "📊 OG IMAGE STATUS:"
for f in daily-practice.html engineer-types.html faq.html journal.html; do
  if grep -q 'og:image' "$f"; then
    echo "✓ $f"
  else
    echo "⚠ $f"
  fi
done
echo ""

echo "⏱️ META TITLE AUDIT:"
for f in recovery.html research.html; do
  TITLE=$(grep '<title>' "$f" | sed 's/<[^>]*>//g' | head -1)
  TITLE_LEN=${#TITLE}
  if [ "$TITLE_LEN" -lt 60 ]; then
    echo "✓ $f: ${TITLE_LEN} chars"
  else
    echo "⚠ $f: ${TITLE_LEN} chars (too long)"
  fi
done
echo ""

echo "✅ SEO IMPROVEMENTS COMPLETE"
