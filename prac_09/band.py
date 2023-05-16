class Band:
    """Band class"""

    def __init__(self, name):
        """Initialize band"""
        self.name = name
        self.musicians = []
        self.musicians_dictionary = {}

    def __str__(self):
        """Return string of the name of band, musicians name and instruments played"""
        return f"{self.name} ({', '.join(self.musicians)})"

    def add(self, member):
        """Add musicians data"""
        self.musicians_dictionary[member.name] = member.instruments
        self.musicians.append(f"{member.name} ({member.instruments})")

    def play(self):
        """Return a string that says the first (or no) instrument the musician played"""
        message = []
        for member in self.musicians_dictionary:
            if not self.musicians_dictionary[member]:
                message.append(f"{member} needs an instrument!")
            else:
                message.append(f"{member} is playing: {self.musicians_dictionary[member][0]}")
        return "\n".join(message)
