def funcDrop(xCoordinate, yCoordinate):
    #Return the axis with the largest number of points(x,y)
	# Write your code here
    dic_x = {}
    dic_y = {}
    max_x = 0
    max_y = 0
    #x = 0
    #y = 0

    for n in xCoordinate:
        dic_x[n]= 1 + dic_x.get(n, 0)
        tem = max_x
        max_x = max(dic_x.get(n), max_x)
        if tem != max_x:
            x = n

    print('x', dic_x, max_x)

    for n in yCoordinate:
        dic_y[n]= 1 + dic_y.get(n, 0)
        tem = max_y
        max_y = max(dic_y.get(n), max_y)
        if tem != max_y:
            y = n

    print('y', dic_y, max_y)

    if max_x > max_y:
        return max_x

    return max_y