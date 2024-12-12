with open("dec6.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)
grid = [list(l) for l in lines]
print(grid)

def part_one(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in ["^", "<", ">", "v"]:
                original_guard_pos = (r, c)
                guard_direction = grid[r][c]
    guard_spots = set()
    guard_spots_dir = set()
    potential_obstacles = 0
    potential_obs_spots = set()
    for obs_r in range(len(grid)):
        for obs_c in range(len(grid[0])):
            guard_pos = original_guard_pos
            print((obs_r, obs_c))
            while guard_pos[0] not in [0,len(grid)-1] and guard_pos[1] not in [0,len(grid[0])-1]:
                obs_found = False
                #find direction and search for obstacles
                if guard_direction == "^":
                    for r in range(guard_pos[0]-1, -1, -1):
                        # if not obs_found:
                        #     for c in range(guard_pos[1]+1, len(grid[0])):
                        #         if ((r, c), ">") in guard_spots_dir:
                        #             potential_obstacles += 1
                        #             potential_obs_spots.add((r-1, guard_pos[1]))
                        #             obs_found = True
                        if grid[r][guard_pos[1]] == "#":
                            #print("obstacle at", (r, guard_pos[1]))
                            #guard_pos = (r, guard_pos[1])
                            if ((r-1, guard_pos[1]), guard_direction) in potential_obs_spots:
                                potential_obstacles += 1
                            potential_obs_spots.add(((r-1, guard_pos[1]), guard_direction))
                            guard_direction = ">"
                        else:
                            guard_pos = (r, guard_pos[1])
                            #print(guard_pos, "going", guard_direction)
                            guard_spots.add(guard_pos)
                            if (guard_pos, guard_direction) in guard_spots_dir:
                                potential_obstacles += 1
                            guard_spots_dir.add((guard_pos, guard_direction))
                        #test for part 2
                        break
                if guard_direction == ">":
                    for c in range(guard_pos[1]+1, len(grid[0])):
                        # if not obs_found:
                        #     for r in range(guard_pos[0]+1, len(grid)):
                        #         if ((r, c), "v") in guard_spots_dir:
                        #             potential_obstacles += 1
                        #             potential_obs_spots.add((guard_pos[0], c + 1))
                        #             obs_found = True
                        if grid[guard_pos[0]][c] == "#":
                            #print("obstacle at", (guard_pos[0], c))
                            #guard_pos = (guard_pos[0], c)
                            potential_obs_spots.add(((guard_pos[0], c + 1), guard_direction))
                            guard_direction = "v"
                            break
                        else:
                            guard_pos = (guard_pos[0], c)
                            #print(guard_pos, "going", guard_direction)
                            guard_spots.add(guard_pos)
                            if (guard_pos, guard_direction) in guard_spots_dir:
                                potential_obstacles += 1
                            guard_spots_dir.add((guard_pos, guard_direction))
                        break
                if guard_direction == "v":
                    for r in range(guard_pos[0]+1, len(grid)):
                        # if not obs_found:
                        #     for c in range(guard_pos[1]-1, -1, -1):
                        #         if ((r, c), "<") in guard_spots_dir:
                        #             potential_obstacles += 1
                        #             potential_obs_spots.add((r + 1, guard_pos[1]))
                        #             obs_found = True
                        if grid[r][guard_pos[1]] == "#":
                            #print("obstacle at", (r, guard_pos[1]))
                            #guard_pos = (r, guard_pos[1])
                            potential_obs_spots.add(((r + 1, guard_pos[1]), guard_direction))
                            guard_direction = "<"
                        else:
                            guard_pos = (r, guard_pos[1])
                            #print(guard_pos, "going", guard_direction)
                            guard_spots.add(guard_pos)
                            if (guard_pos, guard_direction) in guard_spots_dir:
                                potential_obstacles += 1
                            guard_spots_dir.add((guard_pos, guard_direction))
                        break
                if guard_direction == "<":
                    for c in range(guard_pos[1]-1, -1, -1):
                        # if not obs_found:
                        #     for r in range(guard_pos[0]-1, -1, -1):
                        #         if ((r, c), "^") in guard_spots_dir:
                        #             potential_obstacles += 1
                        #             potential_obs_spots.add((guard_pos[0], c - 1))
                        #             obs_found = True
                        if grid[guard_pos[0]][c] == "#":
                            #print("obstacle at", (guard_pos[0], c))
                            #guard_pos = (guard_pos[0], c)
                            potential_obs_spots.add(((guard_pos[0], c - 1), guard_direction))
                            guard_direction = "^"
                        else:
                            guard_pos = (guard_pos[0], c)
                            # print(guard_pos, "going", guard_direction)
                            guard_spots.add(guard_pos)
                            if (guard_pos, guard_direction) in guard_spots_dir:
                                potential_obstacles += 1
                            guard_spots_dir.add((guard_pos, guard_direction))
                        break
    return len(guard_spots), guard_spots_dir, potential_obstacles


ans, guard_spots_dir, potential_obs = part_one(grid)
print(guard_spots_dir)
print(ans)
print(potential_obs)
print(len(grid), len(grid[0]))
print("++++++++++++++++++++++++")



assert False
for r in range(len(grid)):
    for c in range(len(grid[0])):
        #test above
        if r > 0 and ((r-1,c), "<") in guard_spots_dir and ((r-1,c), "v") in guard_spots_dir:
            potential_obstacles += 1
        #test left
        if c > 0 and ((r, c-1), "v") in guard_spots_dir and ((r, c-1), ">") in guard_spots_dir:
            potential_obstacles += 1
        #test below
        if r < len(grid)-1 and ((r+1,c), ">") in guard_spots_dir and ((r+1,c), "^") in guard_spots_dir:
            potential_obstacles += 1
        #test right
        if c < len(grid[0])-1 and ((r, c+1), "^") in guard_spots_dir and ((r, c+1), "<") in guard_spots_dir:
            potential_obstacles += 1
print(potential_obstacles)




def part_ttwo_X(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in ["^", "<", ">", "v"]:
                guard_pos = (r, c)
                guard_direction = grid[r][c]
    guard_spots = set()
    #guard_spots_dir = set()
    potential_obstacles = 0
    #add initial guard pos
    guard_spots_dir = set()
    guard_spots_dir.add((guard_pos, guard_direction))
    while guard_pos[0] not in [0,len(grid)-1] and guard_pos[1] not in [0,len(grid[0])-1]:

        #find direction and search for obstacles
        if guard_direction == "^":

            for r in range(guard_pos[0]-1, -1, -1):
                if grid[r][guard_pos[1]] == "#":
                    print("obstacle at", (r, guard_pos[1]))
                    #guard_pos = (r, guard_pos[1])
                    guard_direction = ">"
                else:
                    guard_pos = (r, guard_pos[1])
                    print(guard_pos, "going", guard_direction)
                    guard_spots.add(guard_pos)
                    if (guard_pos, ">") in guard_spots_dir:
                        potential_obstacles += 1
                        print("OBSTACLE NEXT TO {}".format(guard_pos))
                    guard_spots_dir.add((guard_pos, guard_direction))
                break
        if guard_direction == ">":
            for c in range(guard_pos[1]+1, len(grid[0])):
                if grid[guard_pos[0]][c] == "#":
                    print("obstacle at", (guard_pos[0], c))
                    #guard_pos = (guard_pos[0], c)
                    guard_direction = "v"
                    break
                else:
                    guard_pos = (guard_pos[0], c)
                    print(guard_pos, "going", guard_direction)
                    guard_spots.add(guard_pos)
                    if (guard_pos, "v") in guard_spots_dir:
                        potential_obstacles += 1
                        print("OBSTACLE NEXT TO {}".format(guard_pos))
                    guard_spots_dir.add((guard_pos, guard_direction))
                break
        if guard_direction == "v":
            for r in range(guard_pos[0]+1, len(grid)):
                if grid[r][guard_pos[1]] == "#":
                    print("obstacle at", (r, guard_pos[1]))
                    #guard_pos = (r, guard_pos[1])
                    guard_direction = "<"
                else:
                    guard_pos = (r, guard_pos[1])
                    print(guard_pos, "going", guard_direction)
                    guard_spots.add(guard_pos)
                    if (guard_pos, "<") in guard_spots_dir:
                        potential_obstacles += 1
                        print("OBSTACLE NEXT TO {}".format(guard_pos))
                    guard_spots_dir.add((guard_pos, guard_direction))
                break
        if guard_direction == "<":
            for c in range(guard_pos[1]-1, -1, -1):
                if grid[guard_pos[0]][c] == "#":
                    print("obstacle at", (guard_pos[0], c))
                    #guard_pos = (guard_pos[0], c)
                    guard_direction = "^"
                else:
                    guard_pos = (guard_pos[0], c)
                    print(guard_pos, "going", guard_direction)
                    guard_spots.add(guard_pos)
                    if (guard_pos, "^") in guard_spots_dir:
                        potential_obstacles += 1
                        print("OBSTACLE NEXT TO {}".format(guard_pos))
                    guard_spots_dir.add((guard_pos, guard_direction))
                break
    return len(guard_spots), potential_obstacles



