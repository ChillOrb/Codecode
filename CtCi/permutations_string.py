# Pg 43 Permutaions of a string in python

def permutaions(word):
    if len(word) == 1:
        return [word]

    perms = permutaions(word[1:])
    char = word[0]
    result = []
    for perm in perms:

        for i in range(0, len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result


print(permutaions('abc'))
