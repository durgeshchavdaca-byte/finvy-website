# -*- coding: utf-8 -*-
"""Batch MO (29 Nov 2026): Ind AS vs IFRS - what Ind AS is, when it applies (and to Indian subsidiaries of foreign groups),
why Ind AS financial statements may not be fully IFRS-compliant, verified examples of carve-outs, and what foreign parents
reporting under IFRS need from their Indian subsidiaries.
Demand: sweep ac277 (29 Nov 2026), all 7 markets: 'ind as vs ifrs differences', 'ind as and ifrs difference' (coverage 0.33). No
page on the site. Foreign parents consolidating Indian subsidiaries and Indian companies preparing for listing or foreign
investors need GAAP-difference help. User steer 19 Nov / 26 Nov 2026: insights for foreign companies; more calls.
Facts (verified by web search 29 Nov 2026 - ICAI Ind AS guidance material pages, KPMG Ind AS disclosure guide and first-time
adoption / business combinations implementation guides, ESMA equivalence report, Taxscan carve-outs article): Ind AS are converged
with IFRS but contain carve-outs and carve-ins to suit the Indian legal and economic environment, so financial statements prepared
under Ind AS may not fully comply with IFRS; examples: Ind AS 40 permits only the cost model for investment property (IFRS also
allows fair value); under Ind AS 103 a bargain purchase gain is recognised in other comprehensive income and accumulated in equity
as capital reserve (or directly in equity where there is no clear evidence of a bargain purchase), whereas IFRS 3 recognises it in
profit or loss; Ind AS 21 / Ind AS 101 allow continuation of the previous GAAP treatment for certain long-term foreign currency
monetary items. Applicability under the Companies (Indian Accounting Standards) Rules, 2015: listed companies (and those in the
process of listing), unlisted companies with net worth of INR 250 crore or more, and their holding, subsidiary, joint venture and
associate companies; others may adopt voluntarily; other companies follow the Accounting Standards (Indian GAAP). An Indian
subsidiary of a foreign company applies Ind AS if it meets these criteria itself or opts in. No fees, no portal menu paths, no
comparisons with named firms. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "ind-as-vs-ifrs-differences-carve-outs-applicability-indian-subsidiary-foreign-parent-group-reporting-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the Indian entity's latest financial statements, "
     "its net worth and listing status, the group's reporting framework and calendar, and the areas your group auditors "
     "query most. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Ind AS vs IFRS (2026): Key Differences and Carve-Outs, When Ind AS Applies, and What Foreign Parents Need From Their Indian Subsidiary",
    em="close to IFRS, but not identical.",
    kicker="/ Foreign groups with Indian subsidiaries, Indian companies preparing for listing or foreign investment &middot; Accounting frameworks &middot; Updated 2026-11-29",
    lead=("<strong>Indian Accounting Standards (Ind AS) are converged with IFRS, but they include carve-outs and carve-ins for Indian law and practice - so Ind AS financial statements may not be fully IFRS-compliant. "
          "Ind AS is mandatory for listed companies, unlisted companies with net worth of INR 250 crore or more, and their group companies; other companies use the older Accounting Standards (Indian GAAP). "
          "A foreign parent reporting under IFRS usually needs a reconciliation or a group reporting pack from its Indian subsidiary.</strong>"),
    sections=[
        ("/ Examples of Ind AS carve-outs", "Where Ind AS departs from IFRS.",
         table(["Area", "IFRS", "Ind AS"], [
             ["Investment property", "Cost or fair value model", "Cost model only (Ind AS 40)"],
             ["Bargain purchase gain in a business combination", "Recognised in profit or loss (IFRS 3)", "Recognised in OCI and accumulated as capital reserve, or directly in equity without clear evidence of a bargain purchase (Ind AS 103)"],
             ["Certain long-term foreign currency monetary items", "IAS 21 treatment", "Option to continue the previous GAAP treatment for items covered by the transition relief"],
             ["Overall", "Full IFRS compliance statement possible", "Ind AS statements may not fully comply with IFRS because of carve-outs"]])
         + ul("<strong>Not exhaustive:</strong> there are other carve-outs and carve-ins; check each standard relevant to the business.",
              "<strong>Indian GAAP vs IFRS:</strong> for companies outside Ind AS, the differences from IFRS are much wider.")),
        ("/ Applicability and group reporting", "Who uses Ind AS, and what the parent needs.",
         ul("<strong>Mandatory Ind AS:</strong> listed companies and companies in the process of listing, unlisted companies with net worth of INR 250 crore or more, and their holding, subsidiary, joint venture and associate companies (Companies (Indian Accounting Standards) Rules, 2015).",
            "<strong>Indian subsidiary of a foreign company:</strong> applies Ind AS if it meets these criteria itself or chooses to; otherwise it reports under Indian GAAP.",
            "<strong>Once adopted:</strong> a company that moves to Ind AS continues with it.",
            "<strong>Group reporting pack:</strong> the Indian statutory accounts, and a GAAP-difference reconciliation to IFRS (or US GAAP) for consolidation.",
            "<strong>Calendar mismatch:</strong> Indian companies use an April-March financial year; groups with calendar-year reporting need interim cut-offs.")
         + call_box("Ind AS, IFRS and group reporting", ["Ind AS applicability check",
                                                         "Ind AS vs IFRS / Indian GAAP vs IFRS reconciliation",
                                                         "Group reporting packs for foreign parents",
                                                         "First-time Ind AS adoption",
                                                         "Statutory audit coordination with group auditors"],
                    "Financial statements, net worth and listing status, group framework and calendar, auditor queries.")
         + sources("Companies (Indian Accounting Standards) Rules, 2015; Ind AS 21, 40, 101 and 103; ICAI Ind AS guidance material; KPMG Ind AS guides; ESMA report on the equivalence of Indian Accounting Standards; site audit applicability, IPO-readiness and foreign subsidiary pages.")),
    ],
    faqs=[("What is the difference between Ind AS and IFRS?", "Ind AS are India's converged version of IFRS, with carve-outs and carve-ins for Indian law and practice. For example, Ind AS 40 allows only the cost model for investment property, and Ind AS 103 sends a bargain purchase gain to capital reserve rather than profit or loss. As a result, Ind AS financial statements may not fully comply with IFRS."),
          ("Which companies must follow Ind AS in India?", "Listed companies and those in the process of listing, unlisted companies with net worth of INR 250 crore or more, and their holding, subsidiary, joint venture and associate companies. Others may adopt Ind AS voluntarily; the rest follow the Accounting Standards (Indian GAAP)."),
          ("Does an Indian subsidiary of a foreign company have to use Ind AS?", "Only if it meets the Ind AS criteria itself or chooses to adopt it. Otherwise it prepares statutory accounts under Indian GAAP and gives the parent a reconciliation for consolidation."),
          ("Are Ind AS financial statements IFRS-compliant?", "Not necessarily. Because of carve-outs, Ind AS statements may not fully comply with IFRS, so foreign parents and investors often ask for a reconciliation."),
          ("What does a foreign parent need from its Indian subsidiary at year end?", "The Indian statutory financial statements and a group reporting pack adjusted to the group's framework, covering GAAP differences and any April-March to calendar-year cut-off."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the financial statements, net worth and listing status, the group's framework and calendar, and auditor queries. Or book a call directly.")],
    related=[("audit-applicability-india-company-llp-partnership-proprietorship-trust-statutory-tax-audit-limits-2026.html", "Audit applicability in India"),
             ("ca-for-ipo-ready-startup-sebi-icdr-ind-as-india.html", "IPO readiness and Ind AS"),
             ("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Payroll for an Indian subsidiary"),
             ("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs")],
    cta_h="Consolidating an Indian subsidiary under IFRS?", cta_b=C,
    keywords="ind as vs ifrs differences, ind as and ifrs difference, ind as carve outs, ind as applicability net worth 250 crore, indian subsidiary ind as foreign parent, ifrs reconciliation india, indian gaap vs ifrs, group reporting pack india",
    desc="Ind AS vs IFRS: Ind AS is converged with IFRS but has carve-outs (investment property cost model only, bargain purchase gain to capital reserve, long-term foreign currency items), applies to listed and INR 250 crore net worth companies and their groups, and foreign parents need IFRS reconciliations.",
    howto={"name": "How to align an Indian subsidiary's accounts with group IFRS reporting", "description": "Check, map, reconcile, report.", "steps": [
        {"name": "Check the framework", "text": "Is the Indian entity on Ind AS or Indian GAAP?"},
        {"name": "Map the differences", "text": "List carve-outs and GAAP differences relevant to the business."},
        {"name": "Reconcile", "text": "Prepare adjustments to IFRS for consolidation."},
        {"name": "Align the calendar", "text": "Handle April-March vs calendar-year cut-offs and audit timing."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MO complete")
