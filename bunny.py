flag = 0
name = ""
import random
from time import sleep
player = []       #1조 팀원들!
loser = []                                        
def carrot(user):          #"당근당근" 외치는 함수 설정
    global player
    global flag
    global loser
    _percentage = random.randrange(1,101)
    if (_percentage <= 80):         #성공할 확률
        print(f"({player[user]}) : ㄴ당근ㄱ ㄴ당근ㄱ")   #실수하지 않은 경우
    else:
        flag = 1
        print(f"({player[user]}): 다....ㅇ근 당..")     #실수(탈락)한 경우
        loser.append(player[user])
            
def naega():               # 사용자가 바니바니를 외칠때의 함수
    global player
    global name
    global ind
    
    while True:
        asd = input(f"내차례! 누구에게 바니바니?? -> ({player[0]} , {player[1]} , {player[2]} , {player[3]}) :")    #바니바니 지목할 사람 고르기
        if asd not in player:
            print("누구세요 ??")
            continue
        else: 
            print(f"({name})이 ({asd})에게 : 바니바니")
            break
    
    index = player.index(asd)
    
    left = index - 1 if index-1 >= 0 else 3     
    right = index + 1 if index+1 <= 3 else 0
    
    ind = index
    
    
    carrot(left)        # 지목당한 양옆사람들이 carrot 함수로 돌아가게 만들어 당근당근 외치게 하기
    carrot(right)
    
def com_bnbn():              # 지목을 사용자가 아닌 플레이어가 받았을 때 컴퓨터가 랜덤으로 지목하게 하는 함수
    global name
    global ind
    global player
    ran = random.randrange(0,4)     
    print(f'"({player[ind]}): 바니바니, ({player[ran]}에게) :바니바니"')
    
    left = ran - 1 if ran-1 >= 0 else 3     
    right = ran + 1 if ran+1 <= 3 else 0
     
    ind = ran
    
    carrot(left)        # 지목당한 양옆사람들이 carrot 함수로 돌아가게 만들어 당근당근 외치게 하기
    carrot(right)

    
def game(userName, playerBunny):
    if len(playerBunny) != 4:
        print("친구가 없는 당신!!! 다 같이 한 잔~~!!🍻🍻")
        return playerBunny
    sleep(1)
    print("=====하늘에서 내려온 토끼가 하는 말~=====")
    sleep(1)
    print("=====움chichi 움chichi~ 움chichi 움chichi~=====")
    sleep(1)
    global loser
    global ind
    global name 
    global player
    player = playerBunny
    ind = random.randrange(0,4)
    name = userName
    while True:
        for i in range(2):      #바니바니 외치기 직전마다 딜레이 주기
            print("...")        
            sleep(0.5)
        if (player[ind] == name):   #사용자가 지목 당했을 때 naega 함수 실행
            naega()             
        else:                       #사용자를 제외한 플레이어가 지목 당했을 땐 com_bnbn 함수 실행
            com_bnbn()
        if (flag == 1):
            for i in loser:
                print("누↘가↗ 술을 마셔~~~"+i +"(이)가 술을 마셔~ 쭉!! 쭉쭉! 쭉쭉~! ")
                
            return loser
            
        else:
            continue
        
