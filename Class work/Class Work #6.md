# Project: Gym Equipment & Locker Tracker

## Requirements

### 1. The Constructor (`__init__`)
*   Create a class named `Gym`.
*   The `__init__` method takes no outside arguments besides `self`.
*   Initialize an empty dictionary attribute called `active_rentals` (`{}`). The keys will be member names (strings), and the values will be lists of equipment items they have rented out (lists of strings).
*   Initialize a dictionary attribute called `equipment_inventory` that tracks available rental gear. Use these starting counts:
    *   "Weight Belt": 2
    *   "Yoga Mat": 4
    *   "Resistance Band": 1

### 2. Method: `rent_equipment(self, member_name, equipment_item)`
Rents an item to a gym member if it is in stock.

**Logic:**
*   First, check if `equipment_item` exists in `self.equipment_inventory` AND has a count greater than 0.
*   If it doesn't exist or is out of stock, print: `"Sorry, [equipment_item] is currently out of stock."`
*   If it is available:
    *   Subtract 1 from that item's count in `self.equipment_inventory`.
    *   Check if the `member_name` already exists in `self.active_rentals`.
        *   If they do, append the `equipment_item` to their existing list.
        *   If they don't, add them to `self.active_rentals` with a brand-new list containing that item: `[equipment_item]`.

### 3. Method: `return_equipment(self, member_name, equipment_item)`
Returns a rented item back to the gym storage.

**Logic:**
*   Check if `member_name` is in `self.active_rentals` AND if `equipment_item` is inside that specific member's list of rented items.
*   If they didn't rent it, print: `"[member_name] does not have a [equipment_item] rented."`
*   If they do have it:
    *   Remove the item from their active rental list.
    *   Add 1 back to that item's count in `self.equipment_inventory`.