from utils import format_currency, clamp, percent

print("Price:", format_currency(99.999))
print("Clamped:", clamp(120, 0, 100))
print("Used percent:", f"{percent(30, 50):.1f}%")