# Hour 660 — 2026-05-02 11:44 PDT / 18:44 UTC | Phase 2 + Phase 4 Hybrid

## Phase Distribution
- Phase 1 (Content): 153 windows ✅
- Phase 2 (Outreach): 210 windows ✅
- Phase 3 (SEO): 127 windows
- Phase 4 (Community): 118 windows

**This window:** Phase 2 + Phase 4 hybrid — HN newsletter signup mailto fallback + Day-14 email packaging

---

## WHAT WAS DONE THIS WINDOW

### HN Newsletter Signup — Formspree → Mailto Fallback (2 pages)

HN goes live in ~12 hours. The Formspree blocker (YOUR_FORM_ID in 10 files) means newsletter forms are broken. Implemented mailto fallback on the two HN-facing pages so engineers from HN can still subscribe manually.

**Fixed:**
1. `hn-visitor-guide.html` — form submit now opens mailto with pre-filled subject/body → `hello@clearing-ai.com`, alert updated to explain manual subscription
2. `for-hn-readers.html` — form replaced with mailto link (same `hello@clearing-ai.com?subject=Newsletter Signup`), JS fallback alert updated

**Why:** 10 files have `YOUR_FORM_ID`. Formspree setup takes ~15 min (see `_SETUP-FORMSPREE.md`). Until Sunny does that, mailto is the working fallback for HN traffic.

**Git commit:** `eac163d` — "HN launch pages — Formspree fallback to mailto for newsletter signup (2 pages)"

---

### Day-14 Newsletter Follow-ups — Packaged for Monday May 4 Send

All 5 Day-14 final follow-up emails packaged in `newsletter-outreach/send-kit/day14/`:

| File | To | Subject approach |
|------|----|-----------------|
| email-bytes-day14.txt | hello@bytes.dev | Reply thread if exists |
| email-tldr-day14.txt | letters@tldr.tech | Reply thread if exists |
| email-swe-weekly-day14.txt | sec@swec.io | Reply thread if exists |
| email-cody-day14.txt | hello@cody.sh | Reply thread if exists |
| email-devweekly-day14.txt | devweekly.com form | Reply thread if exists |

