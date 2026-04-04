#!/usr/bin/env python3
"""Add mailto fallback to ai-fatigue-checklist.html and testimonials.html"""

# === FIX 1: ai-fatigue-checklist.html ===
with open('ai-fatigue-checklist.html', 'r') as f:
    content = f.read()

# Add mailto fallback CSS
css_block = """.mailto-fallback{display:none;margin-top:1rem;padding:1.25rem;background:rgba(63,185,80,0.1);border:1px solid rgba(63,185,80,0.25);border-radius:8px}
.mailto-fallback .mf-title{font-weight:700;font-size:0.9rem;color:var(--forest-pale, #c8e6c8);margin-bottom:0.4rem}
.mailto-fallback .mf-note{font-size:0.78rem;color:rgba(200,221,200,0.6);margin-bottom:0.75rem}
.mailto-fallback a{display:inline-flex;align-items:center;gap:0.3rem;background:rgba(63,185,80,0.15);color:#3fb950;padding:0.55rem 1rem;border-radius:6px;text-decoration:none;font-size:0.82rem;font-weight:600;border:1px solid rgba(63,185,80,0.3);transition:background 0.2s}
.mailto-fallback a:hover{background:rgba(63,185,80,0.25)}"""

# Inject CSS before closing </style> tag
old_style_end = "    .cta-success{display:none;color:var(--forest-pale);font-size:1rem;text-align:center;padding:1rem}"
new_style_end = old_style_end + "\n" + css_block
content = content.replace(old_style_end, new_style_end)

# TOP FORM: Add mailto fallback after </form> (first occurrence, in top cta-block)
old_top_form_end = """      </form>
      <div class="cta-success" id="cta-success-top" aria-live="polite">Check your inbox the checklist is on its way.</div>
    </div>
  </section>"""

new_top_form_end = """      </form>
      <div class="mailto-fallback" id="mailto-fallback-top">
        <div class="mf-title">📬 Can't use the form? Subscribe directly:</div>
        <div class="mf-note">Email us and we'll add you manually. First Dispatch goes out Sunday.</div>
        <a id="mailto-link-top" href="mailto:hello@clearing-ai.com?subject=Newsletter%20Signup%20from%20AI%20Fatigue%20Checklist&body=Hi%2C%0A%0AI%20would%20like%20to%20subscribe%20to%20The%20Dispatch.%0A%0AMy%20email%3A%20">Send email to subscribe →</a>
      </div>
      <div class="cta-success" id="cta-success-top" aria-live="polite">Check your inbox the checklist is on its way.</div>
    </div>
  </section>"""

if old_top_form_end in content:
    content = content.replace(old_top_form_end, new_top_form_end, 1)
    print("✅ Fixed top form in ai-fatigue-checklist.html")
else:
    print("⚠️  Could not find top form end pattern in ai-fatigue-checklist.html")

# BOTTOM FORM: Add mailto fallback after </form> (in bottom-cta section)
old_bottom_form_end = """      </form>
      <div class="cta-success" id="cta-success-bottom" aria-live="polite">Welcome. Your first Dispatch arrives Sunday.</div>
    </div>
  </section>
</main>"""

new_bottom_form_end = """      </form>
      <div class="mailto-fallback" id="mailto-fallback-bottom">
        <div class="mf-title">📬 Can't use the form? Subscribe directly:</div>
        <div class="mf-note">Email us and we'll add you manually. First Dispatch goes out Sunday.</div>
        <a id="mailto-link-bottom" href="mailto:hello@clearing-ai.com?subject=Newsletter%20Signup%20from%20AI%20Fatigue%20Checklist&body=Hi%2C%0A%0AI%20would%20like%20to%20subscribe%20to%20The%20Dispatch.%0A%0AMy%20email%3A%20">Send email to subscribe →</a>
      </div>
      <div class="cta-success" id="cta-success-bottom" aria-live="polite">Welcome. Your first Dispatch arrives Sunday.</div>
    </div>
  </section>
</main>"""

if old_bottom_form_end in content:
    content = content.replace(old_bottom_form_end, new_bottom_form_end, 1)
    print("✅ Fixed bottom form in ai-fatigue-checklist.html")
else:
    print("⚠️  Could not find bottom form end pattern in ai-fatigue-checklist.html")

# Add JS to detect YOUR_FORM_ID and show mailto fallback
old_js_check = "document.addEventListener('DOMContentLoaded',function(){render();"
new_js_check = """// Show mailto fallback if Formspree not configured
(function(){
  var forms = document.querySelectorAll('form[id^="checklist-form"]');
  forms.forEach(function(form){
    var action = form.getAttribute('action') || '';
    if (action.indexOf('YOUR_FORM_ID') !== -1) {
      var parent = form.parentElement;
      if (parent) {
        var mfTop = parent.querySelector('#mailto-fallback-top');
        var mfBottom = parent.querySelector('#mailto-fallback-bottom');
        if (mfTop) mfTop.style.display = 'block';
        if (mfBottom) mfBottom.style.display = 'block';
        // Also prefill mailto with email if user typed one
        var emailInput = form.querySelector('input[type="email"]');
        if (emailInput && emailInput.value) {
          var email = encodeURIComponent(emailInput.value);
          var mfLink = parent.querySelector('#mailto-link-top') || parent.querySelector('#mailto-link-bottom');
          if (mfLink) mfLink.href = mfLink.href + email;
        }
      }
    }
  });
  // Prefill mailto links when email is typed
  document.querySelectorAll('input[type="email"]').forEach(function(input){
    input.addEventListener('input', function(){
      var email = encodeURIComponent(this.value);
      var form2 = this.closest('form');
      if (form2) {
        var action = form2.getAttribute('action') || '';
        if (action.indexOf('YOUR_FORM_ID') !== -1) {
          var parent = form2.parentElement;
          var link = parent.querySelector('#mailto-link-top') || parent.querySelector('#mailto-link-bottom');
          if (link && this.value && this.value.includes('@')) {
            var base = link.href.split('&body=')[0];
            link.href = base + '&body=Hi%2C%0A%0AI%20would%20like%20to%20subscribe%20to%20The%20Dispatch.%0A%0AMy%20email%3A%20' + email;
          }
        }
      }
    });
  });
})();

document.addEventListener('DOMContentLoaded',function(){render();"""

