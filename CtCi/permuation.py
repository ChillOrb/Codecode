
def permute(l):
    def dfs(path, used, res):
        if len(path) == len(l):
            # note [:] make a deep copy since otherwise we'd be append the same list over and over
            res.append(path[:])
            return

        for i, letter in enumerate(l):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(l), res)
    return res


ans = str(permute((['(', '(', '(', ')', ')', ')'])))
ans = ans.replace(',', '')
print(ans)
