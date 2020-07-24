def unique(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    x = [i for i, j in dic.items() if dic[i] > 1]
    print(x)


unique("asdfgha")
