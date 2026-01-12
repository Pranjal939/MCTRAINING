import pandas as pd
data = pd.read_csv('products.csv')
data.head()
print(data.info)
print(data['Price'])