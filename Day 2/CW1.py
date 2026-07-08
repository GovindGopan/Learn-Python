#Receipt for bookstore
receipt_header ="""RECEIPT
____________________________
"""
                   
Booktitle_1 = "Python Basics"
Booktitle_2 = "Data Science Intro"
Bookprice_1 = 450
Bookprice_2 = 600

Book1 = "Book Title: {} - {}".format(Booktitle_1, Bookprice_1)
Book2 = "Book Title: {} - {}".format(Booktitle_2, Bookprice_2)


Total_price = Bookprice_1 + Bookprice_2

Ending = "Thank you!"

print(receipt_header + "\n" + Book1 + "\n" + Book2 + "\n" + "Total price: {}".format(Total_price) + "\n"+ "\n" + Ending)