
import pandas as pd

# Show every single column regardless of how wide the DataFrame gets
pd.set_option('display.max_columns', None)

# Prevent pandas from wrapping the text down to a new line
pd.set_option('display.width', 1000)


# Initial data tracking store locations, contact info, and product details
data = {
    'Location': ['NewYork_NY', 'LosAngeles_CA', 'Chicago_IL'],
    'Area_Code': ['212', '310', '312'],
    'Phone_Number': ['555-0199', '555-0144', '555-0177'],
    'Product_Code': ['SHIRT-RED-L', 'PANTS-BLUE-M', 'JACKET-BLACK-XL']
}
df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
loc_split = df['Location'].str.split(
    pat='_',
    expand=True
)
df['City'] = loc_split[0]
df['State'] = loc_split[1]
print('----Split DataFrame----')
print(df)
df['Full_Phone'] = df['Area_Code'].str.cat(
    df['Phone_Number'],
    sep='-'
)
print('----New Phone Split DataFrame----')
print(df)
df[['Item', 'Color', 'Size']] = df['Product_Code'].str.split(
    pat='-',
    expand=True
)
print('----Multi Split DataFrame----')
print(df)
df['Product_Summary'] = df['Color'] + ' ' + df['Item']
print('----Product Summary DataFrame----')
print(df)
cleaned_df = df[['City','State', 'Full_Phone', 'Item', 'Color', 'Size', 'Product_Summary']]
print('----Cleaned DataFrame----')
print(cleaned_df)

