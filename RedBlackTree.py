class Node:
    def __init__(self, value):
        self.value = value
        self.red = True
        self.left = None
        self.right = None
        self.parent = None


class RedBblackTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        current_node = self.root
        while current_node is not None and value != current_node.value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            node.red = False
            self.root = node
            return 'No root'
        last_node = self.root
        while last_node is not None:
            potential_parent = last_node
            if node.value < last_node.value:
                last_node = last_node.left
            else:
                last_node = last_node.right

        node.parent = potential_parent

        if node.value < node.parent.value:
            node.parent.left = node
        else:
            node.parent.right = node
            
        node.left = None
        node.right = None
        self.balance_tree(node)

    def balance_tree(self, node):
        try:
            while node.parent.red is True and node is not self.root:
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    if uncle.red:
                        node.parent.red = False
                        uncle.red = False
                        node.parent.parent.red = True
                        node = node.parent.parent
                    else:
                        if node == node.parent.right:
                            node = node.parent

                else:
                    try:
                        uncle = node.parent.parent.left
                        if uncle.red:
                            node.parent.red = False
                            uncle.red = False
                            node.parent.parent.red = True

                    except AttributeError:
                        print('No uncle')
                        break

            self.root.red = False
        except AttributeError:
            print('Tree done')
