#!/usr/bin/env python3
"""Build ai-fatigue-recovery-checklist.pdf from the spec."""
from fpdf import FPDF
import os

OUT = os.path.join(os.path.dirname(__file__), 'ai-fatigue-recovery-checklist.pdf')

class ChecklistPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_fill_color(26, 58, 42)
            self.rect(0, 0, 210, 16, 'F')
            self.set_font('Helvetica', 'B', 13)
            self.set_text_color(143, 188, 143)
            self.cell(0, 10, 'THE CLEARING - AI Fatigue Recovery Checklist', border=0, new_x='LMARGIN', new_y='NEXT', align='C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'clearing-ai.com | The Dispatch: clearing-ai.com/newsletter.html - Free forever. No account required.', border=0, new_x='LMARGIN', new_y='NEXT', align='C')

pdf = ChecklistPDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, 'For software engineers who are shipping more and learning less.', border=0, new_x='LMARGIN', new_y='NEXT', align='C')
pdf.ln(4)

pdf.set_fill_color(248, 248, 248)
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(0, 5, 'Check all that apply. The more checked, the more intentional recovery needs to be.', border=0, align='L', fill=True)
pdf.ln(6)

pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 7, 'PART 1: Are You Experiencing AI Fatigue?', border=0, new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

checks = [
    "I can't remember the last time I built something from scratch without AI.",
    "I feel productive but not satisfied with my work.",
    "Sunday dread doesn't match the actual difficulty of Monday.",
    "I can't explain why AI-generated code works the way it does.",
    "I've noticed gaps in skills I used to have cold confidence in.",
    "I'm learning less week over week while shipping more.",
    "I feel like a coordinator between AI outputs and actual work.",
    "The gap between 'working' and 'building' has become noticeable.",
    "I'm considering leaving tech - not because of workload, but because the work feels hollow.",
    "I feel guilty for being ungrateful for AI tools that make me tired.",
]

for item in checks:
    pdf.set_x(10)
    pdf.set_font('ZapfDingbats', '', 12)
    pdf.cell(8, 6.5, 'o', border=0)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_x(18)
    pdf.multi_cell(0, 6.5, item, border=0, align='L')
    pdf.ln(1)

pdf.ln(6)
pdf.set_fill_color(232, 240, 232)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(45, 90, 61)
pdf.cell(0, 6.5, 'SCORE INTERPRETATION', border=0, new_x='LMARGIN', new_y='NEXT', fill=True)
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(40, 40, 40)
scores = [
    ('1-3', 'Mild fatigue - you are managing, but watch for escalation.'),
    ('4-6', 'Real fatigue - time to build in recovery practices.'),
    ('7-10', 'Deep fatigue - this checklist is your starting point, not your whole plan.'),
]
for score, desc in scores:
    pdf.set_x(10)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.cell(14, 6, score, border=0)
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_x(24)
    pdf.multi_cell(0, 6, desc, border=0, align='L')

pdf.add_page()

pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 7, 'PART 2: 30-Day Recovery Practices', border=0, new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

sections = [
    ('A. DAILY NON-NEGOTIABLES (do every weekday)', [
        '20 minutes of no-AI coding (before 10am if possible)',
        'Explain one piece of AI code out loud before accepting it',
        'Note one gap between what AI did and what you would have done',
        'End of day: write one sentence about what you built today (not shipped)',
    ]),
    ('B. WEEKLY RESET (once per week)', [
        '90-minute deep work block: build something small, no AI',
        "Review your 'AI gaps logged' - count them, notice patterns",
        'Read one part of a codebase you own without AI assist',
        'Ask: Could I build my current project core feature from scratch?',
    ]),
    ('C. SIGNS YOU NEED A BIGGER RESET', [
        'Sleep disruption from work anxiety',
        'Physical symptoms (back pain, headaches, eye strain) increasing',
        'Dread building before weekends, not just Sundays',
        'Skills you used to trust - debugging, architecture, reading code - feeling shaky',
        "You've stopped explaining code to yourself out loud",
    ]),
]

for sec_title, items in sections:
    pdf.set_fill_color(26, 58, 42)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(240, 240, 240)
    pdf.cell(0, 7, sec_title, border=0, new_x='LMARGIN', new_y='NEXT', fill=True)
    pdf.set_font('ZapfDingbats', '', 12)
    pdf.set_text_color(40, 40, 40)
    for item in items:
        pdf.set_x(10)
        pdf.set_font('ZapfDingbats', '', 12)
        pdf.cell(8, 6, 'o', border=0)
        pdf.set_font('Helvetica', '', 9.5)
        pdf.set_x(18)
        pdf.multi_cell(0, 6, item, border=0, align='L')
    pdf.ln(4)

pdf.ln(2)
pdf.set_fill_color(255, 242, 230)
pdf.set_font('Helvetica', 'B', 9.5)
pdf.set_text_color(160, 80, 0)
pdf.cell(0, 6.5, 'If 3+ of Section C signs are true: This checklist is not enough.', border=0, new_x='LMARGIN', new_y='NEXT', fill=True)
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(100, 80, 0)
pdf.multi_cell(0, 5.5, 'Visit clearing-ai.com/mental-health.html for professional support resources - therapists, crisis lines, and EAP contacts.', border=0, align='L', fill=True)

pdf.output(OUT)
print(f"PDF written to {OUT}")