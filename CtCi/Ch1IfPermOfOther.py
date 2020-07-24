def permutaion(word):
    if len(word) == 1:
        return [word]

    perms = permutaion(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(0, len(perm)+1):
            result.append(perm[:i]+char+perm[i:])

    return result


string2 = 'cab'
x = (permutaion("abc"))

for i in x:
    if i == string2:
        print("found")
