
import time

n = list(map(int, input().split()))

l = len(a)

st = time.process_time()


for i in range(1,l):
    temp = n[i]
    j = i-1
    while j >= 0 and n[j] > temp:
        n[j+1] = n[j]
        j -= 1
    n[j+1] = temp
    
et = time.process_time()

print(n)
print(et-st)
