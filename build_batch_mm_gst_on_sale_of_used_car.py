# -*- coding: utf-8 -*-
"""Batch MM (29 Nov 2026): GST on sale of a used / old car by a company or registered business - the margin scheme for old and
used vehicles, how the margin is worked out (depreciation-claimed sellers vs others), the 18% rate on the margin, when the
margin scheme is not available (input tax credit taken), sales to employees, and private individuals.
Demand: sweep ac275 (29 Nov 2026), all 7 markets: 'gst on sale of used car by company' (coverage 0.40), '... by registered
person', '... by partnership firm', '... by company to employee' (0.33), '... notification' (0.40), '... by company to
individual' (0.50). No page on the site. Companies and firms disposing of business cars need correct invoicing.
Facts (verified by web search 29 Nov 2026 - Lookuptax notification tracker, ClearTax, IndiaFilings, Razorpay, Business Standard
and Upstox explainers): Notification 8/2018-Central Tax (Rate) gives a concessional, margin-based levy on old and used vehicles;
Notification 04/2025-Central Tax (Rate), dated 16 January 2025 on the 55th GST Council's recommendation, brought all old and used
vehicles under it to 18% on the margin (including smaller cars and EVs previously at a lower rate); the September 2025 rate
rationalisation (56th GST Council, effective 22 September 2025) did not change the used-vehicle position; where the seller has
claimed depreciation under section 32 of the Income-tax Act, the margin is the consideration less the depreciated value on the
date of supply; otherwise the margin is the selling price less the purchase price (rule 32(5)); a negative margin is ignored; the
concession is not available where input tax credit was availed on the vehicle; a private individual selling a personal car is not
liable to GST. No new-car rates, no compensation cess figures, no fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "gst-on-sale-of-used-car-by-company-registered-person-margin-scheme-18-percent-depreciated-value-notification-8-2018-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the car's purchase invoice, whether input tax "
     "credit was taken, the depreciation schedule, the sale price and buyer (dealer, employee or outsider), and your GST "
     "registration details. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST on Sale of a Used Car by a Company or Registered Business (2026): Margin Scheme at 18%, Depreciated Value, Sale to Employees and When Full GST Applies",
    em="tax the margin, not the price - if you qualify.",
    kicker="/ Companies, LLPs, firms and proprietors selling business cars &middot; GST on old and used vehicles &middot; Updated 2026-11-29",
    lead=("<strong>A registered business selling a used car usually pays GST only on its margin, at 18%, under the concessional scheme for old and used vehicles. "
          "If depreciation was claimed, the margin is the sale price less the depreciated value; if the result is negative, no GST is payable. "
          "The concession is not available if input tax credit was taken on the car, and a private individual selling a personal car pays no GST.</strong>"),
    sections=[
        ("/ How GST works on a used car sale", "Notification 8/2018-Central Tax (Rate), as amended.",
         table(["Point", "Position"], [
             ["Rate on the margin", "18% for all old and used vehicles under the scheme (from 16 January 2025, Notification 04/2025-Central Tax (Rate)); unchanged by the September 2025 rate rationalisation"],
             ["Seller claimed depreciation", "Margin = sale price less depreciated value on the date of sale"],
             ["Seller did not claim depreciation", "Margin = sale price less purchase price"],
             ["Negative margin", "Ignored - no GST payable"],
             ["Input tax credit taken on the car", "Margin scheme not available - GST on the full value"],
             ["Private individual selling a personal car", "Not a business supply - no GST"]])
         + ul("<strong>Invoice:</strong> issue a tax invoice showing GST on the margin, and keep the depreciation workings as support.",
              "<strong>Income tax:</strong> the sale also affects the block of assets and depreciation - plan both taxes together.")),
        ("/ Common situations", "Employees, dealers and fleets.",
         ul("<strong>Sale to an employee:</strong> the same margin rules apply; price it at fair value, and check any perquisite if sold below value.",
            "<strong>Sale to a dealer or buyback against a new car:</strong> the sale is a separate supply even when adjusted against the new car's price.",
            "<strong>Cars on which credit was blocked:</strong> most business cars were bought without input tax credit, which is why the margin scheme usually applies - confirm from the purchase records.",
            "<strong>Unregistered sellers:</strong> businesses below the registration threshold do not charge GST, but should still keep records.",
            "<strong>Rules can change:</strong> check the current rate notification before invoicing; GST rates are revised by the GST Council.")
         + call_box("GST on used car sales", ["Margin scheme eligibility",
                                              "Depreciated value and margin working",
                                              "Invoice and return reporting",
                                              "Sales to employees and dealers",
                                              "Income tax block of assets impact"],
                    "Purchase invoice, credit position, depreciation schedule, sale price, buyer, GST details.")
         + sources("Notification 8/2018-Central Tax (Rate) as amended by Notification 04/2025-Central Tax (Rate); CGST Rules, 2017 (rule 32(5)); Income-tax Act, 1961 (section 32); site GST on advances, GST return filing and GST registration pages.")),
    ],
    faqs=[("What is the GST rate on sale of a used car by a company?", "18% on the margin, under the concessional scheme for old and used vehicles (Notification 8/2018-Central Tax (Rate) as amended from 16 January 2025). The September 2025 rate rationalisation did not change this."),
          ("How is the margin calculated if depreciation was claimed?", "The margin is the sale price less the depreciated value of the car on the date of sale. If that is negative, it is ignored and no GST is payable."),
          ("When does GST apply on the full sale value of a used car?", "When input tax credit was taken on the car when it was bought - the margin scheme is then not available."),
          ("Is GST payable when a company sells a car to an employee?", "Yes, the same margin rules apply. Price the sale at fair value and check whether any perquisite arises if the car is sold below value."),
          ("Do individuals pay GST when selling their personal car?", "No. A private individual selling a personal car is not making a business supply, so no GST is payable."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the purchase invoice, credit position, depreciation schedule, sale price, buyer and GST details. Or book a call directly.")],
    related=[("gst-on-advance-received-services-goods-time-of-supply-receipt-voucher-refund-voucher-gstr-1-table-11-2026.html", "GST on advance received"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing"),
             ("gst-for-consultants-professionals-india-registration-threshold-18-percent-export-lut-reimbursement-pure-agent-2026.html", "GST for consultants and professionals"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?")],
    cta_h="Selling a business car?", cta_b=C,
    keywords="gst on sale of used car by company, gst on sale of used car by registered person, gst on sale of old car, gst on sale of used car by company to employee, gst on sale of used car notification, margin scheme used car gst, notification 8/2018 used vehicles, gst on sale of car by partnership firm",
    desc="GST on sale of a used car by a company or registered business: 18% on the margin under Notification 8/2018 as amended (from 16 January 2025), margin = sale price less depreciated value, negative margin ignored, full GST if ITC was taken, sales to employees, private sellers exempt.",
    howto={"name": "How to work out GST on a used car sale", "description": "Check, compute, invoice.", "steps": [
        {"name": "Check credit position", "text": "Was input tax credit taken on the car? If yes, full GST applies."},
        {"name": "Compute the margin", "text": "Sale price less depreciated value (or purchase price)."},
        {"name": "Apply 18%", "text": "Only on a positive margin; nil if negative."},
        {"name": "Invoice and report", "text": "Tax invoice, GSTR-1 and GSTR-3B; update the income-tax block of assets."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MM complete")
