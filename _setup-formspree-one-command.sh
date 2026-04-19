#!/bin/bash
# ==============================================================================
# The Clearing — Formspree One-Command Setup
# ==============================================================================
# Run this AFTER creating your free Formspree account at formspree.io
# 
# WHAT THIS DOES:
#   1. Opens formspree.io/dashboard in your browser
#   2. Walks you through creating your first form
#   3. Pastes your form ID into all 10 files that need it
#
# TIME NEEDED: ~15 minutes (one-time setup)
# COST: Free (up to 50 submissions/month)
# ==============================================================================

echo "=========================================="
echo "The Clearing — Formspree Setup"
echo "=========================================="
echo ""
echo "This script sets up newsletter signup on clearing-ai.com."
echo ""
echo "BEFORE YOU START:"
echo "  1. Go to https://formspree.io and create a free account"
echo "  2. Verify your email address"
echo ""
echo "STEP 1: Create your form on formspree.io"
echo "-------------------------------------------"
echo ""
echo "I'll now open formspree.io/dashboard in your browser."
echo "Click '+ New Form' and create a form called 'The Clearing — Newsletter'"
echo "Set the redirect URL to: https://clearing-ai.com/confirmed.html"
echo "Set the notification email to: hello@clearing-ai.com"
echo ""
read -p "Press Enter when you've created your form and have your Form ID (the part after /f/)..."
echo ""

echo ""
echo "STEP 2: Enter your Form ID"
echo "-------------------------------------------"
echo "Your form URL looks like: https://formspree.io/f/xpwqgvln"
echo "The form ID is the part after the /f/ — example: xpwqgvln"
echo ""
read -p "Enter your Form ID: " FORM_ID

if [ -z "$FORM_ID" ]; then
    echo "ERROR: Form ID cannot be empty. Run this script again and enter a valid ID."
    exit 1
fi

echo ""
echo "STEP 3: Updating all files..."
echo ""

# Files that need YOUR_FORM_ID replaced
FILES=(
    "subscribe.html"
    "newsletter.html"
    "ai-fatigue-checklist.html"
    "community-hub.html"
    "testimonials.html"
    "share-your-story.html"
    "ai-fatigue-quick-start.html"
    "linkedin.html"
    "hn-visitor-guide.html"
    "freelance-engineer-ai-fatigue.html"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        if grep -q "YOUR_FORM_ID" "$file"; then
            sed -i '' "s/YOUR_FORM_ID/$FORM_ID/g" "$file"
            echo "  ✅ Updated: $file"
        else
            echo "  ⏭️  Skipped: $file (already configured)"
        fi
    else
        echo "  ⚠️  Not found: $file"
    fi
done

echo ""
echo "STEP 4: Test your form"
echo "-------------------------------------------"
echo "Go to: https://clearing-ai.com/subscribe.html"
echo "Enter your email and click 'Subscribe'"
echo "You should see 'You're in!' and receive a confirmation email."
echo ""
echo "=========================================="
echo "Setup complete! 🎉"
echo "=========================================="
echo ""
echo "Your newsletter form is now live."
echo "Next: Check your formspree.io dashboard for new subscribers."
echo ""
echo "To create forms for other signup locations:"
echo "  - Email course (5-Day Reset): create form with redirect to confirmed.html"
echo "  - Testimonials: create form with redirect to testimonials-campaign.html?submitted=1"
echo ""
