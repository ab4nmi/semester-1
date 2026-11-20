# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """sets name and bday"""
        if type(name) != str:
            raise TypeError("needs to be a string")
        if len(name) == 0:
            raise ValueError("name is empty")
        if type(birth) != date:
            raise TypeError("not a date")
        self.name=name
        self.birth=birth

    def initials(self):
        """returns intials"""
        # split the name into words
        words = self.name.split()
        ans = ""
        for w in words:
            letter = w[0]
            ans = ans + letter.upper()
        return ans

    def is_birthday(self):
        """checks if its their bday"""
        t = date.today()
        if t.month == self.birth.month:
            if t.day == self.birth.day:
                return True
        return False
