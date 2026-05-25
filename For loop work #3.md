# Python Skill Check: Data Cleaning with type()

### **The Scenario**
I am processing a list of bakery order data that contains mixed types. I need to sum only the valid integers while ignoring the placeholder strings like "unknown" or "error."

```python
# Delivery data with placeholder strings
delivery_counts = ["unknown", "pending", "error"]
```

### **The Challenge**
Write a `for` loop to clean this data and calculate a final total of valid orders.

### **Instructions**
1.  **Initialize**: Create a variable `total_orders` and set it to `0`.
2.  **Iterate**: Use a `for` loop to traverse the `delivery_counts` list.
3.  **Clean**: Use an `if` statement with the `type()` function to check if the current item is an integer (`if type(item) == int:`).
4.  **Aggregate**: If it is an integer, add its value to `total_orders`.
5.  **Finalize**: Print the final `total_orders` after the loop finishes.

---

### **Why this matters for AI/ML Engineering**
*   **Data Validation**: Checking object types with `type()` is a fundamental way to verify data before processing it.
*   **Noise Reduction**: Identifying and skipping non-numeric "placeholders" ensures that final calculations—like totals or averages—are accurate and not corrupted by errors.
