class Gym:
    def __init__(self):
        self.active_rentals = {}
        self.equipment_inventory = {
            "Weight Belt" : 2,
            "Yoga Mat" : 4,
            "Resistance Band" : 1
        }

    def rent_equipment(self, member_name, equipment_item):
        if equipment_item in self.equipment_inventory and self.equipment_inventory[equipment_item] > 0:
            self.equipment_inventory[equipment_item] = self.equipment_inventory[equipment_item] - 1
            if member_name in self.active_rentals:
                self.active_rentals[member_name].append(equipment_item)
            else:
                self.active_rentals[member_name] = [equipment_item]

        else:
            print(f"Sorry {equipment_item} is out of stock")

    def return_equipment(self, member_name, equipment_item):
        if member_name in self.active_rentals and equipment_item in self.active_rentals[member_name]:
            self.active_rentals[member_name].remove(equipment_item)
            self.equipment_inventory[equipment_item] =self.equipment_inventory[equipment_item] + 1
        else:
            print(f"{member_name} does not have a {equipment_item} rented.")