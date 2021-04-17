# def letterCasePermutation(S):
#     res = []

#     def backtrack(s, path):
#         if len(path) == len(S):
#             res.append(path)
#             return
#         if s[0].isnumeric():
#             backtrack(s[1:], path + s[0])
#         else:
#             backtrack(s[1:], path + s[0].upper())
#             backtrack(s[1:], path + s[0].lower())

#     backtrack('a1b2', "")
#     return res


# print(letterCasePermutation('a1b2'))

#  AND  is these same ?? look at backtrack(s[i+1:]with for loop, path+s[i]) and backtrack(s[1:], path + s[0].upper())
#

def letterCasePermutation(S):
    res = []

    def backtrack(s, path):
        if len(path) == len(S):
            res.append(path)
        for i in range(len(s)):
            if s[i].isnumeric():
                backtrack(s[i+1:], path+s[i])
            else:
                backtrack(s[i+1:], path+s[i].upper())
                backtrack(s[i+1:], path+s[i].lower())

    backtrack('a1b2', "")
    return res


print(letterCasePermutation('a1b2'))


# Works because when we do s[i+1:] for loop runs a little ahead and adds to path but len(s) gets to 0 faster
# so basically of we write the correct base condition we can do s[i+1] along with for loop = s[1:] without for loop . BUT MAKE SURE S and s are different

# JAb tak i=0 chalra hai normally chalra hai , jaise hi s[i+1] hua for loop skip hone laga and s='' hua but path==S satisfy nahi hua

# http://pythontutor.com/visualize.html#code=def%20letterCasePermutation%28S%29%3A%0A%20%20%20%20res%20%3D%20%5B%5D%0A%20%20%20%20def%20backtrack%28s,%20path%29%3A%0A%20%20%20%20%20%20%20%20if%20len%28path%29%20%3D%3D%20len%28S%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20res.append%28path%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s%5Bi%5D.isnumeric%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20backtrack%28s%5Bi%2B1%3A%5D,%20path%2Bs%5Bi%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20backtrack%28s%5Bi%2B1%3A%5D,%20path%2Bs%5Bi%5D.upper%28%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20backtrack%28s%5Bi%2B1%3A%5D,%20path%2Bs%5Bi%5D.lower%28%29%29%0A%0A%0A%20%20%20%20backtrack%28'a1b2',%20%22%22%29%0A%20%20%20%20return%20res%0A%20%20%20%20%0AletterCasePermutation%28'a1b2'%29&cumulative=false&curInstr=52&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
