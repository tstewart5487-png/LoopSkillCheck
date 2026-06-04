import pandas as pd

# Show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Prevent text wrapping to multiple lines
pd.set_option('display.width', 1000)


# Initial data tracking store inventory updates and shipping data
data = {
    'Restock_Timestamp': ['2026-07-10_11:00', '2026-07-10_16:45', '2026-07-11_08:30'],
    'Supplier_ID': ['S', 'M', 'G'],
    'Supplier_Code': ['101', '202', '303'],
    'Item_Manifest': ['Aisle3-ShelfA-Heavy', 'Aisle1-ShelfB-Fragile', 'Aisle3-ShelfC-Heavy']
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
df[['Restock_Date', 'Restock_Time']] = df['Restock_Timestamp'].str.split(
    pat='_',
    expand=True
)
print('----Split Timestamp DataFrame----')
print(df)
df['Full_Supplier_ID'] = df['Supplier_ID'] + '-' + df['Supplier_Code']
print('----Full Supplier ID DataFrame----')
print(df)
df[['Aisle', 'Shelf', 'Weight_Class']] = df['Item_Manifest'].str.split(
    pat='-',
    expand=True
)
print('----Split Item Manifest DataFrame----')
print(df)
df['Location_Summary'] = df['Aisle'] + ' and ' + df['Shelf']
print('----Recombined Custom String----')
print(df)
cleaned_df = df[['Restock_Date', 'Restock_Time', 'Full_Supplier_ID', 'Location_Summary', 'Weight_Class']]
print('Cleaned DataFrame')
print(cleaned_df)