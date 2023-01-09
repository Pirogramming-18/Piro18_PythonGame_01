import requests
import random as r
from bs4 import BeautifulSoup as bs

#{name : [남은 주량, 치사량]}
data = {"김용현" : [5, 5], "김고은" : [5, 5], "한수현" : [5, 5], "송현지" : [5, 5], "김태영" : [5, 5]}


#단어를 검색하는 함수
def searchWord(soup1, soup2, search, searchNaver):
    #네이버 검색에서 체크
    target1 = list(soup1.select(".main_pack section"))
    result1 = False
    for t in target1:
        if(searchNaver in str(t)):
            # print("naver")
            result1 = True
    
    #만개의 레시피에서 체크
    result2 = False
    
    target2 = list(soup2.select(".talk_content > p > a"))
    for t in target2:        
        if(search in t.string):         
            # print("million")
            result2 = True
        
    return result1, result2


#컴퓨터 데이터 정보 초기화 함수
def initComputer():
    #53~56, 63
    computerData = []
    urlList = ["https://www.10000recipe.com/recipe/list.html?cat4=53",
               "https://www.10000recipe.com/recipe/list.html?cat4=54",
               "https://www.10000recipe.com/recipe/list.html?cat4=55",
               "https://www.10000recipe.com/recipe/list.html?cat4=56",
               "https://www.10000recipe.com/recipe/list.html?cat4=63"]
    
    for url in urlList:
        s = bs(requests.get(url).text, "html.parser")
        for text in s.select(".tag_cont > li > a"):
            computerData.append(text.string)
    
    return computerData

#게임 타이틀 출력 함수
def showTitle():
    print("""
------------------------------------------------------------------------------------------------------
.______        ___       __   __  ___  __      _______.     _______      ___      .___  ___.  _______ 
|   _  \      /   \     |  | |  |/  / (_ )    /       |    /  _____|    /   \     |   \/   | |   ____|
|  |_)  |    /  ^  \    |  | |  '  /   |/    |   (----`   |  |  __     /  ^  \    |  \  /  | |  |__   
|   ___/    /  /_\  \   |  | |    <           \   \       |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |       /  _____  \  |  | |  .  \      .----)   |      |  |__| |  /  _____  \  |  |  |  | |  |____ 
| _|      /__/     \__\ |__| |__|\__\     |_______/        \______| /__/     \__\ |__|  |__| |_______|

-------------------------------------------------------------------------------------------------------                                                                                                      
🤤백종원 게임 시~~작! (백종원 레시피가 없는 음식을 검색하면 원 샷!!)😵‍💫
""")


#백종원 게임 실행 함수
def game(name, users):
    
    showTitle()
    computerData = initComputer()
    while(True):
        player = list(users.keys())[r.randint(0, len(users)-1)]
        
        if(name == player):
            string = input(f"{player}: 검색할 음식을 입력하세요! : ") 
            temp = string.replace(" ", "")
            if(len(temp) == 0):
                print("반드시 음식을 입력하셔야 합니다! 턴이 넘어갑니다!!!")        
                continue   
        else:
            string = computerData[r.randint(0, len(computerData)-1)]
            
        search = string
        searchNaver = "백종원 " + string
        print(f"{player} => {string}")
        #네이버 검색
        url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={searchNaver}"
        #만개의 레시피 백종원 요리 모음
        url2 = "https://www.10000recipe.com/bbs/1266"
        
        soup1 = bs(requests.get(url).text, "html.parser")
        soup2 = bs(requests.get(url2).text, "html.parser")

        #해당 음식의 레시피가 있는지 탐색
        result1, result2 = searchWord(soup1, soup2, search, searchNaver)
        
        if(result1 or result2):    #해당 레시피가 존재하는 경우
            print(f"\'{search}\' 에 대한 백종원 레시피가 존재합니다!")   
        else:   #해당 레시피가 존재하지 않는 경우
            print(f"{string} 은(는) 백종원 선생님도 모르는 음식입니다...............")
            print(f"아 누가 술을 마셔!!! {player}이(가) 술을 마셔~ {player[0]}! 👏 {player[1]}! 👏 {player[2]}! 👏 원~~~ 샷!!")
            print("")
            if(users[player][0] < users[player][1]):
                users[player][0] += 1
            break
        
if(__name__ == "__main__"):
    game("김용현", data)

    