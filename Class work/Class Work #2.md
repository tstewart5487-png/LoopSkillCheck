# Exercise 2: The Smartphone (Beginner)

## Goal
Create a class that models a smartphone to track its battery life and installed apps.

## Requirements
*   Class named `Smartphone`.
*   `__init__` method accepting `brand` and `model`. It should also automatically set a property named `battery_level` to 100 (representing 100%) and a property named `apps` to an empty list `[]`.
*   Method `install_app(app_name)` that adds the app name to the list of apps.
*   Method `use_phone(minutes)` that subtracts 1% from the `battery_level` for every 5 minutes used, but only if the phone has enough battery. If the battery hits 0, it should print a warning. *(Remember to use standard math format instead of shortcut operators!)*

---
