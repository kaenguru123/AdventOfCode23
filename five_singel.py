class five():
    def __init__(self):
        with open('./input5.txt', 'r') as f:
            content = f.read().split('\n\n')
            self.seeds = content[0].split(' ')[1:]
            self.seeds = [int(seed) for seed in self.seeds]
            self.seeds = [self.seeds[i:i+2] for i in range(0, len(self.seeds), 2)]
            self.maps = [map.split('\n')[1:] for map in content[1:]]
            new_list1 = []
            for map in self.maps:
                new_list2 = []
                for line in map:
                    app = line.split(' ')
                    if len(app) == 3:
                        app = [int(n) for n in app]
                    new_list2.append(app)
                new_list1.append(new_list2)
            self.maps = new_list1

            self.locations = []
            for seed_start, seed_range in self.seeds:
                print(f'new range: {seed_range} (start from: {seed_start})')
                range_of_seeds = list(range(seed_start, seed_start + seed_range))
                new_low = -1
                for seed in range_of_seeds:
                    for map in self.maps:
                        seed = self.mapping(seed, map)
                    if new_low > seed or new_low == -1:
                        new_low = seed
                print(f"add new: {new_low}")
                self.locations.append(new_low)
            print(f"lowest location_id: {min(self.locations)}")

    def mapping(self, seed, map):
        for dest, src, range in map:
            if seed >= src and seed < src+range:
                return dest-src+seed
        return seed

if __name__ == "__main__":
        main = five()