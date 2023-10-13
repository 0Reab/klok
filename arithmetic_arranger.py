def arithmetic_arranger(x,bool):
    lst = list()
    for i in x:
        lst.append(i.split())
    print(lst)

    for i in lst:
        for z in i:
            result = list()
            op = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y}
            res = op['+'](z[0], z[2])

            print(result)


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))