from defs_start_game import *

def show_field(field):
    for i in field:
        print(i)
        print()


def move(team, game_pitch):
    # Шаг 1: Определяем новые позиции для всех юнитов
    moves = []
    for unit in team:
        print(f"Определение перемещения для: {unit.name}")
        view = int(unit.vision)
        index = unit.field_index
        uv = player_view(game_pitch, view, index)
        new_index = unit_moving(unit, uv, index)
        moves.append((unit, new_index))

    # Шаг 2: Создаем карту занятости новых позиций
    new_positions_map = {}
    for unit, new_idx in moves:
        key = (int(new_idx[0]), int(new_idx[1]))
        if key not in new_positions_map:
            new_positions_map[key] = []
        new_positions_map[key].append(unit)

    # Шаг 3: Очищаем ВСЕ текущие позиции команды
    for unit in team:
        x, y = int(unit.field_index[0]), int(unit.field_index[1])
        if game_pitch[x][y] == unit.name:
            game_pitch[x][y] = '   '

    # Шаг 4: Применяем перемещения, разрешая конфликты
    for unit, new_idx in moves:
        x, y = int(new_idx[0]), int(new_idx[1])

        # Проверяем, не занята ли клетка другим юнитом
        if game_pitch[x][y] != '   ':
            # Конфликт! Возвращаем на старое место
            old_x, old_y = int(unit.field_index[0]), int(unit.field_index[1])
            game_pitch[old_x][old_y] = unit.name
            print(f"{unit.name} не может переместиться на ({x},{y}) - клетка занята")
        else:
            game_pitch[x][y] = unit.name
            unit.field_index = new_idx

    return team, game_pitch











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
    


