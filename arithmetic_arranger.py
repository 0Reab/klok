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
        #for loop x2, i pretvaram z na indeksu 0 i 2 u ints ako to ne mogu return error

        for i in lst:

            try:
                val1 = int(i[0])
            except:
                print("Error: Numbers must only contain digits.")
                break

            try:
                val2 = int(i[2])
            except:
                print("Error: Numbers must only contain digits.")
                break

            oper = i[1]

            try:
                operat = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y}
                result.append(operat[i[1]](int(i[0]), int(i[2])))

            except:
                print("Error: Operator must be '+' or '-'.")
                break


        if bool == True:
            print(f'')

print(arithmetic_arranger(["1 + 8", "1 + 3801", "9999 + 9999", "523 - 49"], True))
