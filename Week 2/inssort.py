
import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment

for i in range(1,n):
    temp = a[i]
    j = i-1
    while j >= 0 and a[j] > temp:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp
    
et = time.process_time()

print(a)
print(et-st)
