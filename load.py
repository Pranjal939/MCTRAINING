import pandas as pd
data = pd.read_csv('product.csv')
data.head()
print(data.info)
print(data['price'])