from forex_python.converter import CurrencyRates

cr = CurrencyRates()

amount = int(input("Please enter the amount you want to convert: "))

converting_from = input("Please enter the currency code that has to be converted: ").upper()

converting_to = input("Please enter the currency code to convert: ").upper()

output = cr.convert(converting_from, converting_to, amount)

print(amount, converting_from, "to", converting_to, "is", output, converting_to)