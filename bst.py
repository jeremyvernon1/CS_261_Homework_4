# Course: CS261 - Data Structures
# Student Name: Jeremy Vernon
# Assignment: 4
# Description: BST


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the BST
        """
        # establishes root node
        if self.root is None:
            self.root = TreeNode(value)
            return
        # finds position and inserts new node
        current = self.root
        while current is not None:
            # left
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            # right
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def contains(self, value: object) -> bool:
        """
        Searches BST for the given value
        """
        current = self.root
        while current:
            # if value is found
            if current.value == value:
                return True
            # value is less than current value
            elif value < current.value:
                if not current.left:
                    return False
                current = current.left
            # value is more than current value
            elif value > current.value:
                if not current.right:
                    return False
                current = current.right
        return False

    def get_first(self) -> object:
        """
        Returns the value of the root node
        """
        if self.root is None:
            return None
        return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root element, and replaces it if there is a child
        """

        # if empty
        if self.root is None:
            return False

        # if no children
        if self.root.left is None and self.root.right is None:
            self.root = None
            return True

        parent = self.root
        # if left child, but no right children
        if self.root.right is None:
            self.root = self.root.left
            return True
        # if no left child or if both left and right children
        else:
            child = self.root.right
            # if grandchildren
            if child.left and \
                    (child.left.left or child.left.right):
                while child.left:
                    parent = child
                    child = child.left
                parent.left = child.right
                child.right = parent
            # set left branch to new root+
            if self.root.left:
                # if more than one subtree
                if child.left:
                    child = child.left
                    child.right = parent
                child.left = self.root.left
            # set new root
            self.root = child
            return True

    def remove(self, value) -> bool:
        """
        Removes the first node that matches the given value
        """
        above_remove = self.root
        while above_remove:
            # if left child is value to remove
            if above_remove.left and above_remove.left.value == value:
                element_to_remove = above_remove.left
                # if child to remove has no children
                if element_to_remove.left is None and element_to_remove.right is None:
                    above_remove.left = None
                # if child to remove has right child, but no left
                elif element_to_remove.left is None:
                    above_remove.left = element_to_remove.right
                # if child to remove has left child, but no right
                elif element_to_remove.right is None:
                    above_remove.left = element_to_remove.left
                # if child to remove has both left child and right child
                else:
                    # if grandchildren
                    if element_to_remove.left.right:
                        grandchild = element_to_remove.left.right
                        while grandchild.right:
                            grandchild = grandchild.right
                        element_to_remove.left.right = grandchild.left
                        grandchild.right = element_to_remove.right
                        grandchild.left = element_to_remove.left
                        above_remove.left = grandchild
                    else:
                        element_to_remove.right.left = element_to_remove.left
                        above_remove.left = element_to_remove.right
                return True

            # if right child is value to remove
            elif above_remove.right and above_remove.right.value == value:
                element_to_remove = above_remove.right
                # if child to remove has no children
                if element_to_remove.left is None and element_to_remove.right is None:
                    above_remove.right = None
                # if child to remove has right child, but no left
                elif element_to_remove.left is None:
                    above_remove.right = element_to_remove.right
                # if child to remove has left child, but no right
                elif element_to_remove.right is None:
                    above_remove.right = element_to_remove.left
                # if child to remove has both left and right children
                else:
                    # if grandchildren:
                    if element_to_remove.right.left:
                        grandchild = element_to_remove.right.left
                        while grandchild.left:
                            grandchild = grandchild.left
                        element_to_remove.right.left = grandchild.right
                        grandchild.left = element_to_remove.left
                        grandchild.right = element_to_remove.right
                        above_remove.right = grandchild
                    else:
                        element_to_remove.left = element_to_remove.right
                        above_remove.right = element_to_remove.left
                return True

            # continue down the tree
            if value < above_remove.value:
                if above_remove.left is None:
                    return False
                above_remove = above_remove.left
            else:
                if above_remove.right is None:
                    return False
                above_remove = above_remove.right
        # if not found
        return False

    def pre_order_traversal(self) -> Queue:
        """
        Traverses the tree in Root, Left, Right order
        Adds each node to the queue in the order that it is visited
        """
        pre_order_result_Queue = Queue()
        if self.root:

            def pre_order_helper(root):
                if root:
                    pre_order_result_Queue.enqueue(root)
                    pre_order_helper(root.left)
                    pre_order_helper(root.right)

            pre_order_helper(self.root)

        return pre_order_result_Queue

    def in_order_traversal(self) -> Queue:
        """
        Traverses the tree in Left, Root, Right order
        Adds each node to the queue in the order that it is visited
        """
        in_order_result_Queue = Queue()
        if self.root:

            def in_order_helper(root):
                if root:
                    in_order_helper(root.left)
                    in_order_result_Queue.enqueue(root)
                    in_order_helper(root.right)

            in_order_helper(self.root)

        return in_order_result_Queue

    def post_order_traversal(self) -> Queue:
        """
        Traverses the tree in Left, Right, Root order
        Adds each node to the queue in the order that it is visited
        """
        post_order_result_Queue = Queue()
        if self.root:

            def post_order_helper(root):
                if root:
                    post_order_helper(root.left)
                    post_order_helper(root.right)
                    post_order_result_Queue.enqueue(root)

            post_order_helper(self.root)

        return post_order_result_Queue

    def by_level_traversal(self) -> Queue:
        """
        Traverses the tree by level
        Adds each node to the queue in the order that it is visited
        """
        by_level_order_result_Queue = Queue()

        def by_level_helper1(root, level):

            # base case
            if root is None:
                return False

            if level == 1:
                by_level_order_result_Queue.enqueue(root)
                # return true if at least one node is present at a given level
                return True

            left = by_level_helper1(root.left, level - 1)
            right = by_level_helper1(root.right, level - 1)

            return left or right

        def by_level_helper2(root):
            # start from level 1 —— till the height of the tree
            level = 1

            # run till helper1() returns false
            while by_level_helper1(root, level):
                level = level + 1

        by_level_helper2(self.root)

        return by_level_order_result_Queue

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def size(self) -> int:
        """
        Finds the number of nodes in a tree.
        """
        def size_helper(node=self.root):
            if node is None:
                return 0
            else:
                return (size_helper(node.left) + 1 + size_helper(node.right))
            return size

        size = size_helper()
        return size

    def height(self) -> int:
        """
        Returns the height of the tree
        Empty tree returns -1
        """
        def height_helper(node):
            if node is None:
                return 0

            left_height = height_helper(node.left)
            right_height = height_helper(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

        return (height_helper(self.root) - 1)

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

