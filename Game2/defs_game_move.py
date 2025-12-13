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
def move(team, game_pitch):
    print(to_units(team))
    num=int(input('введите номер юнита, который хотите переместить'))
    moving_unit=to_units(team)[num-1]
    index=get_index(game_pitch,moving_unit)
    vis=get_info(moving_unit,team,'vision')




def get_info(team_name, unit_name, team, info):#функция для получения конкретного значения конкретного юнита
    data_unit=team_name.get(unit_name)
    information=data_unit.get(info)
    return information


def player_view(pitch, unit_name, unit_vision):#функция, выводящая часть поля в видимости корабля
    view = []
    index = get_index(pitch, unit_name)
    x = int(index[0])
    y = int(index[1])

    max_x = len(pitch) - 1
    max_y = len(pitch[0]) - 1

    start_x = max(0, x - unit_vision)
    end_x = min(max_x, x + unit_vision)
    start_y = max(0, y - unit_vision)
    end_y = min(max_y, y + unit_vision)


    for row in pitch[start_x:end_x + 1]:
        view.append(row[start_y:end_y + 1])
    return view



