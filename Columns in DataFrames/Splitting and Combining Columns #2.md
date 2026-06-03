# Pandas Skill Check 2: Splitting and Combining

## 🛠️ Part 1: The Challenge

Copy this setup code into a Python file (`script2.py`) inside PyCharm to build your starting DataFrame.

### Setup Code
```python
import pandas as pd

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
```

### Your Tasks
1. **Split Timestamp**: Split the `Order_Timestamp` column at the underscore (`_`) character. Assign the results to two new columns named `Order_Date` and `Order_Time`.
2. **Combine Name**: Combine the `First_Initial` column, a period and space (`". "`), and the `Last_Name` column into a single new column named `Customer_Name` (e.g., `"J. Doe"`).
3. **Multi-Split**: Split the `Flight_Route` column at the hyphen (`-`). Assign the resulting pieces to three new columns named `Origin`, `Destination`, and `Status`.
4. **Recombine Custom String**: Create a new column named `Flight_Summary`. Combine the `Origin` column, the word `" to "`, and the `Destination` column to make descriptions like `"JFK to LAX"`.
5. **Clean Up**: Create a final DataFrame called `cleaned_df` using **double brackets** to only keep your five newly created columns (`Order_Date`, `Order_Time`, `Customer_Name`, `Flight_Summary`, `Status`). Drop all original columns.

---

## 🔑 Part 2: Answer Key

*Try solving all 5 tasks in PyCharm first, then check your code below!*

```python
# 1. Solution for Splitting Timestamp
df[['Order_Date', 'Order_Time']] = df['Order_Timestamp'].str.split('_', expand=True)

# 2. Solution for Combining Names
df['Customer_Name'] = df['First_Initial'] + '. ' + df['Last_Name']

# 3. Solution for Multi-Split Flight Route
df[['Origin', 'Destination', 'Status']] = df['Flight_Route'].str.split('-', expand=True)

# 4. Solution for Recombining Flight Summary
df['Flight_Summary'] = df['Origin'] + ' to ' + df['Destination']

# 5. Solution for Clean Up (using double brackets)
cleaned_df = df[['Order_Date', 'Order_Time', 'Customer_Name', 'Flight_Summary', 'Status']]

# Print the final result to verify
print("\n--- Cleaned DataFrame ---")
print(cleaned_df)
```
