# Lesson: Data Deduplication & Validation
Imagine you work as a data engineer preparing order transaction data for a machine learning model. The raw data stream contains duplicates and error message strings that will crash your processing pipeline if they are not removed.

```python
raw_orders = [101, "ERR_404", 102, 101, "TIMEOUT", 103, "ERR_500", 102]
unique_ids = []

### Skill Check Tasks
# 1. Initialize unique_ids as an empty list to hold the clean integer IDs. (Done above)
# 2. Use a for loop to iterate through the raw_orders list.
# 3. Use an if statement inside the loop to check if the current item is an integer.
# 4. Check if that integer is not already present in your unique_ids list to prevent duplicates.
# 5. Append the valid, unique integers to unique_ids and print the final list.

### Hint
# - You can check a data type using: type(item) == int
# - You can check if an item is missing from a list using: item not in unique_ids
# - Use unique_ids.append(item) to save the valid IDs.

# ---- WRITE YOUR CODE FOR EXERCISE 1 HERE ----


```

---

# Lesson: Customer Review Rating Cleanup
Imagine you work as a data analyst for an e-commerce platform. You are pulling customer review scores from a database to calculate a product's average rating. However, the raw data array contains accidental text comments, missing fields (None), and duplicate entries that will distort your data calculation if they are not cleaned out first.

```python
raw_ratings = [5, 4, "Great product!", 5, None, 3, "Would buy again", 4, 2]
clean_ratings = []

### Skill Check Tasks
# 1. Initialize clean_ratings as an empty list to hold the valid, deduplicated scores. (Done above)
# 2. Use a for loop to iterate through the raw_ratings list.
# 3. Use an if statement inside the loop to check if the current item is an integer.
# 4. Check if that integer is not already present in your clean_ratings list to prevent duplicates.
# 5. Append the valid, unique integers to clean_ratings and print the final list.

### Hint
# - You can check for a numerical integer data type using: type(item) == int
# - You can ensure you do not repeat items by using the 'not in' operator against your new list.
# - Use clean_ratings.append(item) to save the valid ratings.

# ---- WRITE YOUR CODE FOR EXERCISE 2 HERE ----


```
