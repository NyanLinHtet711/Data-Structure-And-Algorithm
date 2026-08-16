import time

K = int(input())
a = list(map(int, input().split()))  # for reading a sequence of numbers
# a list of integers separated using the split function and converted into int using the map function

st = time.process_time()

found = False
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i]*a[j] == K:
            found = True
            break
    if found:
        break

et = time.process_time()

if not found:
    print("No pair exists")
else:
    print(a[i], a[j])
print("running time:", et-st)
