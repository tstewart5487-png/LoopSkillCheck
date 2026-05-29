raw_orders = [101, "ERR_404", 102, 101, "TIMEOUT", 103, "ERR_500", 102]
unique_ids = []
for counter in raw_orders:
    if type(counter) == int and counter not in unique_ids:
        unique_ids.append(counter)
print(unique_ids)
