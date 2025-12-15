from defs_start_game import *
from defs_game_move import *
import random
def attack_goals(pitch, unit, team):#функция выбора цели
    goals=[]
    vis=get_info(unit,team, 'vision')
    new_pitch=player_view(pitch,unit, vis)
    print(show_field(new_pitch))
    for i in new_pitch:
        for j in i:
            if j!='   ':
                goals.append(j)
    print(goals)
    index=int(input('ведите номер корабля, который хотите атаковать'))
    goal=goals[index-1]
    return goal
def attack_effects(unit, team, goal, team2, field):#возвращает исправленный список команды после нанесения урона
    dam_LT=[0, 0, 1, 1, 1, 2, 2, 2, 3, 3]
    dam_MT=[3, 3, 4, 4, 4, 4, 5, 5, 5, 6]
    dam_EQ=[1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
    att=get_info(unit, team, 'att')
    defend=get_info(goal, team2, 'defend')
    if int(att)>int(defend):
        dam_res=random.choice(dam_MT)
    elif int(att)<int(defend):
        dam_res=random.choice(dam_LT)
    elif int(att)==int(defend):
        dam_res=random.choice(dam_EQ)
    team2, field=damage(dam_res,goal,team2, field)
    return team2, field



def damage(damage_amount, target_unit_name, team_dict, field):#анесение урона
    if target_unit_name not in team_dict:
        print(f"Ошибка: Юнит '{target_unit_name}' не найден в команде!")
        return team_dict
    unit_data = team_dict[target_unit_name]
    current_defense = unit_data.get('defend', 0)
    new_defense = current_defense - damage_amount
    if new_defense <= 0:
        del team_dict[target_unit_name]
        print(f"Юнит '{target_unit_name}' уничтожен! (Урон: {damage_amount})")
        x=get_index(field, target_unit_name)[0]
        y=get_index(field, target_unit_name)[1]
        field[int(x)][int(y)]='   '

    else:
        unit_data['defend'] = new_defense
        print(f"Юнит '{target_unit_name}' получил урон {damage_amount}. Защита: {current_defense} → {new_defense}")
    return team_dict, field

