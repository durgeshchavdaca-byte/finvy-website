# -*- coding: utf-8 -*-
"""Batch W: Round 7 - 14 pages. More form checklists + narrow positioning + comprehensive calendar + AEO meta."""
from build_lib import page, write_page


def quick_page(slug, title, hero_em, lead, kicker, sections_pairs, faqs, related_pairs, cta_h, cta_b, keywords, desc):
    return page(
        slug=slug, title=title, description=desc, keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=sections_pairs, faqs=faqs,
        related=[(h, "Related", l) for h, _, l in related_pairs],
        cta_headline=cta_h, cta_body=cta_b,
    )


PAGES = []

# 1. Form 15H / 15G
PAGES.append({
    "slug": "form-15g-15h-no-tds-declaration-india-2026",
    "title": "Form 15G / 15H (2026): How to Avoid TDS on FD Interest, Who Can Submit, NRI Rules and Checklist",
    "hero_em": "senior citizen + non-taxable income TDS avoidance.",
    "lead": "Form 15G (below 60 years) / Form 15H (senior citizen 60+) are self-declarations submitted to deductor (bank / company / payer) to avoid TDS on income (interest / dividend / rental) when overall taxable income is below exemption limit. Section 197A Income Tax Act. Here's the complete 2026 submission framework.",
    "kicker": "/ No-TDS Declaration Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ When Form 15G / 15H applies", "Section 197A core.",
         "<ul>"
         "<li><strong>Form 15G</strong>: individual below 60 years + HUF + trust (not company / firm). Submitted to avoid TDS when total income likely below basic exemption.</li>"
         "<li><strong>Form 15H</strong>: individual 60+ (senior citizen). Submitted to avoid TDS on interest / dividend / rental when total income below exemption.</li>"
         "<li><strong>Deductor must verify</strong>: cannot blindly accept; if declaration appears false, deductor still TDS applicable.</li>"
         "<li>Common deductors: banks (on FD / RD / savings interest above INR 50K senior / INR 40K regular), companies (on dividend above INR 5K), tenants (on rent above INR 50K monthly).</li>"
         "<li>Submitted annually at start of FY (April); refreshed if circumstances change.</li>"
         "</ul>"),
        ("/ Form 15G eligibility (below 60)", "The strict conditions.",
         "<ul>"
         "<li>Individual / HUF / trust (not company / firm / cooperative).</li>"
         "<li>Age below 60 years for individual.</li>"
         "<li>Total income (post all deductions) likely below basic exemption (INR 3 lakh old regime; INR 7 lakh new regime with Section 87A rebate).</li>"
         "<li>Tax on total income is NIL.</li>"
         "<li>Aggregate income from specific sources covered by declaration below specific thresholds.</li>"
         "</ul>"),
        ("/ Form 15H eligibility (60+ senior citizen)", "Simpler.",
         "<ul>"
         "<li>Individual aged 60 years + at any point in FY.</li>"
         "<li>Total income (post all deductions) likely below basic exemption (INR 3 lakh old; INR 7 lakh new with 87A rebate).</li>"
         "<li>Tax on total income is NIL.</li>"
         "<li>No aggregate income threshold for 15H (unlike 15G).</li>"
         "</ul>"),
        ("/ Submission + consequences", "The workflow.",
         "<ul>"
         "<li>Submit to each deductor separately (one bank, one company, one tenant - separate 15G/15H to each).</li>"
         "<li>At beginning of FY (April) ideally; mid-year submission accepted but partial-year TDS already deducted.</li>"
         "<li>Deductor reports to Income Tax Department via Form 15G/15H system online.</li>"
         "<li>If 15G/15H submitted but actual income exceeds exemption: penalty under Section 277 for false declaration + TDS short-collected becomes short-deduction + Section 201 interest.</li>"
         "<li>Deductor verifies PAN linking + aggregates with Form 26AS data.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the difference between Form 15G and 15H?",
         "15G: individual below 60 + HUF / trust - with strict eligibility conditions including aggregate income threshold. 15H: individual 60+ (senior citizen) - simpler eligibility with no aggregate income threshold. Both are for avoiding TDS when overall taxable income is below exemption limit."),
        ("Can I submit 15H if I have multiple sources of income?",
         "Yes - submit to each deductor separately. 15H to Bank A for FD interest, 15H to Bank B for savings interest, 15H to company for dividend, 15H to tenant for rent. Each deductor independently decides based on their payment. But if your TOTAL income exceeds exemption, false 15H exposes you to Section 277 penalty."),
        ("What if I submit 15G/15H and later income exceeds exemption?",
         "Immediate penalty exposure under Section 277 (prosecution + fine) for false declaration + the tax and interest on the shortfall becoming payable by you. Correct action: notify deductors immediately to start TDS deduction; file ITR correctly reflecting all income; pay any shortfall + interest. Prevention: conservative estimation + annual review."),
        ("Does Form 15G/15H apply to NRIs?",
         "No - specifically only for RESIDENT individuals / HUF / trust. NRIs cannot submit 15G/15H. For NRI income, specific TDS at Section 195 rates + treaty rate via Form 41 (old 10F) + TRC applies. Also NRI can claim refund of excess TDS via Indian ITR."),
        ("How can I avoid or reduce TDS on FD interest?", "For a resident, banks deduct TDS only when interest from that bank crosses INR 50,000 in the year (INR 1 lakh for senior citizens), at 10% with a PAN. If your total income is below the taxable limit, give the bank Form 15G (or 15H if you are 60 or over) at the start of the year; otherwise the TDS is simply credited against your tax when you file the ITR, and any excess is refunded. Splitting deposits across banks does not change the tax, only when it is deducted. For an NRI the rules are different: interest on NRE and FCNR deposits is tax-free and has no TDS, while NRO interest suffers TDS at about 31.2% (higher with surcharge) and Forms 15G / 15H cannot be used. An NRI can bring that down by giving the bank a tax residency certificate, Form 41 (old 10F) and PAN to get the lower DTAA rate for their country, or by applying for a lower or nil deduction certificate in Form 128 (old 13) where their actual tax is lower - and can always claim back excess TDS through the Indian return. Without a PAN, TDS goes up. WhatsApp +91 78018 87130 with your residential status, the banks and deposit types (NRE, NRO, FCNR or resident FD), the interest for the year and your Form 168 / AIS, or book a call."),
        ("How do I get a refund when the bank has deducted TDS on my fixed deposit?", "The bank cannot return TDS once it has been deposited with the government. File your income tax return for the year, show the FD interest as income and claim the TDS credit shown in your Form 26AS and AIS. If your total tax is less than the TDS, the excess is refunded to your pre-validated bank account after the return is processed. To avoid it next year, submit Form 15G or 15H at the start of the year if you are eligible; NRIs cannot use these forms but can file a return to claim the refund or apply for a lower deduction certificate."),
        ("What's the dividend TDS threshold for 15G/15H?",
         "Section 194 TDS on dividend from Indian company: 10% TDS above INR 10,000 per FY per person (threshold raised from INR 5,000 from 1 April 2025). 15G/15H can be submitted to company to avoid TDS when overall income is below exemption. Many Indian retail dividend recipients eligible for 15G/15H."),
        ("Does BQP help senior citizens with 15H + Indian ITR?",
         "Yes - standard senior citizen tax engagement. 15H submission to all deductors (banks + companies + tenants) at start of FY + Form 26AS reconciliation + annual ITR filing + Section 80TTA / 80TTB specific deductions + Section 194P / 194A specific exemptions. Scope-based engagement. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("itr-filing-ay-2026-27-deadlines-changes-india.html", "Related", "ITR AY 2026-27"),
                      ("new-vs-old-tax-regime-calculator.html", "Related", "New vs Old Regime")],
    "cta_h": "Senior citizen or low-income individual - avoid unnecessary TDS?",
    "cta_b": "Form 15G / 15H submission + Form 26AS reconciliation + Indian ITR. BQP scope-based engagement for senior citizens.",
    "keywords": "Form 15G 15H India 2026, no TDS declaration senior citizen India, Section 197A India CA",
    "desc": "Form 15G / 15H no-TDS declaration India 2026: Section 197A, 15G (below 60 + HUF / trust) vs 15H (senior citizen 60+), eligibility conditions, deductor-wise submission, Section 277 false declaration penalty, Section 201 interest. Working CA guide by Durgesh Chavda.",
})

