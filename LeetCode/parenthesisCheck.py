 stack = []
    ans = "balanced"
    dic = {'(' : ')', '{' : '}', '[' : ']'}
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif not stack or dic[stack.pop()] != i:
            ans = "not balanced"
            break
    if stack:
        ans = "not balanced"
    return ans
