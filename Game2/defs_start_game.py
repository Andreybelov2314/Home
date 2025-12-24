from Game2.Units_classes.corvette import*
from Game2.Units_classes.destroyer import*
from Game2.Units_classes.frigate import*


def start_ptc():
    game_pitch=[]
    while len(game_pitch)!=15:
        game_pitch.append(['   ','   ','   ','   ','   ','   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ','   '])
#создание игрового поля
    return game_pitch


def create_team_empire():
    team_e = []  # команда империи
    money = 10
    destroyer_q = 1
    frigate_q = 1
    corvette_q = 1

    while money > 0:
        dec = input('выберите тип корабля:1-destroyer,2-frigate, 3-corvette')
        if dec == '1':
            nam = f'ED-{destroyer_q}'
            obj = destroyer(nam)
            team_e.append(obj)
            money = money - 3
            destroyer_q += 1
        elif dec == '2':
            nam = f'EF-{frigate_q}'
            obj = frigate(nam)
            team_e.append(obj)
            money = money - 2.5
            frigate_q += 1
        elif dec == '3':
            nam = f'EC-{corvette_q}'
            obj = corvette(nam)
            team_e.append(obj)
            money = money - 1.5
            corvette_q += 1
        else:
            break
        print(money)
        for i in team_e:
            print(i.name, end=', ')
        print()

    return team_e


def create_team_rebels():
    team_r = []  # команда повстанцев
    money = 10
    destroyer_q = 1
    frigate_q = 1
    corvette_q = 1

    while money > 0:
        dec = input('выберите тип корабля:1-destroyer,2-frigate, 3-corvette')
        if dec == '1':
            nam = f'RD-{destroyer_q}'
            obj = destroyer(nam)
            team_r.append(obj)
            money = money - 3
            destroyer_q += 1
        elif dec == '2':
            nam = f'RF-{frigate_q}'
            obj = frigate(nam)
            team_r.append(obj)
            money = money - 2.5
            frigate_q += 1
        elif dec == '3':
            nam = f'RC-{corvette_q}'
            obj = corvette(nam)
            team_r.append(obj)
            money = money - 1.5
            corvette_q += 1
        else:
            break
        print(money)
        for i in team_r:
            print(i.name, end=', ')
        print()

    return team_r

def starting_field(team1, team2, field):
    for i in team1:
        unit_icon=i.name
        print(field[0])
        print(unit_icon)
        dec=int(input('введите номер поля, но который хотите поставить юнит'))
        field[0][dec-1]=unit_icon
        i.field_index=[0, dec-1]
    for c in team2:
        unit_icon = c.name
        print(field[-1])
        print(unit_icon)
        dec = int(input('введите номер поля, но который хотите поставить юнит'))
        field[-1][dec-1] = unit_icon
        c.field_index=[14, dec-1]
    return field


def start_game():
    field=start_ptc()
    team1=create_team_empire()
    team2=create_team_rebels()
    field=starting_field(team1, team2, field)
    return field, team1, team2






