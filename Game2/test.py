from defs_start_game import *
from defs_game_move import *
field, team1, team2=start(unit_destroyer,unit_corvette,unit_frigate)
vis=get_info(team2,'RD-1', field, 'vision')
print(player_view(field,'RD-1',vis))



