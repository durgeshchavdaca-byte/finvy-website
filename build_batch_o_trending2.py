# -*- coding: utf-8 -*-
"""Batch O part 2: 10 trending foreign-company pages Oct 2026.

Topics genuinely trending in late 2026: DPDP Act compliance, RBI PA/PG
licensing for fintech, Account Aggregator (AA), data localisation,
PLI schemes, space FDI reform, telecom FDI reform, UPI integration,
IEC/GST/customs for exporters, Semiconductor ISM.
"""
from build_lib import page, write_page

# 11. DPDP Act compliance for foreign company
write_page("dpdp-act-india-foreign-company-compliance-2026", page(
    slug="dpdp-act-india-foreign-company-compliance-2026",
    title="DPDP Act India Compliance for Foreign Company 2026 - BQP",
    description="DPDP Act 2023 (Digital Personal Data Protection Act) compliance for foreign companies handling Indian personal data: extraterritorial scope, consent + legitimate use grounds, Data Fiduciary / Significant Data Fiduciary / Data Processor roles, Consent Manager, data principal rights, breach notification, Data Protection Board, penalty up to INR 250 crore. Complete 2026 guide. CA Durgesh Chavda.",
    keywords="DPDP Act India foreign company compliance, Digital Personal Data Protection Act India 2026, DPDP extraterritorial foreign SaaS, Significant Data Fiduciary India, DPDP consent manager",
    hero_kicker="/ Foreign Clients &middot; DPDP Act &middot; Updated 2026-10-15",
    hero_title_html="DPDP Act India, <em>applies to foreign companies too.</em>",
    hero_lead="India's Digital Personal Data Protection Act 2023 (DPDP Act) is India's first comprehensive data protection law. Extraterritorial reach: applies to any entity (Indian or foreign) processing personal data of Indian residents (data principals) in connection with offering goods / services. US SaaS selling to Indian users is in scope. UK fintech with Indian customers in scope. Penalty up to INR 250 crore per breach. Here's the complete 2026 practitioner's framework.",
    sections=[
        ("/ Scope + applicability", "Who is caught.",
         "<p><strong>Section 3 DPDP Act applies to processing of digital personal data</strong>:</p>"
         "<ul>"
         "<li>Within India, if personal data is collected (a) in digital form, OR (b) in non-digital form and digitised subsequently.</li>"
         "<li><strong>Outside India</strong>, if processing is in connection with any activity related to offering of goods or services to data principals (persons) within India.</li>"
         "</ul>"
         "<p>Translation for foreign companies:</p>"
         "<ul>"
         "<li>US SaaS company with Indian paying users (B2C): in scope.</li>"
         "<li>US e-commerce selling to Indian consumers: in scope.</li>"
         "<li>UK fintech serving Indian customers: in scope.</li>"
         "<li>European media platform with Indian subscribers: in scope.</li>"
         "<li>Singapore AI chatbot with Indian users: in scope.</li>"
         "<li>Any processing of Indian individual's email, phone, name, address, device identifier, financial info, location, etc.: in scope.</li>"
         "</ul>"
         "<p>'Personal data' broad: anything that identifies or can identify an individual.</p>"),
        ("/ Core compliance obligations", "What foreign companies must do.",
         "<ul>"
         "<li><strong>Legitimate ground</strong>: process personal data only based on (a) consent, or (b) 'certain legitimate uses' (specified Section 7: employment, performance of contract, legal obligation, public interest, specified medical / disaster response).</li>"
         "<li><strong>Notice (Section 5)</strong>: before/at consent, data principal must receive clear notice of: personal data to be processed, purpose, how to withdraw consent, grievance mechanism, how to make complaint to Data Protection Board.</li>"
         "<li><strong>Consent (Section 6)</strong>: must be free, specific, informed, unconditional, unambiguous. Easy withdrawal. Linguistic requirements (notice in English + any of 22 scheduled Indian languages).</li>"
         "<li><strong>Purpose limitation</strong>: process only for specified purpose; obtain fresh consent for new purposes.</li>"
         "<li><strong>Data accuracy (Section 8)</strong>: Data Fiduciary must take reasonable efforts to ensure accuracy + completeness.</li>"
         "<li><strong>Security safeguards (Section 8(5))</strong>: reasonable security safeguards to prevent personal data breach.</li>"
         "<li><strong>Breach notification (Section 8(6))</strong>: on becoming aware of personal data breach, notify Data Protection Board AND each affected data principal.</li>"
         "<li><strong>Data erasure (Section 8(7))</strong>: delete personal data once purpose served or consent withdrawn.</li>"
         "<li><strong>Grievance redressal</strong>: appoint grievance officer; respond within reasonable time.</li>"
         "<li><strong>Rights of data principal (Section 11-14)</strong>: right to information, correction, erasure, grievance redressal, nominate successor.</li>"
         "<li><strong>Children's data</strong>: verifiable parental consent for processing data of persons under 18 (the government may allow a lower age for fiduciaries it notifies as handling children's data safely). No targeted advertising to children.</li>"
         "<li><strong>Persons with disabilities</strong>: consent of lawful guardian.</li>"
         "</ul>"),
        ("/ Significant Data Fiduciary", "The elevated tier.",
         "<ul>"
         "<li><strong>Section 10</strong>: Central Government may notify any Data Fiduciary / class as 'Significant Data Fiduciary' (SDF) based on factors: volume + sensitivity of personal data, risk to rights of data principals, impact on sovereignty, security of state, public order.</li>"
         "<li><strong>Additional obligations for SDF</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Appoint Data Protection Officer based in India (natural person representing SDF).</li>"
         "<li>&nbsp;&nbsp;&mdash; Appoint independent Data Auditor to assess compliance.</li>"
         "<li>&nbsp;&nbsp;&mdash; Periodic Data Protection Impact Assessment (DPIA) + periodic audit.</li>"
         "<li>&nbsp;&nbsp;&mdash; Other measures as Central Government specifies.</li>"
         "<li><strong>Likely SDF candidates</strong>: large social media, fintech, health and e-commerce platforms. Check whether any SDF notification covers you before assuming the lighter tier.</li>"
         "</ul>"),
        ("/ Cross-border data transfer", "The sovereign carve-out.",
         "<ul>"
         "<li><strong>Section 16</strong>: Central Government may notify countries / territories to which personal data of Indian residents may NOT be transferred.</li>"
         "<li><strong>'Blocklist' approach</strong>: unlike GDPR (adequacy decision whitelist), DPDP uses notifications of restricted jurisdictions.</li>"
         "<li><strong>Current state (2026)</strong>: no restrictions notified yet; cross-border transfer currently unrestricted subject to other sectoral regulations (RBI payment data localisation, SEBI data retention, etc.).</li>"
         "<li><strong>Prudent approach</strong>: foreign Data Fiduciary should document cross-border flows, Data Processing Agreements (DPAs) with India-side processors, Standard Contractual Clauses (SCCs) adapted for India, data residency for sensitive sectors (payment data per RBI).</li>"
         "</ul>"),
        ("/ Penalties + Data Protection Board", "The enforcement.",
         "<ul>"
         "<li><strong>Data Protection Board of India (Section 18-20)</strong>: statutory body for enforcement. Investigates complaints; issues orders; imposes penalties.</li>"
         "<li><strong>Penalty structure (Section 33 + Schedule)</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Failure to take reasonable security safeguards to prevent breach: up to <strong>INR 250 crore</strong>.</li>"
         "<li>&nbsp;&nbsp;&mdash; Failure to notify Data Protection Board of breach: up to INR 200 crore.</li>"
         "<li>&nbsp;&nbsp;&mdash; Non-fulfilment of obligations on processing children's data: up to INR 200 crore.</li>"
         "<li>&nbsp;&nbsp;&mdash; Non-fulfilment of SDF obligations: up to INR 150 crore.</li>"
         "<li>&nbsp;&nbsp;&mdash; Breach of other provisions: up to INR 50 crore.</li>"
         "<li><strong>Appeal</strong>: TDSAT (Telecom Disputes Settlement and Appellate Tribunal) within 60 days.</li>"
         "<li><strong>Effective date</strong>: DPDP Act enacted August 2023; the DPDP Rules, 2025 were notified on 13 November 2025 and apply in phases, with the main duties from about 13 May 2027. Draft Rules were circulated in January 2025 and the final Rules were notified on 13 November 2025.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Does DPDP Act apply to foreign companies without an Indian entity?",
         "Yes - extraterritorial reach under Section 3(b). Any entity processing personal data of Indian residents (data principals) 'in connection with any activity related to offering of goods or services' to persons in India is in scope. US SaaS with Indian users, UK e-commerce selling to Indian consumers, Singapore app with Indian subscribers all captured. No Indian entity required for the Act to apply."),
        ("What is a Significant Data Fiduciary under DPDP?",
         "Entity notified by Central Government as SDF based on volume + sensitivity of personal data handled, risk to data principals, impact on sovereignty / state security / public order. Additional obligations: India-based Data Protection Officer, independent Data Auditor, periodic DPIA, periodic audit. Likely candidates: large social media, fintech, health and e-commerce platforms; check whether a notification covers you."),
        ("Can foreign company transfer Indian personal data abroad under DPDP?",
         "Currently yes - Section 16 provides 'blocklist' approach: Central Government may notify specific countries to which transfer is restricted. No restrictions notified yet (2026). Cross-border transfer currently unrestricted subject to sectoral regulations (RBI payment data localisation, SEBI data retention rules). Prudent approach: document cross-border flows, DPAs with India-side processors, data residency for sensitive sectors."),
        ("What's the DPDP penalty for data breach?",
         "Up to INR 250 crore (~USD 30 million) for failure to take reasonable security safeguards to prevent breach. Separately: up to INR 200 crore for failure to notify Data Protection Board of breach. Penalties under Section 33 + Schedule to the Act. Appeal to TDSAT within 60 days. Enforcement effective from Rules notification date (staggered 2024-2026)."),
        ("How does DPDP compare to GDPR for a foreign company?",
         "Similar concepts: lawful basis for processing, data principal rights, Data Protection Officer for SDFs, breach notification, extraterritorial reach. Differences: DPDP has 'blocklist' approach to cross-border transfer (vs GDPR adequacy whitelist); DPDP consent emphasis (narrower 'legitimate interests'); DPDP specifically governs children (under 18) + persons with disabilities. Foreign companies compliant with GDPR need India-specific adjustments but core governance framework translates."),
        ("Does BQP handle DPDP compliance for foreign companies?",
         "Yes - DPDP applicability analysis, gap analysis against existing compliance (if GDPR-compliant), consent flow design, notice drafting (English + Indian languages), Data Processing Agreement (DPA) templates, breach response plan, SDF-tier obligations if applicable, Data Protection Officer appointment, periodic DPIA + audit. Co-ordinated with foreign client's global privacy counsel. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("oidar-gst-foreign-saas-ecommerce-india.html", "Guide", "OIDAR GST"),
        ("india-data-localisation-rbi-dpdp-foreign-saas.html", "Guide", "Data Localisation"),
    ],
    cta_headline="Foreign SaaS / e-commerce / fintech handling Indian user data?",
    cta_body="DPDP Act applies extraterritorially. INR 250 crore penalty exposure. BQP: applicability analysis + gap analysis + consent flow + DPA + breach plan + ongoing compliance. Scope-based engagement.",
))

# 12. India PA/PG licensing for foreign fintech
write_page("india-payment-aggregator-pa-pg-licence-foreign-fintech", page(
    slug="india-payment-aggregator-pa-pg-licence-foreign-fintech",
    title="India Payment Aggregator (PA) Licence for Foreign Fintech 2026 - BQP",
    description="RBI Payment Aggregator (PA) and Payment Gateway (PG) licence framework for foreign fintech entering India 2026: Section 7 Payment and Settlement Systems Act, PA minimum net worth INR 15 crore (INR 25 crore in year 3), PA Cross-Border, data localisation + storage in India, nodal account, auditor-signed CA certificate. Complete guide. CA Durgesh Chavda.",
    keywords="India Payment Aggregator licence foreign fintech, RBI PA PG licence India, payment aggregator cross-border PA-CB, PA licence net worth INR 15 crore, foreign fintech RBI licence",
    hero_kicker="/ Foreign Clients &middot; RBI PA / PG &middot; Updated 2026-10-15",
    hero_title_html="India Payment Aggregator licence, <em>what foreign fintech needs.</em>",
    hero_lead="Foreign fintech / payment company entering India as a payment aggregator or payment gateway must obtain RBI authorisation under the Payment and Settlement Systems Act 2007. March 2020 RBI PA/PG framework + subsequent amendments. Minimum net worth INR 15 crore (year 1) scaling to INR 25 crore. Mandatory data localisation. PA-CB (Cross-Border) framework for international payment flows. Here's the complete 2026 playbook.",
    sections=[
        ("/ PA vs PG - the distinction", "What each does.",
         "<p><strong>Payment Aggregator (PA)</strong>:</p>"
         "<ul>"
         "<li>Entity that onboards merchants to accept various payment instruments (cards, UPI, net banking, wallet) and settles funds to merchants.</li>"
         "<li>Takes custody of funds for brief period (merchant's funds flow via PA's nodal account to merchant's bank).</li>"
         "<li>Needs RBI authorisation (licence) under PSS Act 2007.</li>"
         "<li>Example: Razorpay, Cashfree, Paytm Payment Services, PhonePe for Business.</li>"
         "</ul>"
         "<p><strong>Payment Gateway (PG)</strong>:</p>"
         "<ul>"
         "<li>Technology provider that routes payment data between merchant, customer, acquirer, issuer. Does NOT handle funds custody.</li>"
         "<li>Does NOT need RBI authorisation separately but is subject to RBI guidelines (data localisation, security standards).</li>"
         "<li>Example: pure PG function of certain gateways (though most Indian PGs are also PAs).</li>"
         "</ul>"
         "<p><strong>PA-CB (Payment Aggregator Cross-Border)</strong>:</p>"
         "<ul>"
         "<li>Specialised PA licence for cross-border payment flows: Indian consumer paying foreign merchant, or foreign consumer paying Indian merchant.</li>"
         "<li>Separate authorisation framework (RBI October 2023 PA-CB circular).</li>"
         "<li>Three sub-categories: PA-E (Export, for Indian merchants selling abroad), PA-I (Import, for Indian consumers buying abroad), PA-CB for both.</li>"
         "<li>Enables UPI international linkages, card payments cross-border, international remittance for e-commerce.</li>"
         "</ul>"),
        ("/ Eligibility + net worth for PA", "The capital requirement.",
         "<ul>"
         "<li><strong>Company incorporated in India</strong> under Companies Act 2013 (private limited / public limited / unlisted / listed). Foreign fintech must have Indian subsidiary.</li>"
         "<li><strong>Net worth</strong>: minimum INR 15 crore in year 1 of application; INR 25 crore in year 3 and ongoing.</li>"
         "<li><strong>Net worth certification</strong>: CA certificate confirming net worth as of latest audited balance sheet date.</li>"
         "<li><strong>Promoters' background</strong>: fit and proper person test. Promoters / directors must not be disqualified; must have relevant financial / technology experience.</li>"
         "<li><strong>IT infrastructure</strong>: dedicated India-hosted infrastructure. Core payment systems hosted in India (data localisation).</li>"
         "<li><strong>Nodal / escrow account</strong>: specified bank for merchant funds; settlement to merchants within T+1 for most instruments.</li>"
         "</ul>"),
        ("/ Application + approval process", "RBI PA licence workflow.",
         "<ol>"
         "<li><strong>Pre-application</strong>: structure Indian subsidiary (WOS of foreign parent typical); fund with min INR 15 crore net worth; set up IT infrastructure in India; appoint CTO + Compliance Officer + Chief Risk Officer.</li>"
         "<li><strong>Application</strong>: Form A to RBI with supporting documents &mdash; company incorporation, MOA/AOA, net worth CA certificate, business plan, system architecture, security assessment, promoter / director KYC.</li>"
         "<li><strong>RBI examination</strong>: typically 6-18 month review. Includes IT infrastructure inspection, business plan evaluation, promoter background check, legal + compliance review.</li>"
         "<li><strong>In-principle approval</strong>: 1-year validity. Applicant must demonstrate operational readiness.</li>"
         "<li><strong>Full authorisation (Certificate of Authorisation)</strong>: upon RBI satisfaction. Entity becomes authorised PA.</li>"
         "<li><strong>Ongoing compliance</strong>: monthly / quarterly reporting, annual CA certification of net worth, periodic IT audit, security incident reporting.</li>"
         "</ol>"),
        ("/ Key RBI PA / PG guidelines", "The compliance stack.",
         "<ul>"
         "<li><strong>Data localisation (RBI April 2018 circular)</strong>: all payment data (card number, CVV, OTP, device data, user data) must be stored ONLY in India. Foreign fintech typically keeps India-only data stores for Indian users.</li>"
         "<li><strong>Card tokenisation (RBI September 2021)</strong>: card storage prohibited by any entity except card networks + issuers. PA / PG must use network tokens for recurring payments.</li>"
         "<li><strong>Merchant onboarding (RBI March 2020 PA/PG circular)</strong>: PA must conduct merchant KYC, maintain merchant database, submit to RBI on request.</li>"
         "<li><strong>Nodal account (RBI March 2020)</strong>: merchant funds in nodal account; cannot be used for own purposes; T+1 settlement for most instruments.</li>"
         "<li><strong>Grievance redressal</strong>: standardised merchant + consumer complaint mechanism.</li>"
         "<li><strong>Security audit (annual)</strong>: PCI DSS + CERT-In empanelled auditor annual audit.</li>"
         "<li><strong>Non-bank PPI (Prepaid Payment Instrument)</strong>: separate licensing framework if issuing wallets.</li>"
         "<li><strong>UPI integration</strong>: NPCI approval + bank partnership for UPI handles.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What is a Payment Aggregator (PA) licence in India?",
         "RBI authorisation under Payment and Settlement Systems Act 2007 for entities that onboard merchants to accept various payment instruments (cards, UPI, net banking, wallet) and settle funds to merchants. Entity takes custody of funds briefly via nodal account before settling to merchant. Required for all PA activities since RBI March 2020 PA/PG circular. Minimum net worth INR 15 crore (year 1) scaling to INR 25 crore (year 3+)."),
        ("Can a foreign fintech obtain Indian PA licence?",
         "Yes - via Indian subsidiary. Foreign parent must incorporate Indian WOS (Pvt Ltd), capitalise it with min INR 15 crore net worth, set up India-based IT infrastructure (data localisation), appoint required officers (CTO, Compliance Officer, CRO), apply to RBI with Form A + documents. 6-18 month approval timeline typical."),
        ("What is PA-CB (Payment Aggregator Cross-Border)?",
         "Specialised PA framework for cross-border payment flows - Indian consumer paying foreign merchant (PA-I Import) or foreign consumer paying Indian merchant (PA-E Export) or both (PA-CB). RBI October 2023 circular established the framework. Enables cross-border e-commerce, international UPI linkages, international card payments through authorised PA-CB entities."),
        ("What is India's data localisation for payment data?",
         "RBI April 2018 directive: all 'payment data' (card number, CVV, device data, user data, OTPs) must be stored ONLY in India. Applies to PAs, PGs, card networks, banks, PPI issuers, any entity in payment ecosystem. Transit outside India permitted for processing but final storage must be India-only. Foreign fintech must architect India-only data stores for Indian users."),
        ("How much net worth does a foreign fintech need for Indian PA licence?",
         "INR 15 crore (~USD 1.8M) minimum at time of application; must scale to INR 25 crore (~USD 3M) by end of year 3 and maintain. Net worth certified by CA via audited balance sheet. Separate from any float / nodal account balance - net worth is own capital of the licensed entity."),
        ("Does BQP handle Indian PA / PA-CB licence applications?",
         "Yes - end-to-end: Indian subsidiary (WOS) incorporation, net worth capitalisation + CA certification, IT infrastructure structuring for data localisation, Form A application, document assembly (business plan, system architecture, security assessment, promoter KYC), RBI follow-up during 6-18 month review, in-principle to full authorisation transition, ongoing monthly compliance. Co-ordinated with Indian regulatory counsel. Scope-based engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-upi-integration-foreign-fintech.html", "Guide", "UPI Integration"),
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
    ],
    cta_headline="Foreign fintech / payment company entering India?",
    cta_body="RBI PA licence process: 6-18 months, INR 15 crore net worth, data localisation, IT infrastructure. BQP end-to-end: WOS + capitalisation + application + ongoing compliance. Scope-based engagement.",
))

# 13. Account Aggregator for foreign fintech
write_page("india-account-aggregator-aa-foreign-fintech", page(
    slug="india-account-aggregator-aa-foreign-fintech",
    title="India Account Aggregator (AA) for Foreign Fintech 2026 - BQP",
    description="India Account Aggregator (AA) framework for foreign fintech integration 2026: RBI consent-based financial data sharing, AA licence (NBFC-AA), FIP (Financial Information Provider) + FIU (Financial Information User) roles, Technical Service Provider (TSP), DEPA (Data Empowerment and Protection Architecture), use cases. CA Durgesh Chavda.",
    keywords="India Account Aggregator AA foreign fintech, NBFC-AA licence India, Financial Information User FIU, DEPA India AA, India FIP consent architecture",
    hero_kicker="/ Foreign Clients &middot; Account Aggregator &middot; Updated 2026-10-15",
    hero_title_html="India's Account Aggregator framework, <em>consent-based financial data for foreign fintech.</em>",
    hero_lead="India's Account Aggregator (AA) framework is a world-first consent-based financial data sharing system. RBI regulates AAs as NBFC-AA (non-banking financial company - Account Aggregator). Lets a user instantly consent to share their bank statements, mutual fund holdings, insurance, GST, Income Tax, pension records across institutions. For foreign fintech building Indian products (lending, insurance, wealth, PFM), AA integration is foundational. Here's the practitioner's framework.",
    sections=[
        ("/ What AA actually does", "Consent-based data pipes.",
         "<ul>"
         "<li><strong>User-initiated consent</strong>: user authorises AA to pull specified financial data for specified purpose for specified time.</li>"
         "<li><strong>Data standardisation</strong>: AAs expose standardised APIs; FIU (Financial Information User) requests data; AA retrieves from FIP (Financial Information Provider).</li>"
         "<li><strong>No data storage at AA</strong>: AA is pure consent manager; data flows FIP &rarr; AA &rarr; FIU without AA storing.</li>"
         "<li><strong>DEPA framework</strong>: Data Empowerment and Protection Architecture &mdash; user controls who sees what for how long. Fully revocable consent.</li>"
         "<li><strong>Interoperability</strong>: any AA can serve any FIP + FIU in the network.</li>"
         "</ul>"
         "<p>Think of it as 'Open Banking' but broader (not just banks &mdash; also MF, insurance, pension, tax) and consent-centric (not just FIU-driven).</p>"),
        ("/ Participants in AA ecosystem", "FIP, FIU, AA, TSP.",
         "<ul>"
         "<li><strong>AA (Account Aggregator)</strong>: NBFC-AA licensed by RBI. Technology-neutral consent manager. Does not store user data or make lending/investment decisions. Earns small fee per consent transaction.</li>"
         "<li><strong>FIP (Financial Information Provider)</strong>: entities holding user's financial data &mdash; banks, NBFCs, mutual fund AMCs, insurance companies, pension funds, GSTN, Income Tax Department. Required to onboard with AAs and share data upon consent.</li>"
         "<li><strong>FIU (Financial Information User)</strong>: entities that consume data via AA for their products &mdash; lenders doing credit assessment, financial planners, PFM apps, insurers. Must register with AAs; approved by respective regulator.</li>"
         "<li><strong>TSP (Technical Service Provider)</strong>: tech company providing API integration, consent flow UI, data standardisation services to AAs / FIPs / FIUs. Many foreign fintech participate as TSP.</li>"
         "</ul>"
         "<p><strong>Current state (2026)</strong>: ~15 licensed AAs; 150+ FIPs onboarded; 500+ FIUs active; several billion consent transactions processed annually. India's open-finance stack is among the most mature globally.</p>"),
        ("/ How foreign fintech participates", "Four pathways.",
         "<ol>"
         "<li><strong>As FIU (financial information user)</strong>: foreign fintech with Indian subsidiary + relevant Indian regulatory licence (lending via NBFC, mutual fund AMC via SEBI, insurance via IRDAI, broker-dealer) can register as FIU with AAs. Standard use cases: credit assessment, income verification, PFM aggregation, portfolio planning.</li>"
         "<li><strong>As AA (account aggregator)</strong>: NBFC-AA licence from RBI. Net worth INR 2 crore. Pure consent manager role. Several foreign-backed AAs exist (Perfios, Finvu, OneMoney, CAMS Finserv).</li>"
         "<li><strong>As TSP (technical service provider)</strong>: no licence; provide tech stack to Indian AAs / FIPs / FIUs. Many foreign SaaS participate here.</li>"
         "<li><strong>Via Indian partner</strong>: foreign fintech partners with Indian FIU to serve Indian users. Simpler + faster than own Indian regulatory setup.</li>"
         "</ol>"),
        ("/ Common use cases + planning", "Where AA adds value.",
         "<ul>"
         "<li><strong>Lending (SME / consumer)</strong>: 30-second bank statement + GST analysis replaces 2-3 week manual underwriting. Materially faster + cheaper credit decisions.</li>"
         "<li><strong>Personal Finance Management</strong>: holistic view of user's bank + MF + insurance + pension across institutions.</li>"
         "<li><strong>Insurance underwriting</strong>: income + liability verification for term life + health insurance.</li>"
         "<li><strong>Wealth management / robo-advisory</strong>: portfolio aggregation + rebalancing recommendations.</li>"
         "<li><strong>Credit scoring enhancement</strong>: traditional CIBIL plus AA-sourced actual bank behaviour.</li>"
         "<li><strong>SME lending (invoice financing)</strong>: GST data + bank cash flow + Udyam MSME verification via AA.</li>"
         "<li><strong>Tax / financial planning tools</strong>: comprehensive data for better recommendations.</li>"
         "</ul>"
         "<p>For foreign fintech, AA integration is often the critical path to launching India products that compete with Indian incumbents.</p>"),
        ("/ Compliance + consent architecture", "The DEPA guardrails.",
         "<ul>"
         "<li><strong>Consent artifact (ReBIT standard)</strong>: machine-readable consent object specifying FIU, purpose, data categories, retention period, revocation terms.</li>"
         "<li><strong>Granular consent</strong>: user can approve only specific data categories (e.g., savings bank statements but not MF).</li>"
         "<li><strong>Time-bound</strong>: consent has specific validity period; auto-expires.</li>"
         "<li><strong>Revocable</strong>: user can revoke anytime; subsequent data flows blocked.</li>"
         "<li><strong>DPDP Act interaction</strong>: AA framework complies with DPDP consent principles; FIU/AA must comply with DPDP in addition to RBI AA rules.</li>"
         "<li><strong>Breach notification</strong>: AA / FIU must notify DPDP Board of personal data breach.</li>"
         "<li><strong>Audit trail</strong>: all consent + data transactions logged, immutable.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What is India's Account Aggregator (AA) framework?",
         "RBI-regulated consent-based financial data sharing system. User consents to share bank / MF / insurance / pension / GST / tax data instantly across institutions via licensed Account Aggregator (NBFC-AA). FIP (Financial Information Provider - banks, MF AMCs, etc.) share data with AA upon consent; FIU (Financial Information User - lenders, planners) consume via AA. Launched 2021; now the backbone of India's open finance stack."),
        ("How can a foreign fintech participate in India's AA framework?",
         "Four routes: (1) Register as FIU via Indian subsidiary with relevant regulatory licence (NBFC lending, MF AMC, insurance intermediary). (2) Obtain NBFC-AA licence from RBI (net worth INR 2 crore) as a pure consent manager. (3) Act as Technical Service Provider (TSP) providing API/UI tech to Indian AAs / FIPs / FIUs - no licence required. (4) Partner with Indian FIU to serve Indian users without own licensing."),
        ("What are typical use cases for AA-based data?",
         "Lending (30-second credit decision replacing weeks of document collection), personal finance management (unified view across institutions), insurance underwriting (income/liability verification), wealth management (portfolio aggregation + rebalancing), SME invoice financing (GST + bank cash flow), credit scoring enhancement (behaviour-based vs just CIBIL). Foreign fintech launching India products typically needs AA integration to compete."),
        ("Does AA framework comply with DPDP Act?",
         "Yes - AA framework was designed with consent-centric principles that align with DPDP. Both apply simultaneously to AAs / FIUs. DEPA (Data Empowerment and Protection Architecture) underlying AA provides granular / time-bound / revocable consent. Foreign fintech using AA must comply with both AA framework (RBI/ReBIT standards) and DPDP Act (notice, consent, breach notification, data principal rights)."),
        ("How much does NBFC-AA licence cost?",
         "Minimum net worth INR 2 crore (vs INR 15 crore for PA). RBI application fee + ongoing compliance infrastructure. Entity must be Indian company (foreign subsidiary acceptable), promoters fit-and-proper, dedicated technology infrastructure, Compliance Officer + CEO. 6-12 month approval timeline typical. BQP coordinates applications."),
        ("Does BQP help foreign fintech enter India via AA framework?",
         "Yes - foreign fintech advisory: route selection (FIU vs AA vs TSP vs partnership), Indian subsidiary setup, relevant regulatory licence (NBFC / MF / insurance), AA integration via API / TSP, DPDP + RBI consent compliance, ongoing operational compliance. Co-ordinated with Indian AAs + regulatory counsel. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-payment-aggregator-pa-pg-licence-foreign-fintech.html", "Guide", "PA / PG Licence"),
        ("india-upi-integration-foreign-fintech.html", "Guide", "UPI Integration"),
    ],
    cta_headline="Foreign fintech building Indian products? AA integration is the foundation.",
    cta_body="Four pathways: FIU, AA licence, TSP, or Indian partner. BQP structures the right route + regulatory licensing + ongoing compliance. Scope-based engagement.",
))

# 14. Data localisation
write_page("india-data-localisation-rbi-dpdp-foreign-saas", page(
    slug="india-data-localisation-rbi-dpdp-foreign-saas",
    title="India Data Localisation Rules 2026 | Foreign SaaS + Fintech - BQP",
    description="India data localisation rules 2026 for foreign SaaS, fintech, e-commerce: RBI payment data localisation (April 2018), DPDP Act Section 16 country blocklist, sector-specific storage rules (SEBI, telecom, insurance), hybrid architecture, India-only data residency, cross-border transfer compliance. Complete guide. CA Durgesh Chavda.",
    keywords="India data localisation foreign SaaS, RBI payment data India localisation, DPDP data residency India, sector data storage India, foreign fintech data localisation India",
    hero_kicker="/ Foreign Clients &middot; Data Localisation &middot; Updated 2026-10-15",
    hero_title_html="India data localisation, <em>what foreign SaaS must architect.</em>",
    hero_lead="India does not have a single unified data localisation law. Instead, sector-specific rules + the DPDP Act's country-blocklist mechanism create a layered localisation regime. For foreign SaaS, fintech, e-commerce handling Indian user / payment / sensitive data, understanding which data must stay in India is critical infrastructure decision. Here's the complete 2026 framework.",
    sections=[
        ("/ The layered regime", "Multiple regulators, different rules.",
         "<ul>"
         "<li><strong>RBI (Reserve Bank of India)</strong>: payment data of Indian consumers &mdash; mandatory India-only storage (April 2018 circular).</li>"
         "<li><strong>DPDP Act 2023</strong>: Section 16 permits Central Government to notify countries where personal data of Indian residents may NOT be transferred. 'Blocklist' approach (no notifications yet 2026).</li>"
         "<li><strong>MeitY (Ministry of Electronics and Information Technology)</strong>: proposed Digital India Act (DIA, pending) may add digital services localisation; current draft framework still being discussed.</li>"
         "<li><strong>SEBI (Securities and Exchange Board of India)</strong>: broker / depository data retention in India; critical records on Indian servers.</li>"
         "<li><strong>TRAI / DoT (telecom)</strong>: subscriber data storage within India under Unified Access Service Licence conditions.</li>"
         "<li><strong>IRDAI (insurance)</strong>: policyholder data in India; cloud hosting restrictions.</li>"
         "<li><strong>Health Ministry / specific health IT framework</strong>: Ayushman Bharat / electronic health records residency rules.</li>"
         "</ul>"
         "<p>Foreign SaaS / fintech must map data types to applicable regulator and architect data residency accordingly.</p>"),
        ("/ RBI payment data localisation", "The strictest.",
         "<ul>"
         "<li><strong>April 2018 circular</strong>: 'all system providers shall ensure that the entire data relating to payment systems operated by them are stored in a system only in India'.</li>"
         "<li><strong>'Payment data'</strong> definition: user data at various stages of payment flow &mdash; customer data, payment sensitive data (card number, CVV, OTP, device data), transaction data (location, origin, destination, timestamp), beneficiary data.</li>"
         "<li><strong>Entities covered</strong>: payment system providers &mdash; banks, non-bank payment system operators (PPI, PA, PG, card networks), payment service providers, international payment networks (Visa, Mastercard, Amex), payment system intermediaries, FinTechs offering payment-related services.</li>"
         "<li><strong>Entire data</strong>: 'end-to-end transaction data'. Full data stored in India; if processed abroad, the data must be deleted there and brought back to India, which RBI's FAQs expect within one business day or 24 hours of payment processing, whichever is earlier.</li>"
         "<li><strong>Audit + reporting</strong>: RBI empanelled CERT-In auditor annual system audit confirming localisation; findings reported to RBI.</li>"
         "<li><strong>Non-compliance</strong>: suspension of payment operations in India. Severe operational risk.</li>"
         "</ul>"),
        ("/ Architectural implications", "What foreign SaaS builds.",
         "<ul>"
         "<li><strong>Hybrid architecture</strong>: India-hosted stack for Indian users + global stack for non-Indian users. Common pattern: Indian AWS Mumbai / Google India / Azure India region for user-facing stack; global edge for non-regulated functions (CDN, analytics without PII).</li>"
         "<li><strong>India-only database replicas</strong>: primary + replica in India regions; no cross-region replication to non-India regions for regulated data.</li>"
         "<li><strong>India-specific tenant / shard</strong>: multi-tenant SaaS with Indian tenants on Indian infrastructure.</li>"
         "<li><strong>Data access controls</strong>: non-India engineers can SEE anonymised / aggregated data; cannot access raw regulated data stored in India.</li>"
         "<li><strong>Processing abroad with deletion</strong>: temporarily permissible to process payment data abroad (e.g., fraud scoring at global data centre) but must delete processed copy after processing complete.</li>"
         "<li><strong>End-to-end audit trail</strong>: logs showing where regulated data was stored / processed / accessed at every stage.</li>"
         "<li><strong>Encryption</strong>: at rest + in transit, with India-held keys for Indian regulated data.</li>"
         "</ul>"),
        ("/ Compliance workflow", "What foreign SaaS does.",
         "<ol>"
         "<li><strong>Data classification</strong>: identify which data categories are regulated (payment data, personal data under DPDP, SEBI records, telecom subscriber, insurance policyholder, health records).</li>"
         "<li><strong>Data map</strong>: document where each category is stored, processed, accessed, retained.</li>"
         "<li><strong>Architecture gap analysis</strong>: identify where current architecture doesn't match localisation requirements.</li>"
         "<li><strong>India infrastructure setup</strong>: AWS/GCP/Azure India regions; India-held encryption keys; India-based disaster recovery.</li>"
         "<li><strong>Data processing agreements</strong>: with Indian processors; cross-border transfer SCCs where applicable (post DPDP Section 16 notifications).</li>"
         "<li><strong>Compliance audit</strong>: CERT-In empanelled auditor annual audit for payment data; sector-specific audits as applicable.</li>"
         "<li><strong>Reporting</strong>: RBI quarterly / annual reports; DPDP breach notifications; sector regulator reports.</li>"
         "<li><strong>Ongoing monitoring</strong>: data access logs, incident response, periodic re-classification.</li>"
         "</ol>"),
        ("/ Common foreign-SaaS mistakes", "Avoidable breaches.",
         "<ul>"
         "<li><strong>Global SaaS stack with India users</strong>: AWS US East holds all data including Indian users. Payment data breach if any payment data flows there.</li>"
         "<li><strong>Analytics with PII to foreign CRM</strong>: Indian user events (clicks, impressions, demographic) streamed to Mixpanel / Segment / Amplitude without PII removal.</li>"
         "<li><strong>Email providers abroad</strong>: Indian user emails sent via Mailgun / SendGrid / Postmark US &mdash; email content touches foreign servers.</li>"
         "<li><strong>Customer support tools</strong>: Zendesk / Intercom / Freshdesk tickets with Indian user data stored outside India.</li>"
         "<li><strong>Payroll / HR</strong>: BambooHR / Rippling with Indian employee data stored outside India (though HR data less strictly regulated).</li>"
         "<li><strong>Backup / DR to foreign regions</strong>: snapshot backup to non-India region containing regulated data.</li>"
         "<li><strong>Not storing audit logs in India</strong>: logs showing user actions = user data = may need India storage.</li>"
         "</ul>"
         "<p>These are breaches only where the data is regulated (payment data under RBI, or sector records under SEBI, IRDAI or telecom licences). For ordinary personal data, the DPDP Act currently allows transfers abroad - no country has been restricted - subject to its consent, security and breach duties. Each case needs an architectural review.</p>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Does India have a general data localisation law?",
         "No single unified law. Instead layered regime: RBI payment data localisation (April 2018, mandatory India-only), DPDP Act Section 16 country blocklist (no notifications yet 2026), sector-specific rules (SEBI, TRAI, IRDAI, health). Foreign SaaS must map data types to applicable regulator and architect data residency accordingly."),
        ("What exactly is 'payment data' under RBI localisation?",
         "User data at various stages of payment flow: customer data (name, address, device), payment sensitive data (card number, CVV, OTP), transaction data (location, origin, destination, timestamp), beneficiary data. End-to-end payment transaction data. Entire data must be stored only in India for payment system operators, PAs, PGs, PPIs, card networks, fintechs offering payment-related services."),
        ("Can I temporarily process payment data abroad for fraud scoring?",
         "Yes - temporary processing abroad is permitted but processed copy must be deleted after processing complete. End-state storage must be India-only. In practice: fraud scoring data flows abroad for ML inference, then is deleted; India-stored transaction record remains. Audit trail must document this flow."),
        ("How does DPDP Section 16 affect cross-border data transfer?",
         "Blocklist approach: Central Government may notify specific countries where personal data of Indian residents may NOT be transferred. Currently no restrictions notified (2026). Prudent approach: document cross-border flows, DPAs with foreign processors, India-side data residency for sensitive sectors, prepare for future restrictions if notified."),
        ("What are the typical architectural patterns for Indian data localisation?",
         "Hybrid architecture: AWS/GCP/Azure India regions for Indian users; global stack for non-Indian users. India-only database replicas (no cross-region to non-India for regulated data). Multi-tenant with Indian tenants on Indian infrastructure. India-held encryption keys. Non-India engineers can access anonymised data but not raw regulated data. India-based disaster recovery."),
        ("Does BQP help foreign SaaS / fintech with India data localisation compliance?",
         "Yes - data classification + mapping, architecture gap analysis, India infrastructure structuring, DPA + SCC drafting, CERT-In empanelled auditor coordination, RBI reporting, DPDP compliance integration. Co-ordinated with foreign client's engineering + security teams + global privacy counsel. Scope-based engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("dpdp-act-india-foreign-company-compliance-2026.html", "Guide", "DPDP Act"),
        ("india-payment-aggregator-pa-pg-licence-foreign-fintech.html", "Guide", "RBI PA Licence"),
    ],
    cta_headline="Foreign SaaS / fintech with Indian user or payment data?",
    cta_body="Multi-regulator localisation regime: RBI + DPDP + sector-specific. BQP: classification + architecture gap analysis + India infrastructure + audit + reporting. Scope-based engagement.",
))

# 15. PLI scheme
write_page("india-pli-scheme-foreign-manufacturer-2026", page(
    slug="india-pli-scheme-foreign-manufacturer-2026",
    title="India PLI Scheme for Foreign Manufacturer 2026 | Production-Linked Incentive - BQP",
    description="India PLI (Production-Linked Incentive) schemes for foreign manufacturers 2026: 14 sectors (electronics, pharma, auto, solar, semiconductors, textiles, food processing, telecom, white goods, drone, specialty steel, battery, medical devices, aluminium), eligibility, investment thresholds, cash incentive 4-6% of incremental sales, 5-year scheme period. Complete 2026 guide. CA Durgesh Chavda.",
    keywords="India PLI scheme foreign manufacturer, Production Linked Incentive India 2026, India electronics PLI semiconductor PLI, India PLI eligibility application, India manufacturing incentive foreign company",
    hero_kicker="/ Foreign Clients &middot; PLI Scheme &middot; Updated 2026-10-15",
    hero_title_html="India PLI schemes, <em>cash incentive for foreign manufacturers.</em>",
    hero_lead="India launched Production-Linked Incentive (PLI) schemes starting 2020 covering 14 strategic sectors. Foreign manufacturers establishing Indian production can receive cash incentive of 4-6% of incremental sales over base year, paid in cash over 5-year scheme period. Combined with Section 115BAB 15% corporate tax for new manufacturing, India offers one of the most generous manufacturing-destination incentive stacks globally. Here's the complete 2026 framework.",
    sections=[
        ("/ Overview of 14 PLI sectors", "What's covered.",
         "<p>PLI schemes launched sector-wise 2020-2024. Each with separate budget, incentive rate, eligibility threshold, nodal ministry:</p>"
         "<ul>"
         "<li><strong>1. Mobile Phones + Specified Electronic Components</strong>: nodal MeitY. Incentive 4-6%. Beneficiaries: Foxconn, Pegatron, Wistron (now Tata), Samsung, Dixon, Lava.</li>"
         "<li><strong>2. Pharmaceuticals</strong>: nodal DoP. 5-10% incentive. KSMs (Key Starting Materials) + Drug Intermediates + APIs + Formulations.</li>"
         "<li><strong>3. Automobile + Auto Components</strong>: nodal MHI. 18% incentive on advanced products.</li>"
         "<li><strong>4. Solar PV Modules</strong>: nodal MNRE. 5-10% incentive. Fully integrated manufacturing (polysilicon to module).</li>"
         "<li><strong>5. Advanced Chemistry Cell (ACC) Battery</strong>: nodal DHI. Up to USD 2.5B subsidy over 5 years.</li>"
         "<li><strong>6. Electronic Semiconductor + Display</strong>: India Semiconductor Mission (ISM) &mdash; up to 50% capex subsidy under Modified SPECS + DLI.</li>"
         "<li><strong>7. Specialty Steel</strong>: nodal MoS. 4-12% incentive.</li>"
         "<li><strong>8. Textiles (MMF + Technical Textiles)</strong>: nodal MoT. 4-24% incentive.</li>"
         "<li><strong>9. Food Processing</strong>: nodal MoFPI. 4-10% incentive.</li>"
         "<li><strong>10. Telecom + Networking Products</strong>: nodal DoT. 4-7% incentive.</li>"
         "<li><strong>11. White Goods (AC + LED)</strong>: nodal DPIIT. 4-6% incentive.</li>"
         "<li><strong>12. Drones + Drone Components</strong>: nodal MoCA. 20% incentive for drone components.</li>"
         "<li><strong>13. IT Hardware (Laptop + Tablet + AIO PC + Server)</strong>: nodal MeitY. 5% incentive.</li>"
         "<li><strong>14. Medical Devices</strong>: nodal DoP. 5% incentive.</li>"
         "</ul>"
         "<p>Expanded sectors under consideration (2026): shipbuilding, chemicals, leather, toys.</p>"),
        ("/ Standard PLI structure", "The common framework.",
         "<ul>"
         "<li><strong>Base year</strong>: FY immediately preceding scheme announcement; manufacturer's sales in base year is baseline.</li>"
         "<li><strong>Incentive calculation</strong>: X% of incremental sales (over base year) achieved in scheme years.</li>"
         "<li><strong>Scheme period</strong>: typically 5 years from first year of production under scheme.</li>"
         "<li><strong>Investment threshold</strong>: sector-specific minimum capex (e.g., mobile phones: INR 150 crore medium / INR 1,000 crore large; semiconductors: much higher).</li>"
         "<li><strong>Sales threshold</strong>: minimum incremental sales targeted year-on-year.</li>"
         "<li><strong>Local value addition</strong>: percentage of value added in India must increase over scheme period.</li>"
         "<li><strong>Direct employment generation</strong>: specific threshold per sector.</li>"
         "<li><strong>Cash disbursement</strong>: quarterly or annual claim; disbursed via respective ministry.</li>"
         "<li><strong>Compliance</strong>: project monitoring agency (PwC / EY / Deloitte / KPMG empanelled) verifies claims.</li>"
         "</ul>"),
        ("/ Combined incentive stack for foreign manufacturer", "The total value.",
         "<ul>"
         "<li><strong>Section 115BAB (15% corporate tax)</strong>: new manufacturing company incorporated post Oct 2019, commence production by extended date, pure manufacturing (no re-labelling/packing). Effective 17.16% (15% + surcharge + cess) vs standard 25% / 22% under 115BAA. See our <a href='section-115baa-115bab-corporate-tax-regime-india.html'>115BAB guide</a>.</li>"
         "<li><strong>PLI cash incentive</strong>: 4-6% of incremental sales for 5 years.</li>"
         "<li><strong>Customs duty optimisation</strong>: PMP (Phased Manufacturing Programme) + specific inverted-duty structures favour local manufacturing.</li>"
         "<li><strong>State-level incentives</strong>: additional state-industrial-policy benefits (land subsidies, electricity rebates, SGST reimbursement). Varies by state &mdash; Gujarat, Tamil Nadu, Karnataka, Maharashtra most proactive.</li>"
         "<li><strong>SEZ benefits</strong>: if SEZ-based unit, additional Section 10AA deduction (but note: 115BAB forfeits 10AA).</li>"
         "<li><strong>CGST / IGST refund</strong>: for export-oriented manufacturers.</li>"
         "<li><strong>Modified SPECS / DLI (semiconductors)</strong>: up to 50% capex subsidy for chip fabs under India Semiconductor Mission.</li>"
         "</ul>"
         "<p>Total stack can equate to 15-30% capex subsidy + 5-7% operating subsidy equivalent &mdash; among the most generous globally.</p>"),
        ("/ Application + ongoing compliance workflow", "The 2-year execution.",
         "<ol>"
         "<li><strong>Sector-specific scheme guidelines review</strong>: eligibility, thresholds, investment commitment, local value add targets.</li>"
         "<li><strong>Indian subsidiary setup</strong>: WOS as foreign manufacturing arm. See <a href='foreign-company-setup-indian-subsidiary-wos.html'>WOS guide</a>.</li>"
         "<li><strong>Section 115BAB opt-in</strong>: Form 10-ID with Indian ITR of first year.</li>"
         "<li><strong>Project proposal</strong>: capex plan + sales forecast + local value add trajectory + employment plan.</li>"
         "<li><strong>Application to nodal ministry</strong>: formal application with proposal + supporting documents.</li>"
         "<li><strong>Approval + Letter of Approval (LoA)</strong>: nodal ministry issues LoA specifying thresholds + incentive rate.</li>"
         "<li><strong>Project execution</strong>: build facility, commence production, hit sales targets.</li>"
         "<li><strong>Base year audit</strong>: establish baseline sales.</li>"
         "<li><strong>Annual / quarterly claim</strong>: submit claim with sales + investment + employment data verified by project monitoring agency.</li>"
         "<li><strong>Disbursement</strong>: cash incentive paid by nodal ministry.</li>"
         "<li><strong>Ongoing compliance</strong>: annual reporting, local value add tracking, employment reporting, variance explanations.</li>"
         "</ol>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What is India's PLI scheme?",
         "Production-Linked Incentive - sector-specific schemes offering cash incentive to manufacturers for incremental production in India. Launched 2020-2024 across 14 strategic sectors (electronics, pharma, auto, solar, semiconductors, textiles, food processing, telecom, white goods, drones, IT hardware, medical devices, specialty steel, batteries). Incentive 4-6% (standard) to 10-18% (strategic) of incremental sales over base year, paid in cash over 5-year scheme period."),
        ("Can a foreign manufacturer apply for PLI?",
         "Yes - via Indian subsidiary (WOS). Foreign parent incorporates Indian Pvt Ltd, meets sector-specific investment + sales thresholds, applies to respective nodal ministry (MeitY for electronics, DoP for pharma, MHI for auto, MNRE for solar, etc.). Approval via Letter of Approval (LoA) specifying thresholds + incentive rate. Co-ordinate PLI with Section 115BAB 15% corporate tax for maximum benefit stack."),
        ("Which PLI sectors are most attractive for foreign manufacturers in 2026?",
         "Mobile phones (established scheme, major foreign players), semiconductors (India Semiconductor Mission 50% capex subsidy), ACC battery (USD 2.5B subsidy pool), auto components (18% incentive for advanced products), drone components (20%), IT hardware (laptop + tablet + server, 5%). Choose based on sector match + capex capacity + strategic India commitment horizon."),
        ("What's the combined incentive stack for foreign manufacturers in India?",
         "Section 115BAB (15% corporate tax, effective 17.16%) + PLI cash incentive 4-6% of incremental sales + State-level incentives (land, electricity, SGST reimbursement) + Customs duty optimisation + Semiconductor-specific capex subsidy up to 50% under ISM. Total equates to 15-30% capex subsidy + 5-7% operating subsidy - among the most generous manufacturing incentive stacks globally."),
        ("How long does PLI application + approval take?",
         "3-9 months typical from application to Letter of Approval (LoA). Then project execution (12-24 months) to commence production. First PLI disbursement in year 1 of production. 5-year scheme period from first production year. Total engagement window from application to final disbursement: 6-7 years."),
        ("Does BQP handle PLI applications for foreign manufacturers?",
         "Yes - end-to-end: sector eligibility analysis, Indian subsidiary setup, Section 115BAB co-ordination, project proposal + financial model, application to nodal ministry, LoA negotiation, annual/quarterly claim submission with project monitoring agency verification, state-level incentive co-ordination, ongoing compliance. Co-ordinated with Indian regulatory counsel + state industrial development authority. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-115baa-115bab-corporate-tax-regime-india.html", "Guide", "Section 115BAB"),
        ("india-market-entry-foreign-company-guide.html", "Guide", "India Market Entry"),
    ],
    cta_headline="Foreign manufacturer evaluating India for production base?",
    cta_body="PLI + 115BAB + state incentives = 15-30% capex + 5-7% opex subsidy stack. BQP end-to-end: sector + state + 115BAB + PLI application + ongoing compliance.",
))

# 16. Space FDI
write_page("india-space-fdi-100-automatic-route-2024-reform-2026", page(
    slug="india-space-fdi-100-automatic-route-2024-reform-2026",
    title="India Space FDI 100% Automatic Route 2024-2026 | Foreign Company - BQP",
    description="India space sector FDI reform February 2024: 100% automatic route for satellite components / ground segment / user segment; 74% automatic (26% approval) for satellite launch vehicles + sub-systems; 49% automatic (51% approval) for satellite operations. Foreign company entry into Indian space, SpaceCom Policy 2023, IN-SPACe authorisation. 2026 guide. CA Durgesh Chavda.",
    keywords="India space FDI 100 automatic route foreign, India space reform 2024 FDI, IN-SPACe authorisation foreign, SpaceCom Policy 2023, India satellite FDI foreign company",
    hero_kicker="/ Foreign Clients &middot; Space FDI &middot; Updated 2026-10-15",
    hero_title_html="India space sector FDI, <em>100% automatic for most activities post 2024.</em>",
    hero_lead="February 2024 FDI reform opened India's space sector dramatically. 100% FDI via automatic route for satellite components, ground segment, user segment. 74% automatic (balance via approval route) for satellite launch vehicles + sub-systems. 49% automatic (balance via approval) for satellite operations. Combined with SpaceCom Policy 2023 + IN-SPACe authorisation framework, foreign space / satellite companies can now establish Indian presence relatively easily. Here's the complete 2026 framework.",
    sections=[
        ("/ The February 2024 FDI reform", "What changed.",
         "<p>Previous regime (pre-Feb 2024): all FDI in space sector required prior government approval. Severely constrained foreign participation.</p>"
         "<p><strong>New regime (post Feb 2024 Cabinet decision)</strong>:</p>"
         "<ul>"
         "<li><strong>Sub-activity 1: Satellites - Manufacturing + Operations</strong></li>"
         "<li>&nbsp;&nbsp;&mdash; Up to 74% FDI: automatic route.</li>"
         "<li>&nbsp;&nbsp;&mdash; Beyond 74%: Government approval route.</li>"
         "<li><strong>Sub-activity 2: Launch Vehicles + Associated Systems / Sub-systems + Creation of Spaceports</strong></li>"
         "<li>&nbsp;&nbsp;&mdash; Up to 49% FDI: automatic route.</li>"
         "<li>&nbsp;&nbsp;&mdash; Beyond 49%: Government approval route.</li>"
         "<li><strong>Sub-activity 3: Manufacturing of components + sub-systems for satellites, ground segment + user segment</strong></li>"
         "<li>&nbsp;&nbsp;&mdash; Up to 100% FDI: automatic route.</li>"
         "</ul>"
         "<p>This is a transformational shift. The 100% automatic route for components + ground segment + user segment opens the entire space-tech ecosystem to foreign capital without any government approval delay.</p>"),
        ("/ SpaceCom Policy 2023 - the enabling framework", "The regulatory architecture.",
         "<ul>"
         "<li><strong>Indian Space Policy 2023</strong>: declared in April 2023, replaced ad-hoc space regulations. Objective: enhance private sector participation in Indian space activities.</li>"
         "<li><strong>Players recognised</strong>: ISRO (strategic + national missions), NSIL (New Space India Limited, commercial arm), IN-SPACe (regulator / enabler for private sector), and now Non-Governmental Entities (NGEs) &mdash; private companies, foreign-owned Indian companies.</li>"
         "<li><strong>IN-SPACe (Indian National Space Promotion and Authorization Centre)</strong>: autonomous body under Department of Space, authorises + licenses private sector space activity.</li>"
         "<li><strong>Scope of activity</strong>: launch services, satellite manufacturing + operation, remote sensing, satellite communication (Satcom), navigation, space transportation, in-space transportation + servicing, ground stations, remote sensing data analytics.</li>"
         "<li><strong>NGE registration</strong>: with IN-SPACe for private space activities.</li>"
         "</ul>"),
        ("/ Pathways for foreign space company into India", "Entry structures.",
         "<p><strong>Route 1: 100% WOS for components / ground segment / user segment</strong></p>"
         "<ul>"
         "<li>Fastest route. Automatic FDI route &mdash; no prior approval.</li>"
         "<li>Suitable for: satellite component manufacturing (sensors, electronics, propulsion), ground stations, remote sensing data analytics, Satcom user terminals, ground segment software.</li>"
         "<li>Standard WOS incorporation + Section 115BAB for new manufacturing.</li>"
         "<li>See our <a href='foreign-company-setup-indian-subsidiary-wos.html'>WOS guide</a>.</li>"
         "</ul>"
         "<p><strong>Route 2: 74% FDI JV with Indian partner for satellite manufacturing + operations</strong></p>"
         "<ul>"
         "<li>Up to 74% foreign ownership automatic; 26% Indian partner.</li>"
         "<li>Beyond 74% requires Government approval.</li>"
         "<li>Suitable for: full satellite manufacturing (not just components), satellite operations (ownership + management of orbital assets).</li>"
         "<li>Indian partner typically brings regulatory relationships + local supply chain.</li>"
         "</ul>"
         "<p><strong>Route 3: 49% FDI JV for launch vehicles + spaceports</strong></p>"
         "<ul>"
         "<li>Up to 49% automatic; majority Indian (strategic sector).</li>"
         "<li>Beyond 49% requires Government approval + strategic sector review.</li>"
         "<li>Suitable for: rocket / launch vehicle development + manufacturing + spaceport operations.</li>"
         "</ul>"
         "<p>In addition to FDI structuring, foreign company must obtain IN-SPACe authorisation for actual space activity.</p>"),
        ("/ IN-SPACe authorisation workflow", "The licensing layer.",
         "<ol>"
         "<li><strong>NGE registration</strong> with IN-SPACe (one-time); establishes identity of foreign-owned Indian entity.</li>"
         "<li><strong>Activity-specific authorisation application</strong>: launch vehicle authorisation, satellite authorisation, ground station authorisation, remote sensing authorisation, Satcom authorisation, in-space activity authorisation.</li>"
         "<li><strong>Documentation</strong>: technical specifications, safety assessment, debris mitigation plan, orbital allocation (if applicable), environmental assessment, financial capability.</li>"
         "<li><strong>IN-SPACe review</strong>: technical + legal + safety + strategic review; may involve DoS / ISRO co-ordination.</li>"
         "<li><strong>Authorisation grant</strong>: 6-18 months typical. Specifies activity scope, conditions, duration.</li>"
         "<li><strong>Ongoing compliance</strong>: periodic reporting, operational safety reviews, debris mitigation evidence, insurance maintenance.</li>"
         "</ol>"
         "<p><strong>Insurance</strong>: third-party liability for launch + operations typically mandatory under IN-SPACe conditions. Specific insurance capacity requirements.</p>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What changed in India's space FDI policy in February 2024?",
         "Dramatic liberalisation: 100% FDI via automatic route for satellite components, ground segment, user segment (previously all required Government approval). 74% automatic for satellite manufacturing + operations; 49% automatic for launch vehicles + spaceports. Beyond these thresholds, Government approval required. First major space FDI liberalisation in Indian history. Combined with SpaceCom Policy 2023 + IN-SPACe authorisation framework, foreign space-tech participation now substantially enabled."),
        ("Can a foreign satellite company own 100% of an Indian satellite subsidiary?",
         "Component / ground segment / user segment manufacturing: yes, 100% FDI automatic. Satellite manufacturing + operations: up to 74% automatic (26% Indian partner required or beyond 74% needs Government approval). Launch vehicles + spaceports: up to 49% automatic (majority Indian partner required). Decide structure based on actual scope of activity."),
        ("What is IN-SPACe and why does it matter?",
         "Indian National Space Promotion and Authorization Centre - autonomous body under Department of Space, established 2020. Authorises + licenses private sector space activity in India. Any foreign-owned Indian space company must register with IN-SPACe as NGE (Non-Governmental Entity) and obtain activity-specific authorisation for launch, satellite operations, ground station, remote sensing, Satcom etc. Separate from (and in addition to) FDI approval."),
        ("How does India's space FDI liberalisation compare globally?",
         "India now more open than many major space nations in several categories. US, China, Russia maintain strategic restrictions on foreign satellite + launch vehicle ownership. EU + UK + Australia more open but with security review for strategic activities. India's 100% automatic route for components / ground segment / user segment is among the most liberal globally in those categories."),
        ("Can foreign space company combine PLI benefits with space FDI?",
         "Partially - no direct space-sector PLI yet, but satellite components + ground stations + user segment components may qualify under adjacent sector PLIs: Electronics PLI (satellite electronics), Semiconductor Mission (chip-level), Drone PLI (certain satellite tech). Standard incentive stack: Section 115BAB 15% corporate tax + state-level incentives + customs optimisation available regardless of PLI."),
        ("Does BQP handle India entry for foreign space / satellite companies?",
         "Yes - specialised foreign-space-sector advisory. FDI structuring (100% / 74% / 49% route selection), Indian subsidiary setup (WOS or JV), Section 115BAB opt-in, IN-SPACe NGE registration + activity authorisation application, insurance capacity structuring, state-level incentive co-ordination (Gujarat, Tamil Nadu, Karnataka proactive), ongoing compliance. Co-ordinated with Indian space-regulatory counsel. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-telecom-fdi-100-automatic-2024.html", "Guide", "Telecom FDI"),
        ("foreign-company-setup-indian-subsidiary-wos.html", "Guide", "WOS Setup"),
    ],
    cta_headline="Foreign space / satellite / ground-station company evaluating India?",
    cta_body="100% automatic FDI for most activities post Feb 2024. IN-SPACe authorisation + Section 115BAB + state incentives. BQP end-to-end: structure + registration + authorisation + ongoing compliance.",
))

# 17. Telecom FDI
write_page("india-telecom-fdi-100-automatic-2024", page(
    slug="india-telecom-fdi-100-automatic-2024",
    title="India Telecom FDI 100% Automatic Route 2024-2026 | Foreign Company - BQP",
    description="India telecom sector FDI post 2024 reform: 100% FDI via automatic route (previously 49% automatic + 100% approval). Telecom licence framework, spectrum policy, Unified Licence (Access + ISP + Infrastructure), network equipment PLI, data localisation + CERT-In compliance. Complete guide for foreign telecom entry. CA Durgesh Chavda.",
    keywords="India telecom FDI 100 automatic 2024, India telecom reform foreign company, Unified Licence India foreign, India spectrum FDI, foreign telecom India entry",
    hero_kicker="/ Foreign Clients &middot; Telecom FDI &middot; Updated 2026-10-15",
    hero_title_html="India telecom sector FDI, <em>100% automatic post 2024.</em>",
    hero_lead="India telecom FDI was liberalised to 100% via automatic route in 2021 (replacing earlier 49% automatic + up to 100% via approval). The reform combined with Telecommunications Act 2023, revised Unified Licence framework, PLI for telecom equipment, and 5G rollout creates a transformed landscape for foreign telecom companies. Here's the complete 2026 entry framework.",
    sections=[
        ("/ The 100% FDI automatic reform", "What's now permitted.",
         "<ul>"
         "<li><strong>Pre-2021</strong>: Telecom sector allowed FDI up to 49% via automatic route; 49-100% via Government approval route. Significant delay for majority foreign-owned telecom.</li>"
         "<li><strong>Post 2021 (DoT/MeitY notification)</strong>: 100% FDI via automatic route for telecom services. No prior approval required.</li>"
         "<li><strong>Reaffirmed by Telecommunications Act 2023</strong>: new consolidated telecom law effective 2024; FDI framework carried forward.</li>"
         "<li><strong>Impact</strong>: Vodafone recapitalisation, Jio's international partnerships, foreign backbone operators + hyperscalers (AWS, Microsoft, Google) acquiring Indian telecom-adjacent assets, satellite ISP (Starlink, Kuiper) permitted.</li>"
         "<li><strong>Sectoral scope</strong>: telecom services (voice, data, SMS), Internet Service Provider (ISP), telecom infrastructure (towers, cables, satellite), telecom equipment manufacturing.</li>"
         "</ul>"),
        ("/ Telecommunications Act 2023 - the new framework", "What it covers.",
         "<ul>"
         "<li><strong>Enacted December 2023</strong>; effective from 2024. Replaces Indian Telegraph Act 1885 + Indian Wireless Telegraphy Act 1933 + Telegraph Wires (Unlawful Possession) Act 1950.</li>"
         "<li><strong>Unified Licence (UL)</strong>: single licensing framework covering Access Service, ISP, National Long Distance (NLD), International Long Distance (ILD), Infrastructure Provider (IP-II), Mobile Virtual Network Operator (MVNO), Audio Conferencing, Public Mobile Radio Trunking Service (PMRTS). Entry fee + annual licence fee variable.</li>"
         "<li><strong>Spectrum policy</strong>: administrative allocation for strategic/government uses; auction for commercial. 5G spectrum auction 2022; 6G readiness being established.</li>"
         "<li><strong>Right of way</strong>: standardised framework for cable laying + tower setting; coordinates with state/municipal RoW rules.</li>"
         "<li><strong>User protection</strong>: strict consent-based commercial communication (TRAI DND); privacy integrated with DPDP Act.</li>"
         "<li><strong>Interception + emergency powers</strong>: Section 20 permits government interception under specified conditions.</li>"
         "<li><strong>Satellite spectrum</strong>: administratively allocated (not auctioned) &mdash; distinguishing feature favouring satellite operators.</li>"
         "</ul>"),
        ("/ Entry structures for foreign telecom", "Three routes.",
         "<p><strong>Route 1: Full telecom operator (ISP + Access Service)</strong></p>"
         "<ul>"
         "<li>Indian WOS incorporated under Companies Act.</li>"
         "<li>Apply for Unified Licence from Department of Telecommunications (DoT).</li>"
         "<li>Entry fee + Performance Bank Guarantee + Financial Bank Guarantee.</li>"
         "<li>Compliance: lawful interception facility, security compliance (DoT Security Guidelines), CERT-In empanelled audit, DPDP compliance.</li>"
         "<li>Spectrum (if required): auction participation.</li>"
         "<li>Timeline: 12-24 months from incorporation to operational.</li>"
         "</ul>"
         "<p><strong>Route 2: Infrastructure Provider (IP-II)</strong></p>"
         "<ul>"
         "<li>Passive infrastructure &mdash; towers, dark fibre, dense cities, in-building.</li>"
         "<li>Simpler licensing framework.</li>"
         "<li>No spectrum obligation.</li>"
         "<li>Entity rents infrastructure to telecom operators.</li>"
         "</ul>"
         "<p><strong>Route 3: Satellite internet / Satcom</strong></p>"
         "<ul>"
         "<li>DoT satellite ISP licence + IN-SPACe authorisation for satellite operation.</li>"
         "<li>Starlink, OneWeb, Project Kuiper working through this route.</li>"
         "<li>Administrative spectrum allocation (vs auction for terrestrial).</li>"
         "<li>Coordinated with SpaceCom Policy 2023.</li>"
         "</ul>"),
        ("/ Compliance stack for foreign telecom", "What ongoing.",
         "<ul>"
         "<li><strong>DoT Security Guidelines</strong>: equipment must be from trusted sources (National Security Directive on Telecommunications Sector); specific country / vendor restrictions apply.</li>"
         "<li><strong>Lawful interception</strong>: operator must maintain lawful interception facility; co-ordinate with Indian LEAs on security matters.</li>"
         "<li><strong>Subscriber verification</strong>: strict Know Your Customer (eKYC via Aadhaar / alternative) + address verification.</li>"
         "<li><strong>Data localisation</strong>: subscriber data + traffic data in India per DoT + DPDP + CERT-In requirements. See our <a href='india-data-localisation-rbi-dpdp-foreign-saas.html'>data localisation guide</a>.</li>"
         "<li><strong>CERT-In directions</strong>: 6-hour breach reporting; audit log retention.</li>"
         "<li><strong>DPDP compliance</strong>: subscriber as data principal; consent + rights framework.</li>"
         "<li><strong>Spectrum compliance</strong>: periodic payment of annual spectrum charges + rollout obligations.</li>"
         "<li><strong>Licence fee</strong>: 8% of Adjusted Gross Revenue (AGR) &mdash; the famous AGR concept.</li>"
         "<li><strong>USO (Universal Service Obligation) Fund</strong>: 5% of AGR contribution.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Can a foreign telecom company own 100% of an Indian telecom operator?",
         "Yes - 100% FDI via automatic route since 2021 (reaffirmed by Telecommunications Act 2023). No prior Government approval needed for ownership. However: operational licence (Unified Licence from DoT) + security compliance (Security Guidelines, Lawful Interception) + spectrum (via auction for terrestrial) + DPDP + CERT-In compliance all apply equally to foreign-owned Indian telecom operators."),
        ("What is India's Unified Licence (UL)?",
         "Single licensing framework replacing earlier separate licences. Covers Access Service, ISP, NLD, ILD, Infrastructure Provider (IP-II), MVNO, Audio Conferencing, PMRTS. Entry fee + annual Licence Fee (8% of Adjusted Gross Revenue) + Performance Bank Guarantee + Financial Bank Guarantee. Single licence authorises multiple services; chose service authorisations within the UL at application. Simpler than pre-2013 fragmented licensing."),
        ("Is foreign satellite internet (Starlink, OneWeb) permitted in India?",
         "Yes - permitted via DoT satellite ISP licence + IN-SPACe authorisation for satellite operation + spectrum (administratively allocated for satellite, vs auction for terrestrial). Starlink + OneWeb + Project Kuiper working through this route. India's 2024 Space FDI reform (100% automatic for components, 74% for operations) + Telecom 100% automatic FDI enables full foreign-owned satellite internet operators."),
        ("What's AGR (Adjusted Gross Revenue) in Indian telecom?",
         "Revenue measure on which Licence Fee (8%) + USO contribution (5%) + Spectrum Usage Charge are calculated. Famous for its broad interpretation by Supreme Court (2019 ruling) including non-telecom revenues like interest + capital gains + handset sales - caused massive demands on operators. Legislatively being narrowed over time but remains financially significant for Indian telecom operators."),
        ("What are DoT Security Guidelines for foreign telecom equipment?",
         "National Security Directive on Telecommunications Sector (2021 + updates): equipment must be from 'trusted sources'. DoT maintains list of trusted vendors + list of concern countries (effectively restricting equipment from specific country of origin). Foreign-owned Indian telecom operator must comply - affects equipment sourcing decisions. Specific procurement + certification processes."),
        ("Does BQP handle India entry for foreign telecom companies?",
         "Yes - specialised telecom advisory. FDI structuring (100% automatic path), Indian subsidiary (WOS) setup, DoT Unified Licence application, Security Guidelines compliance, Lawful Interception setup, DPDP + CERT-In compliance, spectrum auction co-ordination, state-level RoW co-ordination, ongoing AGR + USO + spectrum compliance. Co-ordinated with Indian telecom regulatory counsel. Scope-based engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-space-fdi-100-automatic-route-2024-reform-2026.html", "Guide", "Space FDI"),
        ("india-data-localisation-rbi-dpdp-foreign-saas.html", "Guide", "Data Localisation"),
    ],
    cta_headline="Foreign telecom / ISP / satellite operator evaluating India?",
    cta_body="100% FDI automatic since 2021 + Telecommunications Act 2023 + Unified Licence framework. BQP end-to-end: FDI + licence + security compliance + spectrum + ongoing operations.",
))

# 18. UPI Integration
write_page("india-upi-integration-foreign-fintech", page(
    slug="india-upi-integration-foreign-fintech",
    title="India UPI Integration for Foreign Fintech 2026 | TPAP / PA / International UPI - BQP",
    description="India UPI integration pathways for foreign fintech 2026: Third-Party Application Provider (TPAP) via sponsor bank, Payment Aggregator with UPI handle, UPI-PayNow / UPI-Lanka / international UPI linkages, NPCI onboarding, bank partnership, DPDP + RBI compliance. Complete guide. CA Durgesh Chavda.",
    keywords="India UPI integration foreign fintech, UPI TPAP sponsor bank, international UPI linkage, UPI PayNow Singapore India, NPCI onboarding foreign",
    hero_kicker="/ Foreign Clients &middot; UPI Integration &middot; Updated 2026-10-15",
    hero_title_html="India UPI integration, <em>four pathways for foreign fintech.</em>",
    hero_lead="UPI (Unified Payments Interface) is India's dominant payment system &mdash; 10+ billion transactions / month. Foreign fintech wanting UPI integration has four main pathways: TPAP via sponsor bank, Payment Aggregator with UPI handle, international UPI linkage, or indirect via Indian merchant partnerships. Each has different regulatory requirements. Here's the complete 2026 framework.",
    sections=[
        ("/ UPI stack overview", "Who does what.",
         "<ul>"
         "<li><strong>NPCI (National Payments Corporation of India)</strong>: operates UPI infrastructure. Umbrella organisation of Indian banks. Non-profit regulated by RBI.</li>"
         "<li><strong>Payer Bank</strong>: user's bank holding funds; receives UPI payment request.</li>"
         "<li><strong>Payee Bank</strong>: merchant's bank; receives funds post-authorisation.</li>"
         "<li><strong>PSP (Payment Service Provider)</strong>: banks providing UPI service to users + merchants. Technically operates virtual payment addresses (VPAs) + handles.</li>"
         "<li><strong>TPAP (Third-Party Application Provider)</strong>: apps that provide UPI payment experience to users via sponsor bank. Google Pay, PhonePe, Paytm are TPAPs (via sponsor banks ICICI, YES, HDFC respectively).</li>"
         "<li><strong>Payment Aggregator (PA)</strong>: provides UPI acceptance infrastructure to merchants + end-to-end payment settlement.</li>"
         "</ul>"),
        ("/ Pathway 1: TPAP via sponsor bank", "The Google Pay / PhonePe model.",
         "<ul>"
         "<li><strong>Foreign fintech becomes TPAP</strong>: provides UPI payment experience to users via its app.</li>"
         "<li><strong>Sponsor bank requirement</strong>: must partner with an Indian scheduled commercial bank as sponsor; sponsor bank acts as PSP; foreign fintech acts as TPAP.</li>"
         "<li><strong>User funds</strong>: held in user's regular Indian bank account (any bank); flow via UPI rails to merchant on payment.</li>"
         "<li><strong>Virtual Payment Address (VPA)</strong>: foreign fintech's TPAP app creates VPAs for users; handles routed via sponsor bank's PSP infrastructure.</li>"
         "<li><strong>Market share cap</strong>: NPCI imposed 30% TPAP transaction volume cap on any single TPAP (grace period until Dec 2026). Encourages diverse player ecosystem.</li>"
         "<li><strong>Compliance</strong>: KYC via sponsor bank; NPCI onboarding; DPDP + CERT-In; RBI data localisation (payment data in India).</li>"
         "<li><strong>Timeline</strong>: 6-12 months from sponsor bank LOI to NPCI go-live.</li>"
         "</ul>"),
        ("/ Pathway 2: PA with UPI handle", "The acceptance-side route.",
         "<ul>"
         "<li><strong>Foreign fintech becomes Payment Aggregator</strong>: onboards Indian merchants to accept UPI (plus cards, net banking, wallet).</li>"
         "<li>Needs RBI PA licence (see <a href='india-payment-aggregator-pa-pg-licence-foreign-fintech.html'>PA licence guide</a>).</li>"
         "<li><strong>UPI handle</strong>: PA partners with sponsor bank for UPI acceptance handle (merchant@upiprovider.ifsc).</li>"
         "<li>Suitable for: foreign fintech focused on merchant acceptance side (not consumer side). Example: Razorpay as foreign-backed PA.</li>"
         "<li>Net worth INR 15 crore (year 1), scaling to INR 25 crore. Data localisation + CERT-In audit.</li>"
         "</ul>"),
        ("/ Pathway 3: International UPI linkage", "Cross-border rails.",
         "<ul>"
         "<li><strong>NPCI-NIBC / NPCI-equivalent linkages</strong>: NPCI has signed MoUs for interoperability with:</li>"
         "<li>&nbsp;&nbsp;&mdash; Singapore (PayNow): launched 2023, Indian users can send to Singapore PayNow IDs.</li>"
         "<li>&nbsp;&nbsp;&mdash; Sri Lanka (LankaPay): launched 2024.</li>"
         "<li>&nbsp;&nbsp;&mdash; UAE (future): in-progress.</li>"
         "<li>&nbsp;&nbsp;&mdash; Nepal, Bhutan: tourist payment linkages via UPI (direct QR acceptance).</li>"
         "<li>&nbsp;&nbsp;&mdash; France (Lyra / BNP Paribas pilot), UK (future).</li>"
         "<li><strong>For foreign payment network</strong>: engage NPCI directly for cross-border payment linkage. Lengthy diplomatic / regulatory process. Suitable for governments / major payment networks (not direct for most fintechs).</li>"
         "<li><strong>Practical use case</strong>: Indian consumer paying foreign merchant via UPI (outbound); foreign tourist paying Indian merchant via UPI (inbound).</li>"
         "</ul>"),
        ("/ Pathway 4: Indirect via Indian partner", "The partnership route.",
         "<ul>"
         "<li><strong>Foreign fintech partners with Indian TPAP / PA</strong>: no own regulatory setup; integrates via Indian partner's UPI capability.</li>"
         "<li>Suitable for: foreign e-commerce selling to Indian consumers wanting to accept UPI (partner with Razorpay / Cashfree etc.).</li>"
         "<li>Fastest route (weeks to days integration).</li>"
         "<li>Lower regulatory burden.</li>"
         "<li>Trade-off: dependent on partner's infrastructure + reliability + commercial terms.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("How does UPI work in India?",
         "Unified Payments Interface - real-time inter-bank payment system operated by NPCI. User initiates payment via app (TPAP like Google Pay, PhonePe) using VPA (virtual payment address) or UPI handle; request routes through user's PSP bank, UPI switch, and merchant's PSP bank; funds transferred within seconds; both parties receive confirmation. 10+ billion transactions / month make UPI world's largest real-time retail payment system."),
        ("Can a foreign fintech be a UPI TPAP?",
         "Yes - via Indian subsidiary + Indian sponsor bank partnership. Foreign fintech becomes TPAP (Third-Party Application Provider); Indian scheduled commercial bank acts as PSP (Payment Service Provider). NPCI onboarding required. 6-12 month timeline. KYC via sponsor bank; data localisation + DPDP compliance applies."),
        ("What is NPCI's 30% TPAP market share cap?",
         "To prevent dominance by any single TPAP, NPCI capped TPAP transaction volume share at 30% in 2020. Grace period extended multiple times - current deadline December 2026 (may be further extended). Encourages diverse player ecosystem. In practice: top TPAPs manage share via marketing emphasis + feature differentiation; smaller TPAPs operate below cap."),
        ("What's an international UPI linkage?",
         "NPCI's MoUs with foreign payment systems for cross-border interoperability. Launched: Singapore PayNow (2023), Sri Lanka LankaPay (2024), Nepal + Bhutan tourist payments. In progress: UAE, France (Lyra pilot), UK. Indian user can send to Singapore PayNow ID; foreign tourist can pay Indian merchant via UPI QR. For foreign payment network, engagement is with NPCI directly - diplomatic/regulatory process. For foreign fintech, usually via Indian partner."),
        ("What's the fastest UPI pathway for foreign e-commerce?",
         "Pathway 4: partner with Indian PA (Razorpay, Cashfree, Juspay) for UPI acceptance. Fastest (days to weeks integration), lowest regulatory burden, Indian partner handles compliance. Suitable for foreign e-commerce / SaaS wanting to accept UPI from Indian B2C customers. Trade-off: dependent on Indian partner's infrastructure. Combine with OIDAR GST registration - see our OIDAR guide."),
        ("Does BQP handle UPI integration for foreign fintech?",
         "Yes - pathway selection (TPAP vs PA vs partner), sponsor bank partnership structuring, NPCI onboarding co-ordination, PA licence application if applicable, DPDP + RBI data localisation compliance, Indian partner negotiation if partnership route. Co-ordinated with Indian regulatory counsel + sponsor bank. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-payment-aggregator-pa-pg-licence-foreign-fintech.html", "Guide", "RBI PA Licence"),
        ("india-account-aggregator-aa-foreign-fintech.html", "Guide", "AA Framework"),
    ],
    cta_headline="Foreign fintech wanting India UPI integration?",
    cta_body="TPAP via sponsor bank, PA with UPI handle, international linkage, or Indian partner. BQP pathway recommendation + end-to-end execution.",
))

# 19. IEC + GST + customs
write_page("india-iec-gst-customs-foreign-exporter-importer-2026", page(
    slug="india-iec-gst-customs-foreign-exporter-importer-2026",
    title="Import Export Code (IEC) Registration India 2026: Fees, Annual Renewal, Verification, GST and Customs - BQP",
    description="India IEC (Importer Exporter Code) + GST + customs duty for foreign companies exporting to India or importing Indian goods 2026: IEC application via DGFT (free online), GST registration non-resident + OIDAR, Customs duty (BCD + SWS + IGST), FTA preferential rates (India-UAE CEPA, India-UK CETA, India-Australia ECTA), BIS certification. Complete guide. CA Durgesh Chavda.",
    keywords="India IEC foreign company, DGFT IEC online, India GST non-resident importer, India customs duty foreign exporter, India FTA preferential rate 2026, BIS certification foreign",
    hero_kicker="/ Foreign Clients &middot; IEC + GST + Customs &middot; Updated 2026-10-15",
    hero_title_html="India IEC + GST + Customs, <em>foreign importer and exporter guide.</em>",
    hero_lead="Foreign company exporting to India (selling to Indian customers from abroad) or importing Indian goods (buying from Indian suppliers to re-sell abroad) needs to understand India's three-layer trade framework: IEC (Importer Exporter Code) from DGFT, GST registration (regular or non-resident or OIDAR), Customs duty on physical goods. Plus BIS certification for specific goods + FTA preferential rates where applicable. Here's the complete 2026 framework.",
    sections=[
        ("/ IEC - the trade licence", "The foundation.",
         "<ul>"
         "<li><strong>IEC (Importer Exporter Code)</strong>: 10-digit code issued by DGFT (Directorate General of Foreign Trade). Required for any foreign trade transaction &mdash; export / import of physical goods, services where foreign exchange involved.</li>"
         "<li><strong>Who needs IEC</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Indian company exporting / importing: standard.</li>"
         "<li>&nbsp;&nbsp;&mdash; Foreign company importing from India to re-export: foreign company itself doesn't need IEC; the Indian seller has IEC.</li>"
         "<li>&nbsp;&nbsp;&mdash; Foreign company exporting to India via Indian branch / subsidiary: Indian branch / subsidiary needs IEC.</li>"
         "<li>&nbsp;&nbsp;&mdash; Foreign company importing Indian goods via Indian subsidiary acting as buyer / re-seller: Indian subsidiary needs IEC.</li>"
         "<li><strong>Application</strong>: online via DGFT portal (dgft.gov.in). Free of cost. 1-5 business day issuance.</li>"
         "<li><strong>Documents</strong>: PAN, GST registration (if applicable), bank certificate, address proof.</li>"
         "<li><strong>No renewal</strong> required (post simplification).</li>"
         "</ul>"),
        ("/ GST + customs on inbound (foreign exporting to India)", "The duty stack.",
         "<p>Foreign company's goods arriving at Indian port:</p>"
         "<ul>"
         "<li><strong>Basic Customs Duty (BCD)</strong>: tariff based on HSN code. Varies 0-20%+ depending on product. Published in Customs Tariff.</li>"
         "<li><strong>Social Welfare Surcharge (SWS)</strong>: 10% on BCD.</li>"
         "<li><strong>IGST on imports</strong>: nil, 5%, 18% or 40% depending on HSN (the 12% and 28% slabs were removed from 22 September 2025). On (CIF value + BCD + SWS).</li>"
         "<li><strong>Compensation Cess</strong> (if applicable, luxury goods / tobacco / autos): additional.</li>"
         "<li><strong>Anti-dumping duty / countervailing duty</strong>: if notified for specific product + country of origin.</li>"
         "<li><strong>Customs clearance via Indian CHA (Customs House Agent)</strong>: Indian broker handles clearance; files Bill of Entry; pays duties.</li>"
         "</ul>"
         "<p><strong>IGST on import is creditable</strong> for Indian GST-registered recipient (if goods used for taxable supplies). Business customer essentially pays BCD + SWS as cost; IGST neutralised. Consumer customer pays all.</p>"),
        ("/ FTA preferential rates", "Where to save duty.",
         "<p>India has FTAs reducing BCD for products originating in signatory countries. Significant 2024-2026 agreements:</p>"
         "<ul>"
         "<li><strong>India-UAE CEPA (Comprehensive Economic Partnership Agreement)</strong>: signed May 2022, effective May 2022. Preferential tariffs on 97% of lines. See our <a href='india-uae-tax-treaty-dtaa.html'>India-UAE guide</a>.</li>"
         "<li><strong>India-Australia ECTA (Economic Cooperation and Trade Agreement)</strong>: signed April 2022, effective December 2022. Tariff reductions on 85-96% of lines.</li>"
         "<li><strong>India-EFTA TEPA (Trade and Economic Partnership Agreement)</strong>: signed March 2024 with Switzerland, Norway, Iceland, Liechtenstein. Effective 2025. Investment-focused.</li>"
         "<li><strong>India-UK CETA (Comprehensive Economic and Trade Agreement)</strong>: signed 24 July 2025, in force from 15 July 2026, with UK duty removed on about 99% of Indian tariff lines and Indian tariffs phased down on most UK goods.</li>"
         "<li><strong>India-ASEAN FTA</strong>: 2010; preferential rates for Southeast Asian origin.</li>"
         "<li><strong>India-Japan CEPA</strong>: 2011.</li>"
         "<li><strong>India-South Korea CEPA</strong>: 2010.</li>"
         "</ul>"
         "<p>To claim FTA preferential rate: Certificate of Origin from exporting country authority + customs declaration under FTA + specific product-wise rules of origin (ROO) satisfied.</p>"),
        ("/ GST for foreign exporter / importer", "Three registration types.",
         "<ul>"
         "<li><strong>Regular GST registration (via Indian subsidiary / Indian branch)</strong>: standard. If foreign company has Indian presence as the buyer / seller.</li>"
         "<li><strong>Non-resident taxable person (NRTP) registration</strong>: foreign company occasionally supplying taxable goods / services in India without permanent presence &mdash; e.g., foreign exhibitor at Indian trade fair, foreign company providing services at Indian site. Form GST REG-09. Advance tax deposit required for estimated tax liability.</li>"
         "<li><strong>OIDAR GST</strong>: foreign SaaS / digital services to Indian B2C customers. See <a href='oidar-gst-foreign-saas-ecommerce-india.html'>OIDAR guide</a>.</li>"
         "</ul>"
         "<p>For physical goods trade, Indian subsidiary / Indian branch handles GST; foreign exporter itself typically doesn't register in India (deals with Indian subsidiary as the GST taxpayer).</p>"),
        ("/ BIS + CDSCO + specific certifications", "Non-tariff barriers.",
         "<ul>"
         "<li><strong>BIS (Bureau of Indian Standards)</strong>: ISI mark + certification for specific products (electrical appliances, cement, LPG cylinders, kitchenware, toys, etc.). Mandatory for notified products; foreign exporter must obtain BIS certification before import permitted.</li>"
         "<li><strong>CDSCO (Central Drugs Standard Control Organisation)</strong>: for pharmaceuticals + medical devices + cosmetics. Registration + licensing before import.</li>"
         "<li><strong>FSSAI (Food Safety and Standards Authority of India)</strong>: for food + beverages. Importer requires FSSAI licence.</li>"
         "<li><strong>BIS Compulsory Registration Scheme (CRS)</strong>: for electronic + IT products. Specific electronic products need CRS certification.</li>"
         "<li><strong>CPCB (Central Pollution Control Board)</strong>: for products affecting environment / specific chemicals.</li>"
         "<li><strong>FCI / plant quarantine</strong>: for agricultural products.</li>"
         "<li><strong>Legal Metrology Act</strong>: for packaged products &mdash; labelling + weight / measure declaration.</li>"
         "</ul>"
         "<p>Compliance with these is often more time-consuming than tariff compliance. Pre-plan 6-12 months before first import.</p>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Does a foreign company need an Indian IEC to export to India?",
         "No - foreign exporter doesn't need Indian IEC. The Indian importer (consignee) has an IEC. Foreign company sells FOB / CIF to Indian importer; Indian importer clears customs using their IEC + pays BCD + SWS + IGST. If foreign company sets up Indian subsidiary / branch as the buyer, that Indian entity needs IEC for the customs clearance."),
        ("How do I apply for an IEC code, and what does it cost?", "Apply online on the DGFT portal with the business PAN (one IEC per PAN), bank details and address proof, verified by Aadhaar-linked OTP or a Class 3 digital signature. A small government fee is paid online, and the IEC is usually issued once the details match. The IEC does not expire, but it must be updated or confirmed on the DGFT portal every year between 1 April and 30 June, even if nothing changed; the annual update is free, and an IEC not updated by 30 June is deactivated until the update is completed."),
        ("Does an IEC need renewal, and how do I verify one?", "An IEC does not expire, but it must be updated or confirmed on the DGFT portal every year between 1 April and 30 June, even if nothing changed; the update is free, and an IEC not updated by 30 June is deactivated until it is. To check an IEC, use the IEC lookup on the DGFT portal and match the name and status with the business's GST and company records."),
        ("What's the typical duty stack on goods imported to India?",
         "Basic Customs Duty (BCD, 0-20%+ based on HSN) + Social Welfare Surcharge (10% on BCD) + IGST on imports (0-40% based on HSN since 22 September 2025, mostly 5% or 18%; calculated on CIF value + BCD + SWS) + Compensation Cess only for the few goods still subject to it, such as tobacco + Anti-dumping / Countervailing Duty if notified. IGST portion is creditable for GST-registered business recipient. FTA preferential rate reduces BCD for signatory-country-origin goods."),
        ("Is IGST applicable on import of goods, and can it be claimed as input tax credit?", "Yes. Imports of goods are treated as inter-state supplies, so IGST is charged by customs at clearance under the Customs Tariff Act, on the assessable value plus basic customs duty, and paid against the bill of entry. A GST-registered importer can claim input tax credit of that IGST on the basis of the bill of entry, which flows into the importer's GST records; basic customs duty itself is not creditable."),
        ("How does the India-UAE CEPA affect imports from UAE?",
         "India-UAE Comprehensive Economic Partnership Agreement (CEPA, effective May 2022) provides preferential tariffs on 97% of tariff lines - either reduced BCD or zero duty depending on product. UAE-origin goods must meet Rules of Origin (ROO) under CEPA; Certificate of Origin from UAE Chamber of Commerce required at import. Combined with India's growing trade with Gulf, materially reduces import cost for CEPA-origin goods."),
        ("What is BIS certification and when is it required?",
         "Bureau of Indian Standards certification. Mandatory for notified products (electrical appliances, cement, LPG cylinders, toys, kitchenware, chemicals, electronic goods under CRS). Foreign manufacturer must obtain BIS certification (ISI mark or CRS registration) before product can be imported. Separate framework from customs; often time-consuming (3-9 months). Pre-plan well before first import."),
        ("What's the difference between regular GST registration and NRTP?",
         "Regular GST: for entities with established Indian presence (Indian subsidiary / branch) making taxable supplies. Non-resident Taxable Person (NRTP) - Form GST REG-09: for foreign company occasionally supplying taxable goods/services in India without permanent presence (foreign exhibitor at trade fair, foreign technical consultant at Indian site). Advance tax deposit required covering estimated liability. OIDAR GST is a third category for digital services to Indian B2C."),
        ("Does BQP handle India trade compliance for foreign exporters / importers?",
         "Yes - IEC application (DGFT), GST registration (regular / NRTP / OIDAR as applicable), customs duty optimisation (HSN classification + FTA preferential rate claim), BIS / CDSCO / FSSAI / CPCB / Legal Metrology certification co-ordination, Customs House Agent appointment, ongoing GSTR filing + customs reconciliation. For foreign-origin exports to India + Indian imports to foreign markets. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("oidar-gst-foreign-saas-ecommerce-india.html", "Guide", "OIDAR GST"),
        ("india-uae-tax-treaty-dtaa.html", "Guide", "India-UAE DTAA"),
    ],
    cta_headline="Foreign company trading goods with India?",
    cta_body="IEC + customs duty + GST + FTA preferential rate + BIS / sector certification. BQP end-to-end: application + ongoing compliance + Indian subsidiary structuring. Scope-based engagement.",
))

# 20. Semiconductor ISM
write_page("india-semiconductor-ism-pli-foreign-chip-company", page(
    slug="india-semiconductor-ism-pli-foreign-chip-company",
    title="India Semiconductor Mission (ISM) for Foreign Chip Company 2026 - BQP",
    description="India Semiconductor Mission (ISM) framework for foreign semiconductor / chip / display companies 2026: the Semicon India Programme fab and display schemes (up to 50% fiscal support), DLI (Design Linked Incentive), ATMP / OSAT scheme, compound semiconductor + display fab, section 115BAA tax rate, Gujarat / Tamil Nadu / Karnataka state ecosystem. CA Durgesh Chavda.",
    keywords="India Semiconductor Mission ISM foreign company, India chip fab 50% subsidy, Modified SPECS India semiconductor, DLI Design Linked Incentive India, India ATMP OSAT foreign",
    hero_kicker="/ Foreign Clients &middot; Semiconductor ISM &middot; Updated 2026-10-15",
    hero_title_html="India Semiconductor Mission, <em>what foreign chip companies get.</em>",
    hero_lead="India Semiconductor Mission (ISM) launched December 2021 with INR 76,000 crore (~USD 9.2B) outlay. Updated with Modified SPECS 2022, Design Linked Incentive (DLI), ATMP / OSAT scheme. Combined with Section 115BAB (15% corporate tax), state-level incentives, and Gujarat / Tamil Nadu / Karnataka semiconductor cluster development, India now offers one of the most generous chip-manufacturing incentive packages globally. Here's the complete 2026 framework.",
    sections=[
        ("/ The ISM framework", "Four schemes.",
         "<ul>"
         "<li><strong>Modified SPECS (Scheme for Promotion of Manufacturing of Electronic Components and Semiconductors)</strong>: up to <strong>50% capex subsidy</strong> for semiconductor fabs. INR 76,000 crore outlay (shared across schemes).</li>"
         "<li><strong>Design Linked Incentive (DLI)</strong>: up to 50% reimbursement of eligible expenses for semiconductor chip design &mdash; silicon IP, chip tape-out, prototyping. Targets Indian chip design startups + foreign fabless entering India.</li>"
         "<li><strong>Compound Semiconductor Fab / SiC / GaN / Display Fab</strong>: up to 50% capex subsidy for compound semiconductor fabs + display fabs (OLED / LCD / MicroLED).</li>"
         "<li><strong>ATMP (Assembly, Test, Marking, Packaging) / OSAT (Outsourced Semiconductor Assembly and Test)</strong>: up to 50% capex subsidy. Lower threshold than fab; faster path to Indian presence.</li>"
         "</ul>"
         "<p>Combined with PLI Mobile Phones + Specified Electronic Components (adjacent scheme), India has comprehensive electronics-manufacturing incentive coverage.</p>"),
        ("/ Who's benefiting + current state", "Projects announced + under construction.",
         "<ul>"
         "<li><strong>Tata Group + Powerchip (PSMC Taiwan)</strong>: Dholera (Gujarat) 28nm chip fab. INR 91,000 crore investment; up to INR 45,000 crore subsidy. Operational 2026-2027.</li>"
         "<li><strong>Micron Technology (US)</strong>: Sanand (Gujarat) ATMP facility. USD 2.75B investment; up to USD 1.3B subsidy.</li>"
         "<li><strong>Tata Semiconductor Assembly and Test</strong>: Jagiroad (Assam) OSAT facility, approved February 2024.</li>"
         "<li><strong>CG Power (Murugappa Group) + Renesas + Stars Microelectronics</strong>: Sanand (Gujarat) OSAT. About INR 7,600 crore investment.</li>"
         "<li><strong>Kaynes Semicon</strong>: Gujarat ATMP.</li>"
         "<li><strong>Several design-stage startups</strong>: DLI beneficiaries &mdash; Mindgrove, Netrasemi, Signalchip (foundational IP).</li>"
         "</ul>"
         "<p>As of 2026-10, India has approvals for 5+ semiconductor + display facilities totaling USD 20B+ in investment commitments.</p>"),
        ("/ Entry structures for foreign chip company", "Four routes.",
         "<ol>"
         "<li><strong>Full fab via JV with Indian partner</strong>: Tata-PSMC model. Foreign semiconductor company brings technology + know-how; Indian partner brings local relationships, land, state partnerships, project execution. Equity split varies 26-74% depending on partner leverage.</li>"
         "<li><strong>Full ATMP / OSAT via WOS or JV</strong>: Micron model (WOS). Lower capex than fab; faster execution. 100% FDI automatic route.</li>"
         "<li><strong>Design centre via WOS</strong>: fabless semiconductor company sets up Indian chip-design centre. No ISM subsidy for pure design (DLI available for specific IP / tape-out). Section 115BAB (15%) is closed to new companies (production had to begin by 31 March 2024), so a new Indian entity normally uses the 22% rate under section 115BAA.</li>"
         "<li><strong>Joint-venture with Indian fabless + co-investment</strong>: for foreign chip company wanting partnership route; Indian partner handles ISM / state co-ordination.</li>"
         "</ol>"),
        ("/ Combined incentive stack for foreign fab", "The total value.",
         "<ul>"
         "<li><strong>ISM Modified SPECS</strong>: up to 50% capex subsidy. For INR 50,000 crore investment, up to INR 25,000 crore subsidy.</li>"
         "<li><strong>Section 115BAB</strong>: 15% corporate tax (effective 17.16%). For large fab with substantial profit, material tax saving vs 25% / 22% standard.</li>"
         "<li><strong>State incentives</strong>: Gujarat Semiconductor Policy 2022 (land at 50% subsidised rate + 25% capex subsidy + electricity rebate + SGST reimbursement + stamp duty + registration exemption). Tamil Nadu Semicon Policy 2024 similar. Karnataka Policy 2022.</li>"
         "<li><strong>Customs duty exemption</strong>: specified semiconductor manufacturing equipment / tools / consumables import duty exempt.</li>"
         "<li><strong>Interest subsidy</strong>: specific state schemes offering 5-7% interest subsidy on term loans.</li>"
         "<li><strong>Skilled workforce support</strong>: PMKVY (Pradhan Mantri Kaushal Vikas Yojana) + semiconductor-specific skill development partnerships (IIT / IISc / IIIT).</li>"
         "<li><strong>R&amp;D grants</strong>: SERB / DST + semiconductor-specific research grants.</li>"
         "</ul>"
         "<p>For a USD 10B fab investment, total realised incentive stack can reach USD 4-5B over 5-7 years &mdash; among the most aggressive globally.</p>"),
        ("/ State-level ecosystem", "Where to locate.",
         "<ul>"
         "<li><strong>Gujarat (Dholera + Sanand)</strong>: dedicated Semiconductor City; land + infrastructure + state policy aggressive. Current leader with Tata-PSMC + Micron + CG Power all here.</li>"
         "<li><strong>Tamil Nadu (Hosur / Krishnagiri / Sriperumbudur)</strong>: Semiconductor Policy 2024; adjacent to existing electronics manufacturing cluster. Strong ecosystem.</li>"
         "<li><strong>Karnataka (Bengaluru / Mysuru)</strong>: strongest design talent pool; Semicon Policy 2022; adjacent to IISc + IITs.</li>"
         "<li><strong>Assam</strong>: compound semiconductor fab approved (Tata-ASIP); state offers unique advantages for compound semiconductor supply chain.</li>"
         "<li><strong>Odisha / Telangana / Maharashtra</strong>: emerging semiconductor policy; state governments actively courting investments.</li>"
         "</ul>"
         "<p>Choice of state affects: subsidy quantum, land cost, electricity cost, workforce availability, logistics access, infrastructure quality.</p>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What is India Semiconductor Mission (ISM)?",
         "Launched December 2021 with INR 76,000 crore (~USD 9.2B) outlay to develop India's semiconductor ecosystem. Four schemes: Modified SPECS (up to 50% capex subsidy for silicon fabs), DLI (up to 50% reimbursement for chip design expenses), Compound Semiconductor + Display fab subsidies, ATMP/OSAT subsidy (up to 50% capex). Combined with Section 115BAB 15% corporate tax + state-level incentives, among the most generous chip-manufacturing incentive packages globally."),
        ("Can a foreign semiconductor company get full ISM capex subsidy?",
         "Yes - via Indian subsidiary (WOS or JV). Up to 50% of eligible capex subsidised by Government of India under Modified SPECS (for silicon fab) or compound semiconductor scheme or ATMP/OSAT scheme. Micron (US) ATMP in Sanand received USD 1.3B subsidy on USD 2.75B investment. Tata-PSMC fab in Dholera approved for INR 45,000 crore subsidy on INR 91,000 crore investment."),
        ("What's the fastest entry route for foreign chip company?",
         "ATMP / OSAT via WOS - lower capex (INR 1,000-10,000 crore range vs INR 50,000+ crore for silicon fab), faster project execution (18-24 months vs 36-48 for fab), 100% FDI automatic route, up to 50% capex subsidy, Section 115BAB 15% corporate tax. Micron Sanand ATMP is the model. Suitable for foreign chip companies wanting India presence without full fab commitment."),
        ("Which Indian states have the strongest semiconductor policies?",
         "Gujarat (Dholera + Sanand Semiconductor City, dedicated land + infrastructure + 25% state capex subsidy on top of central ISM): current leader. Tamil Nadu (Hosur / Krishnagiri cluster, Semiconductor Policy 2024). Karnataka (Bengaluru design talent + Semicon Policy 2022). Assam (compound semiconductor focus, Tata-ASIP partnership). Odisha + Telangana + Maharashtra emerging. Choice affects land cost + electricity + workforce + logistics."),
        ("What total incentive stack is available for a USD 10B foreign fab in India?",
         "Approximate stack: ISM Modified SPECS up to USD 5B (50% capex subsidy); State capex subsidy 20-25% up to USD 2.5B; Section 115BAB 15% corporate tax saving vs 25%+ over 5-7 years (depending on profit); customs duty exemption on manufacturing equipment; interest subsidy; skilled workforce support; R&D grants. Total realised incentive can reach USD 4-5B over 5-7 years - among the most aggressive globally."),
        ("Does BQP handle India entry for foreign semiconductor / chip companies?",
         "Yes - specialised semiconductor advisory. Entity structure (WOS vs JV), state selection + state incentive negotiation, Modified SPECS / DLI / ATMP application to IT Ministry, Section 115BAB opt-in, land acquisition + infrastructure co-ordination, workforce development partnerships, ongoing capex certification + claim submission. Co-ordinated with Indian regulatory counsel + state industrial development authority. Scope-based engagement for strategic foreign investment. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("india-pli-scheme-foreign-manufacturer-2026.html", "Guide", "PLI Scheme"),
        ("section-115baa-115bab-corporate-tax-regime-india.html", "Guide", "Section 115BAB"),
    ],
    cta_headline="Foreign semiconductor / chip / display company evaluating India?",
    cta_body="Up to 50% capex subsidy + 15% corporate tax + state incentives. BQP end-to-end: entity + ISM application + state negotiation + ongoing compliance. Standard engagement for strategic foreign investment.",
))

print("Batch O part 2 complete: 10 trending foreign-company pages written")
