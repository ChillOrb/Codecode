

def solve(ip, op, final):
    if len(ip) == 0:
        final = op
        print((final))
        return

    if ip[0].isalpha():
        op1 = str(op)
        op2 = str(op)
        op1 = str(op)+(ip[0].lower())
        op2 = str(op)+(ip[0].upper())
        ip = ip[1:]
        solve(ip, op1, final)
        solve(ip, op2, final)

    else:
        op1 = op
        op2 = op
        op1 = str(op)+(ip[0])
        op2 = str(op)+(ip[0])
        ip = ip[1:]
        solve(ip, op1, final)


if __name__ == "__main__":
    ip = "a1b2"
    op = []
    final = []
    solve(ip, op, final)
