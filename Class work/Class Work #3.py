class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.inventory = {}
    def pick_up_item(self,item):
        if item in self.inventory:
            self.inventory[item] = self.inventory[item] + 1
        else:
            self.inventory[item] = 1
    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated")

hero = Character('Hiltrude', "The Heavy")
print(f"{hero.name} is {hero.character_class}")

hero.pick_up_item('Health Potion')
hero.pick_up_item('Battle Axe')
hero.pick_up_item('Health Potion')
hero.pick_up_item('Bread Loaf')
hero.pick_up_item('Stone Workers Tools')
hero.pick_up_item('Flail')
hero.pick_up_item('Iron Scale Mail')
hero.pick_up_item('Trauma')
print(f"{hero.name}'s  Inventory: {hero.inventory}")

hero.take_damage(50)
print(f"{hero.name} has {hero.health} health remaining")

hero.take_damage(50)
