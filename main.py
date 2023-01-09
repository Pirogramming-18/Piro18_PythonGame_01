import random
import paik
import bunny
import game31
import grapeGame
import guess_game
# {name : [마신 잔 수, 치사량, 게임 시작 여부]}
data = {"용현" : [0, 5, True], "고은" : [0, 5, True], "수현" : [0, 5, True], "현지" : [0, 5, True], "태영" : [0, 5, True]}

#프로그램 실행 시 인트로 출력 함수
def intro():
    pass

# 주량 선택 함수
# 메뉴 번호 입력 시 해당 번호에 해당하는 주량 숫자 반환
def selectAlc():  
    alc = [2,4,6,8,10]  
    showAlcMenu(alc)
    while True:
        try:
            num = int(input("당신의 주량은 얼마나 되나요??(1~5 숫자 선택) : "))
            if(num > 5 or num < 0):
                raise ValueError
            
            return alc[num-1]
        except ValueError:
            print("1~5사이의 숫자를 입력해주세요!!")
            continue
    
# 친구 선택 함수
# 인원 수를 입력하면 data에서 해당 인원 수 만큼 사람을 뽑음
# 반환형: 딕셔너리 {name : [마신 잔 수, 치사량, 게임 시작 여부]}
def selectFriend(player):
    global data
    while True:
        try:
            num = int(input("오늘 함께 기어갈 친구들은 몇 명이나 필요하신가요~?(최대 3명까지 초대 가능합니다!) : "))
            if(num > 3 or num < 1):
                print("친구는 1~3명까지 초대 가능합니다!")
            else:      
                while True:
                    friends = random.sample(list(data.keys()), num)
                    if(player not in friends):
                        friends.append(player)
                        users = {}
                        for user in friends:                            
                            users[user] = data[user]                            
                        return users        
                
        except ValueError:
            print("1~3사이의 정수를 입력해주세요!")

# 게임 선택 함수
# 선택한 메뉴 번호 반환
def selectGame(cur, player):
    showGameMenu()
    while True:
        exit = input(f"술게임 진행 중! {cur}님의 턴 입니다! 그만하고 싶으면 \'exit\'을, 계속하고 싶으면 아무키나 입력해 주세요! : ")
        if(exit == "exit"):
            return True, -1
        try:
            menu = int(input(f"{cur}(이)가 좋아하는 랜덤 게임~ 무슨 게임~? : "))   
            
            if(menu > 5 or menu < 1):
                raise ValueError
            
            return False, menu
        except ValueError:
            print("1~5 사이의 정수를 입력해주세요!")
            
               
# 유저 상태 체크 함수
# 현재 유저들의 상태를 출력하고 치사량 == 마신 잔 수가 된 유저가 있는지 검증
# 치사량에 도달한 유저가 있을 시 True 반환
def checkStatus(users):
    showStatus(users)
    flag = False
    for user in users:
        if(users[user][1] - users[user][0] == 0):
            flag = True
            print(f"{user}님이 전사했습니다... 집까지는 기어서 가시길...")
            
    if(flag):
        showGameOver()
        return True

# 게임을 시작하는 유저 선택 함수
# 랜덤으로 유저를 뽑아오며 한 번이라도 게임을 시작한 적이 있으면 모두 게임을 한 번씩 시작할 때까지 선택 불가
# 모두 한 번 씩 게임을 시작했으면 초기화 진행
# 게임을 시작할 유저 이름 반환
def rotateUser(users):
    cnt = 0
    for user in users:
        if(users[user][2] == False):
            cnt += 1
    
    if(cnt == len(users)):
        for user in users:
            users[user][2] = True
        
    while True:
        target = random.sample(list(users.keys()), 1)
        #게임을 시작한 적이 없는 경우
        if(users[target[0]][2]):
            users[target[0]][2] = False
            return target[0]
    
# 주량 선택 메뉴 화면
def showAlcMenu(alc):
    print("~~~~~~~~~~~~~~~~~~🍻[소주 기준 당신의 주량은?]🍻~~~~~~~~~~~~~~~~~~")
    print(f"                            1. {alc[0]}잔")
    print(f"                            2. {alc[1]}잔")
    print(f"                            3. {alc[2]}잔")
    print(f"                            4. {alc[3]}잔")
    print(f"                            5. {alc[4]}잔")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 현재 상태 화면
def showStatus(users):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for user in users:
        print(f"{user}님은(는) 지금까지 {users[user][0]}잔! 치사량까지 {users[user][1] - users[user][0]}잔!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 게임 선택 메뉴 화면
def showGameMenu():
    print("~~~~~~~~~~~~~~~~~~🍻[오늘의 술 게임]🍻~~~~~~~~~~~~~~~~~~")
    print("                        1. 백종원 게임")
    print("                        2. 바니바니 게임")
    print("                        3. 베스킨라빈스 31 게임")
    print("                        4. 포도 게임")
    print("                        5. 병뚜겅 게임")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 게임 종료 화면
def showGameOver():
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    print("""  _____                            ____                      _
 / ____|                          / __ \                    | |
| |  __   __ _  _ __ ___    ___  | |  | |__   __  ___  _ __ | |
| | |_ | / _` || '_ ` _ \  / _ \ | |  | |\ \ / / / _ \| '__|| |
| |__| || (_| || | | | | ||  __/ | |__| | \ V / |  __/| |   |_|
 \_____| \__,_||_| |_| |_| \___|  \____/   \_/   \___||_|   (_)""")
    print("---------------------------------------------------------------------------")

# 메인 실해 함수
def main():
    intro()
    while True:
        player = input("오늘 거하게 취해볼 당신의 이름은? : ")
        if(player in list(data.keys())):
            break
        else:
            print("누구세요??")
    
    data[player][1] = selectAlc()
    
    users = selectFriend(player)
    
    while True:
        cur = rotateUser(users)        
        exit, menuNum = selectGame(cur, player)
        if(exit):
            print("게임을 종료합니다!")
            showGameOver()
            break
        
        if(menuNum == 1):
            paik.game(player, users)
        elif(menuNum == 2):
            loser = bunny.game(player, list(users.keys()))
            print(loser)
            for lose in loser:
                for user in users:                
                    if(user == lose):
                        if(users[user][0] < users[user][1]):                    
                            users[user][0] += 1
                        
        elif(menuNum == 3):
            loser = game31.game31(list(users.keys()), player)            
            if(users[loser][0] < users[loser][1]):                    
                users[loser][0] += 1
        elif(menuNum == 4):
            loser = grapeGame.grape_game(users, player)
            if(users[loser][0] < users[loser][1]):
                users[loser][0] += 1        
        elif(menuNum == 5):
            loser = guess_game.minigame_guess(player, list(users.keys()))
            for lose in loser:
                for user in users:                
                    if(user == lose):
                        if(users[user][0] < users[user][1]):                    
                            users[user][0] += 1
        
        if(checkStatus(users)):
            break
    
if __name__ == "__main__":
    main()