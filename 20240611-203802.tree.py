class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

root = Node("Akar")
root.left = Node("Anak Kiri")
root.right = Node("Anak Kanan")

def preorder(node):
  if node is None:
    return

  print(node.value)  # Visit the root first in preorder
  preorder(node.left)  # Traverse left subtree
  preorder(node.right)  # Traverse right subtree

# Call the preorder function with the root node
preorder(root)
