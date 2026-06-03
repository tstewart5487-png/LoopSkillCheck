# Pandas Skill Check: Splitting and Combining Columns

## 🛠️ Part 1: The Challenge

Copy the setup code below into a Python file (`script.py`) inside PyCharm to build your starting DataFrame. 

### Setup Code
```python
import pandas as pd

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
```

### Your Tasks
1. **Split Columns**: Split the `Location` column at the underscore (`_`) character. Assign the results to two new columns named `City` and `State`.
2. **Combine Columns**: Combine the `Area_Code` column and the `Phone_Number` column into a single new column named `Full_Phone`. Connect them with a hyphen (`-`).
3. **Multi-Split**: Split the `Product_Code` column at the hyphen (`-`). Assign the resulting pieces to three new columns named `Item`, `Color`, and `Size`.
4. **Recombine Custom String**: Create a new column named `Product_Summary`. Combine the new `Color` column, the word `" "`, and the new `Item` column to make descriptions like `"RED SHIRT"`.
5. **Clean Up**: Create a final DataFrame called `df_clean` that only keeps your five newly created columns (`City`, `State`, `Full_Phone`, `Item`, `Color`, `Size`, `Product_Summary`). Drop all the original starting columns.

---

## 🔑 Part 2: Answer Key

*Try solving all 5 tasks first, then scroll down to verify your code!*

```python
# 1. Solution for Splitting Location
df[['City', 'State']] = df['Location'].str.split('_', expand=True)

# 2. Solution for Combining Phone Numbers
df['Full_Phone'] = df['Area_Code'] + '-' + df['Phone_Number']

# 3. Solution for Multi-Split
# Because there are two hyphens, splitting creates three parts
df[['Item', 'Color', 'Size']] = df['Product_Code'].str.split('-', expand=True)

# 4. Solution for Recombining Custom String
df['Product_Summary'] = df['Color'] + ' ' + df['Item']

# 5. Solution for Clean Up
# We select only the columns we want to keep into a new DataFrame variable
df_clean = df[['City', 'State', 'Full_Phone', 'Item', 'Color', 'Size', 'Product_Summary']]

# Print the final result to verify
print("\n--- Cleaned DataFrame ---")
print(df_clean)
```

### 💡 Codecademy Syntax Tips
* **Multiple Column Splitting**: When a string has multiple delimiters (like `SHIRT-RED-L`), `.str.split()` handles it seamlessly. You just need to provide a list of exactly three new column names on the left side of the `=` sign.
* **Adding Literal Strings**: You can use the `+` operator to combine columns with plain text strings that aren't in your DataFrame, like adding a empty space string `' '`.
* **Column Selection**: Passing a list of column names inside double brackets `df[['Col1', 'Col2']]` is the easiest Codecademy method to filter out unwanted original data.
