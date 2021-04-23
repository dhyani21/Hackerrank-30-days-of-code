'''
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these 3 parameters:
    1. string title
    2. string author
    3. int price
Implements the Book class' abstract display() method so it prints these 3 lines:
    1. title: , a space, and then the current instance's title.
    2. author: , a space, and then the current instance's author.
    3. price: , a space, and then the current instance's price.
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring MyBook or your code will not execute.

'''

class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price 

    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))
