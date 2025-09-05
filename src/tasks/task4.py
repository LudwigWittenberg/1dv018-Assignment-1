import random
from src.utils.ThreeSum import ThreeSum
from src.utils.GetRadomNumbers import get_random_numbers

class Task4:
  def __init__(self, size):
    self.size = size

  def run(self):
    # Get the correct number of random numbers
    random_numbers = get_random_numbers(-self.size, self.size, 2 * self.size)
    three_sum = ThreeSum()
    result = three_sum.find_three_sum(random_numbers)
    print("Random Numbers:", random_numbers)
    print("Three Sum Combinations:", result)
