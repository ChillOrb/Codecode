

class StackWithMin:
    def __init__(self):

        self.mainStack = []

      
        self.trackStack = []

    def push(self, x):
        self.mainStack.append(x)
        if (len(self.mainStack) == 1):
            self.trackStack.append(x)
            return

       
        if (x < self.trackStack[-1]):
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])

    def getMin(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()


# Driver Code
if __name__ == '__main__':

    s = StackWithMax()
    s.push(20)
    s.push(23)
    s.push(60)
    s.push(700)
    print(s.getMin())


