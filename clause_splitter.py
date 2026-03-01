CLAUSES = [
"termination",
"payment",
"liability",
"confidentiality",
"indemnity"
]

def split_clauses(text):

    found = {}

    lower_text = text.lower()

    for clause in CLAUSES:

        if clause in lower_text:

            start = lower_text.find(clause)

            found[clause] = text[start:start+800]

    return found