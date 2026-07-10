class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery_level = 100
        self.apps = []
    def install_app(self, app_name):
        if app_name not in self.apps:
            self.apps.append(app_name)
        else:
            print(f"{app_name} already installed")
    def use_phone(self, minutes):
        battery_drained = minutes / 5
        if self.battery_level >= battery_drained:
            self.battery_level = self.battery_level - battery_drained
            if self.battery_level <= 0:
                print("Battery is dead")
        else:
            print(f"{self.battery_level} is not enough battery!")

my_phone =  Smartphone("Apple", "iPhone 15")

my_phone.install_app("Python Mobile")
my_phone.install_app("Python Mobile")

my_phone.use_phone(250)
print(my_phone.battery_level)
