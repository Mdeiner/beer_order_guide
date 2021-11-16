import pandas as pd
import pprint

df = pd.read_csv(r'C:\Users\Matt\Documents\beer_order.csv')

data = pd.DataFrame(df, columns = ['Product', 'DIST', 'Order'])

data_dict = data.to_dict('records')

order_lst = []

for product in data_dict:
    if product['Order'] >= 1:
        order_lst.append(product)

sorted_lst = sorted(order_lst, key=lambda x: x['DIST'])

pprint.pprint(sorted_lst)

