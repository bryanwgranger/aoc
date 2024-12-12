with open("dec5_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

map_dict = {}
current_map = None
for i, l in enumerate(lines):
    if l == "":
        continue
    if l.startswith("seeds"):
        seeds = [int(n) for n in l.split(":")[-1].split()]
    elif "map" in l:
        current_map = l.split()[0]
        map_dict[current_map] = []
    if current_map and current_map not in l:
        map_dict[current_map].append([int(b) for b in l.split()])

seed_paths = {k:[] for k in seeds}


for s in seeds:
    for i, (k, vals) in enumerate(map_dict.items()):
        if len(seed_paths[s]) == 0:
            current_num = s
        else:
            current_num = seed_paths[s][-1]

        number_to_add = current_num
        for v in vals:
            s_range = range(v[1], v[1]+v[2]+1)

            if current_num in s_range:
                s_idx = current_num - v[1]
                dest_num = v[0] + s_idx
                number_to_add = dest_num

        seed_paths[s].append(number_to_add)

seed_ends = [v[-1] for v in seed_paths.values()]
print("answer part one:", min(seed_ends))

#part 2
part_2_locations = []

total_seeds = 0
min_location = None
for i in range(0, len(seeds), 2):
    # if i != 6:
    #     continue
    print("starting superseed", i+1)
    start_seed = seeds[i]
    seed_length = seeds[i+1]

    seed_range = range(start_seed, start_seed+seed_length+1)
    #seed_paths = {k: [] for k in seed_range}

    for s in seed_range:
        number_to_add = None
        for i, (k, vals) in enumerate(map_dict.items()):
            if not number_to_add:
                current_num = s
            else:
                current_num = number_to_add

            #number_to_add = current_num
            for v in vals:
                s_range = range(v[1], v[1] + v[2] + 1)

                if current_num in s_range:
                    s_idx = current_num - v[1]
                    dest_num = v[0] + s_idx
                    number_to_add = dest_num

            #seed_paths[s].append(number_to_add)
        #part_2_locations.append(number_to_add)
        if not min_location:
            min_location = number_to_add
        else:
            min_location = min(number_to_add, min_location)
        total_seeds += 1
        if total_seeds % 1000000 == 0:
            print(total_seeds, "done, current min_location =", min_location)




print(min_location)