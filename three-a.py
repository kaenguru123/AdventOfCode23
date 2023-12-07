class field():
    def __init__(self):
        with open('./test3.txt', mode='r') as f:
            self.field = f.readlines()
            self.y_max = len(self.field)
            self.x_max = len(self.field[0])

    def get_sum(self):
        sum = 0
        for y, line in enumerate(self.field):
            current_num = ""
            active = False
            for x, char in enumerate(line):
                if char.isnumeric():
                    current_num += char
                    if self.check_surounding(x, y):
                        active = True
                else:
                    if active: sum+=int(current_num)
                    current_num=""
                    active=False
        return sum
    
    def check_surounding(self, x, y):
        range_set = [-1, 0, 1]
        for x_off in range_set:
            for y_off in range_set:
                if not(x+x_off == -1 or x+x_off == self.x_max or y+y_off == -1 or y+y_off == self.y_max):
                    char_to_check = self.field[y+y_off][x+x_off]
                    if self.check_special_char(char_to_check):
                        return True
        return False

    def check_special_char(self, char):
        return not(char.isalnum() or char in '.\n')
    
f = field()
print(f.get_sum())