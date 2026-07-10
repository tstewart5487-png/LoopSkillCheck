# Project: Library Book Tracker

## Requirements

### 1. The Constructor (`__init__`)
* Create a class named `Library`.
* The `__init__` method doesn't need any outside arguments besides `self`.
* Initialize an empty dictionary attribute called `checked_out` (`{}`).
  * *Note: The keys will be member names (strings), and the values will be lists of book titles they have borrowed (lists of strings).*
* Initialize a dictionary attribute called `book_inventory` that tracks how many copies of a book the library owns. Use these starting books:
  * `"The Hobbit"`: `3`
  * `"1984"`: `2`
  * `"Dune"`: `1`

### 2. Method: `check_out_book(self, member_name, book_title)`
* Lends a book to a library member if a copy is available.
* **Logic:**
  * First, check if `book_title` exists in `self.book_inventory` AND has a count greater than `0`. 
  * If it *doesn't* exist or has `0` copies left, print: `"Sorry, [book_title] is currently unavailable."`
  * If a copy *is* available:
    1. Subtract `1` from that book's count in `self.book_inventory`.
    2. Check if the `member_name` already exists in `self.checked_out`. 
       * If they do, `.append()` the `book_title` to their existing list.
       * If they don't, add them to `self.checked_out` with a brand new list containing that book: `[book_title]`.

### 3. Method: `return_book(self, member_name, book_title)`
* Returns a borrowed book back to the library shelves.
* **Logic:**
  * Check if `member_name` is in `self.checked_out` AND if `book_title` is inside that member's list of borrowed books.
  * If they didn't borrow it, print: `"[member_name] does not have [book_title] checked out."`
  * If they do have it:
    1. Remove the book from their borrowed list using `.remove(book_title)`.
    2. Add `1` back to that book's count in `self.book_inventory`.

---

## Test Code
Once you finish your class, copy this code to the bottom of your file to test your library logic in PyCharm:

```python
# Create a new library instance
my_library = Library()

# Test checking out valid books
my_library.check_out_book("Alice", "The Hobbit")
my_library.check_out_book("Alice", "1984") # Alice now has two books
my_library.check_out_book("Bob", "Dune")   # Bob takes the last copy of Dune

# Test checking out a book with 0 copies left
my_library.check_out_book("Charlie", "Dune") # Should say unavailable

print(f"Inventory Left: {my_library.book_inventory}")
print(f"Checked Out Log: {my_library.checked_out}")

# Test returning a book
my_library.return_book("Alice", "The Hobbit")
print(f"Inventory after return: {my_library.book_inventory}")
print(f"Alice's remaining books: {my_library.checked_out['Alice']}")