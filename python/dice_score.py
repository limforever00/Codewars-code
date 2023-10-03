def score(dice):
    dice_dic = {}
    # score_dic = {1 : 1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    # 1과 5일경우에만 추가 점수기때문에 점수계산할때 1,5일경우만 추가점 주는게 더 간단
    score_dic= {1 : 100 , 2:200, 3:300, 4:400, 5:50, 6:600}

    for d in dice:
        dice_dic[d] = dice_dic.get(d,0) +1


    sum = 0

    # for key in dice_dic:
    #     if dice_dic[key] >= 3:
    #         sum += score_dic[key]
    #         dice_dic[key] = dice_dic[key]-3    

    #     if key == 1:
    #         sum += dice_dic[key] * 100
    #     elif key == 5:
    #         sum += dice_dic[key] * 50

    for key, val in dice_dic.items():
        print(key,val)
        if val >= 3 :
            if key == 1:
                sum += 1000
            elif key == 5:
                sum += 500
            else :
                sum += score_dic[key]
            val -= 3
        
        if key == 1 or key == 5:
            sum += score_dic[key] * val
    
    return sum

a = score([5,1,3,4,1]) # 250
print(a)