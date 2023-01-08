
import random

# list = ['고은', '용현', '태영', '수현', '현지']
dictionary = {'고은': [7, 7], '용현': [6, 6],
              '태영': [5, 5], '수현': [5, 5], '현지': [4, 4]}


def grape_game(dictionary_player, user):
    list_player = list(dictionary_player.keys())
    random.shuffle(list_player)
    print(list_player)
    n = len(list_player)
    player = []
    print('포도 게임 포도 게임 ')
    grape_bunch = 5
    grape_current = 0

    active = True
    while active:
        for i in range(0, n):
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
                        f"{list_player[i]} (user) : 포도 {grape}알 {eat} {grape_current}")
                else:
                    print(
                        f"{list_player[i]}  : 포도 {grape}알 {eat} {grape_current}")
                print("다먹었네")
                player.append(list_player[i])
                grape_current = 0

            else:
                if list_player[i] == user:
                    print(
                        f"{list_player[i]} (user) : 포도 {grape}알 {eat} {grape_current}")
                else:
                    print(
                        f"{list_player[i]}  : 포도 {grape}알 {eat} {grape_current}")

                player.append(list_player[i])

            if grape_current < 0 or grape_current > 5:
                print(f"{player[-1]} 원샷")
                active = False
                break
            else:
                active = True

    return player[-1]


print(grape_game(dictionary, '현지'))
