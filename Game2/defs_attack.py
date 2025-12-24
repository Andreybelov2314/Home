from defs_start_game import *
from defs_game_move import *
from Game2.Units_classes.corvette import*
from Game2.Units_classes.destroyer import*
from Game2.Units_classes.frigate import*
import random
def attack_goals(pitch, i):#функция выбора цели
    goals=[]
    for l in pitch:
        for j in l:
            if j!='   ' and j[0]!=i.name[0]:
                goals.append(j)
    return goals
def attack(team2, unit_moving, goals, field):
    dam_LT=[0, 0, 1, 1, 1, 2, 2, 2, 3, 3]
    dam_MT=[3, 3, 4, 4, 4, 4, 5, 5, 5, 6]
    dam_EQ=[1, 2, 2, 2, 3, 3, 3, 4, 4, 5]

    if len(goals)>0:
        print(goals)
        index=int(input('ведите номер корабля, который хотите атаковать'))
        goal=goals[index-1]
        g_ind=0
        att=unit_moving.attack
        defend=0
        for l in team2:
            if l.name==goal:
                g_ind=team2.index(l)
                new_defend=l.defend
        if int(att)>int(defend):
            damage=random.choice(dam_MT)
            new_defend-=damage
            if new_defend<=0:
                print(f'юнит {team2[g_ind].name} уничтожен')
                ind=team2[g_ind].field_index
                field[ind[0]][ind[1]]='    '
                team2.pop(g_ind)
            else:
                print(f'юниту {team2[g_ind].name} нанесено {damage} урона')
                team2[g_ind].defend=new_defend
        elif int(att)<int(defend):
            damage = random.choice(dam_LT)
            new_defend -= damage
            if new_defend <= 0:
                print(f'юнит {team2[g_ind].name} уничтожен')
                ind = team2[g_ind].field_index
                field[ind[0]][ind[1]] = '    '
                team2.pop(g_ind)
            else:
                print(f'юниту {team2[g_ind].name} нанесено {damage} урона')
                team2[g_ind].defend = new_defend
        elif int(att)==int(defend):
            damage = random.choice(dam_EQ)
            new_defend -= damage
            if new_defend <= 0:
                print(f'юнит {team2[g_ind].name} уничтожен')
                ind = team2[g_ind].field_index
                field[ind[0]][ind[1]] = '    '
                team2.pop(g_ind)
            else:
                print(f'юниту {team2[g_ind].name} нанесено {damage} урона')
                team2[g_ind].defend = new_defend
        return field, team2
    else:
        print(' целей для атаки нет')
        return field, team2





















