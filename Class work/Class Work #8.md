# Project Upgrade: Coworking Space Analytics

## Requirements

Extend your existing `CoworkingSpace` class by adding two brand-new methods.

### 1. Method: `has_bookings(self, member_name)`
This method checks if a specific member currently has any active room reservations.

**Logic:**
*   Check if `member_name` exists in `self.member_bookings` AND if the length (`len()`) of their booking list is greater than 0.
*   Instead of just printing a message, this method must **return a Boolean value**:
    *   `return True` if they have bookings.
    *   `return False` if they don't exist or have an empty list.

### 2. Method: `display_occupancy_report(self)`
This method uses a `for` loop to print a clean, readable summary of how many slots are remaining in every room.

**Logic:**
*   Print a header line like: `"--- TODAY'S ROOM AVAILABILITY ---"`
*   Use a `for room, slots in self.room_availability.items():` loop to go through the dictionary.
*   Inside the loop, print each room and its slots left. 
    *   Example line: `"• Boardroom: 2 slots remaining"`

---

## Testing Your Upgrades

Once you write the methods, paste these test lines at the bottom of your file to see them work:

# space = CoworkingSpace()
# space.book_room("Alex", "Boardroom")

# # Test 1: Testing the Return Value method
# print(f"Does Alex have bookings? {space.has_bookings('Alex')}")    # Should print: True
# print(f"Does Sam have bookings? {space.has_bookings('Sam')}")      # Should print: False

# # Test 2: Testing the Loop Report method
# space.display_occupancy_report()
# # Should print all 3 rooms and their current slot counts!