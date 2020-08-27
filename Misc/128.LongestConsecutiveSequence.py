def longestConsecutive(nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


l = [5, 6, 2, 99, 4, 100, 3]
print(longestConsecutive(l))


#read https://www.geeksforgeeks.org/longest-consecutive-subsequence/

# use a hash map and checking for n-1 is so that we know that we have already calcualted longest subsequence for that sequence. 
