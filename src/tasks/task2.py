from src.utils.QuickUnionFind import QuickUnionFind
import time

class Task2:
  def __init__(self, num):
    self.uf = QuickUnionFind(num)

  def add_union(self, num1, num2):
    self.uf.union(num1, num2)

  def is_connected(self, num1, num2):
    return self.uf.connected(num1, num2)

  def get_list(self):
    return self.uf.get_list()