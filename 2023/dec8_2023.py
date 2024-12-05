import math
with open("dec8_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

directions = lines[0]
coord_dict = {}
for l in lines:
    if len(l.split("=")) > 1:
        k = l.split("=")[0].strip()
        v = l.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")
        coord_dict[k] = v

new_pos = "AAA"
def run_route(new_pos, end_pos):
    steps = 0
    zzz_state = False
    while not zzz_state:
        for d in directions:
            pos = new_pos
            if d == "L":
                new_pos = coord_dict[pos][0]
            elif d == "R":
                new_pos = coord_dict[pos][1]
            steps += 1
            #print(new_pos)
            if end_pos:
                if new_pos == end_pos:
                    zzz_state = True
                    break
            else:
                if new_pos.endswith("Z"):
                    zzz_state = True
                    break
    return steps, new_pos
print("answer part one:", run_route("AAA", "ZZZ")[0])

start_nodes = [k for k in coord_dict.keys() if k.endswith("A")]
end_nodes = [e for e in coord_dict.keys() if e.endswith("Z")]

p = []
n = 1
for s in start_nodes:
    st, np = run_route(s, end_pos=None)
    p.append(st)

p2_two = math.lcm(*p)
print("answer part two:", p2_two)
