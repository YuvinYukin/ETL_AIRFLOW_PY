def clean_amount(value: str) -> float:
    """Convert raw CSV amounts like ' 1,234.50 ' or '(200)' to float."""
    if value is None or value.strip() == "":
        return 0.0
    v = value.strip().replace(",", "")
    if v.startswith("(") and v.endswith(")"):   # accounting negative
        return -float(v[1:-1])
    return float(v)