from defs_start_game import *

def show_field(field):
    for i in field:
        print(i)
        print()
    return ''

def move(team, game_pitch):
    old_ind=[]
    new_ind=[]
    for i in team:
        old_ind.append(i.field_index)
    for i in team:
        print(f'перемещение юнита {i.name}')
        uv=player_view(game_pitch, i.vision, i.field_index)
        upd=unit_moving(i, uv, i.field_index)
        new_ind.append(upd)
    for i in new_ind:
        if new_ind.count(i)>1:
            ind=new_ind.index(i)
            new_ind[ind]=old_ind[ind]
    for i in old_ind:
        game_pitch[i[0]][i[1]]='   '
    for i in range(len(team)):
        team[i].field_index=new_ind[i]
        game_pitch[new_ind[i][0]][new_ind[i][1]]=team[i].name
    return game_pitch, team












def player_view(field, view, index):#функция, выводящая часть поля в видимости корабля
    x=int(index[0])
    y=int(index[1])
    field_height = len(field)
    field_width = len(field[0]) if field_height > 0 else 0
    start_x = max(0, x - view)
    end_x = min(field_height, x + view + 1)
    start_y = max(0, y - view)
    end_y = min(field_width, y + view + 1)
    unit_view = []
    for i in range(start_x, end_x):
        row = field[i][start_y:end_y]
        unit_view.append(row)
    return unit_view










def unit_moving( unit, unit_field, unit_index):
    spd=int(unit.speed)
    print(show_field(unit_field))
    dec=input('введите направление перемещения:a-влево, d-вправо, w-вверх s-вниз:')
    new_index=[]
    if dec=='a':
        new_index.append(unit_index[0])
        upd=int(unit_index[1])-spd if int(unit_index[1])-spd>=0 else 0
        new_index.append(upd)
    elif dec=='d':
        new_index.append(unit_index[0])
        upd = int(unit_index[1]) + spd if int(unit_index[1]) + spd <= 14 else 14
        new_index.append(upd)
    elif dec=='w':
        upd=int(unit_index[0])-spd if int(unit_index[0])-spd>=0 else 0
        new_index.append(upd)
        new_index.append(unit_index[1])
    elif dec=='s':
        upd = int(unit_index[0]) + spd if int(unit_index[0]) + spd <= 14 else 14
        new_index.append(upd)
        new_index.append(unit_index[1])
    else:
        return unit_index
    return new_index
    


