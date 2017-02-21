### betcoin hand reader
from game_regex import *
import sqlite3

hands_conn = sqlite3.connect('all_hands.db')
hands_cursor = hands_conn.cursor()
    
def add_hand(hand):
    t = (hand["game_id"], hand["pnl"])
    check = hands_cursor.execute("select game_id from game_pnl where game_id=?",
                         (hand["game_id"],))
    if not check.fetchone():
        hands_cursor.execute("insert into game_pnl values (?,?)",t)
    
GAME_START = "Game started"
GAME_ENDED = "Game ended"
def read_file(betcoin_file, user="xenc", record=False):
    """
    Check hands against game started, game ended.
    """
    pnl_sequence = []
    with open(betcoin_file, 'rb') as f:
        next_line = f.readline()
        #print next_line
        hand = {}
        while next_line:
            # read as tokens
            #next_line = next_line.decode('utf-16','ignore').rstrip()
            # get Game ID:
            is_game, game_id = get_game_id(next_line)
            if is_game:
                hand["game_id"] = game_id
            if is_user(next_line, user):
                is_pnl, pnl = get_pnl(next_line)
                if is_pnl:
                    pnl_sequence.append(pnl)
                    hand["pnl"] = pnl
                    if record:
                        add_hand(hand)
            next_line = f.readline()
    hands_conn.commit()
    return pnl_sequence


