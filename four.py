with open('./input4.txt', mode='r') as f:
    cards = f.readlines()
    sum = 0
    for card in cards:
        id, card = card.split(': ')
        winning_num, actual_num = card.replace('  ', ' ').split(' | ')
        winning_num = winning_num.split(' ')
        actual_num = actual_num.removesuffix('\n').split(' ')
        cnt = 0
        for num in actual_num:
            if num in winning_num:
                cnt += 1

        points = 1 if (cnt != 0) else 0
        if points == 1:
            for i in range(cnt-1):
                points*=2
        
        sum += points
    print(sum)
