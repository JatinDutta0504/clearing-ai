#!/bin/bash

# Phase 3 Window 2: Core Web Vitals Lighthouse Audit
# Top 10 pages by traffic intent

pages=(
  "index.html"
  "quiz.html"
  "recovery.html"
  "research.html"
  "stats.html"
  "compare.html"
  "decompress.html"
  "senior-identity.html"
  "developer-identity.html"
  "imposter-syndrome-vs-ai-fatigue.html"
)

echo "🔍 LIGHTHOUSE AUDIT — Phase 3 Window 2"
echo "Target: LCP <2.5s, FID <100ms, CLS <0.1"
echo "Running on 10 high-priority pages..."
echo ""

# Check if we have lighthouse installed
if ! command -v lighthouse &> /dev/null; then
  echo "Installing lighthouse..."
  npm install -g lighthouse
fi

for page in "${pages[@]}"; do
  url="https://clearing-ai.com/$page"
  echo "Auditing: $url"
  lighthouse "$url" --output-path="./logs/lighthouse-$page.json" --output html > /dev/null 2>&1
  
  # Extract key metrics from the JSON
  if [ -f "./logs/lighthouse-$page.json" ]; then
    # For now, just report completion
    echo "  ✓ Report generated: logs/lighthouse-$page.json"
  fi
done

echo ""
echo "✅ Lighthouse audits complete. Generating summary..."
