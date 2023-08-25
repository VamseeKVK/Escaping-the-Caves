import re

#mark whenever this line appears and the next line contains required output

pattern = re.compile("Slowly, a new text starts appearing on the screen. It reads ...")
flagged = False

f = open("output_pairs.txt", "w")

for line in open("game_outputs.log"):
    if flagged:
        flagged = False
        f.write("{}\n".format(line.strip()))
    else:
        for match in re.finditer(pattern, line):
            if match:
                flagged = True

f.close()

