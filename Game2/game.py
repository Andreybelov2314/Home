from Game2.defs_start_game import*
from Game2.defs_game_move import*
from Game2.defs_attack import*
flag=True
field,team_e, team_r=start(unit_destroyer,unit_corvette,unit_frigate)
while True:
    if flag==True:
        field,moving_unit, new_view=move(team_e,field)
        print(show_field(new_view))
        decision=input('хотите ли вы атаковать юниты соперника(y/n)?')
        if decision=='y':
            goal=attack_goals(field,moving_unit,team_e)
            team_r=attack_effects(moving_unit, team_e, goal, team_r, field)
        flag=False
    elif flag==False:
        field,moving_unit, new_view=move(team_r,field)
        print(show_field(new_view))
        decision=input('хотите ли вы атаковать юниты соперника(y/n)?')
        if decision=='y':
            goal=attack_goals(field,moving_unit,team_r)
            team_r, field=attack_effects(moving_unit, team_r, goal, team_e, field)
        flag=True
    if len(team_r)==0:
        print('Империя победила')
        break
    elif len(team_r)==0:
        print('Повстанцы победили')
        break


