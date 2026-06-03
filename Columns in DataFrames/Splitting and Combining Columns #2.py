import pandas as pd

# Show every single column regardless of how wide the DataFrame gets
pd.set_option('display.max_columns', None)

# Prevent pandas from wrapping the text down to a new line
pd.set_option('display.width', 1000)


# Initial data tracking online order dates, times, and customer details
data = {
    'Order_Timestamp': ['2026-06-01_09:15', '2026-06-01_14:30', '2026-06-02_18:45'],
    'First_Initial': ['J', 'M', 'A'],
    'Last_Name': ['Doe', 'Smith', 'Jones'],
    'Flight_Route': ['JFK-LAX-Direct', 'ORD-MIA-Layover', 'SEA-SFO-Direct']
}
df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
df[['Order_Date', 'Order_Time']] = df['Order_Timestamp'].str.split(
    pat='_',
    expand=True
)
print('----Split DataFrame----')
print(df)
df['Customer_Name'] = df['First_Initial'] + '. ' + df['Last_Name']
print('----Combined Name DataFrame----')
print(df)
df[['Origin', 'Destination', 'Status']] = df['Flight_Route'].str.split(
    pat='-',
    expand=True
)
print('----Multisplit DataFrame----')
print(df)
df['Flight_Summary'] = df['Origin'] + ' to ' + df['Destination']
print('----Flight Summary DataFrame----')
print(df)
cleaned_df = df[['Order_Date', 'Order_Time', 'Customer_Name', 'Flight_Summary', 'Status']]
print('----Cleaned DataFrame----')

print(cleaned_df)

