from queue import Queue

# Node class
class Node:
    # Initial function
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# Binary Tree class
class BinaryTree:

    # Initial function
    def __init__(self):
        self.root = Node(None, None, None)
        self.root = None

    # Insert function
    def insert(self, value):
        newNode = Node(value, None, None)

        if self.root is None:
            self.root = newNode
        else:
            current = self.root

            while True:
                previous = current
                if value <= current.data:
                    current = current.left
                    if current is None:
                        previous.left = newNode
                        return None
                else:
                    current = current.right
                    if current is None:
                        previous.right = newNode
                        return None
    
    # Search function
    def search(self, value):
        if self.root is None:
            return None

        level = 0
        
        current = self.root
        
        while current.data != value:

            if value < current.data:
                level += 1

                current = current.left
            else:
                level += 1
                
                current = current.right
            
            if current is None:
                return None
        
        print(f'This value was found in LEVEL[{level}]')

        return current
    
    # Function that put tree in order
    def inOrder(self, current):
        if current != None:
            self.inOrder(current.left)
            print(current.data, end=' ')
            self.inOrder(current.right)

    # Function that put tree in pre order
    def preOrder(self, current):
        if current != None:
            print(current.data, end= ' ')
            self.preOrder(current.left)
            self.preOrder(current.right)

    # Function that put tree in pos order
    def posOrder(self, current):
        if current != None:
            self.posOrder(current.left)
            self.posOrder(current.right)
            print(current.data, end=' ')

    # Function that put tree in level
    def inLevel(self, current):
        if current is None:
            return None

        queue = Queue()
        queue.put(current)

        while(not queue.empty()):
            node = queue.get()

            if node is None:
                continue

            print(node.data, end=' ')
            queue.put(node.left)
            queue.put(node.right)

    # Test
    def treeHeight(self, current):
        if current is None or current.left is None and current.right is None:
            return 0
        else:
            if self.treeHeight(current.left) > self.treeHeight(current.right):
                return 1 + self.treeHeight(current.left)
            else:
                return 1 + self.treeHeight(current.right)
                
    # Function that show the result related to tree
    def throughTree(self):
        if self.root is not None:
            print('\n**Results(Orders):')
            print('\nTree in order: ', end='')
            self.inOrder(self.root)
            print('\nTree in Pre Order: ', end='')
            self.preOrder(self.root)
            print('\nTree in Pos Order: ', end='')
            self.posOrder(self.root)
            print('\nTree in Level: ', end='')
            self.inLevel(self.root)
            print('\n\n**Results(Specifications):')
            print('\nHeight of Tree: %d' %(self.treeHeight(self.root)))
            print('\n')
        else:
            print('*** Tree has no root, please insert one\n')

# START PROGRAM
print('\n#########################################################')
print('##---------------- PROGRAM BINARY TREE ----------------##')
print('#########################################################\n')

tree = BinaryTree()
option = 0

while option != 4:
    print('[1]: Insert')
    print('[2]: Show')
    print('[3]: Search')
    print('[4]: Stop\n')

    option = int(input('--> '))

    if option == 1:
        value = int(input('Insert a value --> '))
        print('\n')
        tree.insert(value)
    elif option == 2:
        tree.throughTree()
    elif option == 3:
        value = int(input('Insert a value to search in tree --> '))
        print('\n')
        if tree.search(value) != None:
            print('This value was found in Tree\n')
        else:
            print('This value was not found in Tree\n')
        continue
    elif option == 4:
        break
    else:
        print('\n*** Opss, this option does not exist, please choose one of the options\n')
        continue