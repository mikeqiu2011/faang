def calc_rainwater_to_trap(tank):
    pl = 0
    max_left = tank[pl]
    pr = len(tank) - 1
    max_right = tank[pr]
    total_water = 0

    while pl < pr:
        # if max_left <= max_right:
        if tank[pl] <= tank[pr]:
            if tank[pl] <= max_left: # calc water
                total_water += max_left - tank[pl]
            else:
                max_left = tank[pl] # update maxleft
            # move pl to the right
            pl += 1
        else:
            if tank[pr] <= max_right:
                total_water += max_right - tank[pr]
            else:
                max_right = tank[pr]
            pr -= 1
    return total_water


tank = [0,1,0,2,1,0,3,1,0,1,2]
# tank = [0,1,0,2,1,0,3,1,0,1,1]
# tank = [0,1,0,2]
result = calc_rainwater_to_trap(tank)
print(result)
