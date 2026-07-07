# Lesson: Sensor Telemetry Data Streams (While Loops)
Imagine you are a software engineer working on an IoT (Internet of Things) device that collects temperature readings from a smart greenhouse sensor. The sensor streams data into a list, but occasionally loses connection, resulting in `None` entries or empty string errors (`""`). Because the stream can fluctuate, you need to use a `while` loop with an index pointer to process the data element by element.

```python
raw_temperatures = [72, 74, "", 72, None, 75, "SENSOR_ERR", 74, 71]
clean_temperatures = []

### Skill Check Tasks
# 1. Initialize clean_temperatures as an empty list to hold valid, unique numbers. (Done above)
# 2. Create a variable named 'index' and set it to 0 to track your position in the list.
# 3. Write a while loop that runs as long as 'index' is less than the length of raw_temperatures.
#    (Hint: use len(raw_temperatures) to find the length)
# 4. Inside the loop, extract the current item from raw_temperatures using your index.
# 5. Check if the current item is an integer AND not already in clean_temperatures.
# 6. If it passes the check, append it to clean_temperatures.
# 7. CRUCIAL STEP: Increment your index variable by 1 at the very end of the loop block.
# 8. Print clean_temperatures outside the loop.

### Hint
# - Use: while index < len(raw_temperatures):
# - To get the item at the current position, use: item = raw_temperatures[index]
# - Don't forget to advance your loop using: index += 1
#   (If you forget this step, PyCharm will get stuck in an infinite loop!)

# ---- WRITE YOUR CODE FOR THE WHILE LOOP EXERCISE HERE ----


```
