from node import Node

def main():
    l_child = Node("l_child", None, None)
    r_child = Node("r_child", None, None)

    root = Node("root", l_child, r_child)

    print root


main()
