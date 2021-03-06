
class BinarySearchTree(object):

  #---------------------------------

  class Node(object):

    def __init__(self, key, val):
      self.key   = key
      self.val   = val
      self.left  = None
      self.right = None

  #---------------------------------

  def __init__(self, key = None, val = None):
    self.root = self.Node(key, val)

  #---------------------------------
  # public api
  #---------------------------------

  def insert(self, key, val):
    if not self.root.key:
      self.root = self.Node(key, val)
      return self.root
    else:
      self.root = self.__insert(key, val, self.root)

  def delete(self, key):
    node = self.root
    self.root = self.__hibbard_delete(key, self.root)

  def select(self, val):
    node = self.head
    while node:
      if val < node.val:
        node = node.left
      elif val > node.val:
        node = node.right
      else:
        return node

  def display(self, node):
    if node == None:
      return
    print(node.key)
    if node.left:
      print("%d Left: " % (node.key)),
      self.display(node.left)
    if node.right:
      print("%d Right: " % (node.key)),
      self.display(node.right)

  def find_max(self, node):
    while node.right:
      node = node.right
    return node

  def find_min(self, node):
    while node.left:
      node = node.left
    return node

  def bfs(self):
    queue = [self.root]
    while queue:
      node = queue.pop(0)
      print(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  def dfs(self, node):
    print(node.val)
    if node.left:
      self.dfs(node.left)
    if node.right:
      self.dfs(node.right)

  #---------------------------------
  # private helpers
  #---------------------------------

  def __insert(self, key, val, node):
    if node == None: return self.Node(key, val)
    if key < node.key:
      node.left = self.__insert(key, val, node.left)
    elif key > node.key:
      node.right = self.__insert(key, val, node.right)
    else: # key == node.key
      node.val = val
    return node

  def __hibbard_delete(self, key, node):
    # if the delete reaches a node with a value of None, it means the node was never found
    # we return None nevertheless since we are recursing
    # and want to keep this child as is for the parent who will receive this on return
    if node == None:
      return None
    if key < node.key:
      node.left = self.__hibbard_delete(key, node.left)
    elif key > node.key:
      node.right = self.__hibbard_delete(key, node.right)
    else: # key == node.key
      if not node.left and not node.right:
        return None
      if node.left == None: return node.right
      if node.right == None: return node.left
      # by now, if the node has passed the above checks
      # it will have both a left and right child.
      # if so, replace the node with the minumum
      # of the right child, a.k.a the next largest
      next_largest = self.__hibbard_delete_min(node.right)
      left = node.left
      if next_largest == node.right:
        right = next_largest.right
      else:
        right = node.right
      node = next_largest
      node.left = left
      node.right = right
    return node

  def __hibbard_delete_min(self, node):
    while node.left:
      parent = node
      node = node.left
    if 'parent' in locals():
      parent.left = node.right
    return node

bst = BinarySearchTree()

bst.insert(3, "three")
bst.insert(1, "one")
bst.insert(9, "nine")
bst.insert(7, "seven")
bst.insert(11, "eleven")
bst.insert(8, "eight")
bst.insert(10, "ten")
bst.delete(9)

bst.display(bst.root)

