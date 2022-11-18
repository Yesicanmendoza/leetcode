lst = [[1,2,3], [4,5,6], [7,8,9]]
new_lst = [[0,0,0], [0,0,0], [0,0,0]]
n = len(lst)-1
for i in range(len(lst)):
    for j in range(len(lst[i])):
        new_lst[i][j] = lst[n-j][i]
        

