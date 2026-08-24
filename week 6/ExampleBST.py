from BST import *



'''
The following code is a specific code that constructs a binary search tree
from the list x. However, it works ONLY BECAUSE the order of the list items
already allow this code to work correctly.

The code below will not work on a generic list. You will need to add
standard operations to BST for it to work on generic data.
'''

x = []
for k in [56,26,200,18,28,190,213,12,24,27]:
    x.append(Node(k, None))

T = BinST()
T.root = x[0]
for i in range(len(x)//2):
    if 2*i+1 < len(x):
        x[i].left = x[2*i+1]
        x[2*i+1].p = x[i]
    if 2*(i+1) < len(x):
        x[i].right = x[2*(i+1)]
        x[2*(i+1)].p = x[i]

Inorder_Tree_Walk(T.root)
