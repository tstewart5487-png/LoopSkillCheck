# 🐍 Hands-On Pandas Skill Check

Run this setup code in PyCharm to create your starter dataset:

```python
import pandas as pd

# Creating the lists line-by-line to avoid empty dictionary keys
acres_list = list((522419, 146597, 310000))
visitors_list = list((12900000, 4600000, 2800000))

data = {
    'Park_Info': ['Smoky Mountains-TN', 'Zion-UT', 'Grand Teton-WY'],
    'Acres': acres_list,
    'Visitors': visitors_list
}
df = pd.DataFrame(data)
```

---

## 🛠️ Task 1: Split and Assign
Look at the `Park_Info` column. The park name and the state are stuck together with a hyphen (`-`). 

**Your Task:** Split the `Park_Info` column on the hyphen delimiter. Assign the results to two brand new columns in `df` named `ParkName` and `State`.

```python
# Write your split and assignment code below:

```

---

## 🧮 Task 2: Drop the Cleaned Column
Now that you have successfully extracted the park name and state into their own columns, the original `Park_Info` column is redundant.

**Your Task:** Drop the `Park_Info` column from your DataFrame.

```python
# Write your column drop code below:

```

---

## 📊 Task 3: Column Calculation
You want to see how much land space exists per visitor in each park.

**Your Task:** Create a brand new column named `AcresPerVisitor`. Calculate its value by dividing the `Acres` column by the `Visitors` column.

```python
# Write your division calculation code below:

```

---

## 🏁 Submission
Test your code lines inside PyCharm. Once your script runs successfully without errors, paste your code lines back into our chat to **verify your answers**!