# 2. Form 67 Foreign Tax Credit
PAGES.append({
    "slug": "form-67-foreign-tax-credit-india-2026",
    "title": "DTAA (Double Taxation Avoidance Agreement) Relief and Foreign Tax Credit in India (2026): Section 90 vs 91, How Relief Is Calculated and Filing Form 67 (Now Form 44)",
    "hero_em": "DTAA FTC claim mechanism.",
    "lead": "Form 67 is mandatory for Indian resident claiming Foreign Tax Credit (FTC) under Section 90 or 91 of Income Tax Act. Filed with Indian ITR. Covers taxes paid in foreign country on income doubly taxable (India + foreign country). Section 90 for DTAA countries; Section 91 for non-DTAA countries. Here's the complete 2026 filing framework.",
    "kicker": "/ FTC Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ When Form 67 applies", "FTC core.",
         "<ul>"
         "<li>Indian tax resident with foreign-source income that's taxed in BOTH foreign country AND India.</li>"
         "<li>Claiming credit for foreign tax paid against Indian tax liability on same income.</li>"
         "<li>Section 90 (DTAA country, e.g., US / UK / Singapore / UAE / Mauritius): treaty-based FTC.</li>"
         "<li>Section 91 (non-DTAA country): unilateral FTC under domestic law.</li>"
         "<li>Credit is LOWER of (a) foreign tax paid, OR (b) Indian tax attributable to foreign income.</li>"
         "<li><strong>Must file Form 67</strong>: best filed before or with the ITR; rule 128(9) allows it up to the end of the assessment year if the return is filed on time or as a belated return.</li>"
         "</ul>"),
        ("/ Common FTC scenarios", "Where it comes up.",
         "<ul>"
         "<li>Indian green card holder with US salary (also taxed in US) + Indian ITR disclosing worldwide income.</li>"
         "<li>Indian resident with US / UK rental property (foreign tax on rental + Indian tax).</li>"
         "<li>Indian investor in US / foreign stocks (dividend tax in source country + Indian tax).</li>"
         "<li>Indian consultant to foreign client with tax deducted at source (treaty rate).</li>"
         "<li>Indian subsidiary of foreign group - cross-border salary / consulting flows to Indian team.</li>"
         "<li>Indian expat on short-term foreign deputation (foreign tax deducted + Indian tax on repatriated income).</li>"
         "</ul>"),
        ("/ Form 67 structure", "The data.",
         "<ul>"
         "<li>Country of foreign tax.</li>"
         "<li>Nature of income (salary / rental / interest / dividend / capital gain).</li>"
         "<li>Amount of foreign income.</li>"
         "<li>Foreign tax paid.</li>"
         "<li>Indian tax before FTC on same income.</li>"
         "<li>FTC claimed (lower of foreign tax paid or Indian tax).</li>"
         "<li>Supporting: foreign tax authority receipt / foreign withholding certificate / foreign ITR copy.</li>"
         "<li>CA attestation on specific aspects of claim.</li>"
         "</ul>"),
        ("/ Common FTC mistakes", "Where returns trip.",
         "<ul>"
         "<li><strong>Form 67 not filed</strong>: AO denies FTC entirely even if actually paid. Mandatory procedural requirement.</li>"
         "<li><strong>Filed after the end of the assessment year</strong>: FTC can be denied. Up to that date Form 67 is accepted if the return was filed under section 139(1) or 139(4) (rule 128(9)); with an updated return it must be filed by the date of that return.</li>"
         "<li><strong>Over-claim</strong>: credit cannot exceed Indian tax on same income. If foreign tax > Indian tax, excess cannot be refunded.</li>"
         "<li><strong>Wrong currency conversion</strong>: must convert foreign tax at the SBI telegraphic transfer buying rate on the last day of the month before the month in which the foreign tax was paid or deducted (rule 128(4)).</li>"
         "<li><strong>Non-DTAA country mistake</strong>: Section 91 (unilateral) applies to residents with income from a non-DTAA country; Section 90 for DTAA countries. Different credit mechanics.</li>"
         "<li><strong>Specific income DTAA treatment</strong>: some income types (salary via Article 15, dividend via Article 10) have specific allocation rules. FTC under Section 90(1).</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("When is Form 67 due?",
         "For assessment years up to 2026-27, rule 128(9) (substituted by Notification 100/2022, effective 1 April 2022) allows Form 67 to be filed on or before the end of the assessment year, provided the return is filed within the time under section 139(1) or 139(4); with an updated return under section 139(8A), by the date that return is filed. For AY 2026-27 that means by 31 March 2027, but filing Form 67 before or with the ITR avoids processing mismatches. From tax year 2026-27 the form is Form 44 under the Income-tax Rules, 2026; check its time limit."),
        ("What's the difference between Section 90 and 91 FTC?",
         "Section 90: FTC under DTAA (bilateral treaty with specific country - US, UK, Singapore, UAE, Mauritius, Canada, Australia, Germany etc.). Section 91: unilateral relief for residents of India with income from a country that has no treaty with India. Different mechanics - Section 90 relies on treaty article; Section 91 relies on domestic Indian provision."),
        ("Can I claim FTC in Indian ITR without filing Form 67?",
         "No - rule 128(8) requires Form 67 for a foreign tax credit claim. Notification 100/2022 lets it be filed up to the end of the assessment year if the return is filed under section 139(1) or 139(4), and with an updated return by the date that return is filed. Filing Form 67 first, then the ITR, avoids mismatches."),
        ("Is FTC limited to Indian tax on foreign income?",
         "Yes - FTC = LOWER of (a) foreign tax paid, OR (b) Indian tax attributable to foreign income. Excess foreign tax above Indian tax cannot be refunded. Material in high-tax foreign jurisdictions (US / UK) where foreign tax exceeds Indian equivalent."),
        ("How is DTAA relief calculated?", "Under section 90 and rule 128, the credit for each item of foreign income is the lower of the foreign tax paid on it and the Indian tax payable on that income, worked out country by country and source by source; any excess foreign tax is not refunded or carried forward. Under section 91, a resident with income from a country that has no treaty with India gets relief on the doubly taxed income at the Indian rate of tax or the foreign rate, whichever is lower. Foreign tax that is disputed is allowed only once the dispute is settled."),
        ("What should I send to claim foreign tax credit?", "WhatsApp us your foreign tax return or year-end tax statement (for example a US 1040 and 1099 / W-2 forms, a UK SA302, or a payslip with tax withheld), proof of tax paid or deducted with dates, your Indian AIS / Form 168, and the country of the income. We work out the credit country by country, prepare Form 67 (Form 44 from tax year 2026-27) and match it with your ITR."),
        ("How do I convert foreign tax to INR for Form 67?",
         "Use the SBI telegraphic transfer buying rate on the last day of the month before the month in which the foreign tax was paid or deducted (rule 128(4)), not an FY average or the ITR filing date. Keep a record of each payment date and rate; convert each foreign tax payment separately."),
        ("Does BQP handle Form 67 FTC claims?",
         "Yes - standard advisory for cross-border tax clients. Form 67 drafting + supporting document assembly + e-filing before ITR + FTC optimization under DTAA / Section 91 + co-ordination with foreign tax authority receipts + Indian ITR integration. For returning NRIs / US green card holders / Indian expats / cross-border investors. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("us-green-card-holder-india-tax-complete-2026.html", "Related", "US Green Card India Tax"),
                      ("nri-dtaa-claim-practical-trc-form-10f.html", "Related", "NRI DTAA Practical")],
    "cta_h": "Indian resident with foreign-source income taxed abroad?",
    "cta_b": "Form 67 FTC claim before ITR + Section 90/91 under DTAA + currency conversion.",
    "keywords": "Form 67 FTC India 2026, Foreign Tax Credit CA India, Section 90 91 CA India, DTAA FTC CA",
    "desc": "Form 67 Foreign Tax Credit (FTC) India 2026 complete checklist: Section 90 (DTAA countries) vs Section 91 (non-DTAA), Form 67 required for the claim (up to the end of the assessment year with a timely or belated return), foreign tax converted at the SBI TT buying rate, credit limit = lower of foreign tax or Indian tax on same income. Working CA guide by Durgesh Chavda.",
})

