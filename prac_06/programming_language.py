"""
Intermediate Exercise
Programming language file

Estimate: 30 mins
Actual: 14 mins
"""

class ProgrammingLanguage:
    """Represent programming language object"""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialize programming language"""
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if programming language is dynamic typing"""
        if self.typing[0] == "D":
            return True
        else:
            return False

    def __str__(self):
        """Print programming language object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"