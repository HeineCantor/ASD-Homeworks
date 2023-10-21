from random import randint

MAX_RAND_GENERATION = 100

class treapNode:
    def __init__(self, key):
        self.key = key
        self.priority = randint(0, MAX_RAND_GENERATION)

        self.left = None
        self.right = None

class treap:
    def __init__(self):
        self.treeRoot = None

    def insertKey(self, key):
        self.treeRoot = self.insert(self.treeRoot, key)

    def insert(self, root : treapNode, key):
        if root == None:            # if also root is None -> first element to insert
            return treapNode(key)
        
        if key >= root.key:
            root.right = self.insert(root.right, key)

            if(root.right.priority < root.priority):
                root = self.rotateLeft(root)
        else:
            root.left = self.insert(root.left, key)

            if(root.left.priority < root.priority):
                root = self.rotateRight(root)

        return root

    def rotateRight(self, node : treapNode = None):
        if node == None:
            node = self.treeRoot

        leftSon = node.left
        rightSonOfLeft = leftSon.right

        node.left = rightSonOfLeft
        leftSon.right = node

        return leftSon

    def rotateLeft(self, node : treapNode = None):
        if node == None:
            node = self.treeRoot

        rightSon = node.right
        leftSonOfRight = rightSon.left

        node.right = leftSonOfRight
        rightSon.left = node

        return rightSon
    
    def printAll(self):
        self.printTree(self.treeRoot)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.key) + "|" + str(node.priority))
            self.printTree(node.left, level + 1)


    def validate(self):
        return False
    

if __name__ == "__main__":
    testTreap = treap()

    for i in range(15):
        testTreap.insertKey(randint(0, MAX_RAND_GENERATION))

    testTreap.printAll()

