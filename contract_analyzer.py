def detect_contract_redflags(clauses):

    warnings = []

    full_text = " ".join(clauses.values()).lower()

    if "unpaid" in full_text and "full time" in full_text:
        warnings.append(
            "Contract requires full-time work but mentions unpaid engagement."
        )

    if "assign intellectual property" in full_text:
        warnings.append(
            "Company may claim ownership of work created even outside employment."
        )

    if "non compete" in full_text:
        warnings.append(
            "Post-contract work restrictions detected."
        )

    if "terminate" in full_text and "damages" in full_text:
        warnings.append(
            "Termination penalties may financially affect the signer."
        )

    return warnings