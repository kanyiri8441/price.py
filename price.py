user_name = "simon"
amount = 1600
vat_percent = 0.16
vat_amount = vat_percent * amount
inclusive_price = amount + vat_amount
print(int(inclusive_price))
