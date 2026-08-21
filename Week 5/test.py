
table_size = 12     # set table size here
hash_table = [[] for i in range(table_size)]

def hash_func(s):
    char_lst = []
    value = 0
    for char in s:
        char_lst.append(char)
    for each in char_lst:
        value += ord(each)
    return value%table_size

print(hash_func("I"))
print(hash_func("II"))
print(hash_func("III"))
print(hash_func("IV"))
print(hash_func("LXXXI"))

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    h = hash_func(s)
    hash_table[h].insert(0,(s,v))
    return 0

def search(s):
    # return value of the key or
    # return -1 if s does not exist in hash table
    hash_val = hash_func(s)
    for each in hash_table[hash_val]:
        if each[0] == s:
            return each[1]
    return -1

def delete(s):
    hash_val = hash_func(s)
    if search(s) == -1:
        return -1
    else:
        hash_table[hash_val] = None
        return 0







