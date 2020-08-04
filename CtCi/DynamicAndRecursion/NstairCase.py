
# same as fibo , cuz ways to climb n stairs is actually n-1 + n-2 ways.
#O(n) time
#memoization too
def stairs(n):
    store = {}
    if n == 1 or n == 2:
        return n
    elif n in store:
        return store[n]

    else:
        store[n] = helper(n-1)+helper(n-2)
        return store[n]

    return stairs(n)


print(stairs(10))
