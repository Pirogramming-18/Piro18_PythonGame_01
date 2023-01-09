########### 고은 (병뚜껑) 게임) ##########
# 게임방법 
# 1. 병뚜껑의 숫자는 1~15까지 무작위로 배정됩니다.
# 2. 이때 순서는 user가 먼저 실행되고, 이후 랜덤으로 진행됩니다.
# 3. 자기 차례에는 총 2번의 기회가 주어지며, 정답을 맞추지 못하면 술을 마시고 순서는 다음차례로 넘어간다.
# 4. 다음 차례의 사람에게는 새로운 랜덤 숫자가 부여된다.
# 5. 각 시행은 독립적으로 이루어진다.
from random import *

    
def Intro2():

      #게임인트로
    print ('''
    **********************************************************************
    피로가 좋아하는 랜덤게임!                        
    무슨 게임 ~ 게임 스타트 ~~ 게임 스타트 ~~ 
    싸늘하다 가슴에 병뚜껑이 날아와 꽂힌다... "예리미 그 병뚜껑 좀 까봐" ~     
    
                                            ┏━━━━━┓
                                            ┃ 　　 ┃
                                            ┃　┏━┓ ┃
                                            ┗━┛　┃ ┃
                                            　 ┏━┛ ┃
                                            　┃　┏━┛
      "묻고 더블로 가~ "                     　┗━┛
                                            　┏━┓
                                            　┃　┃
                                              ┗━┛
                                            　　〇
                                            　　ｏ
                                            　　(・д・)
                                                                                              
    **********************************************************************''')
    print('**********************************************************************')
    print('게임 방법! : 과연 병뚜껑의 숫자는 무엇일까요?')
    print('step 1: player는 자기 차례에 2번의 기회동안 숫자를 말할 수 있습니다! \n step 2: 다음 차례에 사람에게는 새로운 번호가 주어지고, 만일 맞히지 못한다면 술을 마시고 차례는 다음으로 넘아갑니다\n')

p_list = ['수현','용현','태영','현지']
user = 'user'
loser_list = []

def minigame_guess(p_list):
    Intro2()
    global loser_list
    chance_count = 0
    num = randrange(1, 10, 1)

    shuffle(p_list)

    #사용자 실행
    while True:
      print('**********************************************************************') 
      my_turn = input('병뚜껑 숫자는 뭘까요~? (1~10):' )
      if str(my_turn).isdigit(): #조건1 정수를 입력했는가 
        my_turn = int(my_turn)
        if 0 <= my_turn <= 10: # 숫자가 범위를 초과했는가 #조건2
          chance_count += 1
          if num == my_turn:
            print("와~ 정답{}을 맞춘 당신! 벌주 면제입니다".format(num)) 
            break

          elif num < my_turn:
            print("Down")
          else:
            print("Up")
          print("때~앵! 틀렸데여~ 오답 횟수", ':' ,chance_count)
        
          if(chance_count == 2):
            print("땡! 비수를 맞은 당신 나의 벌주를 받아라..:" )
            print('정답은', num)
            #주량을 -1 해줘야 합니다
            #user[i] -= 1
            loser_list.append(user)
            break

        else:
          print('범위에 맞는 정수를 입력해주세요.', end=' ')
      else:
          print('정수를 입력해주세요.', end=' ')

    #컴퓨터 실행
    for i in range(len(p_list)):
      chance_count = 0
      num = randint(1,10)
      while True:
        chance_count += 1
        c_num = randint(1,10)
        print('**********************************************************************') 
        print(p_list[i],'!병뚜껑 숫자는 뭘까요~? (1~10):', c_num)
        print(p_list[i], '순서, 도전 횟수', chance_count, end=' ')
        if num == c_num:
          print(" 정답{}을 맞춘 당신! 와~ 벌주 면제입니다".format(num)) 
          print('**********************************************************************') 
          break
        elif num < c_num:
          print("Down")
        else:
          print("Up")
        print("때~앵! 틀렸데여~ ")

        if(chance_count == 2):
          print("땡! 비수를 맞은 당신 나의 벌주를 받아라..:" )
          print('정답은', num)
          print('**********************************************************************') 
          #주량에서 -1
          #plist[i].hmcd -= 1
          loser_list.append(p_list[i])

    return loser_list
          


minigame_guess(p_list)  