# 3. Form MGT-14
PAGES.append({
    "slug": "form-mgt-14-board-shareholder-resolution-filing-india-2026",
    "title": "Form MGT-14 Board / Shareholder Resolution Filing India 2026",
    "hero_em": "30-day ROC resolution reporting.",
    "lead": "Form MGT-14 is mandatory ROC filing for specified board + shareholder resolutions within 30 days of passing. Section 117 Companies Act 2013 + Rule 24 Companies (Management and Administration) Rules 2014. Covers specified resolution types requiring ROC reporting. Here's the complete 2026 filing checklist.",
    "kicker": "/ ROC Form Checklist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Resolutions requiring MGT-14", "Specific triggers.",
         "<ul>"
         "<li><strong>Specific board resolutions (Section 117(1)(b))</strong>: calls on partly paid shares, buyback approval, grant of loan / guarantee / security to related party above threshold, borrowing (Section 180), issue of debentures.</li>"
         "<li><strong>Specific board resolutions (Section 179(3))</strong>: borrowing exceeding paid-up + free reserves, investment / loan given > threshold, approving financial statements, appointment / removal of KMP, prospectus approval.</li>"
         "<li><strong>Special resolutions (Section 117(1)(c))</strong>: all special resolutions require MGT-14 (resolutions requiring 75%+ vote - MOA / AOA amendment, change of registered office outside state, voluntary winding up, specific other matters).</li>"
         "<li><strong>Not all resolutions require MGT-14</strong>: ordinary business, standard dividend declaration, routine committee delegations do NOT need MGT-14.</li>"
         "</ul>"),
        ("/ 30-day filing deadline", "The clock.",
         "<ul>"
         "<li>Form MGT-14 due within <strong>30 days of passing the resolution</strong>.</li>"
         "<li>Attach: certified copy of resolution + explanatory statement + annexures.</li>"
         "<li>DSC of director / company secretary who signs.</li>"
         "<li>Late fee: 2x normal fee + delay-period multiplier under MCA Fee Rules.</li>"
         "<li>Section 117(2): company + every officer in default fine up to INR 10 lakh.</li>"
         "</ul>"),
        ("/ Common MGT-14 scenarios", "Where it comes up.",
         "<ul>"
         "<li>Change of registered office outside state (special resolution + MGT-14 + INC-23).</li>"
         "<li>MOA / AOA amendment (special resolution).</li>"
         "<li>Buyback approval (board resolution).</li>"
         "<li>Section 180 borrowing exceeding paid-up + free reserves + securities premium.</li>"
         "<li>Preferential allotment (special resolution + PAS-3 share allotment).</li>"
         "<li>Issue of debentures.</li>"
         "<li>Appointment / removal of CEO / CFO / Managing Director / Company Secretary.</li>"
         "<li>Voluntary winding up resolution.</li>"
         "</ul>"),
        ("/ Compliance workflow", "Step-by-step.",
         "<ol>"
         "<li>Pre-meeting: identify whether resolution needs MGT-14 (consult Section 117 + 179 + special resolution list).</li>"
         "<li>Draft resolution text + explanatory statement.</li>"
         "<li>Hold board / general meeting + pass resolution.</li>"
         "<li>Certified copy of resolution signed by director + company secretary.</li>"
         "<li>Prepare Form MGT-14 with annexures.</li>"
         "<li>DSC apply + file via MCA v3 portal within 30 days.</li>"
         "<li>Preserve filing acknowledgement + resolution copy 8+ years.</li>"
         "<li>If related matters trigger other forms (INC-23 for registered office change, PAS-3 for allotment, DIR-12 for director change): file concurrently.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("Which resolutions require Form MGT-14?",
         "Section 117 Companies Act specifies: specific board resolutions under 179(3), all special resolutions, specific resolutions under 117(1)(b). Includes MOA/AOA amendment, change of registered office outside state, buyback, borrowing above Section 180 limit, preferential allotment, debenture issue, KMP appointment, voluntary winding up. Not all board / ordinary resolutions need MGT-14."),
        ("What's the deadline for MGT-14 filing?",
         "30 days from passing the resolution. Late fee: 2x normal + delay-period multiplier under MCA Fee Rules. Section 117(2) penalty: company + every officer in default up to INR 10 lakh."),
        ("Can I file MGT-14 for multiple resolutions in one form?",
         "Yes - multiple related resolutions passed in same meeting can be filed in one Form MGT-14 with multiple annexures. Example: AGM special resolution + specific board resolution on same topic can be combined. Each resolution attached as separate annexure."),
        ("What's the penalty for missing MGT-14?",
         "Section 117(2): company fine INR 1-5 lakh per failure + every officer in default INR 25,000-5 lakh (minimum penalties post Companies Amendment Act 2020). Also default by directors blocks subsequent MCA filings until resolved. Materially higher than most Companies Act penalties."),
        ("Does the resolution need to be certified by CS?",
         "Yes - certified true copy of resolution signed by director + Company Secretary (if company has CS). For companies without CS, director signs + specifies company doesn't have CS. ICAI UDIN for CS where applicable."),
        ("Does BQP file MGT-14 for board / special resolutions?",
         "Yes - integrated with standard CS services. Resolution drafting + explanatory statement + MGT-14 preparation + MCA v3 portal filing within 30-day deadline + related form coordination (INC-23, PAS-3, DIR-12). Standard engagement for mid-size + large companies. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("company-secretarial-services-india-remote.html", "Related", "CS Services"),
                      ("dir-3-kyc-director-annual-compliance-india.html", "Related", "Director Compliance")],
    "cta_h": "Board / special resolution passed? Form MGT-14 in 30 days.",
    "cta_b": "Resolution drafting + certified copy + MGT-14 + related form coordination. BQP integrated CS services.",
    "keywords": "Form MGT-14 India 2026, Section 117 Companies Act MGT-14, board resolution ROC filing CA, special resolution MGT-14 CA",
    "desc": "Form MGT-14 board / shareholder resolution filing India 2026: Section 117 Companies Act + Rule 24 Companies Rules, 30-day deadline, specific resolution types (special resolutions, Section 179(3) board, 117(1)(b) specific), Section 117(2) penalty up to INR 10 lakh. Working CA guide by Durgesh Chavda.",
})

