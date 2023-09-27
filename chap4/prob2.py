import random

# Hero : hero's HP, Mon : monster's HP / 히어로와 몬스터 HP 모두 처음에 50~100사이에서 랜덤으로 받음
Hero = random.randrange(50, 100)
Mon = random.randrange(50, 100)

# 시행횟수 변수 cnt
cnt = 0

# 1행에 처음에 랜덤으로 받은 상태 표시
print("Hero HP:", Hero, ", Monster HP:", Mon)

# 무한반복, 히어로 공격력과 몬스터 공격력 모두 -10~20사이에서 랜덤으로 받음
while True:
    Hero_att = random.randrange(-10, 20)
    Mon_att = random.randrange(-10, 20)
                
    # 히어로 공격력이 0초과일때 result1이 success, 아닐때는 fail 받음
    if Hero_att > 0:
        result1 = "success"
    else:
        result1 = "fail"
                                                        
    # result2도 result1과 동일
    if Mon_att > 0:
        result2 = "success"
    else:
        result2 = "fail"
                                                                                                
    print("hero(HP:", Hero, ", attack:", Hero_att, ")", result1, "<->", "monster(HP:", Mon, ", attack:", Mon_att, ")", result2)
                                                                                                        
    # 히어로와 몬스터 중 하나라도 0이하의 수가 나오면 멈춤
    if Hero <= 0 or Mon <= 0:
        break
                                                                                                                           
    if Hero_att > 0:
        Mon = Mon - Hero_att
    else:
        Mon = Mon - 0
                                                                                                                

    if Mon_att > 0:
        Hero = Hero - Mon_att
    else:
        Hero = Hero - 0                                                 

    cnt = cnt + 1

print("------------------------------------")

print("Total phase:", cnt, ",")   

# 몬스터의 HP가 0보다 작으면 히어로가 이김, 그 외의 경우 몬스터가 이김
if Mon < 0:
    print("Hero Win!!!!")
else:
    print("Monster Win!!!!")

