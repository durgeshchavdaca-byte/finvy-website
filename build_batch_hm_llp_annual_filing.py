# -*- coding: utf-8 -*-
"""Batch HM (25 Nov 2026): LLP annual filing guide - Form 11 (annual return, 30 May) and Form 8 (statement of account and
solvency, 30 October), ITR-5, audit thresholds, normal fees by contribution, additional fee multiples (small LLP vs other),
first-year filing, checking filing status, what happens if missed (strike-off risk, penalties).
Demand: sweep ac97 (25 Nov 2026), all 7 markets: "llp annual filing", "llp annual filing fees", "llp annual filing status",
"llp annual filing last date", "llp annual filing late fees", "llp annual filing for first year", "llp annual filing forms",
"llp form 11 purpose", "llp form 11 penalty", "llp form 11 pdf".
Facts (checked 25 Nov 2026): Tally, Razorpay Rize, IndiaFilings and CAclubindia LLP Form 11 / Form 8 guides (30 May,
30 October; contribution-based normal fee); LLP (Amendment) Rules, 2022 additional fee multiples as used on the site's
Form 8 page (llp-form-8-due-30-october-2026-no-extension-late-fee.html); LLP Rules, 2009 rule 24(8) audit threshold
(turnover above Rs 40 lakh or contribution above Rs 25 lakh); small LLP limits (contribution up to Rs 5 crore and turnover
up to Rs 50 crore) under the 2022 rules; MCA General Circular 05/2026 extended only AOC-4 and MGT-7."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026"

C = contact("the LLP name or LLPIN, the date of incorporation, the partners' contribution, the turnover, and which forms and years are pending")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="LLP Legal Requirements and Annual Filing (2026): Form 11 by 30 May, Form 8 by 30 October, Late Fees and Penalty, First-Year Filing, Status Check and Strike-Off (Form 24)",
    em="two MCA forms and one tax return, every year, even with no business.",
    kicker="/ LLP partners and founders &middot; MCA compliance &middot; Updated 2026-11-25",
    lead=("<strong>Every LLP in India files two annual forms with the Ministry of Corporate Affairs and an income tax return, whether or not it did any business.</strong> "
          "Form 11 (annual return of partners and contributions) is due by 30 May, within 60 days of the year-end. Form 8 (statement of account and solvency) is due by 30 October. "
          "The income tax return is ITR-5. The MCA&rsquo;s 2026 extension (General Circular 05/2026) covered only company forms AOC-4 and MGT-7, not LLP forms, so a Form 8 for FY 2025-26 filed after 30 October 2026 already carries additional fees that grow with the delay."),
    sections=[
        ("/ Quick answers", "What LLP partners search for.",
         ul("<strong>What are the LLP annual filing forms?</strong> Form 11 (annual return) and Form 8 (statement of account and solvency) with the MCA, plus ITR-5 with the income tax department.",
            "<strong>What is the last date?</strong> Form 11 by 30 May and Form 8 by 30 October, each year, for the financial year ended 31 March.",
            "<strong>Is filing needed if the LLP had no business?</strong> Yes. Nil-activity LLPs still file Form 11, Form 8 and ITR-5. An LLP that wants to stop must apply to be struck off, not just stop filing.",
            "<strong>What is the purpose of Form 11?</strong> It reports the designated partners and partners, their contributions and changes during the year. Form 8 reports the financial position and the partners&rsquo; statement that the LLP is solvent.",
            "<strong>Is an audit compulsory?</strong> Accounts must be audited if turnover exceeds &#8377;40 lakh or contribution exceeds &#8377;25 lakh in the year. A separate income tax audit applies above the income tax turnover limits.",
            "<strong>How do I check filing status?</strong> On the MCA portal, use View Company / LLP Master Data with the LLPIN to see the latest filing dates, or check the LLP&rsquo;s filings in the public documents service.")),
        ("/ Annual calendar", "FY 2025-26 filings.",
         table(["Filing", "What it covers", "Due date", "Signed or certified by"], [
             ["Form 11", "Annual return: partners, contributions, changes", "30 May 2026", "Designated partner; certified by a practising professional where contribution exceeds &#8377;50 lakh or turnover exceeds &#8377;5 crore"],
             ["Form 8", "Statement of account and solvency", "30 October 2026", "Designated partners; certified by a practising professional"],
             ["ITR-5", "Income tax return of the LLP", "31 July (no audit) / audit cases as notified", "Designated partner"],
             ["DIR-3 KYC", "KYC of each designated partner&rsquo;s DIN, now once every three years", "30 June (in the KYC year)", "Each designated partner"]])
         + '<p>More on the Form 8 deadline this year: ' + L("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "LLP Form 8 due date and late fee") + '.</p>'),
        ("/ Fees and late fees", "Normal fee by contribution, then multiples for delay.",
         table(["Partners' contribution", "Normal fee per form"], [
             ["Up to &#8377;1 lakh", "&#8377;50"],
             ["&#8377;1 lakh to &#8377;5 lakh", "&#8377;100"],
             ["&#8377;5 lakh to &#8377;10 lakh", "&#8377;150"],
             ["&#8377;10 lakh to &#8377;25 lakh", "&#8377;200"],
             ["&#8377;25 lakh to &#8377;1 crore", "&#8377;400"],
             ["Above &#8377;1 crore", "&#8377;600"]])
         + table(["Delay after due date", "Small LLP", "Other LLP"], [
             ["Up to 15 days", "1x", "1x"], ["15 to 30 days", "2x", "4x"], ["30 to 60 days", "4x", "8x"],
             ["60 to 90 days", "6x", "12x"], ["90 to 180 days", "10x", "20x"], ["180 to 360 days", "15x", "30x"],
             ["Beyond 360 days", "15x plus &#8377;10 a day", "30x plus &#8377;20 a day"]])
         + '<p>The additional fee is a multiple of the normal fee and applies form by form. A small LLP has contribution up to &#8377;5 crore and turnover up to &#8377;50 crore. Separate penalties under the LLP Act can apply for continuing default. Confirm the fee shown on the MCA portal before paying.</p>'),
        ("/ First year and special cases", "Where people get stuck.",
         ul("<strong>First year:</strong> an LLP incorporated after 30 September can close its first financial year on 31 March of the following year, so its first Form 11 and Form 8 fall in the year after that. An LLP incorporated earlier in the year files for the year ending the next 31 March.",
            "<strong>Overdue years:</strong> file the oldest years first; each form carries its own additional fee. Long default can lead the Registrar to treat the LLP as inactive and start strike-off.",
            "<strong>Foreign or NRI partners:</strong> the same forms apply; foreign contribution also needs FEMA reporting (Form LLP-I / LLP-II through the RBI&rsquo;s FIRMS portal). See " + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration with NRI or foreign partners") + ".",
            "<strong>Moving to a company:</strong> see " + L("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "converting an LLP to a private limited company") + " and " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ".")
         + call_box("LLP annual filing", ["Form 11 and Form 8 filing",
                                          "Overdue years and additional fees",
                                          "Audit and ITR-5",
                                          "Foreign partner FEMA reporting",
                                          "Strike-off or conversion"],
                    "the LLPIN, incorporation date and pending years.")
         + sources("Limited Liability Partnership Act, 2008 and LLP Rules, 2009 (rule 24 accounts and audit), LLP (Amendment) Rules, 2022 (additional fees, small LLP limits); MCA General Circular 05/2026; Tally, Razorpay Rize, IndiaFilings and CAclubindia LLP annual filing guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the due date for LLP annual filing?", "Form 11 (annual return) is due by 30 May and Form 8 (statement of account and solvency) by 30 October each year. The income tax return, ITR-5, follows the income tax due dates."),
        ("What are the legal requirements for an LLP in India?", "From the start: at least two designated partners with DINs, at least one of them resident in India (stayed in India for at least 120 days in the financial year, after the 2021 amendment), and the LLP agreement filed in Form 3 within 30 days of incorporation. Every year: Form 11 (annual return) by 30 May, Form 8 (statement of account and solvency) by 30 October, ITR-5 by the income tax due date, books of account kept on a cash or accrual basis, and an audit of the accounts once turnover exceeds Rs 40 lakh or contribution exceeds Rs 25 lakh. Designated partners file DIR-3 KYC to keep their DINs active. On changes: a new or exiting partner or designated partner is reported in Form 4, and any change to the LLP agreement in Form 3, each within 30 days. GST registration, TDS and any FEMA reporting for foreign partners apply on top where relevant. WhatsApp +91 78018 87130 with the LLPIN, the forms and years filed, the partners' contribution and turnover, and we tell you what is due or overdue."),
          ("Is the LLP Form 8 due date for FY 2025-26 extended?", "No. MCA General Circular 05/2026 extended only the company forms AOC-4 and MGT-7. LLP Form 8 for FY 2025-26 was due on 30 October 2026 and additional fees apply after that."),
          ("What is the late fee for LLP annual filing?", "An additional fee that is a multiple of the normal fee for each late form: from 1x for up to 15 days to 15x for small LLPs or 30x for others after 180 days, plus a per-day amount beyond 360 days."),
        ("What is the penalty for not filing LLP annual returns?", "Two things apply. First, the additional fee on each late form: a multiple of the normal filing fee that rises with the delay, up to 15 times for a small LLP or 30 times for other LLPs, plus Rs 10 or Rs 20 a day beyond 360 days. Second, the LLP Act penalty: for a late annual return (Form 11) under section 35, Rs 100 a day, up to Rs 1 lakh for the LLP and Rs 50,000 for each designated partner. MCA General Circular 05/2026 does not cover LLP forms, so filing the pending forms now stops both from growing."),
        ("What should I send to clear an LLP's overdue annual filings?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the LLPIN, the years and forms pending (Form 11, Form 8, ITR-5), the partners' contribution, the turnover for each year, whether accounts were prepared or audited, and the designated partners' DIN and DSC status. We list the forms, the additional fee position and the order of filing."),
          ("Does an LLP with no business need to file returns?", "Yes. An LLP with no activity still files Form 11, Form 8 and ITR-5 every year until it is struck off."),
        ("How do I strike off or close an LLP?", "An LLP that has not carried on business for a year or more can apply to the Registrar in Form 24 under rule 37 of the LLP Rules, with the consent of all partners. Before filing, the overdue Form 8 and Form 11 up to the end of the financial year in which it stopped business must be filed. Form 24 is usually supported by a statement of accounts showing no assets or liabilities, affidavits and an indemnity by the designated partners, and the partners' authority - check the current MCA instruction kit for the attachment list. Close the bank account, surrender GST registration and settle tax filings first. Separately, the Registrar can strike off an LLP on its own if it has not carried on business for two years or more."),
        ("What should I send to close or strike off our LLP?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the LLPIN, the date business stopped, the last Form 8 and Form 11 filed, recent bank statements, the GST registration status, and details of any assets, liabilities or pending tax matters. We file the overdue returns, prepare the statement of accounts, affidavits and Form 24, and track it to closure."),
          ("When is an LLP audit compulsory?", "When turnover exceeds Rs 40 lakh or partners' contribution exceeds Rs 25 lakh in the financial year. Income tax audit applies separately above the income tax turnover limits."),
          ("Can an LLP partner take a salary, and what is the maximum remuneration?", "Yes, if the LLP agreement authorises it and it is paid to a working partner who is an individual. For tax, the LLP can deduct remuneration up to the section 40(b) limit: on the first INR 6 lakh of book profit (or a loss), the higher of INR 3 lakh or 90% of book profit, and 60% of the balance, from AY 2025-26. Interest on partners' capital is deductible up to 12% simple a year. Remuneration and interest are taxed in the partner's hands as business income, and the LLP deducts TDS at 10% under section 194T once payments to a partner exceed INR 20,000 in the year."),
          ("Can BQP file our LLP's annual returns?", "Yes. CA Durgesh Chavda files Form 11, Form 8 and ITR-5, including overdue years and LLPs with NRI or foreign partners. " + C)],
    related=[("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "LLP Form 8 due date and late fee"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration"),
             ("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "Convert LLP to company"),
             ("deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html", "Deadline desk to 31 January 2027")],
    cta_h="LLP filings pending or overdue?", cta_b=C,
    keywords="LLP annual filing, LLP annual filing due date, LLP annual filing fees, LLP annual filing late fees, LLP Form 11, LLP Form 11 due date, LLP Form 11 penalty, LLP Form 8, LLP annual filing first year, LLP annual filing status",
    desc="LLP annual filing (2026): Form 11 by 30 May and Form 8 by 30 October (FY 2025-26 not extended), ITR-5, audit above Rs 40 lakh turnover or Rs 25 lakh contribution, normal fees, late-fee multiples, first-year filing, status check.",
    howto={"name": "How to complete LLP annual filing", "description": "For each financial year.", "steps": [
        {"name": "Close the books", "text": "Prepare accounts; audit if turnover exceeds Rs 40 lakh or contribution Rs 25 lakh."},
        {"name": "File Form 11 by 30 May", "text": "Annual return of partners and contributions."},
        {"name": "File ITR-5", "text": "Income tax return by the applicable due date."},
        {"name": "File Form 8 by 30 October", "text": "Statement of account and solvency, certified by a practising professional."},
        {"name": "Keep DIN KYC current", "text": "DIR-3 KYC for each designated partner, now once every three years."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HM complete")
