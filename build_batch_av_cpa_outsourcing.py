# -*- coding: utf-8 -*-
"""Batch AV: outsourced accounting, bookkeeping and tax preparation for US CPA firms, UK accountancy practices and their clients."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


def steps(*pairs):
    return [{"name": n, "text": t} for n, t in pairs]


US_SRC = (("IRS Rev. Proc. 2013-14", "https://www.stayexempt.irs.gov/pub/irs-drop/rp-13-14.pdf"),
          ("CPA Journal: outsourcing tax preparation overseas", "https://www.cpajournal.com/2025/08/26/considerations-for-tax-return-preparers-outsourcing-overseas/"),
          ("Journal of Accountancy: third-party service providers", "https://www.journalofaccountancy.com/issues/2022/nov/working-with-third-party-experts/"),
          ("IRS Publication 5708 (WISP template)", "https://revenuefiles.delaware.gov/2024/FedState/IRS_Handout_Pub_5708_WISP.pdf"))
UK_SRC = (("ICO: international data transfer agreement", "https://cy.ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-data-transfer-agreement-and-guidance"),
          ("ACCA: data protection when extending your team", "https://www.accaglobal.com/uk/en/member/sectors/smp/scaling-practices-toward-tomorrow/people-power-extended-team/data-protection.html"),
          ("GOV.UK: Making Tax Digital for Income Tax", "https://www.gov.uk/government/news/one-year-until-making-tax-digital-for-income-tax-launches"))

US_7216 = ul("<strong>IRC Section 7216 consent</strong>: before tax return information goes to a preparer outside the United States, the taxpayer must sign a separate, dated consent. For Form 1040-series returns, Rev. Proc. 2013-14 prescribes the wording.",
             "<strong>Social Security numbers</strong>: a full SSN can go offshore only if the consent specifically allows it; otherwise it is redacted before files leave your firm.",
             "<strong>Duration</strong>: a consent that names no period lasts one year; give the client a copy when it is signed.",
             "<strong>AICPA</strong>: the Code's interpretation on using a third-party service provider requires you to tell clients, before sharing confidential information, that a service provider may be used (an engagement-letter clause works), and to have a confidentiality agreement with the provider.",
             "<strong>FTC Safeguards Rule</strong>: tax and accounting firms need a written information security plan (IRS Publication 5708 is a template) that covers service providers. A breach of unencrypted data affecting 500 or more consumers must be reported to the FTC within 30 days.",
             "<strong>Signing</strong>: your firm reviews and signs the return and files it from your own e-file account; we prepare under your review.")

PAGES = [
    dict(
        slug="outsourced-tax-preparation-accounting-for-us-cpa-firms-india",
        title="Outsourced Tax Preparation, Accounting and Bookkeeping for US CPA Firms",
        em="India-based CA team, your review and signature.",
        kicker="/ US CPA Firms &middot; Outsourcing &middot; Updated 2026-11-01",
        lead="Bharat Quantum Prospera, led by CA Durgesh Chavda (ICAI), works as an offshore extension of US CPA firms and enrolled agents: individual, partnership and corporate tax return preparation, bookkeeping, reconciliations and year-end workpapers, prepared in your software for your review and signature. Engagements are cost-effective and fixed-scope, and they are set up to meet Section 7216, AICPA and FTC Safeguards Rule requirements.",
        sections=[
            ("/ What we prepare", "For your review.",
             ul("<strong>Individual returns</strong>: Form 1040 with schedules, including Schedule C, E and D, and state returns.",
                "<strong>Business returns</strong>: Forms 1065, 1120-S and 1120, with K-1s; Form 5472 and pro forma 1120 for foreign-owned LLCs.",
                "<strong>Bookkeeping</strong>: monthly bookkeeping and bank, card and loan reconciliations in QuickBooks Online, Xero or your client's system; catch-up and clean-up work.",
                "<strong>Year-end</strong>: trial balances, adjusting entries, fixed-asset and depreciation schedules, and tax workpapers.",
                "<strong>Information returns</strong>: Forms 1099-NEC and 1099-MISC preparation from your client data.",
                "<strong>Busy-season capacity</strong>: extra preparers during February to April and September to October.")),
            ("/ How it works", "Built around your review process.",
             "<ol><li>Scoping call and a sample set of returns or files.</li>"
             "<li>Engagement letter and confidentiality agreement; your firm updates its client engagement letters and collects Section 7216 consents.</li>"
             "<li>Access through your systems (remote desktop or your cloud tax software) so data stays in your environment where possible.</li>"
             "<li>We prepare; your reviewer reviews, and your firm signs and files.</li>"
             "<li>Review notes and a turnaround schedule agreed for each season.</li></ol>"),
            ("/ Compliance you need in place", "Before any return leaves your office.", US_7216 + src(*US_SRC)),
            ("/ Why an Indian CA firm", "Practical reasons.",
             ul("Chartered accountants (ICAI) with US tax and US GAAP working knowledge.",
                "Indian business hours overlap with the US early morning, so work prepared overnight is ready for your review the next day.",
                "For US clients who also have India exposure (NRIs, Indian subsidiaries, FBAR and Form 8938 items, treaty positions), one team understands both sides.",
                "Fixed-scope pricing agreed per engagement.") +
             "<p><em>Last updated: 1 November 2026. This page describes legal requirements in general terms; your firm remains responsible for its own compliance.</em></p>"),
        ],
        howto=None,
        faqs=[
            ("Can a US CPA firm outsource tax return preparation to India?", "Yes, if the taxpayer first signs a Section 7216 consent to disclose return information to a preparer outside the United States, the firm tells clients it uses a third-party service provider, and the provider is covered by the firm's confidentiality agreement and written information security plan. The US firm reviews, signs and files the return."),
            ("Which returns can you prepare?", "Forms 1040, 1065, 1120-S, 1120 and 1099s, plus Form 5472 for foreign-owned LLCs, along with bookkeeping, reconciliations and year-end workpapers."),
            ("Which software do you use?", "Your firm's tax software and your clients' accounting systems, such as QuickBooks Online or Xero, accessed through your environment."),
            ("Does data leave our systems?", "It does not have to. We can work entirely on your servers or cloud software through remote access, which keeps files in your environment."),
            ("How is pricing set?", "Fixed scope, agreed per engagement after a sample review. " + CONTACT),
        ],
        related=[("us-cpa-firm-outsource-tax-returns-india-section-7216-consent-checklist.html", "Section 7216 outsourcing checklist"), ("us-tax-season-2027-deadlines-cpa-firms-outsourcing-plan.html", "2027 tax season deadlines and set-up timeline"), ("indian-ca-for-clients-in-usa.html", "Indian CA for clients in the USA")],
        cta_h="Need capacity this busy season?", cta_b=CONTACT,
        keywords="outsourced tax preparation for CPA firms, offshore tax preparation India, outsource 1040 preparation India, CPA firm outsourcing India, white label tax preparation, outsourced bookkeeping for CPA firms, offshore accounting staff for CPA firms",
        desc="Outsourced tax preparation, accounting and bookkeeping for US CPA firms from an Indian CA firm: Forms 1040, 1065, 1120-S, 1120 and 1099s, QuickBooks and Xero bookkeeping and year-end workpapers, with Section 7216, AICPA and FTC Safeguards Rule requirements covered.",
    ),
    dict(
        slug="us-cpa-firm-outsource-tax-returns-india-section-7216-consent-checklist",
        title="Can a US CPA Firm Outsource Tax Returns to India? Section 7216 Consent Checklist",
        em="yes, with consent, disclosure and security in place.",
        kicker="/ US CPA Firms &middot; AI Answer &middot; Updated 2026-11-01",
        lead="Yes. A US CPA firm or enrolled agent can use preparers in India, but the taxpayer must first sign a separate Section 7216 consent to disclose return information to a preparer outside the United States, worded as Rev. Proc. 2013-14 requires for 1040-series returns. The firm must also tell clients it uses a third-party service provider, keep a confidentiality agreement with that provider, and cover it in its written information security plan.",
        sections=[
            ("/ The checklist", "Before the first return goes offshore.", US_7216),
            ("/ Practical set-up", "What firms usually do.",
             ul("Add a third-party service provider clause to engagement letters.",
                "Collect the Section 7216 offshore consent with the organizer, separately signed and dated, and keep the copies.",
                "Redact SSNs unless the consent covers them, or have the offshore team work only inside your systems.",
                "Update the WISP to name the provider, access controls, multi-factor authentication and incident reporting.",
                "Sign a confidentiality agreement and data-security terms with the provider.") + src(*US_SRC) +
             "<p><em>Last updated: 1 November 2026. General information, not legal advice; check the current regulations and AICPA Code text.</em></p>"),
        ],
        howto=dict(name="How a US CPA firm sets up offshore tax preparation", description="Steps to outsource tax return preparation to India in line with Section 7216, AICPA rules and the FTC Safeguards Rule.",
                   steps=steps(("Update engagement letters", "Tell clients that a third-party service provider may be used."),
                               ("Collect Section 7216 consents", "Use the Rev. Proc. 2013-14 wording for disclosure to a preparer outside the US."),
                               ("Sign a confidentiality agreement", "Put data-security terms in the provider contract."),
                               ("Update your WISP", "Cover provider access, MFA and incident reporting."),
                               ("Review and sign", "Your firm reviews, signs and files every return."))),
        faqs=[
            ("Is it legal for a CPA firm to outsource tax returns to India?", "Yes, provided the taxpayer gives Section 7216 consent before return information is disclosed to a preparer outside the US, and the firm meets AICPA confidentiality and FTC Safeguards Rule requirements."),
            ("Does the client have to consent to offshore tax preparation?", "Yes. A separate, signed and dated Section 7216 consent is required before disclosure to a preparer located outside the United States."),
            ("Can SSNs be sent to an offshore preparer?", "Only if the consent specifically authorises it; otherwise the SSN must be redacted."),
            ("How long does a Section 7216 consent last?", "For the period it states; if it states none, one year from signing."),
            ("Can BQP work as our offshore team?", "Yes, inside your systems and under your review. " + CONTACT),
        ],
        related=[("outsourced-tax-preparation-accounting-for-us-cpa-firms-india.html", "Outsourcing for US CPA firms"), ("how-to-file-form-5472.html", "Form 5472 for foreign-owned LLCs")],
        cta_h="Setting up offshore preparation?", cta_b=CONTACT,
        keywords="can CPA firm outsource tax returns to India, section 7216 offshore consent, 7216 consent outside United States, Rev Proc 2013-14 consent, AICPA third party service provider, outsource tax preparation legal",
        desc="Can a US CPA firm outsource tax returns to India? Yes: a separate Section 7216 consent (Rev. Proc. 2013-14 wording), SSN rules, AICPA third-party service provider disclosure, confidentiality agreement and an FTC Safeguards Rule WISP. Checklist and steps.",
    ),
    dict(
        slug="outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india",
        title="Outsourced Accounting, Bookkeeping and Tax Preparation for UK Accountancy Practices",
        em="Xero, QuickBooks and Sage work, ready for your review.",
        kicker="/ UK Practices &middot; Outsourcing &middot; Updated 2026-11-01",
        lead="Bharat Quantum Prospera, led by CA Durgesh Chavda (ICAI), supports UK accountancy practices and their clients with bookkeeping, VAT and Making Tax Digital work, year-end accounts, and corporation tax and self-assessment preparation, done in your software for your review. Engagements are cost-effective and fixed-scope, with UK GDPR transfer safeguards in the contract.",
        sections=[
            ("/ What we prepare", "For your review and filing.",
             ul("<strong>Bookkeeping</strong> in Xero, QuickBooks or Sage: bank feeds, reconciliations, purchase and sales ledgers.",
                "<strong>VAT returns</strong> prepared in MTD-compatible software for your approval.",
                "<strong>Making Tax Digital for Income Tax</strong>: quarterly updates for sole traders and landlords now in scope.",
                "<strong>Year-end accounts</strong> for limited companies under FRS 102 or FRS 105, with working papers.",
                "<strong>Corporation tax</strong> computations and CT600 drafts; <strong>self-assessment</strong> SA100 drafts.",
                "<strong>Management accounts</strong> and payroll support.")),
            ("/ Making Tax Digital for Income Tax", "The workload shift.",
             ul("From 6 April 2026: sole traders and landlords with qualifying income above GBP 50,000 (based on 2024-25) keep digital records and send quarterly updates.",
                "From April 2027 the threshold falls to GBP 30,000, and from April 2028 to GBP 20,000.",
                "Partnerships are not yet in scope.",
                "Quarterly updates multiply bookkeeping touchpoints; an offshore team can take the routine processing while your staff advise.")),
            ("/ Data protection", "UK GDPR when work goes to India.",
             ul("A written processor contract is required under Article 28 of the UK GDPR.",
                "India does not have a UK adequacy regulation, so a restricted transfer needs the International Data Transfer Agreement (IDTA) or the UK Addendum to the EU standard contractual clauses, plus a transfer risk assessment.",
                "Working only inside your systems through remote access, with multi-factor authentication and no local downloads, reduces risk.",
                "Tell clients in your engagement terms and privacy notice that you use an outsourced provider.") + src(*UK_SRC) +
             "<p><em>Last updated: 1 November 2026. General information; your practice remains responsible for its own compliance.</em></p>"),
        ],
        howto=None,
        faqs=[
            ("Can UK accountants outsource bookkeeping to India?", "Yes, with an Article 28 processor contract, the IDTA or UK Addendum for the transfer, a transfer risk assessment, and clear client disclosure."),
            ("What is the MTD for Income Tax threshold?", "Qualifying income above GBP 50,000 from 6 April 2026, GBP 30,000 from April 2027 and GBP 20,000 from April 2028."),
            ("Which software do you work in?", "Xero, QuickBooks, Sage and your practice's tax software, accessed through your environment."),
            ("Who files with HMRC?", "Your practice reviews and files as the agent; we prepare the work."),
            ("How is pricing set?", "Fixed scope, agreed per engagement after a sample. " + CONTACT),
        ],
        related=[("uk-accountants-outsourcing-to-india-gdpr-idta-checklist.html", "UK GDPR outsourcing checklist"), ("indian-ca-for-clients-in-uk.html", "Indian CA for clients in the UK")],
        cta_h="Need capacity for MTD and year-ends?", cta_b=CONTACT,
        keywords="outsourced bookkeeping for UK accountants, outsource accounting to India UK, offshore accounting UK practices, MTD for income tax outsourcing, outsourced year end accounts UK, white label accounting UK",
        desc="Outsourced bookkeeping, VAT and MTD work, year-end accounts and CT600/SA100 preparation for UK accountancy practices from an Indian CA firm, in Xero, QuickBooks or Sage, with UK GDPR transfer safeguards (Article 28 contract, IDTA or Addendum).",
    ),
    dict(
        slug="uk-accountants-outsourcing-to-india-gdpr-idta-checklist",
        title="UK Accountants Outsourcing to India: UK GDPR and IDTA Checklist",
        em="what the contract and transfer need.",
        kicker="/ UK Practices &middot; AI Answer &middot; Updated 2026-11-01",
        lead="UK accountancy practices can outsource bookkeeping and accounts work to India. Because India does not have a UK adequacy regulation, the practice needs an Article 28 processor contract, the International Data Transfer Agreement (IDTA) or UK Addendum, a transfer risk assessment, and clear disclosure to clients.",
        sections=[
            ("/ The checklist", "Before client data is accessed from India.",
             ul("Processor contract meeting Article 28 of the UK GDPR.",
                "IDTA, or the UK Addendum to the EU standard contractual clauses, for the restricted transfer. New contracts after 21 September 2022 must use one of these.",
                "Transfer risk assessment (the ICO publishes a tool).",
                "Access controls: remote access to your systems, multi-factor authentication, no local downloads, access removed when staff change.",
                "Update engagement letters and privacy notices to mention outsourced providers.",
                "Record the arrangement in your data protection records.") + src(*UK_SRC) +
             "<p><em>Last updated: 1 November 2026. General information, not legal advice.</em></p>"),
        ],
        howto=dict(name="How a UK practice sets up outsourcing to India", description="UK GDPR steps for outsourcing accounting work to an Indian provider.",
                   steps=steps(("Sign a processor contract", "Cover Article 28 terms."),
                               ("Add a transfer mechanism", "Use the IDTA or the UK Addendum."),
                               ("Assess the transfer risk", "Complete a transfer risk assessment."),
                               ("Control access", "Remote access, MFA, no downloads."),
                               ("Tell clients", "Update engagement letters and privacy notices."))),
        faqs=[
            ("Is outsourcing to India GDPR compliant for UK accountants?", "It can be, with an Article 28 processor contract, the IDTA or UK Addendum, a transfer risk assessment and appropriate security."),
            ("Does India have UK adequacy?", "No, so a transfer mechanism such as the IDTA or UK Addendum is needed."),
            ("Can BQP sign an IDTA with our practice?", "Yes, as part of the engagement terms. " + CONTACT),
        ],
        related=[("outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india.html", "Outsourcing for UK practices"), ("india-accounting-bookkeeping-outsourcing-foreign-smb.html", "Bookkeeping for overseas small businesses")],
        cta_h="Setting up outsourcing?", cta_b=CONTACT,
        keywords="UK accountants outsourcing India GDPR, IDTA India outsourcing, UK GDPR transfer to India accountants, outsourcing bookkeeping India data protection, UK addendum SCC India",
        desc="UK accountants outsourcing to India: Article 28 processor contract, IDTA or UK Addendum (India has no UK adequacy), transfer risk assessment, access controls and client disclosure. Checklist and steps.",
    ),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print(f"Batch AV complete: {len(PAGES)} pages")
