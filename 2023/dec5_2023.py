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
print(map_dict.keys())
seed_paths = {k:[] for k in seeds}

new_seed = None
for s in seeds:
    print(seed_paths)
    # if not new_seed:
    #     seed = s
    # else:
    #     seed = new_seed
    if len(seed_paths[s]) == 0:
        current_num = s
    else:
        current_num = seed_paths[s][-1]
    print(current_num)
    for i, (k, vals) in enumerate(map_dict.items()):
        mapped = False
        for v in vals:

            #set placeholder
            #seed_paths[s].append(current_num)
            destination_range_start = v[0]
            source_range_start = v[1]
            step = v[2]

            d_range = range(v[0], v[0]+step+1)
            s_range = range(v[1], v[1]+step+1)

            #mapper = zip(s_range, d_range)
            #print(seed)
            if current_num in s_range:
                s_idx = current_num - v[1]
                dest_num = v[0] + s_idx
                print("dest", dest_num)
                print(seed_paths[s])
                seed_paths[s].append(dest_num)
                print(seed_paths[s])
                new_seed = dest_num
                continue


        if not mapped:

            seed_paths[s].append(current_num)
            new_seed = current_num




print(seed_paths)
seed_ends = [v[-1] for v in seed_paths.values()]
print(min(seed_ends))



