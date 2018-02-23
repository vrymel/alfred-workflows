import sys
from functions import calculate_charges 

query = sys.argv[1]
segments = query.split(" ")
number_of_stocks = int(segments[0])
buy_price = float(segments[1])
sell_price = float(segments[2])

gross_purchase = number_of_stocks * buy_price
gross_sell = number_of_stocks * sell_price

net_purchase = gross_purchase + calculate_charges(gross_purchase)
net_sell = gross_sell - calculate_charges(gross_sell, is_sell=True)

gain = net_sell - net_purchase

sys.stdout.write(str(gain))