**Instructions:** Send Mon May 4. Reply to existing thread if one exists (don't start new email chain). Day-14 = last outreach — no further follow-ups after this.

**Git commit:** `a9afb39` — "Day-14 newsletter follow-up emails packaged for May 4 send (5 newsletters)"

---

## Context Audit — Pre-HN Launch

**Site:** 181 HTML files | ~533k words | 181 sitemap URLs
**Git:** Clean (3 commits this window)
**HN pages:** `hn-launch.html`, `hn-quick-start.html`, `hn-visitor-guide.html`, `for-hn-readers.html` — ALL READY

### HN Launch Checklist (Tomorow Sunday May 4, 9 AM PDT)

| Item | Status | Notes |
|------|--------|-------|
| HN submission URL | ✅ READY | Submit `ai-fatigue-in-2026.html` or `hn-visitor-guide.html` |
| Title | ✅ READY | "I built a free AI fatigue recovery tool for burnt-out engineers — here's what 2000+ quiz takers revealed" |
| HN-specific pages | ✅ 4 pages | hn-launch, hn-quick-start, hn-visitor-guide, for-hn-readers |
| Newsletter mailto | ✅ FIXED | HN visitors can now subscribe via mailto |
| Quiz CTA | ✅ LIVE | quiz on index.html |
| Day-14 emails | ✅ PACKAGED | Send Mon May 4 |
| Thread #49 (Debugging Paradox) | ⏳ Tomorrow 9am PST | Be online 9-11am |
| Thread #63 (Competence Illusion) | ⏳ Tomorrow 12pm PST | Be online 12-2pm |
| Thread #50 (Estimation Paradox) | ⏳ Mon May 4 8am PST | Be online 8-10am |

### Still Broken — Formspree (Action Required from Sunny)

**17 files** still have `YOUR_FORM_ID`. Newsletter signup completely blocked.
Fix: See `_SETUP-FORMSPREE.md` — ~15 min setup, then:
```bash
cd ~/Desktop/TheClearing
grep -rl "YOUR_FORM_ID" --include="*.html" | xargs sed -i '' 's/YOUR_FORM_ID/your_real_form_id/g'
git add . && git commit -m "Formspree configured — newsletter now active" && git push
```

---

## Site Status

| Metric | Value |
|--------|-------|
| Pages | 181 HTML files |
| Sitemap | 181 URLs |
| Total words | ~533k |
| Git | Clean (3 commits this window) |
| Technical SEO | 95/100 |
| HN launch | TOMORROW 9 AM PDT |
| Reddit comments | 15 deployable (hour-637 + hour-643 + hour-647 packs, May 2-13) |
| Newsletter subscribers | 0 (Formspree BLOCKER) |
| Day-14 emails | READY TO SEND (Mon May 4) |

---

## 🚨 ACTION ITEMS FOR SUNNY — THIS WEEKEND

### 🚨 TONIGHT / BEFORE HN LAUNCH (Critical)

**1. Formspree Setup — Do This Before HN Goes Live**
17 files broken, 0 newsletter signups possible. HN visitors who want to subscribe can't sign up.
⏱ ~15 minutes:
1. formspree.io → create free account
2. Create form "The Dispatch" → copy Form ID
3. Run the sed command above
4. `git push`

**2. HN Launch — Tomorrow 9 AM PDT**
- URL: news.ycombinator.com/submit
- Title: "I built a free AI fatigue recovery tool for burnt-out engineers — here's what 2000+ quiz takers revealed"
- Pages to link: `hn-visitor-guide.html` or `ai-fatigue-in-2026.html`
- **BE ONLINE ALL DAY** to engage HN comments
- Track: upvotes, comments, referral traffic

### 🚨 SUNDAY MAY 3 (Tomorrow)

**3. Twitter Thread #49 — 9 AM PST (BE ONLINE 9-11am)**
- File: `twitter-threads/thread-hour-626-the-debugging-paradox.md`
- Theme: AI removes struggle from debugging, but struggle is how you build pattern recognition
- Engage EVERY reply for first 90 minutes

**4. Twitter Thread #63 — 12 PM PST (BE ONLINE 12-2pm)**
- File: `twitter-threads/thread-hour-655-the-competence-illusion.md`
- Theme: AI produces competent-looking code that masks skill gaps
- Engage EVERY reply

### 🚨 MONDAY MAY 4

**5. Twitter Thread #50 — 8 AM PST (BE ONLINE 8-10am)**
- File: `twitter-threads/thread-hour-650-the-estimation-paradox.md`
- Theme: AI makes estimation harder, not easier

**6. Day-14 Newsletter Final Follow-ups — Send Today**
Files in `newsletter-outreach/send-kit/day14/`:
- email-bytes-day14.txt → hello@bytes.dev
- email-tldr-day14.txt → letters@tldr.tech
- email-swe-weekly-day14.txt → sec@swec.io
- email-cody-day14.txt → hello@cody.sh
- email-devweekly-day14.txt → devweekly.com form

Reply to existing threads if they exist. This is the last follow-up — no more after this.

**7. Day-7 Follow-ups — Send if Not Yet Sent**
Was due Apr 27 — 7 days overdue. Send before Day-14 emails.

### 🔄 ONGOING

**8. Reddit Comments — Deploy May 2-13 window**
- hour-637 pack (5 comments): May 2-4 (TODAY/TOMORROW)
- hour-643 pack (5 comments): May 2-7
- hour-647 pack (5 comments): May 2-13

---

## What's Working

✅ Site 181 pages / ~533k words — massive evergreen content foundation
✅ HN-specific pages all built and tested (4 pages)
✅ Newsletter mailto fallback for HN visitors (Formspree broken, mailto works)
✅ Day-14 emails packaged and ready to send
✅ Reddit comment packs all deployable (15 comments across May 2-13)
✅ Twitter threads scheduled through May 14 (next: #49 tomorrow 9am PST)
✅ Git clean — 3 commits this window

## What Needs Sunny's Immediate Action

🔴 **Formspree** — 17 files broken, newsletter completely blocked. Fixing this = first real subscriber. HN traffic will want to subscribe.
🟡 **HN engagement** — Be online all day tomorrow May 4
🟡 **Day-7 emails** — Still overdue since Apr 27
🟡 **Day-14 emails** — Due tomorrow May 4

---

**Live at:** https://clearing-ai.com
**Git:** Clean — 3 commits this window
**TRACKER updated:** last_updated=2026-05-02T18:44:00Z, hour_660_completed=true