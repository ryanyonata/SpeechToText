rname = "dictnew"
wname = "hlist"

listsGrammar = []

open(wname, "w")

with open(rname, "r") as r:
    lines = r.readlines()
    listsGrammar.append(lines)
    variable = "$word"
    line1 = variable+" = "
    line2 = "(SENT-START <"+variable+"> SENT-END)\n"
    for gram in listsGrammar[0]:
        # gram = gram[:-1]
        # if gram:
        #     line1 += gram+" | "
        gram = gram[:-1]
        grams = gram.split()
        gram = grams[0]
        if gram:
            line1 += gram+" | "
    line1 = line1[:-3]
    line1 += ";\n"
    with open(wname, "a") as writeFile:
                writeFile.write(line1+line2)

