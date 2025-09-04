from src.printHelper import PrintHelper
from src.utils.UnionFind import UnionFind

def task1():
  printHelper = PrintHelper()

 # -------------------- TASK 1 --------------------
  printHelper.new_task("1")

  uf = UnionFind(10)
  printHelper.print_union(uf, 3, 5)

  printHelper.print_connected(uf, 3, 5)