import re

try:
    book_title = input("Enter book title: ")
    publ_year = input("Enter publication year: ")

    title_pattern = r"^[A-Za-z ]+$"

    year_pattern = r"^(19|20)\d{2}$"

    if not re.fullmatch(title_pattern, book_title):
        raise ValueError("Book title must contain only alphabets and spaces.")

    if not re.fullmatch(year_pattern, publ_year):
        raise ValueError(
            "Publication year must be a 4-digit year starting with 19 or 20.")

    print("Book accepted!")
    print("Title:", book_title)
    print("Year:", publ_year)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program finished.")