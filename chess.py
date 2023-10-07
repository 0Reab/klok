squares = [1,2,3,4,5,6,7,8]
board = list()
temp_dict = ['a',
             'b',
             'c',
             'd',
             'e',
             'f',
             'g',
             'h']

for i in temp_dict:
    board.append(temp_dict[0]+str(squares[0+i]))

print(board)