# https://leetcode.com/problems/target-sum/


def targetsum(arr, S, curr, counter):
    if sum(curr) == S:
        counter += 1

    for i in range(0, len(arr)):
        arr[i] = -1*arr[i]
        curr.append(arr[i])
        targetsum(arr[i+1:], S, curr, counter)
        if sum(curr) == S:
            counter += 1
        arr[i] = abs(arr[i])
        curr.append(arr[i])
        targetsum(arr[i+1:], S, curr, counter)
        if sum(curr) == S:
            counter += 1
    curr.pop()
    return counter


arr = [1, 1, 1, 1, 1]
curr = []
j = 0
counter = 0
print(targetsum(arr, 3, curr, counter))
