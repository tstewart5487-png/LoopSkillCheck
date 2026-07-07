
raw_orders = [101, "ERR_404", 102, 101, "TIMEOUT", 103, "ERR_500", 102]
unique_ids = []

for order in raw_orders:
    if type(order) == int and order not in unique_ids:
        unique_ids.append(order)

print(unique_ids)

raw_ratings = [5, 4, "Great product!", 5, None, 3, "Would buy again", 4, 2]
clean_ratings = []
for rating in raw_ratings:
    if type(rating) == int  and rating not in clean_ratings:
        clean_ratings.append(rating)
print(clean_ratings)