# 4. Best CA Section 54F
PAGES.append({
    "slug": "best-ca-section-54f-capital-gain-reinvestment-india",
    "title": "Best CA for Section 54F Capital Gain Reinvestment India",
    "hero_em": "non-residential LTCG exempt via residential reinvestment.",
    "lead": "Section 54F Income Tax Act: LTCG on sale of any long-term asset (NOT residential property) is EXEMPT if net consideration invested in one residential property in India within specified timelines. Powerful but conditions-rich provision. Post Finance Act 2024, LTCG 12.5% + Section 54F reinvestment combination is a key tax-saving tool. Here's the complete 2026 BQP Section 54F framework.",
    "kicker": "/ Section 54F Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Section 54F core rule", "The exemption.",
         "<ul>"
         "<li>Available to <strong>individual + HUF only</strong> (not companies, firms, LLPs).</li>"
         "<li>LTCG on sale of ANY long-term asset EXCEPT residential property.</li>"
         "<li>Covers: shares + mutual funds + gold + unlisted shares + commercial property + land + specific non-residential assets.</li>"
         "<li><strong>Full exemption</strong> if net consideration (not just gain) invested in ONE residential property in India within:</li>"
         "<li>&nbsp;&nbsp;&mdash; 1 year back from sale OR</li>"
         "<li>&nbsp;&nbsp;&mdash; 2 years forward from sale (purchase) OR</li>"
         "<li>&nbsp;&nbsp;&mdash; 3 years forward (construction).</li>"
         "<li>If part of net consideration invested: proportional exemption.</li>"
         "</ul>"),
        ("/ Section 54F specific conditions", "The strict rules.",
         "<ul>"
         "<li>Taxpayer must NOT own more than ONE residential property on date of sale (other than the new property being purchased).</li>"
         "<li>New residential property must NOT be sold within 3 years of purchase (else exemption clawed back).</li>"
         "<li>Only ONE residential property allowed as reinvestment destination (not multiple).</li>"
         "<li>Property must be in INDIA (not foreign).</li>"
         "<li>Must be residential (not commercial / land).</li>"
         "<li>If LTCG asset is shares: specific application of Section 112A rules (12.5% post Finance Act 2024).</li>"
         "</ul>"),
        ("/ Section 54 vs 54F", "The difference.",
         "<ul>"
         "<li><strong>Section 54</strong>: for LTCG on sale of RESIDENTIAL property reinvested in residential property.</li>"
         "<li><strong>Section 54F</strong>: for LTCG on sale of NON-residential asset (shares, MF, gold, commercial, land) reinvested in residential property.</li>"
         "<li>Section 54: exempts the GAIN (if gain invested).</li>"
         "<li>Section 54F: exempts the full LTCG if full NET CONSIDERATION invested (strict).</li>"
         "</ul>"),
        ("/ Common 54F mistakes", "Where returns trip.",
         "<ul>"
         "<li><strong>Net consideration vs gain confusion</strong>: 54F requires full net consideration invested; 54 requires gain invested. Different standards.</li>"
         "<li><strong>Multiple residential property on sale date</strong>: owning 2+ residential properties (other than reinvestment target) disqualifies 54F.</li>"
         "<li><strong>Investment in commercial / land</strong>: 54F requires RESIDENTIAL. Commercial reinvestment doesn't qualify.</li>"
         "<li><strong>Foreign residential property</strong>: 54F requires property in India.</li>"
         "<li><strong>Sale of new property within 3 years</strong>: clawback - prior-year exemption added back + tax at 54F recapture rate.</li>"
         "<li><strong>Multiple residential properties as reinvestment</strong>: only ONE allowed under 54F.</li>"
         "<li><strong>Timing - 2 vs 3 year window</strong>: purchase 2 years forward; construction 3 years forward. Must complete within window.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's Section 54F exemption?",
         "LTCG on sale of any long-term asset (NOT residential property) is EXEMPT if net consideration (not just gain) invested in ONE residential property in India within specified timelines. Powerful tax-saving provision for sale of shares / MF / gold / commercial property / land + reinvestment in residential property."),
        ("Can I claim Section 54F for sale of shares?",
         "Yes - shares are 'long-term asset' (held > 12 months for listed; > 24 months for unlisted). LTCG on share sale invested in one residential property in India qualifies for 54F. Common tax-saving strategy for retail investors + ESOP exercise + startup secondary sales."),
        ("Can I invest in multiple residential properties under 54F?",
         "No - 54F allows reinvestment in ONLY ONE residential property. Section 54 (for residential property sale) allowed TWO residential properties under specific conditions in some older interpretations - but even that has restrictions. 54F is strictly ONE residential property."),
        ("What if I sell the new residential property within 3 years?",
         "Clawback: prior-year 54F exemption is added back to taxable income in the year of new property sale. Taxed as LTCG. Additional interest + penalty may apply. 3-year lock-in is strict."),
        ("Can NRI claim Section 54F?",
         "Yes - NRI individual can claim Section 54F for LTCG on sale of non-residential Indian asset (shares, MF, gold, commercial property) reinvested in Indian residential property. Same conditions apply. Combined with LDC under Section 197 for TDS reduction."),
        ("Does BQP handle Section 54F planning + LTCG optimisation?",
         "Yes - specialist capital gains practice. Section 54F eligibility + reinvestment timing + Section 54 vs 54F decision + LDC under Section 197 for NRI + Section 54EC bond overflow strategy + Capital Gain Account Scheme (CGAS) parking + ITR filing with exemption claim. Pre-sale planning + post-sale execution. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Related", "LTCG 12.5%"),
                      ("best-ca-nri-property-sale-section-54-reinvestment.html", "Related", "NRI Property Sale 54")],
    "cta_h": "Sold non-residential asset at long-term gain? Section 54F reinvestment.",
    "cta_b": "Full net consideration + one residential property + 2/3 year window. BQP capital gains + reinvestment specialist. 48-hour quote.",
    "keywords": "best CA Section 54F India, Section 54F capital gain CA, 54F residential reinvestment CA, 54F ESOP sale CA",
    "desc": "Best CA for Section 54F capital gain reinvestment India: LTCG exemption on non-residential asset sale via residential property reinvestment, net consideration vs gain, Section 54 vs 54F, 1 year back / 2 years forward purchase / 3 years construction, Finance Act 2024 LTCG 12.5% integration. Working CA guide by Durgesh Chavda.",
})

