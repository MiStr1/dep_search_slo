xpos_tags = set()


with open("../cckres.conllu", "r", encoding="utf-8") as file:
    for line in file:
        l = line.strip()
        if len(l) > 0 and l[0] in "0123456789":
            xpos_tags.add(l.split("\t")[4] + ">")


xpos_tags = sorted(list(xpos_tags))

with open("xpos_tags.txt", "w") as out:
    out.write(" ".join(xpos_tags))
    
