map = [[0 for _ in range(10)] for _ in range(10)] # 10x10 Check
rowMap = [0,7,13,28,44,62,74,75,87,90] #0,7,13,28,44,62,74,75,87,90

for index in rowMap:
    row = index // 10 #整除避免浮點數(小數)
    col = index % 10
    map[row][col] = '*'
    
for i in range(10):
    for j in range(10):
        if map[i][j] == '*':
            continue
        bomb_c = 0
        for x in range(max(0, i-1), min(10,i+2)):
            for y in range(max (0, j-1),min(10, j+2)):
                if map[x][y] == '*':
                    bomb_c +=1
        map[i][j] = bomb_c if bomb_c > 0 else ' '

for row in map:
    print(" ".join(str(cell) for cell in row))