# 5. Best CA Section 44AD/ADA
PAGES.append({
    "slug": "best-ca-section-44ad-44ada-presumptive-scheme-india",
    "title": "Presumptive Taxation Scheme (Section 44AD / 44ADA, Now Section 58) 2026: Meaning, Limits, 6% / 8% / 50% Rates, ITR-4 and CA Help",
    "hero_em": "small business + professional simplified tax regime.",
    "lead": "Section 44AD (small business) + Section 44ADA (specified professionals) presumptive tax scheme: deemed profit at 6% / 8% (business) or 50% (professional). No tax audit obligation. Single advance tax instalment. Simplified compliance. 2026 enhanced thresholds (INR 3 crore / INR 75 lakh for 95%+ digital receipts). Here's the complete BQP presumptive framework.",
    "kicker": "/ Presumptive Scheme Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Section 44AD (small business)", "The core.",
         "<ul>"
         "<li>Available for: resident individual + HUF + Partnership firm (not LLP) + eligible business.</li>"
         "<li><strong>Turnover threshold</strong>: INR 2 crore standard; INR 3 crore if 95%+ digital receipts (Finance Act, 2023).</li>"
         "<li><strong>Deemed profit</strong>: 8% of gross receipts (6% for digital receipts).</li>"
         "<li>Exempt from: tax audit under Section 44AB, books of accounts under Section 44AA.</li>"
         "<li>Advance tax: payable in single instalment by 15 March of FY (vs 4 instalments standard).</li>"
         "<li>Must declare 8%/6% deemed profit; cannot declare lower without tax audit.</li>"
         "<li>Opt-in binding for 5 years - if opt-out any year, 5-year lockout from re-opting.</li>"
         "</ul>"),
        ("/ Section 44ADA (specified professionals)", "The professionals.",
         "<ul>"
         "<li>Available for: resident individual + HUF (specific professionals - not entity).</li>"
         "<li><strong>Covered professions</strong>: legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, other notified professions.</li>"
         "<li><strong>Turnover threshold</strong>: INR 50 lakh standard; INR 75 lakh if 95%+ digital receipts.</li>"
         "<li><strong>Deemed profit</strong>: 50% of gross receipts.</li>"
         "<li>Exempt from tax audit + books of accounts.</li>"
         "<li>Advance tax: single instalment by 15 March.</li>"
         "<li>Cannot declare lower than 50% without tax audit.</li>"
         "</ul>"),
        ("/ When presumptive vs normal regime", "The decision.",
         "<ul>"
         "<li><strong>Presumptive makes sense</strong>: Business with gross margin above deemed % (actual profit > 8%/6% for 44AD, > 50% for 44ADA). Deemed profit is cap on tax; actual higher margin isn't taxed.</li>"
         "<li><strong>Normal regime makes sense</strong>: Business with gross margin BELOW deemed % (actual profit lower than 8%/50%). Normal regime allows reporting actual lower profit with proper books + audit if above threshold.</li>"
         "<li><strong>Also consider</strong>: compliance burden (presumptive is much simpler), advance tax structure, cash flow, deductibility of specific expenses.</li>"
         "</ul>"),
        ("/ Common presumptive scheme mistakes", "Where filings trip.",
         "<ul>"
         "<li><strong>Turnover exceeded in later year</strong>: must exit presumptive + apply normal regime + tax audit if applicable.</li>"
         "<li><strong>Opt-out triggers 5-year lockout</strong>: cannot opt back into presumptive for 5 FYs after opt-out. Material if circumstances fluctuate.</li>"
         "<li><strong>95%+ digital receipts threshold</strong>: higher INR 3 crore / INR 75 lakh thresholds apply only if 95%+ receipts digital. Cash-heavy business doesn't qualify for higher limit.</li>"
         "<li><strong>Declaring profit below deemed %</strong>: triggers tax audit + books of accounts obligation. Common for low-margin business - must choose: deemed % profit OR normal regime with audit.</li>"
         "<li><strong>Non-specified profession under 44ADA</strong>: software consultancy / management consultancy / specific tech services - borderline cases. CBDT clarifications matter.</li>"
         "<li><strong>Firm vs individual</strong>: 44ADA covers resident individuals and partnership firms (not LLPs) - not HUFs. 44AD covers resident individuals, HUFs and partnership firms (not LLPs).</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the Section 44AD turnover threshold for 2026?",
         "INR 2 crore standard; INR 3 crore if 95%+ receipts digital (raised by the Finance Act, 2023 from AY 2024-25). Deemed profit 8% of gross receipts (6% for digital). Available for resident individual + HUF + Partnership firm (not LLP) + eligible business."),
        ("What's the Section 44ADA turnover threshold for 2026?",
         "INR 50 lakh standard; INR 75 lakh if 95%+ receipts digital. Deemed profit 50% of gross receipts. Available to resident individuals and partnership firms (other than LLPs) carrying on specified professions (legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration and other notified professions) - not to HUFs."),
        ("What is presumptive taxation?", "A scheme that lets small businesses and professionals declare income at a fixed percentage of turnover or receipts instead of keeping full books and getting a tax audit: 8% of turnover (6% for digital receipts) for eligible businesses under section 44AD, and 50% of gross receipts for specified professionals under section 44ADA. From tax year 2026-27 these are merged into section 58 of the Income-tax Act, 2025, with the same core rates."),
        ("Which ITR form is used for presumptive taxation?", "ITR-4 (Sugam) for resident individuals, HUFs and firms (other than LLPs) with total income up to Rs 50 lakh who opt for presumptive taxation; others, including those with capital gains beyond the simple cases or foreign assets, use ITR-3 (or ITR-5 for firms)."),
        ("Can I declare profit lower than 8% or 50%?",
         "Yes - but triggers tax audit under Section 44AB + books of accounts under Section 44AA + advance tax in 4 instalments. Essentially exits presumptive scheme. If business genuinely has lower margin, normal regime + audit is appropriate. Just presumptive declaration below deemed % without audit is non-compliant."),
        ("What is a 44AD audit?", "It is the common name for the tax audit under section 44AB that applies when a business eligible for section 44AD declares profit below 8% of turnover (6% for digital receipts), or has opted out of 44AD within the last five years, and its total income exceeds the basic exemption limit. The business must then keep books of account and have them audited by a chartered accountant, with the audit report filed by its due date. Professionals under section 44ADA face the same rule if they declare less than 50% of receipts. From tax year 2026-27 the equivalent provisions sit in the Income-tax Act, 2025."),
        ("Can my LLP opt into Section 44AD?",
         "No - LLP specifically excluded. 44AD covers: resident individual + HUF + Partnership firm (not LLP). For LLP, normal regime applies + tax audit if turnover > INR 1 crore (standard INR 10 crore for 95%+ digital). Consider conversion to partnership firm if presumptive beneficial."),
        ("What's the 5-year lockout rule under 44AD?",
         "If taxpayer opts out of presumptive scheme (declaring lower profit or using normal regime), they cannot opt back into 44AD for 5 FYs following opt-out. Section 44AD(4). Must think long-term before opt-out. Doesn't apply to 44ADA."),
        ("Does BQP handle presumptive vs normal regime decision + ITR?",
         "Yes - standard tax advisory. Presumptive vs normal regime comparison + 5-year projection + ITR-3 / ITR-4 filing + advance tax structure + Section 54 reinvestment planning if applicable + tax audit coordination if normal regime. For individual / HUF / Partnership firm clients. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("freelancer-consultant-tax-india-2026-complete.html", "Related", "Freelancer / Consultant Tax"),
                      ("best-ca-freelancer-consultant-tax-india-2026.html", "Related", "Best CA for Freelancer")],
    "cta_h": "Small business / professional - presumptive or normal regime?",
    "cta_b": "Section 44AD / 44ADA eligibility + deemed vs actual profit + 5-year projection + ITR filing. BQP presumptive scheme specialist.",
    "keywords": "best CA Section 44AD India, Section 44ADA presumptive CA, 44AD 44ADA presumptive scheme CA India",
    "desc": "Best CA for Section 44AD / 44ADA presumptive scheme India 2026: 44AD small business 8%/6% deemed profit INR 2-3 crore threshold, 44ADA professional 50% deemed profit INR 50-75 lakh threshold, Finance Act 2023 enhanced thresholds, 5-year lockout rule, single advance tax instalment. Working CA guide by Durgesh Chavda.",
})

