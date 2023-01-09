# 31게임
# -룰
# 1. 참가자는 1, 2, 3, 4, 5, 6까지 각각 4개의 카드로 구성된 총 24개의 카드더미에서 카드를 뽑음
# 2. 한 번의 시행마다 카드를 더 이상 뽑을지 말지 결정 가능
# 3. 특정 참가자가 현재 소지하고 있는 카드의 합이 31을 초과하게 된다면 그 참가자의 패배
# 4. 만약 모든 참가자가 현재 소지하고 있는 카드의 합이 31 미만이라면 가장 작은 숫자를 가진 사람의 패배
# 5 만약 4에서 가장 작은 카드의 합을 가진 사람이 여러 명이라면 그 사람들 중에서 제비뽑기에서 꽝이 나온 사람이 패배

import random
import time

def game31Intro():

  print("=============================================================")
  print()
  print("⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤")
  print("⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⣿⣿⠿⣿⡿⠿⠿⠿⣿⣿⣿")
  print("⣿⣿⣿⣿⣾⣿⠈⣿⣿⣥⡄⣿⣿⣿⣿⣿⡟⣡⣾⣿⣷⣾⣿⡿⢠⠘⣿⣿⡇⠀⢿⣿⣿⠏⡄⣿⡇⢰⣶⣾⣿⣿⣿")
  print("⣿⣿⣿⣿⣯⣍⡚⣿⣿⣿⡇⣿⣿⣿⣿⣿⡁⣿⣿⣏⣉⢻⣿⠃⠿⠧⢹⣿⡇⢸⡌⢿⡟⣼⡇⣿⡇⢨⣭⣽⣿⣿⣿")
  print("⣿⣿⣿⣿⠿⠿⢃⣿⣿⣿⡇⣿⣿⣿⣿⣿⣧⡙⠿⠿⠿⢸⠇⣶⣶⣶⡆⢿⡇⢸⣿⡘⣰⣿⡇⣿⡇⠸⠿⢿⣿⣿⣿")
  print("⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛")
  print()
  print("=============================================================")
  
def cardGenerator31(card_deck31):

  for i in range(1, 7):
    for _ in range(4):
      card_deck31.append(i)

  random.shuffle(card_deck31)

  return card_deck31

def gameOver31 (loser31):

  print(f"{loser31} Lose!")
  print()

  print("            █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█         ")
  print("            █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄         ")
  
def drawingLots31(loser31):
  
  raffle31 = [""]*(len(loser31)-1) + ["꽝"]

  random.shuffle(raffle31)

  for i in range(len(loser31)):
    if (raffle31[i] == '꽝'):
      return i

def game31End(card_sum31, entry):
  min_sum31 = min(card_sum31)

  loser31 = [i for i in range(len(entry)) if card_sum31[i] == min_sum31]
  if len(loser31) == 1:
    gameOver31(entry[loser31[0]])

    return entry[loser31[0]]

  else:
    print("동점자가 있기 때문에 제비뽑기를 진행하겠습니다.")
    idx = drawingLots31(loser31)
    print(f'{entry[loser31[idx]]}님이 꽝을 뽑았습니다!')
    
    gameOver31(entry[loser31[idx]])
    return entry[loser31[idx]]



def game31 (entry, player31): #참가자 명단
  
  game31Intro()

  num31 = len(entry)
  card_deck31 = []
  card_sum31 = [0]*num31
  retire31 = [0]*num31
  
  card_deck31 = cardGenerator31(card_deck31)
  
    
  for i in range(24):
    
    if (retire31[i%num31] == 1):
      continue
    else:
      print(f'{entry[i%num31]}님의 차례입니다')
    
    time.sleep(0.5)
    if (entry[i%num31] == player31):

      while 1:
        choice31 = input("카드를 더 뽑으시겠습니까? (y/n) :").strip()

        if (choice31 == "y"):
          print(f'{player31} : call!')
          break

        elif (choice31 == "n"):
          print(f'{player31} : fold.')
          retire31[i%num31] = 1
          print()
          break

        else:
          print("y 혹은 n만 입력해주십시오.")
          continue
    
    else:
      if card_sum31[i%num31] <= 25:
        print(f'{entry[i%num31]} : call!')
      else:
        choice = random.choice([True, False])
        if choice:
          print(f'{entry[i%num31]} : call!')
        else:
          print(f'{entry[i%num31]} : fold.')
          retire31[i%num31] = 1

    if (retire31[i%num31] == 1):
      continue

    time.sleep(0.5)

    picked_card31 = card_deck31.pop()
    print(f'{entry[i%num31]}님이 뽑은 카드는 {picked_card31}입니다.')

    card_sum31[i%num31] += picked_card31

    time.sleep(0.5)
    limitNumber = 31
    if (card_sum31[i%num31] > limitNumber):
      print(f'{entry[i%num31]}님의 카드 합계가 {limitNumber}이 넘었습니다!')
      gameOver31(entry[i%num31])
      return entry[i%num31]
    else:
      print(f"현재 {entry[i%num31]}님이 소지한 카드의 합은 {card_sum31[i%num31]}입니다")
    print()
  loser = game31End(card_sum31, entry)
  return loser
  

