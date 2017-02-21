# setup dbs
import sqlite3
hands_conn = sqlite3.connect('all_hands.db')
hands_cursor = hands_conn.cursor()
hands_cursor.execute("create table game_pnl (game_id, pnl)")
hands_conn.commit()
hands_conn.close()
