class CoworkingSpace:
    def __init__(self):
        self.member_bookings = {}
        self. room_availability = {
            "Boardroom" : 2,
            "Phone Booth" : 5,
            "Creative Studio" : 1
        }

    def book_room(self, member_name, room_name):
        if room_name in self.room_availability and self.room_availability[room_name] > 0:
            self.room_availability[room_name] = self.room_availability[room_name] - 1
            if member_name in self.member_bookings:
                self.member_bookings[member_name].append(room_name)
            else:
                self.member_bookings[member_name] = [room_name]
        else:
            print(f"Sorry, {room_name} has no available slots today.")

    def cancel_booking(self, member_name, room_name):
        if member_name in self.member_bookings and room_name in self.member_bookings[member_name]:
            self.member_bookings[member_name].remove(room_name)
            self.room_availability[room_name] = self.room_availability[room_name] + 1
        else:
            print(f"{member_name} does not have a booking for {room_name}")
