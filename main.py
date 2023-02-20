class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        #
        if node is None:
            return None, parent, False

        #
        if value == node.data:
            return node, parent, True

        #
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        #
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        #
        return node, parent, False

    #
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    #
    def __del__leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del__one__child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    #
    def show_tree_show(self, node):
        #
        if node is None:
            return

        #
        self.show_tree_show(node.left)
        print(node.data)
        self.show_tree_show(node.right)

    #
    def show_tree_upend(self, node):
        #
        if node is None:
            return

        #
        self.show_tree_show(node.right)
        print(node.data)
        self.show_tree_show(node.left)

    #
    def show_wind_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    #
    def __find__min(self, node, parent):
        if node.left:
            return self.__find__min(node.left, node)

        return node, parent

    #
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del__leaf(s, p)

        elif s.left is None or s.right is None:
            self.__del__one__child(s, p)

        else:
            sr, pr = self.__find__min(s.right, s)
            s.data = sr.data
            self.__del__one__child(sr, pr)


def main():
    v = [10, 5, 7, 16, 13, 2, 20, 18, 24, 20, 17, 19, 26, 30]

    t = Tree()

    for x in v:
        t.append(Node(x))

    t.show_wind_tree(t.root)


if __name__ == '__main__':
    main()
