prices = [200, 700, 500]
vat = 0.16
def get_inclusive(prices,vat):
    for price in prices:
        vatamount = price * vat 
        inclusiveprice = price + vatamount
        print(inclusiveprice)
get_inclusive(prices, vat)


