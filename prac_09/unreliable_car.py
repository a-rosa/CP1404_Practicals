import random
from prac_06.car import Car


class UnreliableCar(Car):
    """Car with reliability"""

    def __init__(self, name, fuel, reliability=float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.uniform(0, 100)
        if random_number < float(self.reliability):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
