import pandas as pd

# Creating the lists line-by-line so they don't get erased
acres_list = list((522419, 146597, 310000))
visitors_list = list((12900000, 4600000, 2800000))

data = {
    'Park_Info': ['Smoky Mountains-TN', 'Zion-UT', 'Grand Teton-WY'],
    'Acres': acres_list,
    'Visitors': visitors_list
}
df = pd.DataFrame(data)
print(df)

park_split = df['Park_Info'].str.split(
    pat='-',
    expand=True
)
df['ParkName'] = park_split[0]
df['State'] = park_split[1]
df = df.drop('Park_Info', axis=1)
df['AcresPerVisitor'] = df['Acres'] / df['Visitors']
print(df)
