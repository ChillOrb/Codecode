def combine(arr, curr):
    if len(curr) == k:
        res.append(curr)
        return res
    for i in range(0, len(arr)):
        curr.append(arr[i])
        combine(arr[i+1:], curr)
        curr.pop()
    


n = 4
k = 2
arr = [x for x in range(1, n+1)]
curr = []
res = []
print(combine(arr, curr))
