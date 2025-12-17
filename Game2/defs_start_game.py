
from classes import Units
def start_ptc():
    game_pitch=[]
    while len(game_pitch)!=15:
        game_pitch.append(['   ','   ','   ','   ','   ','   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ','   '])
#создание игрового поля
    return game_pitch
unit_destroyer=Units('D',12,10,3,3)
unit_corvette=Units('C',5,7,4,4)
unit_frigate=Units('F',15,5,5,2)
def Team_emp(unit_destroyer,unit_corvette,unit_frigate):#функция для добавления кораблей в команду имп.
    team_emp={}
    destroyer_quanity=1
    corvette_quanity=1
    frigate_quanity=1
    money=10
    while money>0:
        type=input('выберите тип: 1-destroyer, 2-corvette, 3-frigate')
        if type=='1':
            upd={'att':unit_destroyer.attack,'defend':unit_destroyer.defend, 'vision':unit_destroyer.vision,'speed':unit_destroyer.speed}
            team_emp[f'ED-{destroyer_quanity}']=upd
            destroyer_quanity+=1
            money-=2.5
        elif type=='2':
            upd={'att':unit_corvette.attack, 'defend':unit_corvette.defend, 'vision':unit_corvette.vision,'speed':unit_corvette.speed }
            team_emp[f'EC-{corvette_quanity}'] = upd
            corvette_quanity+=1
            money-=1.5
        elif type=='3':
            upd={'att':unit_frigate.attack, 'defend':unit_frigate.defend,'vision':unit_frigate.vision,  'speed':unit_frigate.speed}
            team_emp[f'EF-{frigate_quanity}'] = upd
            frigate_quanity+=1
            money-=1
        else:
            break
        print(money)
        print(list(team_emp.keys()))
    return team_emp
def team_rebel(unit_destroyer,unit_corvette,unit_frigate):#функция для добавления в команду повст.
    team_rebel={}
    destroyer_quanity=1
    corvette_quanity=1
    frigate_quanity=1
    money=10
    while money>0:
        type=input('выберите тип: 1-destroyer, 2-corvette, 3-frigate')
        if type=='1':
            upd={'att':unit_destroyer.attack,'defend':unit_destroyer.defend, 'vision':unit_destroyer.vision,'speed':unit_destroyer.speed}
            team_rebel[f'RD-{destroyer_quanity}']=upd
            destroyer_quanity+=1
            money-=2.5
        elif type=='2':
            upd={'att':unit_corvette.attack, 'defend':unit_corvette.defend, 'vision':unit_corvette.vision,'speed':unit_corvette.speed }
            team_rebel[f'RC-{corvette_quanity}'] = upd
            corvette_quanity+=1
            money-=2
        elif type=='3':
            update={'att':unit_frigate.attack, 'defend':unit_frigate.defend,'vision':unit_frigate.vision,  'speed':unit_frigate.speed}
            team_rebel[f'RF-{frigate_quanity}'] = update
            frigate_quanity+=1
            money-=1.5
        else:
            break
        print(money)
        print(list(team_rebel.keys()))
    return team_rebel

def start_place(team_1, team_2, starting_pitch):#создание стартового поля
    team_1_units=list(team_1.keys())
    team_2_units=list(team_2.keys())
    new_str = starting_pitch[0]
    new_str2 = starting_pitch[-1]
    for i in range(len(team_1_units)):
        print(new_str)
        dec=int(input('введите номер поля(1-20), на которое хотите поставить юнит'))
        new_str[dec-1]=team_1_units[i]
    for i in range(len(team_2_units)):
        print(new_str2)
        dec=int(input('введите номер поля(1-20), на которое хотите поставить юнит'))
        new_str2[dec-1]=team_2_units[i]
    starting_pitch[0]=new_str
    starting_pitch[-1]=new_str2
    return starting_pitch
def show_field(starting_pitch):#выводит поле
    for i in starting_pitch:
        print(i)
        print()

def start(unit_destroyer,unit_corvette,unit_frigate):#начало игры.
    pitch=start_ptc()
    team1=Team_emp(unit_destroyer,unit_corvette,unit_frigate)
    team2=team_rebel(unit_destroyer,unit_corvette,unit_frigate)
    starting_pitch=start_place(team1,team2,pitch)
    show_field(starting_pitch)
    return starting_pitch, team1, team2









