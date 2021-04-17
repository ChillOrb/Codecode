def subsets(Nums):
    def backtrack(nums, curr):

        if list(curr) not in res:
            res.append(list(curr.copy()))
# everything is done in curr list. then append curr list to res.
        for i in range(len(nums)):                   # For loop
            curr.append(nums[i])                     # Chose
            # Explore  We do i+1 to run same loop on i+1th element it is not same as for i in range
            backtrack(nums[i+1:], curr)
            curr.pop()  # unchose
    res = []
    backtrack(Nums, [])
    return res


print(subsets([1, 2, 2]))

# def letterCasePermutation(S):
#     def backtrack(s, path):
#         if len(path) == len(S):
#             res.append(path)
#             return
#         for i in range(len(s)):
#             if s[i].isnumeric():
#                 path=path+s[i]
#                 backtrack(s[i+1:], path+s[i])

#             else:
#                 backtrack(s[i+1:], path+s[i].upper())
#                 backtrack(s[i+1:], path+s[i].lower())
#     res = []
#     backtrack('a1b2', "")
#     return res

# letterCasePermutation('a1b2')

# def subsets(A, output, result):
#     if len(A) == 0:
#         output.append(result)
#         return

#     L = result[:]
#     R = result[:]
#     R.append(A[0])
#     A = A[1:]
#     subsets(A, output, R)
#     if result == L:
#         break

#     subsets(A, output, L)


# A = [1, 2, 3]
# output = []
# result = []

# subsets(A, output, result)
# print(output)
