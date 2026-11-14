# -*- coding: utf-8 -*-
"""Batch CJ (14 Nov 2026): closing a company in India (sweep-2 demand: "close company in India", "company strike off
procedure India", "strike off company meaning", "how to activate strike off company in India", seen in all 7 markets).
Facts: voluntary strike off under section 248(2) of the Companies Act, 2013 in Form STK-2, after extinguishing all
liabilities, with a special resolution or consent of 75% of members by paid-up capital; supporting indemnity (STK-3),
affidavits (STK-4) and a statement of accounts certified by a chartered accountant; restrictions in section 249 (e.g. no
change of name or registered office, disposal of property or business activity in the preceding three months); the ROC
publishes notice and strikes off; applications are processed centrally by the MCA's C-PACE (Centre for Processing
Accelerated Corporate Exit) since 2023. Effects: section 248(6)-(7) (liabilities of directors and members continue).
Restoration under section 252: appeal to the NCLT within 3 years of the Registrar's order, or application within 20 years
of gazette publication where the company was carrying on business or it is otherwise just; restoration orders usually
require pending filings and penalties. Solvent companies with assets: voluntary liquidation under section 59 of the IBC.
Sources: Companies Act, 2013 ss.248-252; Companies (Removal of Names of Companies from the Register) Rules, 2016;
iPleaders, Taxmann, Sansa Legal (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the company name, whether it has any assets, loans, GST registration or employees, and where the shareholders are. "
           "We reply the same working day with the right exit route and a fixed-scope quote.")
SLUG = "close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Foreign parent closing its Indian subsidiary?</p>'
       f'<p style="margin:0">The order matters: settle tax and GST, close payroll, clear inter-company balances, repatriate the remaining capital through the bank, and only then apply for strike off or liquidation. '
       f'<a href="{wa("Hi Durgesh, our foreign company wants to close its Indian subsidiary. Can you advise the steps?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="How to Close a Company in India (2026): Strike Off in Form STK-2, Conditions, Restoring a Struck-Off Company and Closing a Foreign Subsidiary",
    em="clear the liabilities first, then file STK-2.",
    kicker="/ Company law &middot; Exit &middot; Foreign subsidiaries &middot; Updated 2026-11-14",
    lead=("The simplest way to close a private company in India is <strong>voluntary strike off</strong> under section 248(2) of the Companies Act, 2013: once all liabilities are paid, the company files <strong>Form STK-2</strong> with a special resolution (or consent of 75% of members by paid-up capital), indemnity and affidavits from directors, and a statement of accounts certified by a chartered accountant. "
          "The Registrar publishes a notice and then strikes the name off; applications are processed centrally by the MCA's <strong>C-PACE</strong>. "
          "A company that still has assets to distribute uses <strong>voluntary liquidation</strong> under the Insolvency and Bankruptcy Code instead. A struck-off company can be <strong>restored by the NCLT</strong> under section 252."),
    sections=[
        ("/ Choose the exit route", "Strike off or liquidation.",
         table(["Route", "When it fits", "Main steps"], [
             ["Voluntary strike off (section 248(2), Form STK-2)", "No assets or liabilities left, no pending litigation, business stopped", "Close bank account last, file pending returns, pass special resolution, file STK-2 with STK-3 indemnity, STK-4 affidavits and CA-certified statement of accounts"],
             ["Voluntary liquidation (IBC section 59)", "Solvent company with assets to distribute or creditors to settle in an orderly way", "Declaration of solvency, liquidator appointed, assets realised and distributed, final order"],
             ["Sale of shares or merger", "Business or licences have value to a buyer or group company", "Share transfer (FC-TRS where non-residents are involved) or merger scheme"],
             ["Strike off by the Registrar (section 248(1))", "Company inactive and not filing", "Not a planned exit: directors can be disqualified and liabilities continue"]])
         + "<p>The company cannot apply for strike off if, in the previous three months, it changed its name or registered office, disposed of property or rights for value, or carried on business other than what is needed to close (section 249).</p>"),
        ("/ Closing checklist", "In this order.",
         ul("Stop operations; settle vendors, employees (final salary, gratuity, PF and ESI exits) and statutory dues.",
            "File all pending income tax, TDS and GST returns; cancel the GST registration; close professional tax and other registrations.",
            "Prepare a statement of accounts showing nil assets and liabilities, certified by a chartered accountant (not older than 30 days at filing).",
            "Pass the board and shareholder resolutions; directors sign the indemnity (STK-3) and affidavits (STK-4).",
            "File Form STK-2 on the MCA portal with the fee; the Registrar publishes the notice (STK-6) and, after the objection period, strikes off the name.",
            "Close the bank account after the final payments, and keep the records for the statutory period.")
         + BOX),
        ("/ Restoring a struck-off company", "Section 252.",
         table(["Who and when", "Route"], [
             ["Company or member aggrieved by the Registrar's strike-off order", "Appeal to the NCLT within 3 years of the order"],
             ["Company, member, creditor or workman, where the company was carrying on business or it is otherwise just", "Application to the NCLT within 20 years of publication in the Official Gazette"],
             ["After restoration", "File pending annual returns and financial statements and pay any costs or penalties ordered"]])
         + '<p>Related: <a href="director-disqualified-section-164-2-din-deactivated-fix-india.html">director disqualified under section 164(2)</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up an Indian subsidiary</a> &middot; <a href="repatriate-profits-india-foreign-parent.html">repatriating profits to a foreign parent</a> &middot; <a href="form-fc-trs-filing-checklist-india-2026.html">Form FC-TRS checklist</a>.</p>'
         + f'<p><strong>Sources:</strong> Companies Act, 2013, sections 248 to 252; Companies (Removal of Names of Companies from the Register) Rules, 2016 (Forms STK-2, STK-3, STK-4, STK-6); Insolvency and Bankruptcy Code, 2016, section 59; MCA C-PACE. Secondary summaries checked 14 November 2026: iPleaders, Taxmann, Sansa Legal. <em>{UPDATED}</em> General information, not legal advice for your situation.</p>'),
    ],
    faqs=[("How do I close a private limited company in India?", "If it has no assets or liabilities, file for voluntary strike off in Form STK-2 under section 248(2) of the Companies Act, 2013, with a special resolution, director indemnity and affidavits, and a CA-certified statement of accounts. Companies with assets to distribute use voluntary liquidation under the IBC."),
          ("What does strike off mean for a company?", "The company's name is removed from the register and it ceases to exist as a legal entity, but the liabilities of directors, officers and members continue."),
          ("Who processes strike-off applications?", "The MCA's Centre for Processing Accelerated Corporate Exit (C-PACE), which handles voluntary strike-off filings centrally."),
          ("Can a struck-off company be revived?", "Yes, by the NCLT under section 252: an appeal within 3 years of the Registrar's order, or an application within 20 years of gazette publication where the company was carrying on business or it is otherwise just."),
          ("How does a foreign company close its Indian subsidiary?", "Settle all liabilities and taxes, close payroll and GST, repatriate remaining funds through the bank, then strike off (if nothing is left) or use voluntary liquidation."),
          ("Can BQP handle the closure?", "Yes. " + CONTACT)],
    related=[("director-disqualified-section-164-2-din-deactivated-fix-india.html", "Director disqualified under section 164(2)"), ("repatriate-profits-india-foreign-parent.html", "Repatriate profits to a foreign parent"),
             ("foreign-company-setup-indian-subsidiary-wos.html", "Indian subsidiary set-up")],
    cta_h="Closing a company in India?", cta_b=CONTACT,
    keywords="close company in India, company strike off procedure India, STK-2 strike off, how to close private limited company India, strike off company meaning, restore struck off company NCLT section 252, close Indian subsidiary foreign company, C-PACE strike off",
    desc="How to close a company in India in 2026: voluntary strike off under section 248(2) with Form STK-2 (conditions, documents, C-PACE), voluntary liquidation for solvent companies, restoring a struck-off company under section 252, and closing a foreign-owned subsidiary.",
    howto={"name": "How to close a company in India by strike off", "description": "Steps for a private company with no assets or liabilities.", "steps": [
        {"name": "Settle everything", "text": "Pay vendors, employees and statutory dues; file pending tax and GST returns; cancel GST."},
        {"name": "Prepare the accounts", "text": "Statement of accounts with nil assets and liabilities, certified by a chartered accountant."},
        {"name": "Pass resolutions and sign forms", "text": "Special resolution or 75% member consent; directors sign STK-3 and STK-4."},
        {"name": "File STK-2", "text": "File on the MCA portal; after the public notice and objection period the Registrar strikes off the name."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CJ complete")
