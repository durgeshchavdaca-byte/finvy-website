# -*- coding: utf-8 -*-
"""Batch CI (14 Nov 2026): second autocomplete sweep (45 new seeds x 7 markets): three clusters seen in all seven
markets with no proper page: NRI EPF withdrawal, permanent establishment in India, US citizens buying property in India.
Facts:
- EPF: final settlement allowed on settling or taking employment abroad (Form 19; Form 10C for pension withdrawal
  benefit where service is under 10 years, otherwise a scheme certificate); claim online on the EPFO member portal with
  UAN and KYC, or offline; paid to an Indian bank account in the member's name. Withdrawal after 5 years of continuous
  service (including transferred previous service) is tax-free; earlier withdrawal is taxable (employer share and interest
  as salary, own contributions to the extent deducted, interest as other income) and EPFO deducts TDS; Form 15G/15H is
  only for residents, so NRIs use a lower deduction certificate (Form 128) or claim a refund. Interest on employee
  contributions above INR 2.5 lakh a year is taxable (from 1 April 2021).
- PE: fixed place, service, construction and dependent-agent PE under treaties; Supreme Court: Morgan Stanley (2007),
  Formula One World Championship (2017), E-Funds (2017); profits attributable taxed at 35% plus surcharge and cess for a
  foreign company; MLI widened agency PE.
- US citizens and property: OCI cardholders (including US citizens of Indian origin) can buy residential and commercial
  property but not agricultural land, farmhouses or plantations; a foreign national of non-Indian origin resident in India
  can acquire property (prior RBI approval for citizens of Pakistan, Bangladesh, Sri Lanka, Afghanistan, China, Iran,
  Nepal, Bhutan, Macau, Hong Kong, DPRK); other foreign nationals need RBI permission except inheritance; US persons report
  Indian accounts and property income (FBAR, Form 8938, Schedule E) with foreign tax credit.
Sources: RBI FAQ on immovable property; NDI Rules 2019; nriinformation, finright, scopex (EPF); Supreme Court judgments;
checked 14 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."
DATE = "2026-11-14"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, body, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">{body} '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')


def src(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not advice for your situation.</p>'


C_EPF = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your years of service, the date you left India and your current country. "
         "We reply the same working day with the tax on withdrawal and the steps.")
C_PE = ("Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130 with what your people or agents do in India, for how long, and your country of residence. "
        "We reply within one working day with a PE risk view and a fixed-scope quote.")
C_USP = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your citizenship, OCI status, where you live and the property you want to buy, hold or sell. "
         "We reply the same working day with the FEMA and tax position in India and what to report in the US.")

EPF = dict(
    slug="nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026",
    title="EPF/PF Withdrawal for NRIs (2026): Can You Withdraw After Moving Abroad, the Online Process, Tax and Why Form 15G Does Not Apply",
    em="yes, in full, once you settle abroad.",
    kicker=f"/ NRI &middot; EPF &middot; Provident fund &middot; Updated {DATE}",
    lead=("An employee who leaves India to <strong>settle or take up employment abroad can withdraw the full EPF balance</strong> using <strong>Form 19</strong> (and <strong>Form 10C</strong> for the pension portion if service is under 10 years), online on the EPFO member portal with your UAN or through your last employer. "
          "The withdrawal is <strong>tax-free after 5 years of continuous service</strong> (counting previous employers' service transferred to the same account); before that it is taxable and EPFO deducts TDS. "
          "<strong>NRIs cannot use Form 15G</strong>, which is only for residents; to avoid excess TDS, apply for a lower deduction certificate (Form 128) or claim a refund in your Indian return."),
    sections=[
        ("/ Can you withdraw, and how much", "By situation.",
         table(["Situation", "Position"], [
             ["Moved abroad to settle or for a job abroad", "Full PF withdrawal allowed (exit reason: settlement abroad); pension withdrawal benefit via Form 10C if service is under 10 years, otherwise a scheme certificate"],
             ["Still in India, left employment", "Full withdrawal after two months without employment; partial withdrawals for specified purposes"],
             ["Do nothing", "The account can stay; interest is credited under EPFO rules, but interest credited after you stop working is generally taxable each year"]])),
        ("/ Tax on withdrawal", "Five years is the line.",
         table(["Service", "Tax"], [
             ["5 years or more of continuous service", "Withdrawal is tax-free"],
             ["Under 5 years", "Employer contributions and interest taxed as salary; your own contributions taxed to the extent you claimed a deduction; interest on your contributions as other income; EPFO deducts TDS"],
             ["Contributions above INR 2.5 lakh a year (from 1 April 2021)", "Interest on the excess employee contribution is taxable"]])
         + box("TDS on your PF and no Form 15G option?", "As an NRI, a lower deduction certificate before you file the claim, or a return to claim the refund afterwards, recovers excess TDS; treaty relief may also apply.",
               "Hi Durgesh, I am an NRI and want to withdraw my EPF. Can you tell me the tax and help with TDS?")),
        ("/ The online process", "From abroad.",
         ul("Activate your UAN on the EPFO member portal; complete KYC (bank account in India in your name, PAN, and Aadhaar where required).",
            "Make sure your exit date is updated by the last employer.",
            "File the claim online (Form 19 for PF, Form 10C for pension) and choose the exit reason for settlement abroad; or submit physical forms through the employer.",
            "The money is paid to your Indian bank account; for NRIs this is usually an NRO account, from which it can be repatriated with Forms 145/146.",
            "Report the withdrawal and TDS in your Indian return if taxable, and in your country of residence as its rules require.")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR tax rules</a> &middot; <a href="nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html">lower TDS certificate (Form 128)</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating money from India</a>.</p>'
         + src("Employees' Provident Funds Scheme, 1952 (final settlement, Form 19); Employees' Pension Scheme, 1995 (Form 10C); Income-tax Act exemption for withdrawal after five years of continuous service and TDS on premature withdrawal (carried into the Income-tax Act, 2025); Finance Act, 2021 (INR 2.5 lakh limit). Secondary summaries checked 14 November 2026: nriinformation, finright, scopex.")),
    ],
    faqs=[("Can an NRI withdraw EPF after moving abroad?", "Yes. Employees who settle or take up employment abroad can withdraw the full PF balance with Form 19, and the pension portion with Form 10C if service is under 10 years."),
          ("Can I withdraw EPF online from abroad?", "Yes, through the EPFO member portal with an active UAN and completed KYC, choosing settlement abroad as the reason. Payment goes to your Indian bank account."),
          ("Is EPF withdrawal taxable for NRIs?", "Not after 5 years of continuous service. Before that, the withdrawal is taxable and EPFO deducts TDS."),
          ("Can an NRI submit Form 15G for PF withdrawal?", "No. Forms 15G and 15H are only for residents. NRIs can apply for a lower deduction certificate (Form 128) or claim a refund in their return."),
          ("Does EPF keep earning interest after I leave India?", "Interest continues to be credited under EPFO rules, but interest credited after you stop working is generally taxable in the year it is credited."),
          ("Can BQP help?", "Yes. " + C_EPF)],
    related=[("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower TDS certificate"), ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India")],
    cta_h="PF stuck in India after you moved abroad?", cta_b=C_EPF,
    keywords="NRI EPF withdrawal, NRI PF withdrawal process, EPF withdrawal online for NRI, EPF withdrawal NRI tax, NRI PF withdrawal Form 15G, Form 19 settlement abroad, EPF withdrawal after moving abroad, PF TDS NRI",
    desc="EPF/PF withdrawal for NRIs in 2026: full withdrawal on settling abroad (Form 19, Form 10C), online process on the EPFO portal, tax-free after 5 years of continuous service, TDS otherwise, why Form 15G does not apply to NRIs, and repatriation.",
    howto={"name": "How an NRI withdraws EPF from abroad", "description": "Steps for employees who have moved abroad.", "steps": [
        {"name": "Activate UAN and complete KYC", "text": "Bank account in India in your name, PAN and Aadhaar where required."},
        {"name": "Check the exit date", "text": "Ensure the last employer has updated your date of leaving."},
        {"name": "File Form 19 and Form 10C", "text": "Claim online with settlement abroad as the reason, or through the employer."},
        {"name": "Handle tax and repatriation", "text": "Claim any TDS refund in your return and repatriate from your NRO account with Forms 145/146."}]})

PE = dict(
    slug="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026",
    title="Permanent Establishment (PE) in India (2026): Meaning, the Four Types, How Foreign Companies Trigger It and What It Costs",
    em="where a foreign company becomes taxable in India.",
    kicker=f"/ Foreign companies &middot; International tax &middot; PE &middot; Updated {DATE}",
    lead=("A <strong>permanent establishment (PE)</strong> is the taxable presence a foreign company creates in India under a tax treaty. Once there is a PE, India taxes the <strong>profits attributable to it</strong> at the foreign company rate of <strong>35% plus surcharge and cess</strong>, and the company must file Indian returns and keep transfer pricing documentation. "
          "Treaties recognise four main types: a <strong>fixed place</strong> (office, branch, site at the company's disposal), a <strong>service PE</strong> (staff providing services in India beyond a time threshold), a <strong>construction or installation PE</strong>, and a <strong>dependent agent PE</strong> (someone in India habitually concluding contracts or playing the principal role in them). "
          "Without a treaty, India's broader domestic 'business connection' test applies, including significant economic presence."),
    sections=[
        ("/ The four types of PE", "And what usually triggers them.",
         table(["Type", "Typical trigger", "Leading case"], [
             ["Fixed place PE", "Premises in India at the foreign company's disposal through which its business is carried on, even without a formal office", "Formula One World Championship (Supreme Court, 2017)"],
             ["Service PE", "Employees or personnel furnishing services in India beyond the treaty's day threshold within 12 months", "Morgan Stanley (Supreme Court, 2007)"],
             ["Construction or installation PE", "A building site or installation project lasting longer than the treaty period", "Treaty-specific thresholds"],
             ["Dependent agent PE", "A person in India habitually concluding contracts, or playing the principal role leading to them, for the foreign company", "Widened by the MLI where India's treaty partner adopted it"]])
         + "<p>Back-office support that is merely preparatory or auxiliary generally does not create a PE; the Supreme Court in E-Funds (2017) found no PE where the Indian subsidiary performed back-office services for its US parent.</p>"),
        ("/ How foreign companies trigger PE by accident", "Common situations.",
         ul("Senior staff of the foreign company working from India for long periods, or remote employees who negotiate and close deals; see <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">PE risk from remote employees</a>.",
            "Seconded employees whose work is controlled by the foreign parent rather than the Indian company.",
            "Indian distributors or sales agents who effectively sign contracts for the foreign company.",
            "Project teams on site in India beyond the treaty period.",
            "Using an Indian subsidiary's premises as the parent's own office.")
         + box("Planning people or projects in India?", "A short PE review before people travel or contracts are signed usually costs far less than defending an assessment later.",
               "Hi Durgesh, our foreign company has staff and agents working in India. Can you review our permanent establishment risk?")),
        ("/ If a PE exists", "What it costs and how to manage it.",
         table(["Consequence", "Detail"], [
             ["Tax on attributable profit", "35% plus surcharge and cess on profits attributable to the PE"],
             ["Compliance", "PAN, Indian tax return, possible transfer pricing report; withholding on payments to the foreign company"],
             ["Attribution", "If the Indian affiliate is paid at arm's length for its functions, further profit attribution is limited (Morgan Stanley)"],
             ["Treaty claim", "Treaty benefits need a tax residency certificate and Form 10F (Form 41)"],
             ["Alternatives", "Subsidiary, employer of record or genuine independent contractors, chosen with the PE test in mind"]])
         + '<p>Related: <a href="significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html">significant economic presence</a> &middot; <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">branch vs liaison vs subsidiary</a> &middot; <a href="transfer-pricing.html">transfer pricing</a>.</p>'
         + src("India's tax treaties (Article 5) and the Multilateral Instrument; Income-tax Act, 2025 (business connection and significant economic presence); DIT v Morgan Stanley (Supreme Court, 2007); Formula One World Championship v CIT (Supreme Court, 2017); ADIT v E-Funds IT Solution (Supreme Court, 2017). Facts checked 14 November 2026.")),
    ],
    faqs=[("What is a permanent establishment in India?", "The taxable presence a foreign company creates in India under a tax treaty, for example an office, staff providing services beyond a time threshold, a long construction project, or a dependent agent concluding contracts."),
          ("What tax applies if a foreign company has a PE in India?", "Profits attributable to the PE are taxed at 35% plus surcharge and cess, and the company must file Indian returns."),
          ("Can remote employees in India create a PE?", "Yes, especially if they negotiate or conclude contracts, work from a fixed place for long periods, or provide services beyond the treaty threshold."),
          ("Does an Indian subsidiary create a PE for its parent?", "Not by itself. A subsidiary is a separate taxpayer; a PE can arise if the parent uses the subsidiary's premises or staff as its own, but back-office services alone did not create a PE in E-Funds (2017)."),
          ("What is a service PE?", "Under many Indian treaties, a PE arising when a foreign company's employees or personnel furnish services in India beyond a specified number of days within a 12-month period."),
          ("Can BQP review our PE risk?", "Yes. " + C_PE)],
    related=[("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "PE risk from remote employees"), ("significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html", "Significant economic presence"),
             ("branch-office-vs-liaison-vs-wos-india-foreign.html", "Branch vs liaison vs subsidiary")],
    cta_h="Worried about a PE in India?", cta_b=C_PE,
    keywords="permanent establishment India, permanent establishment India tax, PE risk India, service PE India, dependent agent PE India, fixed place PE India, permanent establishment meaning India, Morgan Stanley PE, Formula One PE case, foreign company taxable presence India",
    desc="Permanent establishment in India in 2026: meaning, fixed place, service, construction and dependent agent PE, Supreme Court cases (Morgan Stanley, Formula One, E-Funds), accidental triggers, 35% tax on attributable profit and how to manage it.",
    howto={"name": "How a foreign company checks PE risk in India", "description": "Steps before people, agents or projects start in India.", "steps": [
        {"name": "Map India activity", "text": "List people, premises, agents and projects in India and how long each lasts."},
        {"name": "Test each PE type", "text": "Fixed place, service days, construction period and contract-concluding authority under the relevant treaty."},
        {"name": "Fix the structure", "text": "Use a subsidiary, employer of record or independent contractors, and arm's length pricing."},
        {"name": "Document", "text": "Keep contracts, travel logs and transfer pricing support; obtain TRC and Form 41 for treaty claims."}]})

USP = dict(
    slug="us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026",
    title="Can a US Citizen Buy or Own Property in India? (2026): OCI Route, Foreign Nationals Living in India, Inheritance, Tax in India and What to Report in the US",
    em="with an OCI card, yes; without one, usually not.",
    kicker=f"/ US citizens &middot; OCI &middot; Property &middot; FEMA &middot; Updated {DATE}",
    lead=("A US citizen with an <strong>OCI card</strong> (or otherwise of Indian origin) can <strong>buy residential and commercial property in India</strong>, like an NRI, but <strong>not agricultural land, farmhouses or plantations</strong>. "
          "A US citizen who is <strong>not of Indian origin</strong> can buy only if <strong>resident in India</strong> under FEMA (for example, living and working in India), and otherwise only through <strong>inheritance</strong> or with RBI permission. "
          "Rent and gains from Indian property are taxed in India, and the US also taxes them as worldwide income with a <strong>foreign tax credit</strong>; Indian accounts and assets may need <strong>FBAR</strong> and <strong>Form 8938</strong> reporting."),
    sections=[
        ("/ Who can buy what", "By status.",
         table(["You are", "Can buy in India?"], [
             ["US citizen with OCI card (or of Indian origin)", "Yes: residential and commercial property, any number; not agricultural land, farmhouse or plantation"],
             ["US citizen not of Indian origin, living in India (FEMA resident)", "Yes, for property in India (no RBI approval needed for US citizens; citizens of certain neighbouring countries need approval)"],
             ["US citizen not of Indian origin, living abroad", "No purchase without RBI permission; can inherit; leases up to five years are allowed"],
             ["Any of the above inheriting property", "Yes, by inheritance from a person who held it lawfully"]])
         + '<p>Detail for OCIs and agricultural land: <a href="nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html">NRIs and OCIs and agricultural land</a>.</p>'),
        ("/ Tax in India and the US", "Both countries tax it.",
         table(["Income", "India", "United States"], [
             ["Rent", "Taxable; tenant deducts about 31.2% TDS for non-residents", "Report on Schedule E; foreign tax credit for Indian tax"],
             ["Sale", "Long-term gains 12.5% for non-residents; buyer deducts TDS unless a lower deduction certificate", "Capital gain on the 1040; foreign tax credit; currency gain or loss can matter"],
             ["Accounts and assets", "NRO account for rent and sale proceeds", "FBAR if foreign accounts exceed USD 10,000 in aggregate; Form 8938 above its thresholds"]])
         + box("US citizen with property in India?", "We handle the Indian side (TDS, lower deduction certificate, return, repatriation up to USD 1 million a year) and coordinate the numbers your US preparer needs.",
               "Hi Durgesh, I am a US citizen with property in India. Can you help with the Indian tax and repatriation?")
         + '<p>Related: <a href="ca-for-nri-us-citizen-dual-tax-india-us-coordinated.html">US citizens with Indian income</a> &middot; <a href="india-us-tax-treaty-dtaa.html">India-US tax treaty</a> &middot; <a href="nri-us-estate-tax-indian-assets.html">US estate tax and Indian assets</a> &middot; <a href="nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html">NRI rental income</a>.</p>'
         + src("Foreign Exchange Management (Non-debt Instruments) Rules, 2019 and RBI FAQ on acquisition of immovable property by NRIs, OCIs and foreign nationals; Income-tax Act, 2025; US Internal Revenue Code (foreign tax credit), FinCEN FBAR and Form 8938 rules. Facts checked 14 November 2026.")),
    ],
    faqs=[("Can a US citizen buy property in India?", "Yes if they hold an OCI card or are of Indian origin (not agricultural land), or if they are resident in India under FEMA. A US citizen of non-Indian origin living abroad cannot buy without RBI permission but can inherit."),
          ("Can an OCI cardholder buy agricultural land?", "No. OCIs can buy residential and commercial property but not agricultural land, farmhouses or plantation property; they can inherit them."),
          ("Does a US citizen pay tax in India on Indian rent?", "Yes. Rent from Indian property is taxable in India, and the tenant deducts TDS for non-residents. The US also taxes it, with a foreign tax credit."),
          ("Do I report Indian property to the IRS?", "Property itself is not reported on FBAR, but Indian bank accounts holding rent or sale proceeds are, if foreign accounts exceed USD 10,000 in aggregate; income goes on the US return, and Form 8938 may apply."),
          ("Can BQP handle the Indian side?", "Yes. " + C_USP)],
    related=[("ca-for-nri-us-citizen-dual-tax-india-us-coordinated.html", "US citizens with Indian income"), ("india-us-tax-treaty-dtaa.html", "India-US tax treaty"),
             ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "OCIs and agricultural land")],
    cta_h="US citizen buying, holding or selling in India?", cta_b=C_USP,
    keywords="can US citizen buy property in India, US citizen owning property in India, OCI buy property India, US citizen holding property in India, foreign national buy property India FEMA, US citizen Indian property tax FBAR, OCI agricultural land",
    desc="Can a US citizen buy property in India in 2026? With an OCI card or Indian origin, yes (not agricultural land); foreign nationals only if resident in India or by inheritance; Indian tax on rent and sale, and US reporting (Schedule E, foreign tax credit, FBAR, Form 8938).",
    howto={"name": "How a US citizen buys and holds property in India", "description": "Steps for US citizens.", "steps": [
        {"name": "Confirm eligibility", "text": "OCI or Indian origin, or FEMA residence in India; no agricultural land."},
        {"name": "Pay through proper channels", "text": "Inward remittance or NRE/NRO/FCNR funds; keep purchase records for later repatriation."},
        {"name": "Handle Indian tax", "text": "TDS on rent or sale, lower deduction certificate where useful, Indian return."},
        {"name": "Report in the US", "text": "Rent on Schedule E, gains on the 1040 with foreign tax credit, FBAR and Form 8938 where thresholds are met."}]})

for p in [EPF, PE, USP]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CI complete")
