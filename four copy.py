def get_points_of_card(card):
    winning_num, actual_num = card.replace('  ', ' ').split(' | ')
    winning_num = winning_num.split(' ')
    actual_num = actual_num.removesuffix('\n').split(' ')
    cnt = 0
    for num in actual_num:
        if num in winning_num:
            cnt += 1

    points = 1 if (cnt != 0) else 0
    if points == 1:
        for _ in range(cnt-1):
            points*=2
    return points

def recur(list_cp, ans):
    for c, p in enumerate(list_cp):
        ans += sum(len(cards_points[c+1:p-1]))
    recur()

with open('./test4.txt', mode='r') as f:
    cards = f.readlines()
    ans = 0
    cards_points = []
    for card in cards:
        id, card = card.split(': ')
        id = int(id.replace('  ', ' ').replace('  ', ' ').split(' ')[1])
        points = get_points_of_card(card)
        cards_points.append(points)
        ans += 1
    CARD_POINTS = cards_points.copy()
    ans = recur(cards_points, ans)

    print(ans)
