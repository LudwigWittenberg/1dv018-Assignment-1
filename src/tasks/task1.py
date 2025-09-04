from src.printHelper import PrintHelper
from src.utils.UnionFind import UnionFind
import time

class Task1:
  def __init__(self, num):
    self.uf = UnionFind(num)

  # uf = UnionFind(10)
  # print_union(uf, 3, 5)

  # print_connected(uf, 3, 5)

  def add_union(self, num1, num2):
    print("")
    print(num1, "unioned with", num2)
    self.uf.union(num1, num2)

  def is_connected(self, num1, num2):
    is_connected = self.uf.connected(num1, num2)

    print("")
    print("Is", num1, "connected to", num2, "?", is_connected)

    return is_connected
