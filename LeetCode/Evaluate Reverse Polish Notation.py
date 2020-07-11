class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == '+': res = left + right
                if token == '-': res = left - right
                if token == '*': res = left * right
                if token == '/': res = left / right
                stack.append(int(res))
        return stack.pop()
Comments: 0
