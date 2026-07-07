raw_temperatures = [72, 74, "", 72, None, 75, "SENSOR_ERR", 74, 71]
clean_temperatures = []
index = 0
while index < len(raw_temperatures):
    item = raw_temperatures[index]
    if type(item) == int and item not in clean_temperatures:
        clean_temperatures.append(item)
    index = index + 1
print(clean_temperatures)

