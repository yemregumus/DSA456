class bstList:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            self.data = data
            return
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = bstList(data)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = bstList(data)

    def find_height(self):
        if self is None:
            print("Tree is empty!")
            return -1

        left = self.left.find_height() if self.left else -1
        right = self.right.find_height() if self.right else -1

        return max(left, right) + 1

    def find_min(self):
        if self is None:
            print("Tree is empty!")
            return -1
        current = self

        while current.left != None:
            current = current.left
        return current

    def find_max(self):
        if self is None:
            print("Tree is empty!")
            return -1
        current = self

        while current.right != None:
            current = current.right
        return current

    def traverse_preorder(self):
        if self is not None:
            print(self.data)
            if self.left:
                self.left.traverse_preorder()
            if self.right:
                self.right.traverse_preorder()

    def traverse_inorder(self):
        if self is not None:
            if self.left:
                self.left.traverse_inorder()
            print(self.data)
            if self.right:
                self.right.traverse_inorder()

    def traverse_postorder(self):
        if self is not None:
            if self.left:
                self.left.traverse_postorder()
            if self.right:
                self.right.traverse_postorder()
            print(self.data)

    def is_subtree_Lesser(self, val):
        if self is not None:
            if self.data > val:
                is_subtree_Greater(self.left, val)
                is_subtree_Greater(self.right, val)
                return True
            else:
                return False
