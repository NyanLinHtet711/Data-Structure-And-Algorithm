import sys

from priorityqueue import *

class HeapNode:
    def __init__(self, key):
        self.key = key
        self.v

    def precede(self, x):
        return self.key < x.key   # do not use <= or >=

    def assign(self, v):  # v must be of higher priority value than the current key
        x = MyClass(v)  # x is a local temporary instance
        if not self.precede(x):
            self.key = v
            return True
        else:
            return False


V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v,w = map(int, input().split())
    adj_list[u].append((v,w))
    #IMPORTANT: Prim's require 2 way connection representation
    adj_list[v].append((u,w))


def Prim_MST(r):
    total = 0
    l = []
    parent = [None] * V
    for u in range(V):
        U = HeapNode(sys.maxsize)
        l.append(U)

    l[r].key = 0
    Q = Priority_Queue()
    for U in l:
        Q.enqueue(U)


    while not Q.empty():
        u = Q.dequeue()
        print(u.key)
        for v,w in adj_list[u.key]:
            if v in (map(lambda a:a.key, pq.a)) and w < v.key:

                total += u.key
                parent[v] = u
                Q.elevate_key(v,w)

    return total

print(Prim_MST(0))