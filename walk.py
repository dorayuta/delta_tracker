# walk
import os
import hand_reader

hand_file_path = r"C:\Users\yutak\OneDrive\Poker\betcoin tracker\hand_files"
def walk(record=False):
    pnl_sequence = []
    for file_name in os.listdir(hand_file_path):
        try:
            file_name.index(".txt")
        except ValueError:
            continue
        f = hand_file_path+r"/"+file_name
        print file_name
        #test(f)
        earnings = hand_reader.read_file(f, user="xenc", record=record)
        print "number of hands: ", len(earnings)
        pnl_sequence.extend(earnings)
    return pnl_sequence

walk(True)
print "done"
