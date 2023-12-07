def findFirst(line: str, number_list):
    index_first = len(line)
    digit_first = None
    for num, digit in enumerate(number_list):
        i = line.find(digit)
        if not i == -1:        
            if i < index_first:
                index_first = i
                digit_first = num+1

    for c in line[:index_first+1]:
        if c.isdigit() and not c == '0':
            digit_first = c
            break

    return str(digit_first)

with open('./input1.txt', mode='r') as f:
    lines = f.readlines()
    # sum = solution(lines)
    sum = 0
    numbers = "one,two,three,four,five,six,seven,eight,nine".split(',')
    numbers_rev = []
    for num in numbers:
        numbers_rev.append(num[::-1])
    cnt = 1
    for line in lines:
        first = findFirst(line, numbers)
        last = findFirst(line[::-1], numbers_rev)
        sum += int(first+last)
        print(str(cnt) + ": " + first+last + "-> " + line[:len(line)-1] )
        cnt+=1
    print(sum)



