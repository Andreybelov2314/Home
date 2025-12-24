from Game2.defs_start_game import*
from Game2.defs_game_move import*
from Game2.defs_attack import*
from Game2.Units_classes.corvette import*
from Game2.Units_classes.destroyer import*
from Game2.Units_classes.frigate import*

flag = True
field, team_e, team_r = start_game()

while True:
    if flag == True:
        print('Ходит команда 1 (Империя)')
        field, team_e = move(team_e, field)
        print('Фаза атаки Империи')
        for i in team_e:
            print(i.name)
            uv=player_view(field, i.vision, i.field_index)
            print(show_field(uv))
            g_lst=attack_goals(uv, i)
            print(g_lst)
            field, team_r=attack(team_r,i,g_lst,field)
            flag=False
    elif flag==False:
        print('Ходит команда 2 (Повстанцы)')
        field, team_r = move(team_r, field)
        print('Фаза атаки Повстанцев')
        for i in team_r:
            print(i.name)
            uv = player_view(field, i.vision, i.field_index)
            print(show_field(uv))
            g_lst = attack_goals(uv, i)
            print(g_lst)
            field, team_e = attack(team_e, i, g_lst, field)
            flag=True
    if len(team_r)==0:
        print('Империя победила')
        break
    elif len(team_e)==0:
        print('Повстанцы победили')
        break