# 6. Best CA Section 194R
PAGES.append({
    "slug": "best-ca-section-194r-tds-business-perquisites-compliance",
    "title": "Best CA for Section 194R TDS Business Perquisites Compliance",
    "hero_em": "10% TDS on business freebies + gifts + sampling.",
    "lead": "Section 194R Income Tax Act (effective 1 July 2022): 10% TDS on business perquisites + gifts + benefits given by payer to resident recipient during business / profession. Applies to free samples, conference / travel sponsorship, equipment / vehicles / electronics gifts, award / prize, hospitality above INR 20,000 per year per recipient. Pharma + tech + consumer-goods industries primary impact. Here's the complete BQP compliance framework.",
    "kicker": "/ Section 194R Specialist &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Section 194R core rule", "The 10% + aggregation.",
         "<ul>"
         "<li>Any person (business / profession) giving benefit / perquisite to resident recipient (business / profession receiver) must deduct 10% TDS.</li>"
         "<li>Threshold: INR 20,000 per FY per recipient (aggregated).</li>"
         "<li>Perquisite / benefit forms: free samples, free equipment / vehicles / electronics, conference / travel sponsorship, hospitality, awards, prizes, specific free services.</li>"
         "<li>Deductor: payer (business providing benefit).</li>"
         "<li>TDS at 10% on fair market value of benefit (not just cash cost).</li>"
         "<li>Form 26Q quarterly return + Form 16A to recipient.</li>"
         "<li>Section 206AA: 20% rate if recipient PAN unavailable.</li>"
         "</ul>"),
        ("/ Common 194R trigger scenarios", "Where it applies.",
         "<ul>"
         "<li><strong>Pharma marketing to doctors</strong>: samples + conference sponsorship + equipment loans + hospitality. Primary 194R target when introduced 2022.</li>"
         "<li><strong>Tech / SaaS to beta customers</strong>: free API credits, free POCs, free equipment loans, hackathon prizes.</li>"
         "<li><strong>Consumer goods to influencers / content creators</strong>: free products, sponsored travel, event tickets.</li>"
         "<li><strong>Banking + financial services to intermediaries</strong>: referral rewards, free training programmes, travel incentives.</li>"
         "<li><strong>Insurance to agents</strong>: incentive trips, equipment grants, free training.</li>"
         "<li><strong>Platform / marketplace to sellers</strong>: free promotional campaigns, equipment grants, specific free services.</li>"
         "<li><strong>Agencies to clients</strong>: free upgrades, promotional additions beyond contracted scope.</li>"
         "</ul>"),
        ("/ Who's exempt", "The carve-outs.",
         "<ul>"
         "<li>Benefits to resident SALARIED employee: Section 192 TDS applies instead (salary perquisite route).</li>"
         "<li>Benefits in cash: Section 194R applies if cash > INR 20K / FY. For non-business cash gifts: Section 56(2)(x).</li>"
         "<li>Discounts + rebates in course of trade: typically not 194R (reduces sale value, not separate benefit).</li>"
         "<li>Specific entity benefits: company to subsidiary own-group benefits may not be 194R-triggered (specific CBDT clarifications).</li>"
         "<li>Below INR 20K / recipient / FY aggregate threshold: no 194R.</li>"
         "</ul>"),
        ("/ Compliance workflow", "The operating playbook.",
         "<ol>"
         "<li>Identify all benefit-giving activities + recipients.</li>"
         "<li>Fair market value estimation for non-cash benefits (equipment, hospitality, travel, prizes).</li>"
         "<li>Recipient PAN collection + verification.</li>"
         "<li>Section 206AA 20% rate if PAN missing - decide: collect PAN or absorb higher rate.</li>"
         "<li>TDS deposit via Challan ITNS 281 within 7 days of month-end.</li>"
         "<li>Form 26Q quarterly return.</li>"
         "<li>Form 16A to each recipient quarterly.</li>"
         "<li>Recipient-side: Section 194R benefit treated as income under 'Business / Profession' or 'Other Sources' depending on nature; must disclose in ITR.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's Section 194R and when does it apply?",
         "10% TDS on business perquisites / benefits given by payer to resident recipient during business / profession. Threshold: INR 20,000 per FY per recipient. Applies to free samples, equipment loans, conference sponsorship, hospitality, awards, prizes above threshold. Introduced Finance Act 2022, effective 1 July 2022."),
        ("Does Section 194R apply to employee bonus / perquisite?",
         "No - employee perquisites are under Section 192 TDS (salary perquisite route). Section 194R specifically for business / profession benefits (payer giving benefit to another business or professional person) - NOT employer giving to employee."),
        ("How to value non-cash benefits for 194R?",
         "Fair market value. For equipment: current purchase price or market rate. For hospitality: actual cost. For travel: actual cost of ticket + accommodation. For prizes: declared / announced value. Deductor's responsibility to document FMV methodology; defensible to AO scrutiny."),
        ("What if recipient refuses to provide PAN?",
         "Section 206AA applies: 20% TDS rate (vs 10% standard). Can either collect PAN or absorb higher rate. For material benefit values, PAN collection usually easier than 20% hit."),
        ("Does 194R apply to discounts and trade margins?",
         "Generally no - discounts / rebates in course of ordinary trade reduce sale consideration, not separate benefit. CBDT clarifications (Circulars 2022-2023) specifically address this. Documentary trail (sale invoice reflecting discount) important to defend non-194R classification."),
        ("Does BQP handle Section 194R compliance for industries with high perquisite activity?",
         "Yes - specialist practice for pharma + tech + consumer goods + financial services + insurance industries. 194R applicability analysis + recipient master + FMV methodology + Form 26Q quarterly + Form 16A issuance + CBDT clarification advisory + specific exemption cases. Scope-based engagement for mid-size + large companies. WhatsApp +91 78018 87130."),
    ],
    "related_pairs": [("section-194r-tds-business-perquisites-india.html", "Related", "Section 194R Full Guide"),
                      ("best-ca-healthtech-india-2026.html", "Related", "Best CA for Healthtech")],
    "cta_h": "Business giving perquisites to doctors / influencers / agents?",
    "cta_b": "194R compliance stack: identification + FMV + PAN + 10% TDS + Form 26Q + Form 16A. BQP pharma / tech / consumer goods specialist practice.",
    "keywords": "best CA Section 194R TDS India, 194R business perquisite CA, 194R pharma doctor TDS CA, 194R compliance CA India",
    "desc": "Best CA for Section 194R TDS business perquisites compliance India: 10% TDS on business benefits above INR 20K / recipient / FY, pharma / tech / consumer goods primary impact, FMV methodology, PAN + Section 206AA 20% rate, Form 26Q quarterly, Form 16A issuance. Working CA guide by Durgesh Chavda.",
})

