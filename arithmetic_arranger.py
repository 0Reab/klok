from icecream import ic
def arithmetic_arranger(x, bool):
    if len(x) > 5:
        print("Error: Too many problems.")

    else:
        lst = list()
        result = list()

        for i in x:
            lst.append(i.split())
        #print(lst)

        if len(x) > 5:
            print("Error: Too many problems.")
        ic(lst)
        #for loop x2, i pretvaram z na indeksu 0 i 2 u ints ako to ne mogu return error
        for i in lst:
            for z in i:
                ic(z[0])

            ic(type(i[0]))
            # if not all(isinstance(z, int) for z in [int(i[0]), int(i[2])]):
            #     print("Error: Numbers must only contain digits.")
            #     break

            val1 = int(i[0])
            val2 = int(i[2])
            oper = i[1]


            if oper == ("+", "-"):
                print("Error: Operator must be '+' or '-'.")
                break

            # ic(type(val1))
            # ic(type(val2))
            #
            # ic(isinstance([val1, val2], int))
            # ic(isinstance(val1, int))
            #ic(not all(isinstance(i, int) for i in [val1, val2]))


            # if isinstance((val1, val2), int) != True:
            #     print("Error: Numbers must only contain digits.")
            #     break

            else:
                operat = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y}
                result.append(operat[i[1]](int(i[0]), int(i[2])))

        if bool == True:
            print(f'')


print(arithmetic_arranger(["a + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
