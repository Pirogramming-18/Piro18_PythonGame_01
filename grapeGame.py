
import random

# list = ['고은', '용현', '태영', '수현', '현지']
dictionary = {'고은': [7, 7], '용현': [6, 6],
              '태영': [5, 5], '현지': [4, 4]}


def grape_game(dictionary_player, user):
    # 게임 참여자는 돌아가면서 포도를 한알, 두알, 세알을 먹거나 빼야한다.
    # 포도가 5알이 되면 다같이 다먹었네
    list_player = list(dictionary_player.keys())
    random.shuffle(list_player)
    n = len(list_player)
    player = []
    print('🍇포도 게임~~ 포도 게임~~ 🍇')
    grape_bunch = 5
    grape_current = 0

    active = True
    while active:
        for i in range(0, n):
            if user == list_player[i]:
                while True:
                    grape = input('한알 두알 세알 중 선택하세요(1,2,3 중 선택): ')
                    if grape == '1' or grape == '2' or grape == '3':
                        grape = int(grape)
                        break
                    else:
                        print('다시 입력하세요-', end='')

                while True:
                    eat = input('먹고 빼고 중에 선택하세요(먹고, 빼고 중 선택): ')
                    if eat == '먹고' or eat == '빼고':
                        break
                    else:
                        print("다시 입력하세요-", end='')

                if eat == '먹고':
                    grape_current += grape
                elif eat == '빼고':
                    grape_current -= grape

            else:
                grape = random.randint(1, 3)
                eat = random. randint(1, 3)
                if eat == 1 or eat == 2:
                    grape_current += grape
                    eat = '먹고'
                else:
                    grape_current -= grape
                    eat = '빼고'

            if grape_current == 5:
                if list_player[i] == user:
                    print(
                        f"{list_player[i]} (user) : 포도 {grape}알 {eat} ")  # grape_current 삭제
                else:
                    print(
                        f"{list_player[i]}  : 포도 {grape}알 {eat} ")  # grape_current 삭제
                print("다먹었네")
                player.append(list_player[i])
                grape_current = 0

            else:
                if list_player[i] == user:
                    print(
                        f"{list_player[i]} (user) : 포도 {grape}알 {eat} ")  # grape_current 삭제
                else:
                    print(
                        f"{list_player[i]}  : 포도 {grape}알 {eat} ")  # grape_current 삭제

                player.append(list_player[i])

            if grape_current < 0 or grape_current > 5:
                print(f"{player[-1]} 원샷")
                active = False
                break
            else:
                active = True

    return player[-1]

if __name__ == "__main__":
    print(grape_game(dictionary, '현지'))
