"""
Represents a time of day in hours, minutes, and seconds.
"""
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


"""
Converts a Time object to the number of seconds since midnight.
"""
def time_to_seconds(t):
    return t.hour * 3600 + t.minute * 60 + t.second


"""
Write a function called subtract_time that takes two Time objects and
returns the interval between them in seconds — assuming they are from the same day.
"""
def subtract_time(t1, t2):
    return time_to_seconds(t1) - time_to_seconds(t2)


"""
Write a function called is_after that takes two Time objects and
returns True if the first time is later in the day than the second.
"""
def is_after(t1, t2):
    return time_to_seconds(t1) > time_to_seconds(t2)


"""
Represents a year, month, and day.
"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


"""
Write a function called make_date that takes year, month, and day as parameters,
makes a Date object, assigns the parameters to attributes, and returns the result.
"""
def make_date(year, month, day):
    return Date(year, month, day)


"""
Write a function called print_date that takes a Date object and
uses an f-string to format and print it as YYYY-MM-DD.
"""
def print_date(date):
    print(f"{date.year:04}-{date.month:02}-{date.day:02}")


"""
Returns a tuple of (year, month, day) from a Date object.
"""
def date_to_tuple(date):
    return (date.year, date.month, date.day)


"""
Returns True if the first Date object comes after the second.
"""
def is_date_after(d1, d2):
    return date_to_tuple(d1) > date_to_tuple(d2)


# --- Tests ---
if __name__ == "__main__":
    # Time tests
    t1 = Time(3, 2, 1)
    t2 = Time(3, 2, 0)
    t3 = Time(9, 40, 0)
    t4 = Time(11, 12, 0)

    print("Time Tests:")
    print("Subtract time:", subtract_time(t1, t2))  # Expected: 1
    print("Is after?", is_after(t1, t2))           # Expected: True
    print("Is after same time?", is_after(t1, t1))  # Expected: False
    print("Is 11:12 after 9:40?", is_after(t4, t3)) # Expected: True

    # Date tests
    date1 = make_date(1933, 6, 22)
    date2 = make_date(1933, 9, 17)

    print("\nDate Tests:")
    print("Date 1:")
    print_date(date1)  # Expected: 1933-06-22

    print("Date 2:")
    print_date(date2)  # Expected: 1933-09-17

    print("Is date2 after date1?", is_date_after(date2, date1))  # Expected: True
    print("Is date1 after date2?", is_date_after(date1, date2))  # Expected: False