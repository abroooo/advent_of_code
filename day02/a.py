# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock



# A -> Rock
# B -> Paper
# C -> Scissors


# X -> Rock
# Y -> Paper
# Z -> Scissors


# A vs X => draw
# A vs Y => win 
# A vs Z => loss

# B vs X => loss
# B vs Y => draw
# B vs Z => win

# C vs X => win
# C vs Y => loss
# C vs Z => draw
A = 1
B = 2
C = 3
X = A
Y = B
Z = C
score = 0

with open('input') as i:
    lines = i.readlines()
    for line in lines:
        line = line.strip()
        picks = tuple(line.split(' '))
        if picks[0] == 'A' and picks[1] == 'X': #=> draw 
            score += 3 + X
        elif picks[0] == 'A' and picks[1] == 'Y': #=> win
            score += 6 +  Y
        elif picks[0] == 'A' and picks[1] == 'Z': #=> loss
            score += Z
            pass

        elif picks[0] ==  'B' and picks[1] == 'X':# => loss
            score += X
            pass
        elif picks[0] ==  'B' and picks[1] == 'Y':# => draw
            score += 3 + Y
            pass
        elif picks[0] ==  'B' and picks[1] == 'Z':# => win
            score += 6 + Z

        elif picks[0] ==  'C' and picks[1] == 'X':# => win
            score += 6 + X
        elif picks[0] ==  'C' and picks[1] == 'Y':# => loss
            score += Y
            pass
        elif picks[0] ==  'C' and picks[1] == 'Z':# => draw
            score += 3 + Z

print(score)
score=0
with open('input') as i:
    lines = i.readlines()
    for line in lines:
        line = line.strip()
        picks = tuple(line.split(' '))
        # X => should lose
        # Y => should draw
        # Z => should win
        if picks[0] == 'A' and picks[1] == 'X': #=> draw 
            score += 0 + Z
        elif picks[0] == 'A' and picks[1] == 'Y': #=> win
            score += 3 +  A
        elif picks[0] == 'A' and picks[1] == 'Z': #=> loss
            score += 6 + Y
            pass

        elif picks[0] ==  'B' and picks[1] == 'X':# => loss
            score += 0 + A
            pass
        elif picks[0] ==  'B' and picks[1] == 'Y':# => draw
            score += 3 + B
            pass
        elif picks[0] ==  'B' and picks[1] == 'Z':# => win
            score += 6 + Z

        elif picks[0] ==  'C' and picks[1] == 'X':# => win
            score += 0 + B
        elif picks[0] ==  'C' and picks[1] == 'Y':# => loss
            score += 3 + C
            pass
        elif picks[0] ==  'C' and picks[1] == 'Z':# => draw
            score += 6 + A

print(score)
