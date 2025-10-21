import pandas as pd

data = pd.DataFrame({
    'AIMS': ['GOOD', 'BETTER', 'BEST', 'BETTER', 'GOOD','GREATEST']})

size_order = ['GOOD', 'BETTER', 'BEST','GREATEST']

def ordinal_encode(column, order):
    mapping = {category: idx for idx, category in enumerate(order)}
    return column.map(mapping)

data['Size_encoded'] = ordinal_encode(data['AIMS'], size_order)
print(data)