content = content.replace(old_js_check, new_js_check)
print("✅ Injected mailto fallback JS into ai-fatigue-checklist.html")

with open('ai-fatigue-checklist.html', 'w') as f:
    f.write(content)


# === FIX 2: testimonials.html ===
with open('testimonials.html', 'r') as f:
    content = f.read()

# Add mailto fallback CSS for testimonials
testimonial_css = """.story-mailto-fallback{display:none;margin-top:1rem;padding:1.25rem;background:rgba(63,185,80,0.1);border:1px solid rgba(63,185,80,0.25);border-radius:8px}
.story-mailto-fallback .smf-title{font-weight:700;font-size:0.9rem;color:#c8e6c8;margin-bottom:0.4rem}
.story-mailto-fallback .smf-note{font-size:0.78rem;color:rgba(200,221,200,0.6);margin-bottom:0.75rem}
.story-mailto-fallback a{display:inline-flex;align-items:center;gap:0.3rem;background:rgba(63,185,80,0.15);color:#3fb950;padding:0.55rem 1rem;border-radius:6px;text-decoration:none;font-size:0.82rem;font-weight:600;border:1px solid rgba(63,185,80,0.3);transition:background 0.2s}
.story-mailto-fallback a:hover{background:rgba(63,185,80,0.25)}"""

# Find the style block and inject CSS before </style>
# Look for the story-submit section pattern
old_test_style_end = ".story-submit-btn:hover{background:#2d8a3e}"
if old_test_style_end in content:
    content = content.replace(old_test_style_end, old_test_style_end + "\n" + testimonial_css)
    print("✅ Added mailto fallback CSS to testimonials.html")
else:
    print("⚠️  Could not find style end pattern in testimonials.html")

# Find the story-form and add mailto fallback after the submit button / before closing tag
# The form has </form> followed by the success div
old_story_form_end = """        </form>
        <div class="story-success" id="story-success" role="alert" aria-live="polite"></div>
      </div>
    </div>
  </section>"""

new_story_form_end = """        </form>
        <div class="story-mailto-fallback" id="story-mailto-fallback">
          <div class="smf-title">📬 Can't submit the form? Share your story via email:</div>
          <div class="smf-note">We'll keep it anonymous unless you say otherwise. All submissions are reviewed before publication.</div>
          <a id="story-mailto-link" href="mailto:hello@clearing-ai.com?subject=Story%20Submission%20from%20The%20Clearing&body=Hi%2C%0A%0AI%20would%20like%20to%20share%20my%20story%20with%20The%20Clearing.%0A%0A">Email us your story →</a>
        </div>
        <div class="story-success" id="story-success" role="alert" aria-live="polite"></div>
      </div>
    </div>
  </section>"""

if old_story_form_end in content:
    content = content.replace(old_story_form_end, new_story_form_end, 1)
    print("✅ Added mailto fallback to story-form in testimonials.html")
else:
    print("⚠️  Could not find story-form end pattern in testimonials.html")
    # Try alternate pattern
    alt_pattern = """        </form>
        <div class="story-success\" id=\"story-success\""
    if alt_pattern in content:
        print("  Found alternate pattern, but skipping (already fixed?)")

# Add JS to detect YOUR_FORM_ID and show mailto fallback for testimonials
old_test_js = """    var form = document.getElementById('story-form');
    form.onsubmit ="""

new_test_js = """    // Show mailto fallback if Formspree not configured
    (function(){
      var form = document.getElementById('story-form');
      if (!form) return;
      var action = form.getAttribute('action') || '';
      if (action.indexOf('YOUR_FORM_ID') !== -1) {
        var mf = document.getElementById('story-mailto-fallback');
        if (mf) mf.style.display = 'block';
      }
    })();

    var form = document.getElementById('story-form');
    form.onsubmit ="""

if "var form = document.getElementById('story-form');\n    form.onsubmit" in content:
    content = content.replace("var form = document.getElementById('story-form');\n    form.onsubmit =", new_test_js)
    print("✅ Injected mailto fallback JS into testimonials.html")
elif old_test_js in content:
    content = content.replace(old_test_js, new_test_js)
    print("✅ Injected mailto fallback JS into testimonials.html (alt)")
else:
    print("⚠️  Could not find testimonials JS pattern")

with open('testimonials.html', 'w') as f:
    f.write(content)

print("\n🎉 All fixes applied!")
