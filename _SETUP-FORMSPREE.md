# Formspree Setup Guide — The Clearing Newsletter

**Time needed:** ~3 minutes  
**Cost:** Free (up to 50 submissions/month)  
**What this fixes:** Email signup forms on subscribe.html, newsletter.html, community-hub.html, testimonials.html, recovery-toolkit.html, and 7 other pages.

---

## Why Formspree?

The newsletter forms currently use a `mailto:` fallback (opens your email app). That's functional but clunky. Formspree gives you a proper invisible form — subscribers never leave the page.

Formspree forwards submissions to any email address you own (e.g. your personal Gmail).

---

## Step 1: Create a Formspree Account

1. Go to **[formspree.io](https://formspree.io)**
2. Click **"Get Started"** → Sign up with GitHub or email
3. Choose the **Free plan** (50 submissions/month — more than enough to start)

---

## Step 2: Create Your Form

1. In your Formspree dashboard, click **"+ New Form"**
2. **Name it:** `The Dispatch`
3. **Confirm your email** — Formspree will send a confirmation email to the address you provide. Click the link inside to activate the form.
4. You'll land on your form's page. Look at the URL — it ends with your **Form ID**:
   ```
   https://formspree.io/f/xyzabc123
                              ^^^^^^^^
                              This is your Form ID
   ```

---

## Step 3: Add Your Form ID to These Files

Replace `YOUR_FORM_ID` with your actual Form ID in each file:

| File | Line | What to replace |
|------|------|-----------------|
| `subscribe.html` | ~186 | `https://formspree.io/f/YOUR_FORM_ID` |
| `newsletter.html` | ~834 | `https://formspree.io/f/YOUR_FORM_ID` |
| `community-hub.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `testimonials.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `recovery-toolkit.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `ai-fatigue-checklist.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `ai-fatigue-quick-start.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `freelance-engineer-ai-fatigue.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `hn-visitor-guide.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |
| `linkedin.html` | (grep for it) | `https://formspree.io/f/YOUR_FORM_ID` |

**Quick find command:**
```bash
grep -rl "YOUR_FORM_ID" /path/to/TheClearing/*.html
```

---

## Step 4: Verify It Works

1. Open `subscribe.html` in your browser
2. Fill in a test email (use a real address you can check)
3. Click Subscribe
4. You should see "You're in." success message
5. Check your email inbox — you should receive the Formspree confirmation, then the submission

---

## After Setup — What Happens

When someone subscribes:
1. Formspree receives the submission
2. Formspree emails you (hello@clearing-ai.com or wherever you pointed it)
3. The email contains: name, email, timestamp
4. You manually add them to your newsletter list (or connect Formspree to Mailchimp/Zapier for automation)

**Tip:** Connect Formspree to Zapier → Gmail filter rule to automatically star/tracking-label new subscribers.

---

## FAQ

**Q: What if I already have a newsletter platform (Mailchimp, ConvertKit, Buttondown)?**  
A: Replace the Formspree action with your platform's form embed. The JS mailto fallback logic still applies — if the form action isn't recognized, it falls back to mailto.

**Q: Can I see all submissions in one place?**  
A: Yes — Formspree dashboard shows all submissions. You can also forward to Slack, Zap to a spreadsheet, etc.

**Q: 50/month seems low.**  
A: The free plan is for small sites. If you need more, Formspree's paid plans start at $16/month for 500 submissions. But start free — you'll know when you need more.

**Q: The mailto is working fine. Do I need to fix this?**  
A: No — the mailto fallback was intentionally added so the forms work right now. Formspree just makes the UX smoother. Fix it when you have time.

---

**Last updated:** Hour 421 (2026-04-18)  
**Files needing update:** 10 HTML files with `YOUR_FORM_ID` placeholder
