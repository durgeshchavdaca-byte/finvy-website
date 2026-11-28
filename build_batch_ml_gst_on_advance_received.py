# -*- coding: utf-8 -*-
"""Batch ML (29 Nov 2026): GST on advance received - services vs goods, time of supply, receipt voucher, refund voucher,
the 18% default rate where the rate is not known, reporting and adjusting advances in returns.
Demand: sweep ac275 (29 Nov 2026), all 7 markets: 'gst on advance received against supply of service' (coverage 0.33), '...
for supply of services' / 'for works contract' (0.40), '... for goods', '... from customer', '... for services' (0.50). No
page on the site. Service businesses, contractors and exporters taking advances need compliance help. User steer 26 Nov 2026.
Facts (CGST Act sections 12, 13 and 31; CGST Rules 50 and 51; Notification 66/2017-Central Tax): for services, the time of
supply is the earliest of the invoice date (if issued within the time allowed), the date of receipt of payment, or the date of
provision of service, so GST is payable on an advance received for services; where an amount up to INR 1,000 is received in
excess of the invoice amount, the supplier may treat the invoice date as the time of supply for that excess; for goods,
Notification 66/2017-Central Tax (15 November 2017) exempts registered persons (other than composition taxpayers) from paying
GST on advances, so tax is paid when the invoice is issued; a receipt voucher must be issued for an advance; where the rate or
nature of supply is not known at the time of the advance, tax is paid at 18% and, if the nature is not known, it is treated as
an inter-state supply; if the supply does not take place and no invoice is issued, a refund voucher is issued; advances and
their later adjustment are reported in GSTR-1 (Table 11) and reflected in GSTR-3B; works contracts are services. No fees, no
portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "gst-on-advance-received-services-goods-time-of-supply-receipt-voucher-refund-voucher-gstr-1-table-11-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you supply (goods, services, works "
     "contract), how advances are received and adjusted, a sample receipt and invoice, and any notice on unpaid tax on "
     "advances. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST on Advance Received (2026): Services vs Goods, Time of Supply, Receipt Voucher, Refund Voucher and Reporting Advances in GSTR-1",
    em="services pay on the advance, goods usually do not.",
    kicker="/ Service providers, contractors and suppliers taking customer advances &middot; GST time of supply &middot; Updated 2026-11-29",
    lead=("<strong>GST is payable on an advance received for services, because the time of supply is the earlier of the invoice or the payment. "
          "For goods, registered suppliers (other than composition taxpayers) do not pay GST on advances - the tax is paid when the invoice is issued. "
          "Either way, issue a receipt voucher for the advance, report it in GSTR-1, and adjust it when you invoice.</strong>"),
    sections=[
        ("/ When GST applies to advances", "Sections 12 and 13 and Notification 66/2017-Central Tax.",
         table(["Situation", "GST on the advance"], [
             ["Advance for services (including works contracts)", "Payable - time of supply is the earlier of invoice and payment"],
             ["Advance for goods (regular registered supplier)", "Not payable - tax is paid when the invoice is issued"],
             ["Advance received by a composition taxpayer for goods", "The exemption for advances does not cover composition taxpayers"],
             ["Rate or nature of supply not known at the time", "Pay at 18%; treat as inter-state if the nature is not known"],
             ["Excess of up to INR 1,000 over the invoice", "Supplier may treat the invoice date as the time of supply for the excess"]])
         + ul("<strong>Receipt voucher:</strong> issue one for every advance, showing the amount, rate and tax.",
              "<strong>Reporting:</strong> show advances in GSTR-1 (Table 11) and adjust them in the month the invoice is raised, with GSTR-3B matching.")),
        ("/ Cancellations, refunds and common errors", "Get the trail right.",
         ul("<strong>Supply cancelled:</strong> if no invoice is issued and the advance is returned, issue a refund voucher and adjust the tax paid on the advance in the return.",
            "<strong>Export advances:</strong> advances for export of services under an LUT carry no tax, but the export conditions must still be met when the service is supplied.",
            "<strong>Long-term contracts:</strong> milestone advances on service contracts trigger tax as each advance is received.",
            "<strong>Notices:</strong> departments compare advances in bank statements and books with tax paid - unpaid tax on service advances attracts interest.",
            "<strong>Input tax credit:</strong> the recipient can claim credit only after the supply is received and the invoice is issued, not on the receipt voucher.")
         + call_box("GST on advances", ["Time of supply review for advances",
                                         "Receipt and refund voucher formats",
                                         "GSTR-1 Table 11 reporting and adjustment",
                                         "Interest and notices on unpaid tax",
                                         "Contracts with milestone billing"],
                    "What you supply, how advances work, sample receipt and invoice, any notice.")
         + sources("CGST Act, 2017 (sections 12, 13 and 31); CGST Rules, 2017 (rules 50 and 51); Notification 66/2017-Central Tax; site GST return filing, e-invoicing and consultant GST pages.")),
    ],
    faqs=[("Is GST payable on advance received for services?", "Yes. For services, the time of supply is the earliest of the invoice date, the date payment is received or the date of provision, so GST is due on the advance in the month it is received. Issue a receipt voucher and report it in GSTR-1."),
          ("Is GST payable on advance received for goods?", "No, for regular registered suppliers. Notification 66/2017-Central Tax removed the liability on advances for goods, so tax is paid when the invoice is issued. The exemption does not cover composition taxpayers."),
          ("What rate applies if the rate is not known when the advance is received?", "Tax is paid at 18%, and if the nature of supply is not known it is treated as an inter-state supply."),
          ("What happens if the advance is refunded and the supply never happens?", "Issue a refund voucher and adjust the tax paid on the advance in the return for the period."),
          ("Is GST payable on advance received for a works contract?", "Yes. A works contract is a supply of services, so GST is payable on each advance when it is received."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you supply, how advances are received and adjusted, a sample receipt and invoice, and any notice. Or book a call directly.")],
    related=[("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and due dates"),
             ("gst-e-invoicing-applicability-5-crore-30-day-reporting-limit-irn-exemptions-cancellation-2026.html", "GST e-invoicing"),
             ("gst-for-consultants-professionals-india-registration-threshold-18-percent-export-lut-reimbursement-pure-agent-2026.html", "GST for consultants and professionals"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "GST mismatch notices")],
    cta_h="Taking advances from customers?", cta_b=C,
    keywords="gst on advance received, gst on advance received for services, gst on advance received for goods, gst on advance received from customer, gst on advance works contract, receipt voucher gst, refund voucher gst, notification 66/2017, gstr-1 table 11 advance",
    desc="GST on advance received: payable on advances for services (time of supply), not on advances for goods for regular suppliers under Notification 66/2017, 18% where the rate is unknown, receipt and refund vouchers, and reporting in GSTR-1 Table 11.",
    howto={"name": "How to handle GST on customer advances", "description": "Classify, voucher, report, adjust.", "steps": [
        {"name": "Classify the supply", "text": "Goods or services (works contracts are services)."},
        {"name": "Issue a receipt voucher", "text": "Amount, rate and tax - 18% if the rate is not yet known."},
        {"name": "Pay and report", "text": "Tax on service advances in that month; report in GSTR-1 Table 11."},
        {"name": "Adjust or refund", "text": "Adjust on invoicing; refund voucher if the supply is cancelled."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ML complete")
