# matrices = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrices[2][1])
row1 =[1,2,3]
row2 = [4,5,6]
row3 =[7,8,9]
matrice = [row1,row2,row3]
position = input("which position do you want to locate?")
row_number = int(position[0])
column_number =int(position[1])
row_selected = matrice[row_number-1]
row_selected[column_number -1]='p'
print(matrice)