def format_currency(amount):
    return f"${amount:.2f}"

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def percent(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100