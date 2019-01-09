rows = int(input('Enter no of rows: '))
col = int(input('Enter no of col: '))
# print(rows,col)
def drw(rows,col):
    for row in range(rows*2-1):
        if row%2 == 0:
            for cols in range(1,col*2):
                if cols%2 == 1:
                    if cols != col*2-1:
                        print(' ', end = '')
                    else:
                        print(' ')
                else: print('|',end = '')
        else: print('-'*(col*2-1))
    return True
# drw(rows,col)
x = drw(rows,col)
print(x)
