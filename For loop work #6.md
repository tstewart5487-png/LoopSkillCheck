Lesson: Data Deduplication & Validation

Imagine you work as a data engineer preparing order transaction data for a machine learning model. The raw data stream contains duplicates and error message strings that will crash your processing pipeline if they are not removed.

```python
raw_orders = [101, "ERR_404", 102, 101, "TIMEOUT", 103, "ERR_500", 102]
unique_ids = []
```

### Skill Check Tasks
1. Initialize `unique_ids` as an empty list to hold the clean integer IDs.
2. Use a `for` loop to iterate through the `raw_orders` list.
3. Use an `if` statement inside the loop to check if the current item is an integer (hint: use `type(item) == int`).
4. Check if that integer is not already present in your `unique_ids` list to prevent duplicates.
5. Append the valid, unique integers to `unique_ids` and print the final list.

### Hint
You can check a data type using `type(item) == int`. You can check if an item is missing from a list using the `not in` operator. Use `unique_ids.append(item)` to save the valid IDs.

```python
# write your code here
```
