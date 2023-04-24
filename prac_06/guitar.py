"""
Guitars Exercise
guitar file

Estimate: 40 mins
Actual: 50 mins
"""


class Guitar:
    """Representing guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate age of the guitar object"""
        return 2023 - self.year

    def is_vintage(self):
        """Decide if guitar is vintage or not"""
        return self.get_age() >= 50
