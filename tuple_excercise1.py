test_tup = (3,7,1,18,9)
k = 2
sorted_tup = sorted(test_tup)
min_k = tuple(sorted_tup[:k])
max_k = tuple(sorted_tup[-k:])
print(min_k,max_k)
output = min_k + max_k
print(f"output : {output}")