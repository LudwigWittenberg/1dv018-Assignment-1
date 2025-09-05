import random
from src.utils.FasterThreeSum import FasterThreeSum
from src.utils.GetRadomNumbers import get_random_numbers

class Task5:
  def __init__(self, size):
    self.size = size

  def run(self):
    # Get the correct number of random numbers
    random_numbers = get_random_numbers(-self.size, self.size, 2 * self.size)
    faster_three_sum = FasterThreeSum()
    result = faster_three_sum.find_three_sum(random_numbers)
    print("Random Numbers:", random_numbers)
    print("Three Sum Combinations:", result)
