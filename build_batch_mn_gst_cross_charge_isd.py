# -*- coding: utf-8 -*-
"""Batch MN (29 Nov 2026): GST cross charge between head office and branches (distinct persons) vs Input Service Distributor
(ISD) - Circular 199/11/2023-GST on valuation, internally generated services, and the mandatory ISD for third-party common input
services from 1 April 2025.
Demand: sweep ac276 (29 Nov 2026), all 7 markets: 'circular on cross charge under gst' (coverage 0.40), 'gst circular on cross
charge', 'gst cross charge notification' (0.50). No page on the site. Multi-state Indian businesses and foreign-owned groups with
offices in several states need structuring and compliance help. User steer 26 Nov / 19 Nov 2026.
Facts (verified by web search 29 Nov 2026 - GST Council copy of Circular 199/11/2023-GST dated 17 July 2023; EY, Grant Thornton,
Mondaq, Taxmann, TaxGuru commentary; Notification 16/2024-Central Tax dated 6 August 2024 per EY / BDO / Business Today / TaxGuru):
registrations of the same entity in different states are distinct persons (section 25(4)); services between them are supplies
even without consideration (Schedule I); where an invoice is issued by the head office to a branch, the value declared in the
invoice is treated as the open market value (rule 28), and for internally generated services the value declared, or nil where no
invoice is raised, is accepted, as clarified by Circular 199/11/2023 for recipients eligible for full input tax credit; where the
branch cannot take full credit, valuation must follow rule 28 (open market value, like-kind value or 110% of cost); from 1 April
2025 (amended sections 2(61) and 20, Notification 16/2024-Central Tax), credit on common input services procured from third
parties for distinct persons must be distributed through an ISD registration, replacing the earlier option of cross-charging it.
No penalty or fee figures, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "gst-cross-charge-head-office-branch-circular-199-2023-isd-mandatory-1-april-2025-distinct-persons-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the states you are registered in, which office "
     "buys common services (rent, software, audit, consultancy), whether internal teams serve other states, whether each branch "
     "can take full input tax credit, and whether you have an ISD registration. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Cross Charge Between Head Office and Branches (2026): Circular 199/11/2023, Valuation, Internally Generated Services and Mandatory ISD From 1 April 2025",
    em="third-party costs through ISD, internal services by cross charge.",
    kicker="/ Multi-state businesses, foreign-owned groups and GCCs with several GST registrations &middot; Distinct persons &middot; Updated 2026-11-29",
    lead=("<strong>Each GST registration of a business is a separate &lsquo;distinct person&rsquo;, so services between the head office and branches in other states are taxable supplies even without payment. "
          "Circular 199/11/2023 settled valuation: where the receiving branch can take full credit, the value on the invoice - or nil if no invoice is raised for internal services - is accepted. "
          "From 1 April 2025, credit on common services bought from third parties must be distributed through an Input Service Distributor (ISD) registration instead of being cross-charged.</strong>"),
    sections=[
        ("/ Cross charge vs ISD", "Who uses which route.",
         table(["Situation", "Route"], [
             ["Common services bought from third parties (rent, software, audit) used by several registrations", "Distribute credit through an ISD registration - mandatory from 1 April 2025"],
             ["Internally generated services (head office teams serving branches)", "Cross charge by tax invoice where applicable"],
             ["Recipient branch eligible for full input tax credit", "Value declared on the invoice accepted as open market value; nil if no invoice for internal services (Circular 199/11/2023)"],
             ["Recipient branch not eligible for full credit (exempt or blocked supplies)", "Value under rule 28 - open market value, like-kind value or 110% of cost"]])
         + ul("<strong>Distinct persons:</strong> registrations of the same PAN in different states are distinct persons under section 25(4), and Schedule I treats supplies between them as taxable even without consideration.",
              "<strong>Salary costs:</strong> employees are not separately supplying services to their employer, and the circular addresses how internal services are valued for full-credit recipients.")),
        ("/ Practical compliance", "Set it up once, review yearly.",
         ul("<strong>ISD registration:</strong> needed where third-party invoices for common services are received at one office but used by several registrations.",
            "<strong>Distribution:</strong> the ISD distributes credit to the registrations that use the services, in the prescribed ratio, through monthly ISD returns.",
            "<strong>Exempt or partly exempt branches:</strong> cross-charge valuation matters most here, because tax on the cross charge becomes a cost.",
            "<strong>Foreign-owned groups and GCCs:</strong> intercompany charges from the foreign parent are imports of services under reverse charge - separate from branch cross charges.",
            "<strong>Audits and notices:</strong> departments test missing ISD registrations and unreported cross charges, so document the policy and the allocation basis.")
         + call_box("cross charge and ISD", ["Mapping services between registrations",
                                              "ISD registration and distribution",
                                              "Cross-charge valuation under rule 28",
                                              "Exempt-branch cost analysis",
                                              "Notice replies on cross charge and ISD"],
                    "States, common services, internal teams, credit position of each branch, ISD status.")
         + sources("CGST Act, 2017 (sections 2(61), 20 and 25(4); Schedule I); CGST Rules, 2017 (rule 28); Circular 199/11/2023-GST dated 17 July 2023; Notification 16/2024-Central Tax dated 6 August 2024; site GST reverse charge on imports, GST return filing and GCC pages.")),
    ],
    faqs=[("What is cross charge in GST?", "A tax invoice raised by one GST registration of a business, usually the head office, on another registration of the same business in a different state for services it provides, such as management or IT support. The registrations are distinct persons, so the supply is taxable even without payment."),
          ("What did Circular 199/11/2023 clarify on cross charge?", "Where the receiving branch is eligible for full input tax credit, the value declared on the head office's invoice is treated as the open market value, and for internally generated services the value can be nil if no invoice is raised. Where the branch cannot take full credit, valuation follows rule 28."),
          ("Is ISD mandatory under GST?", "Yes, from 1 April 2025. Credit on common input services bought from third parties for use by more than one registration must be distributed through an Input Service Distributor registration (amended sections 2(61) and 20, Notification 16/2024-Central Tax)."),
          ("What is the difference between ISD and cross charge?", "ISD distributes credit on services bought from third parties; cross charge taxes services the business provides internally from one registration to another."),
          ("Does cross charge apply to services from a foreign parent company?", "No. Charges from a foreign parent are imports of services, taxed under reverse charge by the Indian entity - a separate issue from cross charges between Indian branches."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your registrations, common services, internal teams, each branch's credit position and ISD status. Or book a call directly.")],
    related=[("gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026.html", "GST reverse charge on import of services"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing"),
             ("gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html", "Setting up a GCC in India"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "GST mismatch notices")],
    cta_h="Registered in more than one state?", cta_b=C,
    keywords="gst cross charge, circular on cross charge under gst, circular 199/11/2023, gst cross charge notification, isd mandatory 1 april 2025, input service distributor vs cross charge, head office branch gst, distinct persons gst, rule 28 valuation",
    desc="GST cross charge between head office and branches: distinct persons, Circular 199/11/2023 valuation (invoice value or nil for full-credit branches), rule 28 for others, and the mandatory ISD for third-party common services from 1 April 2025.",
    howto={"name": "How to set up cross charge and ISD", "description": "Map, register, value, document.", "steps": [
        {"name": "Map the services", "text": "Third-party common services vs internally generated services."},
        {"name": "Register an ISD", "text": "For third-party common services used by several registrations."},
        {"name": "Value cross charges", "text": "Invoice value for full-credit branches; rule 28 otherwise."},
        {"name": "Document the policy", "text": "Allocation basis, invoices and ISD returns, reviewed yearly."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MN complete")
