import random


class Bot:
    def __init__(self, hp, energy, dmg):
        self.hp = hp
        self.energy = energy
        self.dmg = dmg
        
def change_pos(posx, posy):
    coin = random.randint(0, 1)
    if coin == 0:
        en1 = posx
        while en1 > 19 or en1 < 1 or en1 == posx:
            en1 = random.randint(posx-1, posx+1)
        en2 = posy
    else:
        en1 = posx
        en2 = -1000
        while en2 > 19 or en2 < 1 or en2 == posx:
            en2 = random.randint(posy-1, posy+1)
    return en1, en2

def boost(posx, posy):
    if field[posx -1][posy - 1] == 'B':
            en3 = random.randint(1, 3)
            if en3 == 1:
                player1.hp = player1.hp + 1
            elif en3 == 2:
                player1.energy = player1.energy + 1
            else: 
                player1.dmg = player1.dmg + 1

def face(posx_old, posx, posy_old, posy):
 
    if posx != posx_old:
        if posx > posx_old:
            faces[posx][posy - 1] = 1
            faces[posx - 2][posy - 1] = 3
            faces[posx - 1][posy - 2] = 2
            faces[posx - 1][posy] = 2
        else:
            faces[posx][posy - 1] = 3
            faces[posx - 2][posy - 1] = 1
            faces[posx - 1][posy-2] = 2
            faces[posx - 1][posy] = 2
    if posy != posy_old:
        if posy > posx_old:
            faces[posx - 1][posy] = 1
            faces[posx - 1][posy - 2] = 3
            faces[posx - 2][posy - 1] = 2
            faces[posx][posy - 1] = 2
        else:
            faces[posx - 1][posy] = 3
            faces[posx - 1][posy - 2] = 1
            faces[posx - 2][posy - 1] = 2
            faces[posx][posy - 1] = 2
    faces[posx - 1][posy - 1] = '&'

    

field = [[0 for x in range(20)] for y in range(20)]
faces = [[0 for x in range(20)] for y in range(20)]



posx, posy = map(int, input('Введите координаты стартовой позиции: ').split())

boost_count = int(input('Введите количество бустов на карте: '))

for i in range(boost_count):
    en1 = random.randint(0, 19)
    en2 = random.randint(0, 19)
    field[en1][en2] = 'B'

field[posx - 1][posy - 1] = '&'
faces[posx - 1][posy - 1] = '&'

hp, energy, dmg = map(int, input('Введите Здоровье, Энергию, Урон: ').split())

player1 = Bot(hp, energy, dmg)

print(player1.hp, player1.energy, player1.dmg)

for j in range(len(field)):
        print(field[j])
print()
print()
print()  

for i in range(6):
    count = player1.energy
    print('Энергия = ', count)
    print()
    for l in range(count):
        en1, en2 = change_pos(posx, posy)
        field[posx - 1][posy - 1] = 0
        face(posx, en1, posy, en2)
        posx, posy = en1, en2
        boost(posx,posy)
        print('Статы на ', i + 1 , ' ход')
        print(player1.hp, player1.energy, player1.dmg)
        print()

        field[posx - 1][posy - 1] = '&'
        print('Карта на ', i + 1 , ' ход')
        print()
        for j in range(len(field)):
            print(field[j])
        print()
        print()
        print('Лицо на ', i + 1, ' ход')
        print()
        for l in range(len(faces)):
            print(faces[l])
        print()
        print()
        
    