raw_events = [2001, "PING", 2002, 2001, None, 2003, "WARN_DISCONNECT", 2002, 2004]
dispatch_queue = []
index = 0
while index < len(raw_events):
    item = raw_events[index]
    if type(item) == int and item not in dispatch_queue:
        dispatch_queue.append(item)
    index = index + 1
print(dispatch_queue)