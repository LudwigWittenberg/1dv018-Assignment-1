class QuickUnionFind:
  def __init__(self, size):
    self.list = list(range(size))

  def root(self, value):
    while value != self.list[value]:
      value = self.list[value]

    return value

  def union(self, a, b):
    ra = self.root(a)
    rb = self.root(b)

    self.list[ra] = rb

  def connected(self, a, b):
    return self.root(a) == self.root(b)

  def get_list(self):
    return self.list