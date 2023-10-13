def arithmetic_arranger(x,bool):
    lst = list()
    for i in x:
        lst.append(i.split())
    print(lst)

    for i in lst:
        for x in i:
            if x[1] == "+":
                op = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y}

                print(op['+'](1, 2))


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))