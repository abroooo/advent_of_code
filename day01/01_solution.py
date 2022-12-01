
id = 1
cal = 0

with open('01_input', 'r') as i:
    lines = i.readlines()
    cc = 0
    tid = 1
    for line in lines:
        if line == '\n':
            if cc > cal:
                cal = cc
                id = tid
            cc = 0
            tid += 1
        else:
            cc += int(line.strip())

    print('Solution to A - most packed elf: {} with {}'.format(id,cal))

    topelfs = {}
    cc = 0
    tid = 1
    for line in lines:
        if line == '\n':
            if len(topelfs) < 3:
                topelfs[tid] = cc
            else:
                min_key = min(topelfs.keys(), key=lambda k: topelfs[k])
                if topelfs[min_key] < cc:
                    del topelfs[min_key]
                    topelfs[tid] = cc
            cc = 0
            tid += 1
        else:
            cc += int(line.strip())
    sum = 0
    for _,v in topelfs.items():
        sum += v
    print("Solution to B - top 3 elfs have {} calories combined".format(sum))
    
