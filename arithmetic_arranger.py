def arithmetic_arranger(x,bool):
    if len(x) > 5:
        print("Error: Too many problems.")

    else:
        lst = list()
        result = list()

        for i in x:
            lst.append(i.split())
        print(lst)

        if len(x) > 5:
            print("Error: Too many problems.")

        for i in lst:
            val1 = i[0]
            val2 = i[2]
            oper = i[1]

            operat = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y}
            result.append(operat[i[1]](int(i[0]), int(i[2])))

        if bool == True:
            print(f'')

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))