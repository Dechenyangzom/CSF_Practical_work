
#Step 1: Define the Node Class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Step 2: Implement the Binary Search Tree Class


class BinarySearchTree:
    def __init__(self):
        self.root = None



#Step 3: Implement the Insertion Method


class BinarySearchTree:
    # ... (previous code)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)



#Step 4: Implement the Search Method

class BinarySearchTree:
    # ... (previous code)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Test search
print(bst.search(4))  # Should return a Node
print(bst.search(9))  # Should return None



#Step 5: Implement Traversal Methods

class BinarySearchTree:
    # ... (previous code)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

# Test traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())




#Step 6: Implement the Deletion Method


class BinarySearchTree:
    # ... (previous code)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())



#Exercises



# 1.to find the maximum value in the BST.

class BinarySearchTree:
    def find_max(self):
        if not self.root:
            return None  # If tree is empty
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

print("Maximum value in the BST:", bst.find_max())  


# 2. to count the total number of nodes in the BST.
class BinarySearchTree:
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        left_count = self._count_nodes_recursive(node.left)
        right_count = self._count_nodes_recursive(node.right)
        return 1 + left_count+right_count
    
bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

print("Total number of nodes in the BST:", bst.count_nodes())



# 3.a level-order traversal (breadth-first search) for the BST.

class BinarySearchTree:
      def level_order_traversal(self):
        if not self.root:
            return
        
        queue = deque([self.root])  # Initialize the queue with the root node
        while queue:
            node = queue.popleft()  # Dequeue the front node
            print(node.data, end=" ")  # Visit the node
            
            # Enqueue the left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

print("Level-order traversal of the BST:")
bst.level_order_traversal() 



# 4.a method to find the height of the BST.

class BinarySearchTree:
    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if node is None:
            return -1  # Base case: an empty tree has height -1
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height,right_height)
    
bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

print("Height of the BST:", bst.find_height()) 



# 5.to check if the tree is a valid BST.

class BinarySearchTree:
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True  
        if not (min_value < node.data < max_value):
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.data) and
                self._is_valid_bst_recursive(node.right, node.data,max_value))
    
bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

print("Is the tree a valid BST?", bst.is_valid_bst())  

# Example of an invalid BST
invalid_bst = BST()
invalid_bst.insert(10)
invalid_bst.insert(5)
invalid_bst.insert(15)
invalid_bst.insert(6)  

print("Is the invalid tree a valid BST?", invalid_bst.is_valid_bst())