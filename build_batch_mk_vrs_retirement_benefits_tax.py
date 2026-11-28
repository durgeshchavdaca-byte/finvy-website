# -*- coding: utf-8 -*-
"""Batch MK (29 Nov 2026): Tax on VRS compensation and retirement benefits in India - VRS exemption up to INR 5 lakh,
commuted and uncommuted pension, gratuity, leave encashment, and the salary deductions that matter in the exit year (standard
deduction, employer NPS under 80CCD(2), relief under section 89).
Demand: sweep ac272 (29 Nov 2026), all 7 markets: 'vrs amount taxable' (coverage 0.33), 'vrs taxability', 'vrs taxation'
(0.50), 'gratuity tax exemption for private sector employees' (0.33), 'standard deduction 75000 applicable from which year'
(0.33), 'employer nps 80ccd(2)' (0.50). No VRS page on the site; gratuity and leave encashment pages exist. Employees taking
VRS or retiring need computation and regime advice. User steer 26 Nov 2026: more call bookings.
Facts (Income-tax Act, 1961 sections 10(10), 10(10A), 10(10AA), 10(10C), 16, 80CCD(2), 89 and rule 2BA; matched to the site's
gratuity, leave encashment and regime pages): VRS compensation under a scheme meeting rule 2BA is exempt up to INR 5 lakh,
once in a lifetime, and if the exemption is claimed, relief under section 89 is not available for the same compensation;
commuted pension fully exempt for government employees, for others one-third of the full commuted value is exempt if gratuity is
also received and one-half if not; uncommuted (monthly) pension is taxable as salary; gratuity for non-government employees exempt
up to INR 20 lakh (site gratuity page); leave encashment on retirement or resignation exempt up to INR 25 lakh for non-government
employees (site leave encashment page); these retirement exemptions are also available under the new regime (matched to the
site's leave encashment page); standard deduction INR 75,000 under the new regime from FY 2024-25 and INR 50,000 under the old
regime; employer NPS contribution deductible under 80CCD(2) up to 14% of salary under the new regime from FY 2024-25 (10% for
non-government employees under the old regime); section 89 relief (Form 10E) for arrears or advance salary. The same rules
continue in the Income-tax Act, 2025 under new section numbers. No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "vrs-compensation-tax-india-5-lakh-exemption-section-10-10c-commuted-pension-gratuity-retirement-benefits-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your relieving or VRS letter, the full and final "
     "settlement statement, Form 16, whether you are a government or private employee, years of service, and any pension "
     "commutation. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="VRS Compensation Tax in India (2026): The INR 5 Lakh Exemption, Commuted Pension, Gratuity, Leave Encashment and the Deductions That Matter in Your Exit Year",
    em="plan the exit year before the money lands.",
    kicker="/ Employees taking VRS, retiring or leaving with a large final settlement &middot; Retirement benefits tax &middot; Updated 2026-11-29",
    lead=("<strong>Compensation under a voluntary retirement scheme (VRS) is tax-free up to INR 5 lakh, once in a lifetime, if the scheme meets the prescribed conditions; the rest is taxed as salary. "
          "Gratuity, leave encashment and commuted pension have their own exemptions, which are also available under the new regime. "
          "Because the whole settlement lands in one year, the choice between the VRS exemption and section 89 relief, and between regimes, can change the tax noticeably.</strong>"),
    sections=[
        ("/ How each exit payment is taxed", "Retirement and VRS exemptions.",
         table(["Payment", "Tax treatment"], [
             ["VRS compensation (scheme meeting rule 2BA)", "Exempt up to INR 5 lakh, once in a lifetime; balance taxed as salary"],
             ["Gratuity", "Government employees fully exempt; others exempt up to INR 20 lakh under the prescribed formula"],
             ["Leave encashment on retirement or resignation", "Government employees fully exempt; others exempt up to INR 25 lakh"],
             ["Commuted pension", "Government employees fully exempt; others one-third exempt if gratuity is also received, one-half if not"],
             ["Monthly (uncommuted) pension", "Taxable as salary"],
             ["Arrears or advance salary", "Relief under section 89 via Form 10E - but not on VRS compensation if the 5 lakh exemption is claimed"]])
         + ul("<strong>New regime:</strong> the gratuity, leave encashment, commuted pension and VRS exemptions remain available.",
              "<strong>New Act:</strong> the same exemptions continue in the Income-tax Act, 2025 from tax year 2026-27, under new section numbers.")),
        ("/ Deductions and planning in the exit year", "Get the year right.",
         ul("<strong>Standard deduction:</strong> INR 75,000 under the new regime from FY 2024-25; INR 50,000 under the old regime.",
            "<strong>Employer NPS (80CCD(2)):</strong> employer contribution deductible up to 14% of salary under the new regime from FY 2024-25; 10% for non-government employees under the old regime.",
            "<strong>VRS exemption or section 89:</strong> compare both - spreading the compensation back over earlier years can sometimes save more than the 5 lakh exemption.",
            "<strong>Regime choice:</strong> recheck the old vs new regime for the exit year; a large settlement can change the answer.",
            "<strong>Check Form 16:</strong> employers sometimes miss exemptions on the final settlement - you can claim them in your return.")
         + call_box("VRS and retirement benefits", ["Exit-year tax computation",
                                                    "VRS exemption vs section 89 relief",
                                                    "Gratuity, leave encashment and pension commutation",
                                                    "Old vs new regime for the exit year",
                                                    "Correcting Form 16 in the return"],
                    "VRS or relieving letter, full and final statement, Form 16, employer type, service years, commutation.")
         + sources("Income-tax Act, 1961 (sections 10(10), 10(10A), 10(10AA), 10(10C), 16, 80CCD(2) and 89) and Income-tax Rules (rule 2BA) and the corresponding provisions of the Income-tax Act, 2025; site gratuity calculator, leave encashment and new vs old regime pages.")),
    ],
    faqs=[("Is VRS compensation taxable in India?", "Up to INR 5 lakh is exempt, once in a lifetime, if the scheme meets the prescribed conditions (rule 2BA). Any amount above INR 5 lakh is taxed as salary in the year received."),
          ("Can I claim section 89 relief on VRS compensation?", "Only if you do not claim the INR 5 lakh VRS exemption for the same compensation. Compare both: spreading the compensation back over earlier years under section 89 can sometimes give more relief."),
          ("How much gratuity is tax-free for private sector employees?", "Up to INR 20 lakh, worked out under the prescribed formula. Gratuity received by government employees is fully exempt."),
          ("Is commuted pension taxable?", "For government employees it is fully exempt. For others, one-third of the full commuted value is exempt if gratuity is also received, and one-half if it is not. Monthly pension is taxable as salary."),
          ("From which year does the INR 75,000 standard deduction apply?", "From FY 2024-25 (AY 2025-26) under the new tax regime. The old regime continues with INR 50,000."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the VRS or relieving letter, full and final statement, Form 16, employer type, years of service and any commutation. Or book a call directly.")],
    related=[("gratuity-calculator-new-labour-codes-2026.html", "Gratuity calculator and tax-free limit"),
             ("leave-encashment-tax-exemption-section-10-10aa-25-lakh-new-regime-retirement-resignation-2026.html", "Leave encashment tax"),
             ("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "New vs old tax regime"),
             ("new-vs-old-tax-regime-calculator.html", "Income tax calculator")],
    cta_h="Taking VRS or retiring this year?", cta_b=C,
    keywords="vrs compensation tax, vrs amount taxable, vrs taxability, section 10(10c), vrs 5 lakh exemption, commuted pension tax, gratuity tax exemption private sector, standard deduction 75000 from which year, employer nps 80ccd(2), section 89 vrs",
    desc="VRS compensation tax in India: exempt up to INR 5 lakh once under section 10(10C), VRS exemption vs section 89, gratuity up to INR 20 lakh, leave encashment up to INR 25 lakh, commuted pension, INR 75,000 standard deduction and employer NPS under 80CCD(2).",
    howto={"name": "How to plan tax on a VRS or retirement settlement", "description": "List, exempt, compare, file.", "steps": [
        {"name": "List each payment", "text": "VRS compensation, gratuity, leave encashment, pension, arrears."},
        {"name": "Apply the exemptions", "text": "5 lakh VRS, gratuity and leave encashment limits, commuted pension share."},
        {"name": "Compare options", "text": "VRS exemption vs section 89; old vs new regime for the exit year."},
        {"name": "File correctly", "text": "Claim missed exemptions in the return and file Form 10E if using section 89."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MK complete")
