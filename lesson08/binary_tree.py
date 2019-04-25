from random import (
    randint,
    choice
)


class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'Node[{self.value:^5}]'


class Tree:
    def __init__(self) -> None:
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, value=0):
        return Node(value, None, None)

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if right_height < left_height:
                return left_height + 1
            else:
                return right_height + 1

    # функция для вычисления ширины дерева
    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1

        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        elif level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1


def same_tree(a, b):
    if a is None and b is None:
        return 1
    elif a and b:
        return (
            a.value == b.value and
            same_tree(a.left, b.left) and
            same_tree(a.right, b.right)
        )
    return 0


def main():
    t = Tree()
    t.root = t.new_node(8)
    t.root.left = t.new_node(4)
    t.root.right = t.new_node(12)
    t.root.left.left = t.new_node(2)
    t.root.left.right = t.new_node(6)
    t.root.right.left = t.new_node(10)
    t.root.right.right = t.new_node(14)
    t.root.left.left.left = t.new_node(0)
    t.root.left.left.right = t.new_node(3)
    t.root.left.right.left = t.new_node(5)
    t.root.left.right.right = t.new_node(7)
    t.root.right.left.left = t.new_node(9)
    t.root.right.left.right = t.new_node(11)
    t.root.right.right.left = t.new_node(13)
    t.root.right.right.right = t.new_node(15)


    t.print_level_order(t.root)
    print(f'высота: {t.height(t.root)}')
    print(f'ширина: {t.get_max_width(t.root)}')


if __name__ == '__main__':
    main()