def calc(a,b,c,d,e,f,g,h):

    def numFormat(number):
        values = []
        for x in range(len(number)):
            num = ""
            for y in range(len(number[x])):
                num = num + str(number[x][y])
            values.append(num)
        return values


    def trigMode(trigNum):
        if trigNum[0] != 0:
            trigNum[0] = trigNum[0] * trigNum[2]
        else:
            trigNum[0] = trigNum[2]
        if trigNum[1] == "sin":
            trigNum[1] = "cos"


    number = [[a, "x", b], [c, "x", d], [e, "x", f], [g, "sin", h, "x", 0]]
    # trigNum = [2, "x", 3, "x", 0]

    print("Before:", numFormat(number))


    for x in range(len(number)):
        if len(number[x]) == 5:
            trigMode(number[x])
            continue

        if number[x][1] == "sinx":
            number[x][1] = "cosx"
        elif number[x][1] == "cosx":
            number[x][1] = "sinx"
            number[x][0] = number[x][0] * -1
            continue

        if number[x][2] == 0:
            if number[x][0] > 0:
                number[x][1] = number[x][0]
                number[x][0] = 0
            else:
                number[x][1] = 1
        else:
            number[x][0] = number[x][0] * number[x][2]
            number[x][2] -= 1

    print("After:", numFormat(number))
    
calc(2,4,5,6,7,3,5,2)