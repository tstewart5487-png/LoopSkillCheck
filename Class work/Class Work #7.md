# Project: Coworking Space Meeting Room Tracker

## Requirements

### 1. The Constructor (`__init__`)
*   Create a class named `CoworkingSpace`.
*   The `__init__` method takes no outside arguments besides `self`.
*   Initialize an empty dictionary attribute called `member_bookings` (`{}`). The keys will be member names (strings), and the values will be lists of room names they have reserved (lists of strings).
*   Initialize a dictionary attribute called `room_availability` that tracks how many total time slots are left for each meeting room today. Use these starting counts:
    *   "Boardroom": 2
    *   "Phone Booth": 5
    *   "Creative Studio": 1

### 2. Method: `book_room(self, member_name, room_name)`
Reserves a time slot in a specific room for a member if slots are left.

**Logic:**
*   First, check if `room_name` exists in `self.room_availability` AND has a slot count greater than 0.
*   If it doesn't exist or is fully booked, print: `"Sorry, [room_name] has no available slots today."`
*   If a slot is available:
    *   Subtract 1 from that room's count in `self.room_availability`.
    *   Check if the `member_name` already exists in `self.member_bookings`.
        *   If they do, append the `room_name` to their existing list.
        *   If they don't, add them to `self.member_bookings` with a brand-new list containing that room: `[room_name]`.

### 3. Method: `cancel_booking(self, member_name, room_name)`
Cancels a booking and returns the time slot back to the room's availability.

**Logic:**
*   Check if `member_name` is in `self.member_bookings` AND if `room_name` is inside that specific member's list of bookings.
*   If they didn't book it, print: `"[member_name] does not have a booking for [room_name]."`
*   If they do have it:
    *   Remove the room from their active booking list.
    *   Add 1 back to that room's count in `self.room_availability`.