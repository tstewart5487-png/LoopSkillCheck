class Library:
    def __init__(self):
        self.checked_out = {}
        self.book_inventory = {
            'The Hobbit' : 3,
            '1984' : 2,
            'Dune' : 1
        }
    def check_out_book(self, member_name, book_title):
        if book_title in self.book_inventory and self.book_inventory[book_title] > 0:
            self.book_inventory[book_title] = self.book_inventory[book_title] - 1
            if member_name in self.checked_out:
                self.checked_out[member_name].append(book_title)
            else:
                self.checked_out[member_name] = [book_title]
        else:
            print(f"Sorry, {book_title} is currently unavailable.")
    def return_book(self, member_name, book_title):
        if member_name in self.checked_out and book_title in self.checked_out[member_name]:
            self.checked_out[member_name].remove(book_title)
            self.book_inventory[book_title] = self.book_inventory[book_title] + 1
        else:
            print(f"{member_name} does not have {book_title} checked out.")