# 7. India Compliance Calendar FY 2026-27
PAGES.append({
    "slug": "india-tax-compliance-calendar-fy-2026-27-complete",
    "title": "India Tax Compliance Calendar FY 2026-27: ITR, Tax Audit, TDS, GST and Advance Tax Due Dates for Individuals and Companies",
    "hero_em": "every deadline, every form, every month.",
    "lead": "Comprehensive India tax + ROC + FEMA + GST compliance calendar for FY 2026-27 (April 2026 - March 2027). Every form + every deadline + every return. Companies + LLPs + individuals + partnerships + specific industry adds. Printable + sharable. Working CA calendar by Durgesh Chavda. Here's the complete year-at-a-glance.",
    "kicker": "/ Annual Compliance Calendar &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Monthly recurring compliance", "Every month.",
         "<ul>"
         "<li><strong>7th of month</strong>: TDS / TCS deposit for prior month (Challan ITNS 281). GST monthly PMT-06 payment.</li>"
         "<li><strong>10th</strong>: GSTR-7 TDS return + GSTR-8 TCS return (for specified).</li>"
         "<li><strong>11th</strong>: GSTR-1 (regular). Monthly return of outward supplies.</li>"
         "<li><strong>13th</strong>: GSTR-6 ISD (Input Service Distributor).</li>"
         "<li><strong>20th</strong>: GSTR-3B (monthly). Summary return + tax payment.</li>"
         "<li><strong>13th</strong>: GSTR-1 for small taxpayers under QRMP (quarterly; optional IFF monthly).</li><li><strong>22nd / 24th</strong>: GSTR-3B for small taxpayers under QRMP (by state), after each quarter.</li>"
         "<li><strong>28th</strong>: GSTR-5A (OIDAR).</li>"
         "<li><strong>Varies</strong>: PF (15th), ESI (15th), Professional Tax (state-specific).</li>"
         "</ul>"),
        ("/ Quarterly compliance", "Four times per year.",
         "<ul>"
         "<li><strong>15 June, 15 September, 15 December, 15 March</strong>: Advance tax instalments (15% / 45% / 75% / 100% cumulative).</li>"
         "<li><strong>31 July, 31 October, 31 January, 31 May</strong>: Quarterly TDS returns (Form 138 salary, 140 non-salary, 144 non-resident and 143 TCS from tax year 2026-27, replacing 24Q, 26Q, 27Q and 27EQ).</li>"
         "<li><strong>15 July, 15 October, 15 January, 15 May</strong>: Form 16A (Form 131 from tax year 2026-27) to recipients (within 15 days after the quarterly TDS statement).</li>"
         "<li><strong>End of each quarter</strong>: ESIC return (if applicable), listed company LODR Reg 33 / 29 quarterly filings.</li>"
         "</ul>"),
        ("/ Half-yearly compliance", "September + March.",
         "<ul>"
         "<li><strong>30 September + 31 March</strong>: half-year end for specific reporting.</li>"
         "<li><strong>29 November (60 days from 30 Sep)</strong>: Form PAS-6 (Rule 9B demat reconciliation). MSME Form I (dues to MSE above 45 days) for the same half-year is due earlier, by 31 October.</li>"
         "<li><strong>30 May (60 days from 31 Mar)</strong>: Form PAS-6. MSME Form I for the October-March half-year is due by 30 April.</li>"
         "<li><strong>30 September</strong>: DIR-3 KYC, now once every three years (by 30 June of the due year).</li>"
         "<li>End of HY: specific ESIC / PF statutory contributions reconciliation.</li>"
         "</ul>"),
        ("/ Annual compliance (ITR + ROC + FEMA)", "Big deadlines.",
         "<ul>"
         "<li><strong>31 May</strong>: Form 10BA / 15H self-declarations for FY (if applicable).</li>"
         "<li><strong>15 June</strong>: Q1 advance tax (15%).</li>"
         "<li><strong>30 June</strong>: Form DPT-3 (annual return of deposits) + specific state-specific due.</li>"
         "<li><strong>15 July</strong>: FLA Return (foreign liabilities + assets) to RBI.</li>"
         "<li><strong>31 July</strong>: Individuals + HUFs ITR (non-audit) + Form 10E (salary arrears relief).</li>"
         "<li><strong>31 August</strong>: AGM (if company's AGM date is specific).</li>"
         "<li><strong>30 September</strong>: AGM (last date for most companies). DIR-3 KYC is now due by 30 June, once every three financial years (from 31 March 2026).</li>"
         "<li><strong>31 October</strong>: AOC-4 (financial statements) + ITR (tax audit cases) + Form 3CA/CB + Form 3CD + Form 10-IC (115BAA opt-in) + Form 10-ID (115BAB opt-in) + MSME Form I (April-September half-year).</li>"
         "<li><strong>29 November</strong>: MGT-7 (annual return) + Form 3CEB (TP audit) + PAS-6 (September HY).</li>"
         "<li><strong>31 December</strong>: GSTR-9 (annual return) + GSTR-9C (reconciliation) + Form APR (old Form ODI Part II) + belated / revised ITR deadline.</li>"
         "<li><strong>15 December</strong>: Q3 advance tax (75% cumulative).</li>"
         "<li><strong>31 January</strong>: specific sector returns.</li>"
         "<li><strong>15 March</strong>: Q4 advance tax (100%).</li>"
         "<li><strong>31 March</strong>: FY end + Updated ITR (24-month window closes).</li>"
         "</ul>"),
        ("/ Specific-sector adds", "Industry overlays.",
         "<ul>"
         "<li><strong>Listed companies</strong>: LODR Reg 33 (financial results quarterly), Reg 29 (secretarial compliance), Reg 76 (statement of unclaimed dividend) etc.</li>"
         "<li><strong>SEBI AIF</strong>: quarterly AUM + annual AIF return.</li>"
         "<li><strong>NBFC</strong>: monthly / quarterly RBI returns + annual RBI Audit Report.</li>"
         "<li><strong>Insurance</strong>: IRDAI quarterly + annual returns.</li>"
         "<li><strong>Startups</strong>: DPIIT annual self-declaration.</li>"
         "<li><strong>Foreign-shareholder companies</strong>: FC-GPR within 30 days of allotment; FLA Return annually; Form ODI APR annually.</li>"
         "<li><strong>In BEPS Pillar 2 scope</strong>: no Indian filing yet (India has not enacted Pillar 2 rules); supply data for the group&rsquo;s return filed abroad.</li>"
         "<li><strong>In CSR scope (Section 135)</strong>: Form CSR-2 90 days post FY.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("What's the biggest-impact deadline in Q3 of FY 2026-27?",
         "15 December 2026: Q3 advance tax (75% cumulative). Material cash outflow for profitable companies + individuals. Also 29 November 2026: MGT-7 (annual return) + Form 3CEB TP audit + PAS-6 Rule 9B demat. 31 October 2026: AOC-4 + tax audit ITR + Form 3CA/CB/CD."),
        ("Which deadlines are most commonly missed?",
         "DIR-3 KYC (30 June, once every three financial years from 31 March 2026) - missing it deactivates the DIN. Form MSME-1 (31 October for April-September, 30 April for October-March) - where dues to micro or small suppliers are outstanding beyond 45 days. Form ODI APR (31 Dec) for Indian parent of foreign subsidiary. PAS-6 (29 Nov / 30 May) - Rule 9B demat. FLA Return (15 Jul) - foreign liabilities + assets to RBI."),
        ("What are the GST filing deadlines?",
         "Monthly: GSTR-1 by 11th + GSTR-3B by 20th + GSTR-7 (TDS) by 10th + GSTR-8 (TCS) by 10th. Small taxpayers under QRMP: GSTR-1 by the 13th and GSTR-3B by the 22nd or 24th (by state) of the month after each quarter, with tax paid monthly in PMT-06 by the 25th. Annual: GSTR-9 (annual return) + GSTR-9C (reconciliation) by 31 December."),
        ("What are the TDS return due dates for FY 2026-27?", "For tax year 2026-27 the quarterly TDS statements are due on 31 July 2026 (April-June), 31 October 2026 (July-September), 31 January 2027 (October-December) and 31 May 2027 (January-March). They are filed in the new forms under the Income-tax Act, 2025: Form 138 for salary, Form 140 for other payments to residents and Form 144 for payments to non-residents, with TCS in Form 143; the January-March 2026 quarter was the last filed in the old 24Q, 26Q and 27Q. Late filing attracts a fee of INR 200 a day up to the TDS amount, and a penalty can follow if the delay runs beyond a year."),
        ("Can I file ITR after the tax audit deadline?",
         "First, the deadline itself moved: for AY 2026-27 CBDT Circular 07/2026 extended the tax audit report to 21 October 2026 and the ITR for audit cases to 21 November 2026 (transfer pricing cases stay at 30 November). After the due date you can still file, but with the Section 234F late fee (INR 5,000; INR 1,000 for small income) and Section 234A interest at 1% per month. Belated ITR by 31 December 2026 for AY 2026-27. Updated return under Section 139(8A) up to 31 March 2029 (24-month window) with specific additional tax."),
        ("What is the ITR due date for a private limited company?", "Companies file ITR-6 (or ITR-7 if claiming charitable exemptions) even with a loss or nil income. Because company accounts are audited, the normal due date is 31 October after the year end, or 30 November where transfer pricing applies. For AY 2026-27, CBDT Circular 07/2026 moved the audit-case ITR date to 21 November 2026 (transfer pricing cases 30 November 2026). A company that has missed it can file a belated return by 31 December 2026 with late fee and interest."),
        ("Does BQP maintain compliance calendar for client companies?",
         "Yes - annual engagement includes maintenance of all compliance deadlines for client companies with automated monthly / quarterly / annual reminder cadence. Daily / weekly / monthly / quarterly / annual cycles tracked. Email + WhatsApp reminders. One-firm point of accountability for complete compliance stack. WhatsApp +91 78018 87130."),
        ("What's the single biggest compliance gap BQP sees?",
         "Director DIR-3 KYC (30 September). Deactivates DIN; blocks ALL subsequent MCA eForm filings. 2026-27 catch-up with INR 5,000 late fee + 24-72 hour reactivation. Many directors miss because they assume someone else is handling or forget about resigned-but-not-cancelled DINs."),
    ],
    "related_pairs": [("itr-filing-ay-2026-27-deadlines-changes-india.html", "Related", "ITR AY 2026-27 Full Guide"),
                      ("company-secretarial-services-india-remote.html", "Related", "CS Services")],
    "cta_h": "FY 2026-27 compliance calendar in one place.",
    "cta_b": "Monthly + quarterly + half-yearly + annual deadlines. BQP annual engagement includes complete compliance tracking + reminders. One-firm point of accountability.",
    "keywords": "India tax compliance calendar FY 2026-27, India compliance deadlines 2026, ITR GST ROC FEMA calendar India, India CA annual compliance",
    "desc": "India tax + ROC + FEMA + GST compliance calendar FY 2026-27 complete: every form + every deadline + every month. Monthly (GST, TDS), quarterly (advance tax, TDS returns), half-yearly (PAS-6, MSME-1, DIR-3 KYC), annual (ITR, AOC-4, MGT-7, Form 3CEB, GSTR-9, FLA, APR, DPT-3). Working CA calendar by Durgesh Chavda.",
})

