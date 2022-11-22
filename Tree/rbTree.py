RED = True
BLACK = False
class Node:
    def __init__(self, val):
        self.val = val
        self.color = RED
        self.left = None
        self.right = None

def search(root, val):
    if root is None:
        return False
    if root == val:
        return root
    if root.val > val:
        search(root.left)
    return search(root.right)

def rotateLeft(root):
    newNode = root.right
    root.right = newNode.left
    newNode.left = root
    newNode.color, root.color = root.color, newNode.color
    return newNode

def rotateRight(root):
    newNode = root.left
    root.left = newNode.right
    newNode.right = root
    newNode.color, root.color = root.color, newNode.color
    return newNode

def flipColor(node):
    node.color = RED
    node.left.color = BLACK
    node.right.color = BLACK

def isRed(node):
    if node is None:
        return False
    return  node is None or node.color == RED

def printTree(root):
    tree = []
    travel(root, tree)
    for level in tree:
        print(level)

def printLog(string, debug):
    if debug:
        print(string)

def insert(node, val, debug = False, level = 1):
    
    if node is None:
        return Node(val)
    printLog(f"node.val {node.val} insert {val}", debug)
    if node.val > val:
        printLog(f"  inserting node, val = {val} to the left of {node.val}", debug)
        node.left = insert(node.left, val, debug, level + 1)
       
    elif node.val < val:
        printLog(f"  inserting node, val = {val} to the right of {node.val}", debug)
        node.right = insert(node.right, val, debug, level + 1)
    printLog(f"{level * ' '} {node.val} After insert {val}", debug)
    if isRed(node.left) and isRed(node.right):
        printLog(f"    {node.val} both child is red so we flip color ", debug)
        flipColor(node)
    if isRed(node.right) and not isRed(node.left):
        printLog(f"    {node.val} red node was on the right, so we rotate left", debug)
        node = rotateLeft(node)
    printLog(f"{level * ' '}still in {level * ' '} {node.val} After insert {val}", debug)
    if isRed(node.left) and isRed(node.left.left):
        printLog(f"    {node.val} two red nodes consecutive so we rotate right", debug)
        node = rotateRight(node)
        # printTree(node)
    printLog(f"{level * ' '} still in {level * ' '} {node.val} After insert {val}", debug)
    
    printLog(f"{level * ' '} {node.val} finish call stack for inserting {val}", debug)
    
    return node
def travel(node, treeAsArray, level = 0):
    if node is None:
        return
    if level == len(treeAsArray):
        treeAsArray.append([])
    travel(node.left, treeAsArray, level + 1)
    treeAsArray[level].append((node.val, "R" if node.color else "B"))
    travel(node.right, treeAsArray, level + 1)
    

root = Node("S")
root.color = BLACK

root = insert(root, "E")
root = insert(root, "A", True)

printTree(root)
