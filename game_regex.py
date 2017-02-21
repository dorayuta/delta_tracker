### betcoin game regex
import re
game_regex = "^Game ID: ([0-9]+)"
def get_game_id(line):
    is_id, game_id = False, None
    game_line = re.search(game_regex, line)
    if game_line is not None:
        game_id = int(game_line.group(1))
        is_id = True
    return is_id, game_id

pnl_regex = "(Wins|Loses): ([0-9]+\.?[0-9]*)\."
WIN = "Wins"
LOSS = "Loses"
def get_pnl(pnl_string):
    match = re.search(pnl_regex, pnl_string)
    is_pnl, pnl = False, None
    if match is not None:
        is_pnl = True
        win_loss = match.group(1)
        pnl = float(match.group(2))
        if win_loss == LOSS: pnl = -1.0*pnl
    return is_pnl, pnl

def is_user(line, username):
    return re.search("^[\*]?Player "+username, line) is not None    
