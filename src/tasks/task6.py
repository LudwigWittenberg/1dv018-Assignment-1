from src.tasks.task4 import Task4
from src.tasks.task5 import Task5
import timeit
import random

class Task6:
  def __init__(self):
    self.sizes = [100, 200, 400, 800, 1000]

  def time_task_4(self):
    print("Testing Task 4: ")
    for size in self.sizes:
      array = self.get_random_numbers(size)
      t4 = Task4(array)
      total_time = 0

      elapsed_time = timeit.timeit(lambda: t4.run(), number=3)

      self.print_to_console(size, elapsed_time)
      print("")

  def time_task_5(self):
    print("Testing Task 5: ")
    for size in self.sizes:
      array = self.get_random_numbers(size)
      t5 = Task5(array)
      total_time = 0

      elapsed_time = timeit.timeit(lambda: t5.run(), number=3)

      self.print_to_console(size, elapsed_time)
      print("")

  def print_to_console(self, size, elapsed_time):
    print("=============================")
    print(f"Results for size {size}:")
    print(f"Total run time: {elapsed_time:0.6f} seconds. Iterations: 3")

  def get_random_numbers(self, size):
  # Returnera hela intervallet från -size till +size
    rng = random.Random(42)

    arr = [rng.randint(-1000, 1000) for _ in range(size)]

    return arr