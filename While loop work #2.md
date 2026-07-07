# Lesson: Real-Time Event Notification Queue (While Loops)
Imagine you are building a notification dispatch system for a mobile app. The system receives a batch of inbound event payloads. Some messages are valid integer user IDs that need notifications, but others are broken heartbeats (`"PING"`), empty payloads (`None`), or system warnings (`"WARN_DISCONNECT"`). 

Because notifications must be sent in strict chronological order and tracked entry-by-entry, use a `while` loop with an index counter to extract, deduplicate, and clean the data.

```python
raw_events = [2001, "PING", 2002, 2001, None, 2003, "WARN_DISCONNECT", 2002, 2004]
dispatch_queue = []

### Skill Check Tasks
# 1. Initialize 'dispatch_queue' as an empty list to store valid user IDs. (Done above)
# 2. Create an 'index' counter variable starting at 0.
# 3. Write a while loop that iterates through 'raw_events' using its length as the boundary.
# 4. Inside the loop, extract the current item using your index counter.
# 5. Check if the item is an integer AND make sure it is not already in 'dispatch_queue'.
# 6. Append the valid unique item to 'dispatch_queue'.
# 7. Remember to increment your index by 1 so the loop advances!
# 8. Print 'dispatch_queue' at the very end outside of the loop.

### Expected Output
# When successful, your final printed list must look exactly like this:
# [2001, 2002, 2003, 2004]

# ---- WRITE YOUR CODE FOR THE TEST HERE ----


```
