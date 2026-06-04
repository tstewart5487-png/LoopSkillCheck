# Pandas Skill Check 3: Splitting and Combining (Practice)

## 🛠️ Part 1: The Challenge

Copy this setup code into a Python file (`script3.py`) inside PyCharm to build your starting DataFrame.

### Setup Code
```python
import pandas as pd

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
```

### Your Tasks
1. **Split Timestamp**: Split the `Restock_Timestamp` column at the underscore (`_`) character. Assign the results to two new columns named `Restock_Date` and `Restock_Time`.
2. **Combine Supplier**: Combine the `Supplier_ID` column, a hyphen (`-`), and the `Supplier_Code` column into a single new column named `Full_Supplier_ID` (e.g., "S-101").
3. **Multi-Split**: Split the `Item_Manifest` column at the hyphen (`-`). Assign the resulting pieces to three new columns named `Aisle`, `Shelf`, and `Weight_Class`.
4. **Recombine Custom String**: Create a new column named `Location_Summary`. Combine the `Aisle` column, the word `" and "`, and the `Shelf` column to make descriptions like `"Aisle3 and ShelfA"`.
5. **Clean Up**: Create a final DataFrame called `cleaned_df` using double brackets to only keep your five newly created columns (`Restock_Date`, `Restock_Time`, `Full_Supplier_ID`, `Location_Summary`, `Weight_Class`). Drop all original columns.

---

## 🔑 Part 2: Answer Key

Try solving all 5 tasks in PyCharm first, then check your code below!

```python
# 1. Solution for Splitting Timestamp
df[['Restock_Date', 'Restock_Time']] = df['Restock_Timestamp'].str.split('_', expand=True)

# 2. Solution for Combining Supplier
df['Full_Supplier_ID'] = df['Supplier_ID'] + '-' + df['Supplier_Code']

# 3. Solution for Multi-Split Item Manifest
df[['Aisle', 'Shelf', 'Weight_Class']] = df['Item_Manifest'].str.split('-', expand=True)

# 4. Solution for Recombining Location Summary
df['Location_Summary'] = df['Aisle'] + ' and ' + df['Shelf']

# 5. Solution for Clean Up (using double brackets)
cleaned_df = df[['Restock_Date', 'Restock_Time', 'Full_Supplier_ID', 'Location_Summary', 'Weight_Class']]

# Print the final result to verify
print("\n--- Cleaned DataFrame ---")
print(cleaned_df)
```

### Expected Output
When you run your complete script, your `cleaned_df` will generate this exact output:

```text
--- Cleaned DataFrame ---
  Restock_Date Restock_Time Full_Supplier_ID    Location_Summary Weight_Class
0   2026-07-10        11:00            S-101  Aisle3 and ShelfA         Heavy
1   2026-07-10        16:45            M-202  Aisle1 and ShelfB       Fragile
2   2026-07-11        08:30            G-303  Aisle3 and ShelfC         Heavy
```
