from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more fancy taxi"""
    price_per_km = Taxi.price_per_km
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize the silver service taxi based on taxi parent class"""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return the total price of the fare"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return total fare"""
        return super().get_fare() + self.flagfall