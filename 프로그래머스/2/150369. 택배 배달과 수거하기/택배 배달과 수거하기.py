    
'''
1, 0, 2, 0, 1, 0, 2
0, 2, 0, 1, 0, 2, 0


7번집 2개 챙겨감
올 때 6번집 2개 챙겨옴
7 + 7

1번 3번집 챙겨감
올 때 4번집 1개 챙겨옴
5 + 5

3번집 2개 챙겨감
2번집 2개 챙겨옴
3+ 3
'''

'''    answer = -1
    
    is_delivering = 0
    
    dp = n-1
    pp = n-1
    far_point = n-1
    
    sum_d = sum(deliveries)
    sum_p = sum(pickups)
    
    ans = 0
    while sum_d > 0 and sum_p > 0:
        
        if is_delivering == 0:
            rlt, place = caring_cargo(far_point, deliveries, cap)
            sum_d -= rlt
            dp = max(place, 0)
            # print("=====================")
            # print("deliever", rlt, place, sum_d)
            # print("left", deliveries)
            # print("dp", dp)
            # print("=====================")
        else : # is_pickup
            rlt, place = caring_cargo(far_point, pickups, cap)
            sum_p -= rlt
            pp = max(place, 0)
            # print("=====================")
            # print("pickup", rlt, place, sum_p)
            # print("left", pickups)
            # print("pp", pp)
            # print("=====================")
        
        ans += (far_point+1)
        
        is_delivering += 1
        if is_delivering == 2:
            is_delivering = 0
            far_point = max(dp, pp)
            # print("far point", far_point)
    ans += (far_point+1)'''

def caring_cargo(place, target, capacity):
    rlt = 0
    while (capacity != rlt) and (place >= 0):
        count = target[place]
        
        if (count + rlt) < capacity:
            target[place] = 0
            rlt = rlt + count
            place -= 1
        elif (count + rlt) == capacity:
            target[place] = 0
            rlt = rlt + count
            place -= 1
        elif (count + rlt) > capacity:
            target[place] = (count + rlt - capacity)
            rlt = capacity

    while target[place]<= 0 and place > 0:
        place -= 1
        
    return rlt, place

def solution(cap, n, deliveries, pickups):
    
    ans = 0

    have_to_deliever = 0
    have_to_pickup = 0
    for i in range(n-1, -1, -1):
        have_to_deliever += deliveries[i]
        have_to_pickup += pickups[i]
        
        while have_to_deliever > 0 or have_to_pickup > 0:
            have_to_deliever -= cap
            have_to_pickup -= cap
            ans += (i+1)*2
            # print(i)
    return ans