# 8. How to engage Indian CA remotely from USA/UK
PAGES.append({
    "slug": "how-to-engage-indian-ca-remotely-from-usa-uk-step-by-step",
    "title": "How to Engage Indian CA Remotely from USA / UK Step-by-Step",
    "hero_em": "complete remote engagement guide.",
    "lead": "Foreign company (US / UK / EU / Singapore / UAE / Australia / Canada) engaging an Indian Chartered Accountant for India services - how to do it remotely, efficiently, without a visit to India. Step-by-step from first email to final deliverable. Here's the complete practitioner's step-by-step.",
    "kicker": "/ Remote Engagement Guide &middot; Updated 2026-10-22",
    "sections_pairs": [
        ("/ Step 1: Define what you need", "Clarity first.",
         "<p>Foreign company engaging Indian CA typically needs one or more of:</p>"
         "<ul>"
         "<li>India entity setup (WOS / Branch / Liaison) or operational compliance for existing Indian subsidiary.</li>"
         "<li>Due diligence on Indian target company (M&A / investment).</li>"
         "<li>Form 15CA/15CB CA certificate for foreign remittance.</li>"
         "<li>OIDAR GST registration + monthly compliance.</li>"
         "<li>Transfer pricing (Form 3CEB) + benchmarking study.</li>"
         "<li>Annual audit coordination (statutory + tax + TP).</li>"
         "<li>Section 195 TDS advisory + opinion letter.</li>"
         "<li>Profit repatriation (dividend / royalty / FTS / buyback).</li>"
         "<li>India market entry / research / supplier verification.</li>"
         "<li>FEMA compounding of past breaches.</li>"
         "<li>India IP registration (trademark / patent).</li>"
         "<li>EOR India or own-subsidiary hiring setup.</li>"
         "</ul>"
         "<p>Define needs in a one-paragraph email - BQP can advise on specific scope.</p>"),
        ("/ Step 2: First outreach", "Email + 48-hour quote.",
         "<ol>"
         "<li>Email info@bharatquantumprospera.com with:</li>"
         "<li>&nbsp;&nbsp;&mdash; Your company name + country + brief context.</li>"
         "<li>&nbsp;&nbsp;&mdash; What you need (one paragraph).</li>"
         "<li>&nbsp;&nbsp;&mdash; Timeline urgency.</li>"
         "<li>Response within 24 business hours.</li>"
         "<li>30-min Zoom scoping call scheduled at your preferred time zone.</li>"
         "<li>Scoped quote within 48 hours of scoping call: fixed scope + fixed fee + timeline + deliverables.</li>"
         "<li>No obligation at this stage.</li>"
         "</ol>"),
        ("/ Step 3: Scoping call", "30 minutes.",
         "<p>What to discuss on the scoping call:</p>"
         "<ul>"
         "<li>Specific business situation + context.</li>"
         "<li>Specific deliverables you need.</li>"
         "<li>Timeline + specific deadlines.</li>"
         "<li>Format preferences (PDF / Word / Excel / Google Workspace / Microsoft 365).</li>"
         "<li>Communication preferences (email / WhatsApp / weekly call cadence).</li>"
         "<li>Specific regulatory / compliance context (prior audits, pending notices, ongoing transactions).</li>"
         "<li>Co-ordination with your foreign counsel / Big-4 global auditor / US CPA (if applicable).</li>"
         "</ul>"
         "<p>BQP partner CA Durgesh Chavda personally conducts scoping calls - not junior staff.</p>"),
        ("/ Step 4: Engagement letter + onboarding", "Signed remotely.",
         "<ol>"
         "<li>Receive scoped quote email with engagement letter attached (PDF).</li>"
         "<li>Review scope + fee + timeline + deliverables.</li>"
         "<li>Sign electronically (DocuSign / HelloSign / Adobe Sign) + email back.</li>"
         "<li>BQP counter-signs + returns.</li>"
         "<li>Shared workspace setup (Google Drive / Dropbox / Microsoft 365 / Box - your preference).</li>"
         "<li>Document request list issued (what we need from you).</li>"
         "<li>Delivery begins.</li>"
         "</ol>"),
        ("/ Step 5: Delivery cadence", "Weekly status + ad-hoc.",
         "<ul>"
         "<li>Weekly 30-min status call (Zoom at your time zone).</li>"
         "<li>Deliverables shared via workspace in your preferred format.</li>"
         "<li>Email / WhatsApp for ad-hoc questions.</li>"
         "<li>Partner-level access: no junior-staff gatekeeping.</li>"
         "<li>Co-ordination with your foreign counsel if cross-border matter.</li>"
         "<li>Co-ordination with your US CPA / UK accountant if dual-tax matter.</li>"
         "<li>Co-ordination with Big-4 group auditor if parent uses Big-4.</li>"
         "</ul>"),
        ("/ Step 6: Final deliverable + post-engagement", "Closure + continuity.",
         "<ul>"
         "<li>Final deliverables shared + signed off.</li>"
         "<li>30-day Q&amp;A window on deliverables.</li>"
         "<li>Ongoing retainer available if continuing need (annual compliance, quarterly MIS, periodic Form 15CB).</li>"
         "<li>Preservation of workpapers for 8+ years.</li>"
         "<li>Reference for future scope.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-22.</em></p>"),
    ],
    "faqs": [
        ("Do I need to visit India to engage an Indian CA?",
         "No - 100% remote engagement is standard at BQP. All services (incorporation, audit, DD, 15CB, GST, TP, FEMA, repatriation) delivered via Zoom + cloud workspace + electronic signing. Foreign clients never visit India for engagement."),
        ("How long does the initial engagement setup take?",
         "First email to signed engagement letter: depends on how quickly scope and documents are agreed. Email → scoping call scheduled → 30-min Zoom → scoped quote within 48 hours → review + e-sign engagement letter → workspace setup → delivery begins. Urgent matters (Form 15CB): same-day engagement possible via WhatsApp +91 78018 87130."),
        ("What's BQP's typical fee structure?",
         "Scoped engagement letter with fixed scope + fixed fee (or clearly-defined retainer for ongoing work). No hourly billing surprises. Fee set at scoping call stage based on actual work involved + timeline + deliverables. Transparent + no hidden costs."),
        ("Does BQP coordinate with my US CPA / UK accountant / global advisor?",
         "Yes - standard. BQP handles India-side (Indian ITR + FEMA + TP + audit) + co-ordinates with your foreign counterpart. Shared workspace + weekly cross-firm status call + document version control + aligned deliverables."),
        ("What if I need urgent India work (Form 15CB in 24 hours)?",
         "WhatsApp +91 78018 87130 for same-day urgent response. Form 15CB CA certificate standard turnaround 24-48 hours. Section 148A show-cause response, FEMA deadline, assessment representation - urgent engagement model standard. CA Durgesh Chavda personally handles urgent matters."),
        ("What's BQP's track record with foreign clients?",
         "Works remotely with clients in the US, UK, EU, Singapore, UAE, Australia, Canada, Japan, Mauritius and Hong Kong. 300+ working guides at bharatquantumprospera.com demonstrate practitioner depth."),
    ],
    "related_pairs": [("for-foreign-clients.html", "Related", "For Foreign Clients Hub"),
                      ("how-to-pick-indian-ca-firm-for-foreign-company-complete.html", "Related", "How to Pick Indian CA")],
    "cta_h": "US / UK / EU / Singapore / UAE company needing Indian CA?",
    "cta_b": "Email + 30-min Zoom + 48-hour quote + e-sign + delivery. Full remote engagement model.",
    "keywords": "how to engage Indian CA from USA UK, remote Indian CA engagement foreign company, Indian CA for US company remote, hire Indian CA from abroad",
    "desc": "How to engage Indian CA remotely from USA / UK / EU / Singapore / UAE step-by-step: define need, email outreach, 48-hour quote, 30-min scoping call, e-sign engagement letter, workspace setup, weekly delivery cadence, final sign-off. Engagements run fully remotely. CA Durgesh Chavda complete guide.",
})

# Build all pages
for p in PAGES:
    html = quick_page(
        slug=p["slug"], title=p["title"], hero_em=p["hero_em"], lead=p["lead"],
        kicker=p["kicker"], sections_pairs=p["sections_pairs"],
        faqs=p["faqs"], related_pairs=p["related_pairs"],
        cta_h=p["cta_h"], cta_b=p["cta_b"],
        keywords=p["keywords"], desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch W complete: {len(PAGES)} pages")
