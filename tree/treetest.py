# import operator
# op = operator.add
# n = op(1,2)
# print(n)


# from pythonds.trees import BinaryTree
# import operator
#
# def printexp(tree):
#     sVal = ""
#     if tree:
#         sVal = '(' + printexp(tree.getLeftChild())
#         sVal = sVal + str(tree.getRootVal())
#         sVal = sVal + printexp(tree.getRightChild()) + ')'
#     return sVal
#
# def postordereval(tree):
#     opers = {'+':operator.add, '-':operator.sub,\
#              '*':operator.mul, '/':operator.truediv}
#     res1 = None
#     res2 = None
#     if tree:
#         res1 = postordereval(tree.getLeftChild())
#         res2 = postordereval(tree.getRightChild())
#         if res1 and res2:
#             return opers[tree.getRootVal()](res1,res2)
#         else:
#             return tree.getRootVal()
#
# x = BinaryTree('*')
# x.insertLeft('+')
# l = x.getLeftChild()
# l.insertLeft(4)
# l.insertRight(5)
# x.insertRight(7)
# print(printexp(x))
# print(postordereval(x))

import operator
op = operator.add
n = op(1,3)
print(n)
op1 = operator.mul
m = op1(1,3)
print(m)


