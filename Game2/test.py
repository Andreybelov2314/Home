from defs_start_game import *
from defs_game_move import *


field, team1, team2=start(unit_destroyer,unit_corvette,unit_frigate)
new_field=move(team1,field)
print(show_field(new_field))


