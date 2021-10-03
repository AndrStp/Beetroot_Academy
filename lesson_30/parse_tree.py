"""
Task 1

Extend the `build_parse_tree` function to handle mathematical expressions 
that do not have spaces between every character.
===============================================================================
Task 2

Modify the `build_parse_tree` and `evaluate functions to handle boolean statements 
(and, or, and not). Remember that “not” is a unary operator, so this will 
somewhat complicate your code.
===============================================================================
Task 3

Clean up the `print_exp` function so that it does not include an 
‘extra’ set of parentheses around each number.
===============================================================================
"""



import operator
from typing import Generic, TypeVar, List
from oop_tree import BinaryTree


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """Return True if empty, False otherwise"""
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def parse_expression(math_exp: str) -> list:
    operators = ['+', '-', '*', '/', '(', ')']
    splited = []
    temp = ''
    for index in range(len(math_exp)):
        if temp and not math_exp[index].isdigit():
            splited.append(temp)
            temp = ''
        if math_exp[index] in operators:
            splited.append(math_exp[index])
        elif math_exp[index].isdigit():
            temp += math_exp[index]
    return splited


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = parse_expression(math_exp)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree: BinaryTree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child())+')'
    return s_val


if __name__ == "__main__":
    expression1 = "((10+5)*3)"
    expression2 = "((7+3)*(5-2))"
    pt: BinaryTree = build_parse_tree(expression2)
    print(evaluate(pt))
    # # print()
    # # pt.pre_order()
    # # print()
    # # pt.post_order()
    # # print()
    # # pt.in_order()
    # # print("__")
    # print(print_exp(pt))

