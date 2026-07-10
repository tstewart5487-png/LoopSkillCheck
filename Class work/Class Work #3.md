# Project: Video Game Character Class (Upgraded)

## Requirements

### 1. The Constructor (`__init__`)
* Create a class named `Character`.
* The `__init__` method should accept `name` and `character_class` (e.g., "Warrior", "Wizard") as arguments and save them as attributes.
* Initialize a `health` attribute to start at `100`.
* Initialize an empty **dictionary** attribute called `inventory` (`{}`) to keep track of item counts.

### 2. Method: `pick_up_item(self, item)`
* Adds an item to the character's inventory while handling duplicates.
* **Logic:**
  * If the item is already a key in `self.inventory`, increment its count value by `1`.
  * If the item is not in the inventory, add it as a new key with a starting value of `1`.

### 3. Method: `take_damage(self, amount)`
* Subtracts the `amount` of damage from the character's `health` using standard math format.
* If health drops to `0` or below, set `health` to exactly `0` and print: `"[Name] has been defeated!"`

---

## Test Code
Once you finish your class, you can use this code at the bottom of your file to test the dictionary tracking and damage logic in PyCharm:

```python
# Create a character
hero = Character("Aragorn", "Warrior")

# Test picking up items (including duplicates)
hero.pick_up_item("Health Potion")
hero.pick_up_item("Iron Sword")
hero.pick_up_item("Health Potion")  # Duplicate item!
print(f"Inventory Counts: {hero.inventory}") 
# Expected output: {'Health Potion': 2, 'Iron Sword': 1}

# Test taking damage
hero.take_damage(40)
print(f"Health remaining: {hero.health}")

# Test defeat logic
hero.take_damage(70) 
print(f"Final Health: {hero.health}")