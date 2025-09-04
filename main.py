from src.tasks.task1 import Task1

def main():
  print("----------- Task 1 -----------")

  t1 = Task1(10)

  t1.add_union(1, 2)
  t1.add_union(2, 3)
  t1.is_connected(1, 3)

  print("")
  print("----------- Task 2 -----------")

main()

