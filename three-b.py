class field():
    def __init__(self):
        with open('./input3.txt', mode='r') as f:
            self.field = f.readlines()
            self.y_max = len(self.field)
            self.x_max = len(self.field[0])
            self.list_of_gears = []
            for x, line in enumerate(self.field):
                for y, char in enumerate(line):
                    if char == '*':
                        self.list_of_gears.append((x, y))

    def get_sum(self):
        sum = 0
        numbers = []
        for y, line in enumerate(self.field):
            current_num = ""
            gear = None
            for x, char in enumerate(line):
                if char.isnumeric():
                    current_num += char
                    y_gear, x_gear = self.check_surounding(x, y)
                    if y_gear != -1 and x_gear -1:
                        gear = (y_gear, x_gear)
                else:
                    if gear != None: numbers.append(((current_num), gear))
                    current_num=""
                    gear = None
        flipped = []
        list_of = []
        self.num_copy = numbers.copy()
        for i, (num, value) in enumerate(numbers):
            if i+1 < len(numbers):
                for icopy, (numcopy, valuecopy) in enumerate(numbers[i+1:]):
                    if value == valuecopy:
                        list_of.append((int(num), int(numcopy)))
        #     self.how_many_numbers_with_this_gear(i, num, value)
        #     if value not in flipped:
        #         flipped.append((value, num))
        #     else: #if len(key) == 2:
        #         flipped.append((value, num))

        # gear_number_list = []
        # for values in flipped.values():
        #     if len(values) == 2:
        #         gear_number_list.append((int(values[0]), int(values[1])))

        for (first, second) in list_of:
            sum+=first*second
        return sum

    def check_surounding(self, x, y):
        range_set = [-1, 0, 1]
        for x_off in range_set:
            for y_off in range_set:
                if not(x+x_off == -1 or x+x_off == self.x_max or y+y_off == -1 or y+y_off == self.y_max):
                    char_to_check = self.field[y+y_off][x+x_off]
                    if char_to_check == '*':
                        return y+y_off, x+x_off
        return -1, -1

    def check_special_char(self, char):
        return not(char.isalnum() or char in '.\n')
    
f = field()
print(f.get_sum())