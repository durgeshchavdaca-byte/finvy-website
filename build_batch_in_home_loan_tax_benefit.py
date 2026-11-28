# -*- coding: utf-8 -*-
"""Batch IN (25 Nov 2026): home loan tax benefit India 2026 - interest under section 24(b) of the 1961 Act / section 22
of the 2025 Act: self-occupied up to Rs 2 lakh a year (old regime only; Rs 30,000 if construction not completed within
5 years from end of the FY of the loan); let-out: interest deductible in full in both regimes, loss set-off against
other income up to Rs 2 lakh (old regime only; carry forward 8 years), no set-off in new regime; principal + stamp
duty / registration under 80C (section 123 of the 2025 Act per commentary) within Rs 1.5 lakh, old regime only,
reversed if sold within 5 years of possession; pre-construction interest in 5 equal instalments from completion;
joint borrowers who are co-owners each claim separately; 80EE / 80EEA closed to new loans (80EEA: loans sanctioned
1 April 2019 - 31 March 2022).
Demand: sweep ac112 (25 Nov 2026), all 7 markets: "home loan tax benefit", "home loan tax benefit which section",
"home loan tax benefit calculator", "how much tax benefit on home loan", "home loan tax benefit for first-time buyer",
"do we get tax benefit on home loan", "home loan tax benefit india".
Facts (checked 25 Nov 2026): Cleartax, Taxguru, TheTaxCorp (2025 Act mapping), Piramal Realty (80EE / 80EEA status),
Finnovate, Bajaj Finserv; site house property page (same new / old regime treatment)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "home-loan-tax-benefit-india-2026-section-24b-2-lakh-80c-principal-new-regime-joint-loan-calculation"

C = contact("the home loan interest and principal paid this year, whether the house is self-occupied or let out, the rent, co-owners and co-borrowers, and the tax regime you use")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Home Loan Tax Benefit 2026: Which Section (24(b) Rs 2 Lakh Interest, 80C Principal), New Regime, Joint Loan, Under-Construction Property and Calculation",
    em="old regime for your own home, both regimes if it is let out.",
    kicker="/ Home buyers and borrowers &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Under the old tax regime, home loan interest on a house you live in is deductible up to &#8377;2 lakh a year (section 24(b)), and principal repayment up to &#8377;1.5 lakh within section 80C, so the total benefit can reach &#8377;3.5 lakh a year.</strong> "
          "Under the new regime there is no deduction for a self-occupied home, but interest on a let-out house is still deductible against its rent. "
          "From tax year 2026-27 the interest deduction sits in section 22 of the Income-tax Act, 2025."),
    sections=[
        ("/ Which section gives what", "Old and new regime side by side.",
         table(["Benefit", "Old regime", "New regime"], [
             ["Interest, self-occupied house (24(b) / section 22)", "Up to &#8377;2,00,000 a year", "Not allowed"],
             ["Interest, let-out house", "Full interest; loss set-off against other income up to &#8377;2 lakh, rest carried forward 8 years", "Full interest against rent; loss cannot be set off or carried forward"],
             ["Principal, stamp duty, registration (80C)", "Within the &#8377;1.5 lakh 80C limit", "Not allowed"],
             ["Pre-construction interest", "In 5 equal instalments from the year of completion, within the limits above", "Let-out only"],
             ["80EE / 80EEA (first-time buyers)", "Only for loans sanctioned in the original windows (80EEA: 1 April 2019 to 31 March 2022)", "Not allowed"]])
         + '<p>See the ' + L("section-80c-complete-list-india-2026.html", "full 80C list") + ' and ' + L("income-from-house-property-calculation-deductions-30-percent-home-loan-interest-new-regime-2026.html", "income from house property") + ' for how rent and the 30% deduction work.</p>'),
        ("/ Calculation (illustrative)", "Old regime, 30% slab, self-occupied.",
         table(["Item", "Paid", "Deduction"], [
             ["Interest", "&#8377;2,40,000", "&#8377;2,00,000 (cap)"],
             ["Principal (80C room available)", "&#8377;1,20,000", "&#8377;1,20,000"],
             ["Total deduction", "", "&#8377;3,20,000"],
             ["Tax saved at 30% + 4% cess", "", "&#8377;99,840"]])
         + '<p>Illustrative only. Whether this beats the new regime depends on your other deductions; check with the ' + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ' or the ' + L("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "regime decision guide") + '.</p>'),
        ("/ Rules that trip people up", "Before you claim.",
         ul("<strong>Joint home loan:</strong> each co-borrower who is also a co-owner can claim interest up to &#8377;2 lakh and principal within their own 80C limit, in proportion to what they pay.",
            "<strong>Under construction:</strong> no interest deduction until the year construction is completed; earlier interest is claimed in five equal parts from then. If construction is not completed within five years from the end of the year the loan was taken, the self-occupied interest cap falls to &#8377;30,000.",
            "<strong>Selling early:</strong> if the house is sold within five years from the end of the year of possession, 80C principal deductions already claimed are added back to income.",
            "<strong>Two self-occupied homes:</strong> up to two houses can be treated as self-occupied, but the &#8377;2 lakh interest cap is combined.",
            "<strong>First-time buyers:</strong> there is no separate deduction for new loans now; 80EE and 80EEA apply only to loans sanctioned in their original windows.",
            "<strong>Proof:</strong> keep the lender&rsquo;s interest certificate and the possession or completion certificate; employers need them for payroll TDS.",
            "<strong>NRIs:</strong> the same deductions apply against Indian income; see " + L("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "NRIs buying property and home loans") + ".")
         + call_box("Home loan tax", ["Old vs new regime with a home loan",
                                       "Joint loan split between co-owners",
                                       "Pre-construction interest",
                                       "Let-out property and rent",
                                       "ITR and payroll proof"],
                    "your loan certificate.")
         + sources("Income-tax Act, 1961 sections 24(b), 71(3A), 80C, 80EE and 80EEA; Income-tax Act, 2025 section 22 (house property deductions) and section 123 (per commentary); Cleartax, Taxguru, TheTaxCorp, Finnovate, Piramal Realty and Bajaj Finserv explainers; site guide on income from house property. Checked 25 November 2026.")),
    ],
    faqs=[("Which section gives tax benefit on a home loan?", "Interest: section 24(b) of the Income-tax Act, 1961, which is section 22 of the Income-tax Act, 2025 from tax year 2026-27. Principal, stamp duty and registration: section 80C (section 123 of the 2025 Act per commentary)."),
          ("How much tax benefit can I get on a home loan?", "Under the old regime, up to Rs 2 lakh of interest on a self-occupied home plus principal within the Rs 1.5 lakh 80C limit, so up to Rs 3.5 lakh of deductions a year. For a let-out house, the full interest is deductible against rent."),
        ("Can I claim a home loan tax benefit on an under-construction property?", "Not while it is under construction. Interest paid before completion (from the date of borrowing to 31 March before the year of completion) is pre-construction interest: it becomes deductible in five equal instalments starting from the year construction is completed, and for a self-occupied home those instalments sit within the same Rs 2 lakh yearly cap as current interest under the old regime. The Rs 2 lakh limit needs construction or acquisition to be completed within five years from the end of the financial year of borrowing; otherwise the self-occupied cap falls to Rs 30,000. Principal repayments qualify under 80C only from the year you get possession - EMIs paid during construction do not - while stamp duty and registration qualify in the year you pay them. A let-out property gets the full interest against rent, and the new regime gives no deduction for a self-occupied home. Selling within five years of possession reverses the 80C principal claimed. WhatsApp +91 78018 87130 with the loan sanction, interest certificates, possession date and regime, or book a call."),
          ("Is home loan interest deductible in the new tax regime?", "Only for a let-out property, against its rent, and any loss cannot be set off against other income. For a self-occupied home there is no deduction in the new regime."),
          ("Can both joint borrowers claim the home loan tax benefit?", "Yes, if each is a co-owner and contributes to the repayments. Each can claim up to Rs 2 lakh of interest and principal within their own 80C limit under the old regime."),
          ("Is there a tax benefit on a joint home loan with a non-working wife?", "Only for the spouse who has taxable income. A non-working spouse with no taxable income gets no use from the deductions in their share. The earning co-borrower can claim interest and principal in line with their ownership share and the EMIs they actually pay from their own funds, so the ownership split and the payment trail matter. If the earning spouse funds the non-earning spouse's share of the property, income from that share can be clubbed with the earning spouse."),
          ("Is there a tax benefit for first-time home buyers in 2026?", "Not for new loans. Section 80EEA applied to loans sanctioned between 1 April 2019 and 31 March 2022, and 80EE to earlier windows; new borrowers use the normal interest and 80C deductions."),
          ("Can BQP work out my home loan tax benefit?", "Yes. CA Durgesh Chavda can compute the deductions, compare regimes, split a joint loan and file your return. " + C)],
    related=[("income-from-house-property-calculation-deductions-30-percent-home-loan-interest-new-regime-2026.html", "Income from house property"),
             ("section-80c-complete-list-india-2026.html", "Section 80C list"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "Which regime to choose"),
             ("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "NRIs buying property")],
    cta_h="Paying a home loan?", cta_b=C,
    keywords="home loan tax benefit, home loan tax benefit which section, home loan tax benefit calculator, section 24(b) 2 lakh, home loan principal 80C, home loan new tax regime, joint home loan tax benefit, first time home buyer tax benefit 2026, section 22 Income-tax Act 2025",
    desc="Home loan tax benefit 2026: interest up to Rs 2 lakh (section 24(b), now section 22) and principal under 80C in the old regime; new regime only for let-out property; joint loans, pre-construction interest, 80EEA status, worked calculation.",
    howto={"name": "How to claim the home loan tax benefit", "description": "For resident and NRI borrowers.", "steps": [
        {"name": "Choose your regime", "text": "Self-occupied home deductions need the old regime."},
        {"name": "Get the interest certificate", "text": "From the lender, splitting interest and principal."},
        {"name": "Claim interest", "text": "Up to Rs 2 lakh self-occupied; full for let-out."},
        {"name": "Claim principal", "text": "Under 80C within Rs 1.5 lakh, with stamp duty and registration."},
        {"name": "Report in the return", "text": "Schedule HP for interest, Chapter VI-A for 80C."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IN complete")
