class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ...

    def __find(self, key, node, least_deep=False):
        if node is None:
            return None
        if key < node.key:
            return self.__find(key, node.left, least_deep)
        elif key > node.key:
            return self.__find(key, node.right, least_deep)
        elif least_deep:  # If least_deep is True, search for the least deep node
            return self.__find(key, node.left, least_deep) or self.__find(key, node.right, least_deep)
        else:  # By default, return the deepest node
            return node

    def search(self, key, least_deep=False):
        return self.__find(key, self.root, least_deep)

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            current = self.root
            while current:
                if key == current.key:
                    if current.left is None:
                        current.left = Node(key, data)
                        return
                    current = current.left
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, data)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, data)
                        return
                    current = current.right

    def delete(self, key):
        def find_deepest(node):
            if node.right:
                return find_deepest(node.right)
            return node

        def delete_deepest(node, deepest):
            if node.right is deepest:
                node.right = None
            else:
                delete_deepest(node.right, deepest)

        if self.root is None:
            return
        if self.root.key == key:
            if self.root.left:
                deepest = find_deepest(self.root.left)
                self.root.key, self.root.data = deepest.key, deepest.data
                delete_deepest(self.root.left, deepest)
            else:
                self.root = self.root.right
        else:
            current = self.root
            parent = None
            while current and current.key != key:
                parent = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
            if current:
                if current.left:
                    deepest = find_deepest(current.left)
                    current.key, current.data = deepest.key, deepest.data
                    delete_deepest(current.left, deepest)
                else:
                    if parent.left is current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
