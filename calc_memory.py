


with open("memory.csv", "r") as f:
    lines = f.readlines()

print(len(lines))
_sum = 0
for i, line in enumerate(lines):
    #line.strip().replace(" ", "").replace("\xa0", "")
    s = line.split("\t")[1]
    s = s.replace(" ", "").replace("\xa0", "").replace("B", "").replace(",", "")
    s = s.replace("K", "000").replace("M", "00000").replace("G", "0000000")
    print(s)
    _sum += int(s)
    if i == 1000:
        break
print(_sum / 1024**3)