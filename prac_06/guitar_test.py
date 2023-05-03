"""
Guitar Exercise
Guitar Testing file

Estimate and actual in guitar file
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_one = Guitar("Another guitar", 1973, 1000.23)
print(2023 - gibson.year, gibson.get_age())
print(2023 - another_one.year, another_one.get_age())
print(gibson.is_vintage(), another_one.is_vintage())
