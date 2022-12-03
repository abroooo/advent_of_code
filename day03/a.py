priorities ={
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,
        'A':27,
        'B':28,
        'C':29,
        'D':30,
        'E':31,
        'F':32,
        'G':33,
        'H':34,
        'I':35,
        'J':36,
        'K':37,
        'L':38,
        'M':39,
        'N':40,
        'O':41,
        'P':42,
        'Q':43,
        'R':44,
        'S':45,
        'T':46,
        'U':47,
        'V':48,
        'W':49,
        'X':50,
        'Y':51,
        'Z':52,
        }

sum = 0
lists = []

with open('input') as i:
    lines = i.readlines()
    for line in lines:
        line = line.strip()
        middle = int(len(line)/2)
        comp_1 = line[:middle]
        comp_2 = line[middle:]
        common = list(set(comp_1).intersection(comp_2))
        sum += priorities[common[0]]
    print(sum)
print('--------------------')

sum = 0
cnt = 0
with open('input') as i:
    lines = i.readlines()
    for line in lines:
        line = line.strip()
        lists.append(line)
        cnt +=1
        if cnt == 3:
            # compute priority
            cnt = 0
            common = set.intersection(*map(set,lists))
            sum += priorities[next(iter(common))]
            lists = []
    print(sum)
