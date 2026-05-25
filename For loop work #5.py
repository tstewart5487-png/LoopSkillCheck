raw_orders = ["ERR_", "ERR_", "TIMEOUT"]
unique_orders = []
total_unique = 0
for order in raw_orders:
    if type(order) == int and order not in unique_orders:
        unique_orders.append(order)
        total_unique = total_unique + order
print(f'Unique orders: {unique_orders}')
print(f'Total unique orders: {total_unique}')



