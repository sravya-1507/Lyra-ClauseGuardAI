import re


# =================================
# HIGH RISK PATTERNS
# =================================
HIGH_RISK_PATTERNS = [

    # Non compete
    r"non[- ]?compete",
    r"post[- ]termination",
    r"cannot work.*compet",
    r"restrict.*employment",
    r"work for.*competitor",

    r"post employment restriction",
    r"engage.*similar business",
    r"directly or indirectly compete",
    r"anywhere in.*country",
    r"after termination.*years",
    r"long restriction periods"

    # IP ownership grab
    r"assign.*intellectual property",
    r"irrevocably assign",
    r"waive.*moral rights",
    r"ownership.*invention",

    r"company shall own",
    r"work product belongs to company",

    # Indemnity / liability
    r"indemnify",
    r"hold harmless",
    r"defend.*claim",
    r"attorneys?'?\sfees",
    r"legal fees",

    r"costs and expenses",
    r"including legal expenses",

    # Termination abuse
    r"terminate.*without notice",
    r"with or without cause",
    r"sole discretion",
    r"immediate termination",

    r"terminate.*any time",
    r"may terminate.*any time",
    r"without prior notice",
    r"company may terminate",
    r"intern may not terminate",
    r"cannot terminate",

    # Penalties
    r"liquidated damages",
    r"penalty",
    r"pay.*company.*cost",

    r"replacement cost",
    r"recruitment cost",
    r"training cost recovery",
    r"training.*cost",
    r"recover.*cost",

    # Monitoring
    r"monitor.*communication",
    r"access.*device",
    r"track.*activity",

    r"personal messages",
    r"access.*personal data",
    r"monitor.*without notice",

    # Jurisdiction traps
    r"exclusive jurisdiction",
    r"irrevocably submits",
    r"foreign law",

    # Amendment abuse
    r"amend.*any time",
    r"modify.*agreement.*any time",

    # Agreement traps
    r"agrees.*reasonable",
    r"waives.*right.*challenge",

    # Work control risk
    r"work hours determined",
    r"under supervision",
    r"company control",

    # Confidentiality survival
    r"obligation.*survive",
    r"survive.*agreement",

    # =============================
    # SaaS / Auto Pay HIGH RISK
    # =============================

    # automatic billing traps
    r"automatically.*charge",
    r"trial.*ends.*charge",
    r"free trial.*automatically",
    r"convert.*paid",

    # payment auto update
    r"obtain updated payment method",
    r"update.*payment method automatically",
    r"continue charging.*updated",

    # refund denial
    r"non[- ]refundable",
    r"no prorated refund",
    r"payments are non refundable",

    # suspension for payment
    r"suspend.*access",
    r"limit access.*payment",
    r"terminate.*subscription.*payment",

    # collection recovery
    r"costs of collection",
    r"collection charges",
    r"recover unpaid amounts",

    # unilateral pricing
    r"change.*charges",
    r"price change",
    r"modify.*pricing",
    r"increase subscription fee",

    # chargeback punishment
    r"chargeback.*suspension",
    r"chargeback.*termination",
]


# =================================
# MEDIUM RISK
# =================================
MEDIUM_RISK_PATTERNS = [

    r"confidential",
    r"confidentiality",

    r"arbitration",

    r"governing law",

    r"registration statement",
    r"securities act",
    r"sec",

    r"non disclosure",
    r"proprietary information",
    r"trade secrets",
    r"survive indefinitely",

    r"not an employee",
    r"independent contractor",
    r"business information",

    # SaaS medium risks
    r"subscription billing",
    r"recurring billing",
    r"auto[- ]pay",
    r"recurring charges",
]


# =================================
# LOW RISK
# =================================
LOW_RISK_PATTERNS = [

    r"notice period",
    r"mutual agreement",
    r"written consent",
]


# =================================
# MAIN FUNCTION
# =================================
def detect_risk(clause):

    if not clause or not isinstance(clause, str):
        return "Low", 0

    text = clause.lower()
    score = 0


    # HIGH
    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, text):
            score += 5


    # MEDIUM
    for pattern in MEDIUM_RISK_PATTERNS:
        if re.search(pattern, text):
            score += 3


    # LOW
    for pattern in LOW_RISK_PATTERNS:
        if re.search(pattern, text):
            score += 1


    # =================================
    # SMART LEGAL DETECTIONS
    # =================================

    if "indemnify" in text and "defend" in text:
        score += 10

    if "survive" in text and "termination" in text:
        score += 7

    if "securities act" in text:
        score += 5

    if "claim" in text and "expense" in text:
        score += 5

    if re.search(r"\b(2|3|5)\s*\(?years?\)?", text):
        score += 6

    if "company may" in text and "any time" in text:
        score += 6

    if "intern" in text and "liquidated damages" in text:
        score += 10

    if "company may terminate" in text and "intern" in text:
        score += 8

    if "personal" in text and "monitor" in text:
        score += 7

    if "forever" in text or "perpetual" in text:
        score += 6

    # SaaS smart detections
    if "recurring" in text and "charge" in text:
        score += 7

    if "continue until you cancel" in text:
        score += 8

    if "trial" in text and "automatically" in text:
        score += 9


    # =================================
    # NORMALIZE
    # =================================
    score = min(score * 4, 100)


    # =================================
    # LEVEL
    # =================================
    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return level, score