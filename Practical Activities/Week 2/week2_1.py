""" 
1. Write a definition for a Date class that represents a date—that is, a year, month, and day of the month.
2. Write an __init__ method that takes year, month, and day as parameters and assigns the parameters to attributes.
3. Create an object that represents June 22, 1933.
4.Write a __str__ method that uses an f-string to format the attributes and returns the result. If you test it with the Date you created, the result should be 1933-06-22.
5.Write a method called is_after that takes two Date objects and returns True if the first comes after the second. Create a second object that represents September 17, 1933, and check whether it comes after the first object.
"""

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def is_after(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        else:
            return False

date1 = Date(1933, 6, 22)
print(date1)  # Output: 1933-06-22

date2 = Date(1933, 9, 17)
print(date2)  # Output: 1933-09-17

print(date2.is_after(date1))  # Output: True