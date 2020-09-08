SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def to_subscript_number(digit):
    return f"{digit}".translate(SUB)
