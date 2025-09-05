from src.tasks.task4 import Task4
from src.tasks.task5 import Task5
import timeit
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

class Task6GenerateGraphs:
  def __init__(self):
    self.sizes = [100, 200, 400, 800, 1000]
    # Create figure and subplots at initialization
    self.fig = plt.figure(figsize=(8, 10))
    self.ax = self.fig.add_subplot(1, 1, 1)

  def time_task_4(self):
    print("Testing Task 4: ")
    sizes_list = []
    times = []
    
    for size in self.sizes:
      array = self.get_random_numbers(size)
      t4 = Task4(array)
      total_time = 0

      elapsed_time = timeit.timeit(lambda: t4.run(), number=3)
      
      sizes_list.append(size)
      times.append(elapsed_time)

      self.print_to_console(size, elapsed_time)
      print("")
      
    # Plot Task4 results
    self.ax.plot(sizes_list, times, marker='o', color='blue', label='ThreeSum')

  def time_task_5(self):
    print("Testing Task 5: ")
    sizes_list = []
    times = []
    
    for size in self.sizes:
      array = self.get_random_numbers(size)
      t5 = Task5(array)
      total_time = 0

      elapsed_time = timeit.timeit(lambda: t5.run(), number=3)
      
      sizes_list.append(size)
      times.append(elapsed_time)

      self.print_to_console(size, elapsed_time)
      print("")
      
    # Plot Task5 results on the same figure
    self.ax.plot(sizes_list, times, marker='o', color='orange', label='FasterThreeSum')
    
    # Setup formatting and save the figure
    self.ax.set_xlabel("n elements")
    self.ax.set_ylabel("execution time (ms)")
    self.ax.grid(True)
    self.ax.legend()
    
    # Add a title for the entire figure
    plt.suptitle("Execution Times for ThreeSum and FasterThreeSum", fontsize=16)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig("graphs/3sum_graph.png")

  def print_to_console(self, size, elapsed_time):
    print("=============================")
    print(f"Results for size {size}:")
    print(f"Total run time: {elapsed_time:0.6f} seconds. Iterations: 3")

  def get_random_numbers(self, size):
  # Returnera hela intervallet från -size till +size
    rng = random.Random(42)

    arr = [rng.randint(-1000, 1000) for _ in range(size)]

    return arr