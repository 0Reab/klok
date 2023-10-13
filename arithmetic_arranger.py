def arithmetic_arranger(x,bool):
    lst = list()
    for i in x:
        lst.append(i.split())
    print(lst)

    for i in lst:
        result = list()

        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y}
        print(op[i[1]](int(i[0]), int(i[2])))



print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))