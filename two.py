with open('./input2.txt', mode='r') as f:
    lines = f.readlines()
    # sum = 0
    sum = 0
    impossibleSets = ""
    possibleSets = ""
    for line in lines:
        # impossible = False
        power = 1
        id, game = line.split(':')
        id = id.split(' ')[1]
        game = game[1:]
        game = game.replace(';', ',')
        game = game.split(', ')
        max_set = {'red': 1, 'green': 1, 'blue': 1}
        for set in game:
            cnt, color = set.split(' ')
            color = color.removesuffix('\n')
            cnt = int(cnt)
            if max_set[color] < cnt:
                max_set[color] = cnt
            # if max_set['red'] > 12 or max_set['green'] > 13 or max_set['blue'] > 14:
            #     impossible = True
        for n in max_set.values():
            power *= n
        sum += power
        # if not impossible:
        #     sum+=int(id)
    print(sum)