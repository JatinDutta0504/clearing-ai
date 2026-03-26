#!/bin/bash

echo "=== CLEARING-AI.COM SEO AUDIT ==="
echo ""

echo "📄 PAGE INVENTORY:"
TOTAL=$(find . -name "*.html" -type f | wc -l)
echo "Total pages: $TOTAL"
echo ""

echo "📝 META TAG AUDIT (sampling 5 pages):"
for f in index.html recovery.html quiz.html research.html community.html; do
  if [ -f "$f" ]; then
    TITLE=$(grep '<title>' "$f" | sed 's/<[^>]*>//g' | head -1)
    DESC=$(grep 'name="description"' "$f" | grep -o 'content="[^"]*"' | sed 's/content="//;s/"$//')
    TITLE_LEN=${#TITLE}
    DESC_LEN=${#DESC}
    
    STATUS_T="✓"
    STATUS_D="✓"
    [ "$TITLE_LEN" -lt 30 ] || [ "$TITLE_LEN" -gt 60 ] && STATUS_T="⚠"
    [ "$DESC_LEN" -lt 120 ] || [ "$DESC_LEN" -gt 160 ] && STATUS_D="⚠"
    
    echo "$STATUS_T $f: Title=$TITLE_LEN chars, Desc=$DESC_LEN chars"
  fi
done
echo ""

echo "🔗 INTERNAL LINKS:"
grep -h 'href="/' *.html 2>/dev/null | grep -v '://' | sed 's/.*href="\([^"]*\)".*/\1/' | sort | uniq | wc -l | xargs echo "Total unique internal links:"
echo ""

echo "🖼️  OG IMAGE:"
OG_COUNT=$(grep -l 'og:image' *.html | wc -l)
echo "Pages with og:image: $OG_COUNT/$TOTAL"
[ $OG_COUNT -eq $TOTAL ] && echo "✓ All pages have OG image" || echo "⚠ Missing OG images"
echo ""

echo "📊 SCHEMA.ORG:"
SCHEMA_COUNT=$(grep -l 'schema.org' *.html | wc -l)
echo "Pages with schema.org: $SCHEMA_COUNT/$TOTAL"

echo ""
echo "🔍 MISSING SCHEMA.ORG (critical):"
for f in *.html; do
  if ! grep -q 'schema.org' "$f"; then
    echo "  ⚠ $f — MISSING SCHEMA"
  fi
done
echo ""

echo "⚡ CRITICAL SEO GAPS:"
echo "1. Check for missing canonical tags"
CANON_COUNT=$(grep -l 'rel="canonical"' *.html | wc -l)
echo "   Pages with canonical: $CANON_COUNT/$TOTAL"
[ $CANON_COUNT -eq $TOTAL ] && echo "   ✓ OK" || echo "   ⚠ ADD CANONICAL TO ALL"
echo ""

echo "2. Check robots.txt"
[ -f "robots.txt" ] && echo "   ✓ robots.txt exists" || echo "   ⚠ MISSING robots.txt"
echo ""

echo "3. Check sitemap.xml"
[ -f "sitemap.xml" ] && echo "   ✓ sitemap.xml exists" || echo "   ⚠ MISSING sitemap.xml"
[ -f "sitemap.xml" ] && grep -c '<url>' sitemap.xml | xargs echo "   URLs in sitemap:"
echo ""

echo "4. Mobile meta viewport:"
VIEWPORT=$(grep -l 'viewport' *.html | wc -l)
echo "   Pages with viewport: $VIEWPORT/$TOTAL"
[ $VIEWPORT -eq $TOTAL ] && echo "   ✓ OK" || echo "   ⚠ MISSING on some pages"
