import pandas as pd
hourly_sales = [12, 15, 8, 22, 14]
total_sales = 0
for item in hourly_sales:
    total_sales = total_sales + item
print(total_sales)