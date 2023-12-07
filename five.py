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

            locations = []
            for seed_start, seed_range in self.seeds:
                cnt = 0
                print(f'new range: {seed_range} (start from: {seed_start})')
                range_of_seeds = list(range(seed_start, seed_start + seed_range))
                tenths = seed_range/1000
                for seed in range_of_seeds:
                    for map in self.maps:
                        seed = self.mapping(seed, map)
                    locations.append(seed)
                    if cnt%tenths==0:
                        print('#')
                    cnt+=1
            print(f"lowest location_id: {min(locations)}")

    def mapping(self, seed, map):
        for dest, src, range in map:
            if seed >= src and seed < src+range:
                return dest-src+seed
        return seed

if __name__ == "__main__":
    main = five()
