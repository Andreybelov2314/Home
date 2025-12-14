from defs_start_game import *
from classes import *
def get_index(pitch, object):#функция для получения индекса обьекта во вложенных списках
    x=0
    y=0
    for i in pitch:
        for j in i:
            if j == object:
                x=pitch.index(i)
                y=i.index(j)
    index=[x,y]
    return index
def move(team, game_pitch):#функция для перемещения
    print(to_units(team))
    num=int(input('введите номер юнита, который хотите переместить'))
    moving_unit=to_units(team)[num-1]
    vis=get_info(moving_unit,team,'vision')
    index=get_index(game_pitch, moving_unit)
    unit_field=player_view(game_pitch, moving_unit,vis)
    new_index=unit_moving(team,moving_unit, unit_field,index)
    game_pitch[int(index[0])][int(index[1])] = '  '
    game_pitch[int(new_index[0])][int(new_index[1])] = moving_unit
    new_view=player_view(game_pitch, moving_unit,vis)
    return game_pitch, moving_unit, new_view





def get_info(unit_name, team_dict, info):#функция для получения конкретного значения конкретного юнита
    data_unit=team_dict.get(unit_name)
    information=data_unit.get(info)
    return information


def player_view(pitch, unit_name, unit_vision):#функция, выводящая часть поля в видимости корабля
    view = []
    index = get_index(pitch, unit_name)
    x = int(index[0])
    y = int(index[1])
    max_x = len(pitch) - 1
    max_y = len(pitch[0]) - 1
    start_x = max(0, x - int(unit_vision))
    end_x = min(max_x, x + int(unit_vision))
    start_y = max(0, y - int(unit_vision))
    end_y = min(max_y, y + int(unit_vision))
    for i in pitch[start_x:end_x + 1]:
        view.append(i[start_y:end_y + 1])
    return view
def unit_moving(team, unit, unit_field, unit_index):
    new_index = [unit_index[0], unit_index[1]]
    unit_speed=get_info(unit,team,'speed')
    print(show_field(unit_field))
    dec=input('введите направление перемещения:a-влево, d-вправо, w-вверх s-вниз: ')
    if dec=='a':
        if int(unit_index[1])-int(unit_speed)>=0:
            new_index[1]=int(unit_index[1])-int(unit_speed)
        else:
            new_index[1]=0
    elif dec=='d':
        if int(unit_index[1])-int(unit_speed)<=9:
            new_index[1]=int(unit_index[1])+int(unit_speed)
        else:
            new_index[1]=9
    elif dec=='w':
        if int(unit_index[0])-int(unit_speed)>=0:
            new_index[0]=int(unit_index[0])-int(unit_speed)
        else:
            new_index[0]=0
    elif dec=='s':
        if int(unit_index[0])+int(unit_speed)<=9:
            new_index[0]=int(unit_index[0])+int(unit_speed)
        else:
            new_index[0]=9
    return new_index


