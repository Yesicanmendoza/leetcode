"""Counting camaras, if  ">"  and "<" are cars moving in oposites lanes, and "." are cameras
how many cameras they will cross
input '>>>.<<<'
output 6
'.>.<.>' 4
'<<<<.>>>>' 0
 """
def count_cam(S):
    
    car_l = 0
    cam_l = 0

    car_r = 0
    cam_r = 0

    i_cam_l = None
    i_cam_r = None

    
    if len(S) <= 1:
        return 0


    for i, char in enumerate(S):
        if char == '>':
            car_l += 1
            i_car_l = i

        if char == '.' and car_l > 0:            
            cam_l +=1
            i_cam_l = i

    for i in range(len(S)-1, -1, -1):
        if S[i] == '<':
            car_r += 1
            i_car_r = i

        if S[i] == '.' and car_r > 0:            
            cam_r +=1
            i_cam_r = i
    print(car_l, cam_l,    car_r, cam_r)

    if i_car_l and  i_cam_l and i_car_l > i_cam_l:
        car_l -= 1

    if i_car_r and i_cam_r and i_car_r < i_cam_r:
        car_r -= 1

    print(car_l, cam_l,    car_r, cam_r)
    return car_l*cam_l + car_r*cam_r     

