

class StackWithMaitem:
    def __init__(self, capacity):

        self.Stack = []
        if capacity < 1:
            raise NameError('dsa')
        else:
            self.capacity = capacity

    def push(self, item):
        if self.Stack == []:
            self.Stack.append([item])
        else:
            if len(self.Stack[-1]) >= self.capacity:
                self.Stack.append([item])
            else:
                self.Stack[-1].append([item])

    def __str__(self):
        return str(self.Stack)

    def pop(self):
        if self.Stack == []:
            raise NameError('whattss')
        else:
            popped_data = self.Stack[-1][-1]

            if len(self.Stack[-1]) == 1:
                del self.Stack[-1]

            else:

                del self.Stack[-1][-1]

        return popped_data

    def popat(self, index):
        if self.Stack == []:
            raise NameError('whahshds')

        elif index-1 > len(self.Stack):
            raise NameError('out of range')

        else:
            popped_data = self.Stack[index-1][-1]
            if len(self.Stack[index-1]) == 1:
                del self.Stack[-1]

            elif len(self.Stack) == index:
                del self.Stack[-1][-1]

            else:
                self.Stack[index-1][-1] = self.Stack[index][0]

                for i in range(index, len(self.Stack)):

                    for j in range(0, len(self.Stack[i])-1):
                        self.Stack[i][j] = self.Stack[i][j+1]

                    if i < len(self.Stack)-1:
                        self.Stack[i][-1] = self.Stack[i+1][0]

                del self.Stack[-1][-1]

                if len(self.Stack[-1]) == 0:
                    del self.Stack[-1]

        return popped_data


# Driver Code
if __name__ == '__main__':

    s = StackWithMaitem(4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    print(s)

    s.popat(2)
    print(s)
