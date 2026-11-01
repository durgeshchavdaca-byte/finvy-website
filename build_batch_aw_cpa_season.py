# -*- coding: utf-8 -*-
"""Batch AW: 2027 US tax season deadlines and outsourcing set-up timeline for CPA firms."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "us-tax-season-2027-deadlines-cpa-firms-outsourcing-plan"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


TABLE = ("<table><thead><tr><th>Return (calendar-year filers)</th><th>Due</th><th>Extended due date</th></tr></thead><tbody>"
         "<tr><td>Forms W-2 and 1099-NEC</td><td>1 February 2027 (31 January falls on a Sunday)</td><td>&mdash;</td></tr>"
         "<tr><td>Form 1065 (partnerships) and Form 1120-S (S corporations)</td><td>15 March 2027</td><td>15 September 2027 (Form 7004)</td></tr>"
         "<tr><td>Form 1040 (individuals)</td><td>15 April 2027</td><td>15 October 2027 (Form 4868)</td></tr>"
         "<tr><td>Form 1120 (C corporations), including pro forma 1120 with Form 5472 for foreign-owned LLCs</td><td>15 April 2027</td><td>15 October 2027 (Form 7004)</td></tr>"
         "<tr><td>FBAR (FinCEN Form 114)</td><td>15 April 2027</td><td>15 October 2027 (automatic)</td></tr></tbody></table>")

sections = [
    ("/ The 2027 filing-season dates", "Calendar-year returns for tax year 2026.",
     TABLE + "<p>An extension extends the time to file, not to pay. Fiscal-year entities follow their own dates.</p>"),
    ("/ When to line up outsourced help", "Work back from the deadlines.",
     "<ol><li><strong>November to December 2026</strong>: choose the provider, sign the confidentiality agreement, add the third-party provider clause to engagement letters, add the Section 7216 offshore consent to organizers, update the written information security plan, set up remote access and test with sample returns.</li>"
     "<li><strong>January 2027</strong>: W-2 and 1099 preparation, year-end bookkeeping clean-up and reconciliations.</li>"
     "<li><strong>February to mid-March 2027</strong>: Forms 1065 and 1120-S, K-1s.</li>"
     "<li><strong>Mid-March to mid-April 2027</strong>: Forms 1040 and 1120, Form 5472, FBARs; extensions for the rest.</li>"
     "<li><strong>May to October 2027</strong>: extended returns, with peaks before 15 September and 15 October.</li></ol>"
     "<p>Firms that start onboarding in January usually lose the first weeks of the season to access and consent paperwork.</p>"),
    ("/ What we take off your desk", "Prepared in your software, for your review.",
     ul("Individual and business return preparation (1040, 1065, 1120-S, 1120) with workpapers.",
        "1099 preparation and year-end bookkeeping clean-up in QuickBooks Online or Xero.",
        "Form 5472 and pro forma 1120 for foreign-owned single-member LLCs.",
        "Returns for clients with India exposure: NRIs, Indian income, FBAR and Form 8938 items.") +
     '<p>See <a href="outsourced-tax-preparation-accounting-for-us-cpa-firms-india.html">how outsourcing works for US CPA firms</a> and the <a href="us-cpa-firm-outsource-tax-returns-india-section-7216-consent-checklist.html">Section 7216 consent checklist</a>.</p>'
     '<p><strong>Sources:</strong> <a href="https://www.irs.gov/publications/p509" rel="nofollow noopener" target="_blank">IRS Publication 509, Tax Calendars</a>; '
     '<a href="https://www.fincen.gov/report-foreign-bank-and-financial-accounts" rel="nofollow noopener" target="_blank">FinCEN: FBAR</a>.</p>'
     "<p><em>Last updated: 1 November 2026. Check IRS announcements for disaster-area relief and any changes to these dates.</em></p>"),
]

faqs = [
    ("When are 2026 partnership and S corporation returns due?", "Calendar-year Forms 1065 and 1120-S are due on 15 March 2027, or 15 September 2027 with a Form 7004 extension."),
    ("When are 2026 individual returns due?", "Form 1040 is due on 15 April 2027, or 15 October 2027 with Form 4868. Tax is still due by 15 April."),
    ("When are 1099-NEC forms due for 2026?", "1 February 2027, because 31 January 2027 falls on a Sunday."),
    ("When should a CPA firm set up outsourcing for busy season?", "In November or December, so that consents, engagement letters, the security plan and system access are ready before January."),
    ("Can BQP add capacity for the 2027 season?", "Yes: return preparation, bookkeeping and 1099s inside your systems, for your review. " + CONTACT),
]

html = page(slug=SLUG,
            title="US Tax Season 2027 Deadlines for CPA Firms, and When to Line Up Outsourced Help",
            description="2027 filing-season deadlines for tax year 2026: 1099-NEC/W-2 1 February, 1065/1120-S 15 March, 1040/1120/FBAR 15 April, extensions 15 September and 15 October. A November-to-April timeline for setting up outsourced tax preparation.",
            keywords="tax season 2027 deadlines, 1065 due date 2027, 1120-S due date March 15 2027, 1040 due date April 15 2027, 1099-NEC due date 2027, CPA firm busy season outsourcing, seasonal tax preparer outsourcing",
            hero_kicker="/ US CPA Firms &middot; Busy Season &middot; Updated 2026-11-01",
            hero_title_html="US Tax Season 2027 Deadlines for CPA Firms, <em>and when to line up help.</em>",
            hero_lead="For tax year 2026, W-2s and 1099-NECs are due on 1 February 2027, partnership and S corporation returns on 15 March, and individual and C corporation returns and FBARs on 15 April, with extensions to 15 September and 15 October. Firms that want outsourced capacity should set it up in November and December, before the season starts.",
            sections=sections, faqs=faqs,
            related=[("outsourced-tax-preparation-accounting-for-us-cpa-firms-india.html", "Related", "Outsourcing for US CPA firms"),
                     ("us-cpa-firm-outsource-tax-returns-india-section-7216-consent-checklist.html", "Related", "Section 7216 consent checklist")],
            cta_headline="Planning busy-season capacity?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AW complete")
