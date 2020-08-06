# iterative easy single 

output = [[]]

nums = [1, 2, 3]

for i in nums:
    output = output + [lst + [i] for lst in output]
    print(output)


# Do recursive too using binary representation ..
