def stacksort(stack1):

    temp = []
    curr = 0

    while stack1 != []:

        curr = stack1.pop()

        if temp == [] or curr > temp[-1]:
            temp.append(curr)

        else:
            j = True

            while j:
                if curr < temp[-1]:
                    stack1.append(temp.pop())
                    if len(temp) == 0:
                        j = False # This is if temp is empty , we will jsut want to add curr to stack temp then 
                else:
                    j = False  # This is so that it exits and enters > condition in a way that it just appends curr , not really entring the > condioton but just logically
                    
            temp.append(curr)

    return temp


stack1 = [3, 4, 1, 7, 2, 9]

print(stacksort(stack1))
