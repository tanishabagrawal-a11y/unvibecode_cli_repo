def _rate(code):
    return 0.1 if code == "SAVE10" else 0.0


def apply_discount(total, code):
    return total * (1 - _rate(code))
