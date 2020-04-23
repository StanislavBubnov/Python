import random
import time


class LotoCard:
    def __init__(self):
        number_set = set()
        while len(number_set) != 15:
            number_set.add(random.randint(1,90))
        number_list = list(number_set)
        str_1 = sorted(number_list[:5])
        str_2 = sorted(number_list[5:10])
        str_3 = sorted(number_list[10:])
        i = 4
        while i != 0:
            str_1.insert(random.randint(0,len(str_1)),'-')
            i -= 1
        i = 4
        while i != 0:
            str_2.insert(random.randint(0, len(str_2)), '-')
            i -= 1
        i = 4
        while i != 0:
            str_3.insert(random.randint(0, len(str_3)), '-')
            i -= 1
        self.number_list = str_1 + str_2 + str_3
        self.name = None




class CompCard(LotoCard):
    def __init__(self):
        super().__init__()
        self.name = ' Карточка компьютера '

class PlayerCard(LotoCard):
    def __init__(self):
        super().__init__()
        self.name = 'Карточка игрока: ' + input('Введите имя игрока: ')

class Game:
    def lets_go(self):
        print('Игра начинается!')
        all_numbers = [el for el in range(1,90)]
        time.sleep(3)
        while True:
            random_number = all_numbers[random.randint(0, len(all_numbers)-1)]
            print(f'Бочонок №: {random_number} осталось {len(all_numbers)}')
            all_numbers.remove(random_number)
            print('-'*5 + player_card.name + '-'*5)
            print(' '.join(str(e) for e in player_card.number_list[0:9]))
            print(' '.join(str(e) for e in player_card.number_list[9:18]))
            print(' '.join(str(e) for e in player_card.number_list[18:27]))
            print('-' * 30)
            print('-'*5 + comp_card.name + '-'*5)
            print(' '.join(str(e) for e in comp_card.number_list[0:9]))
            print(' '.join(str(e) for e in comp_card.number_list[9:18]))
            print(' '.join(str(e) for e in comp_card.number_list[18:27]))
            print('-' * 30)
            player_ans = input('Есть ли у вас это число? y/n: ')
            if player_ans == 'y':
                if player_card.number_list.count(random_number) == 1:
                    ind_num = player_card.number_list.index(random_number)
                    player_card.number_list.remove(random_number)
                    player_card.number_list.insert(ind_num,'-')
                    if player_card.number_list.count('-') == 27:
                        print('Вы победили!')
                        break
                    elif comp_card.number_list.count(random_number) == 1:
                        ind_num = comp_card.number_list.index(random_number)
                        comp_card.number_list.remove(random_number)
                        comp_card.number_list.insert(ind_num, '-')
                        if comp_card.number_list.count('-') == 27:
                            print('Победил компьютер!')
                            break
                else:
                    print('Вы ошиблись и проиграли!')
                    break
            elif player_ans == 'n':
                if player_card.number_list.count(random_number) != 1:
                    if comp_card.number_list.count(random_number) == 1:
                        ind_num = comp_card.number_list.index(random_number)
                        comp_card.number_list.remove(random_number)
                        comp_card.number_list.insert(ind_num, '-')
                        if comp_card.number_list.count('-') == 27:
                            print('Победил компьютер!')
                            break
                else:
                    print('Вы ошиблись и проиграли!')
                    break





player_card = PlayerCard()

comp_card = CompCard()


game = Game()
game.lets_go()

