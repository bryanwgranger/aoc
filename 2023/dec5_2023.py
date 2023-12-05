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
print(map_dict)
seed_paths = {k:[] for k in seeds}

new_seed = None
for s in seeds:
    if not seed_paths[s]:
        seed = s
    else:
        seed = seed_paths[s][-1]
    for k, vals in map_dict.items():
        mapped = False
        for v in vals:
            destination_range_start = v[0]
            source_range_start = v[1]
            step = v[2]

            d_range = range(v[0],v[0]+step+1)
            s_range = range(v[1], v[1]+step+1)

            #mapper = zip(s_range, d_range)

            if seed in s_range:
                s_idx = seed - v[1]
                dest_num = v[0] + s_idx
                seed_paths[s].append(dest_num)
                mapped = True

        if not mapped:
            seed_paths[s].append(seed)



print(seed_paths)
seed_ends = [v[-1] for v in seed_paths.values()]
print(min(seed_ends))



