from src.tasks.task1 import Task1
from src.tasks.task2 import Task2

def main():
  print("----------- Task 1 -----------")

  t1 = Task1(10)

  t1.add_union(1, 2)
  t1.add_union(2, 3)
  t1.is_connected(1, 3)

  print("")
  print("----------- Task 2 -----------")

  t2 = Task2(100)

  t2.add_union(1, 2)
  t2.add_union(2, 3)
  t2.add_union(50, 60)
  t2.add_union(99, 4)
  t2.is_connected(1, 3)

main()