# look at db
import sqlite3
import numpy
import matplotlib.pyplot as plt

hands_conn = sqlite3.connect('all_hands.db')
print "connected to all_hands.db"
hc = hands_conn.cursor()
print "cursor constructed."
res = hc.execute("""
select sum(pnl) from game_pnl
limit 1;
""").fetchall()
for a in res:
    print a

def graph_pnl():
    hc.execute('''select * from game_pnl
            order by game_id asc
            ;''')    
    seq = [b for a,b in hc.fetchall()]
    tot = numpy.cumsum(seq)
    plt.plot(tot)
    plt.ylabel("pnl (mBTC)")
    plt.xlabel("hands")
    plt.show()

graph_pnl()
