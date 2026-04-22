#!/usr/bin/env python3
"""Build Tier 4 quiz results page."""
import sys

tier4_content = sys.argv[1] if len(sys.argv) > 1 else ""

with open('quiz-results-tier-4.html', 'w') as f:
    f.write(tier4_content)
print(f"Written {len(tier4_content)} chars")
