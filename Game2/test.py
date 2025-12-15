from defs_start_game import *
from defs_attack import *
from defs_game_move import *
print("=== НАЧАЛО ИГРЫ ===")
field,team_e, team_r = start(unit_destroyer,unit_corvette,unit_frigate)
print(f"Размер field: {len(field)}x{len(field[0])}")
print(f"Тип team_e: {type(team_e)}, количество юнитов: {len(team_e)}")
print(f"Тип team_r: {type(team_r)}, количество юнитов: {len(team_r)}")
print("Содержимое team_e:", team_e)
print("=== НАЧАЛО ЦИКЛА ===")

