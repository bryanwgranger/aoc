with open("dec9.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)
def print_mem(mem_tups):
    return "".join([str(m[0]) for m in mem_tups])
files = lines[0].strip()
mem_tups = []
mem = []
id_count = 0
file_indictator = True
for f in files:
    if file_indictator:
        for _ in range(int(f)):
            mem.append(str(id_count))
        mem_tups.append((id_count, int(f)))
        id_count += 1
        file_indictator = False
    else:
        # if f != "0":
        #     mem.append("."*int(f))
        # else:
        #     pass
        for _ in range(int(f)):
            mem.append(".")
            mem_tups.append((".", None))
        file_indictator = True

print(mem)
print(mem_tups)
test = [m for m in mem_tups if mem_tups[0] != "."]

rev_files = sorted([m for m in mem_tups if not m[0] == "."], reverse=True, key=lambda x: x[0])
print(rev_files)
#print(mem_tups)
ans = 0
print("rev_files:", len(rev_files))
part1 = False
if part1:
    i = 0
    ans_pt1 = 0
    ###Part one
    while i < len(mem):
        ch = mem[i]
        # print(print_mem(mem_tups))
        # print("i =", i, len(mem_tups))
        if ch == ".":
            while mem[-1] == ".":
                mem.pop(-1)
            mem[i] = mem.pop(-1)
            ans_pt1 += i * int(mem[i])
            i += 1
        else:
            ans_pt1 += i * int(ch)
            # print("b", i, ch)
            i += 1

    print(ans_pt1)
    print("EEEEEND")
###part two
seen_files = set()
ans_pt2 = 0
i = 0
while i < len(mem_tups):
    file_idx, file_count = mem_tups[i]
    print(file_idx, file_count)
    if file_idx != ".":
        for j in range(file_count):
            ans += i+j * file_idx
        seen_files.add(file_idx)
        i += 1
    else:
        k = 0
        while mem_tups[k+i][0] == ".":
            print("yes")
            k += 1
        r_i = -1
        while (mem_tups[r_i][1] > k or mem_tups[r_i][0] == ".") and mem_tups[r_i] not in seen_files:
            seen_files.add(mem_tups[r_i])
            r_i -= 1
        repl_idx, repl_count = mem_tups[r_i]
        for j in range(repl_count):
            ans += i+j * int(file_idx)
        seen_files.add(file_idx)
        i += 1 + j

print(ans)

        # r_i = len(mem_tups)
        # while (mem_tups[r_i][1] > k or mem_tups[r_i][0] == ".") and r_i > 0:
        #     if mem_tups[r_i] not in seen_files:
        #         seen_files.add(mem_tups[r_i])



assert False
#     #print(mem_tups[i])
#     #print("".join(mem))
#     #print(print_mem(mem_tups))
#     #print("i =", i, len(mem_tups))
# if mem_tups[i][0] == ".":
#
#     block_length = mem_tups[i][1]
#     #for _ in range(len(ch)):
#         # print("free space num", free_space_num, "->", free_space_num-1)
#         # print("rev_files:", len(rev_files), "->", len(rev_files)-1)
#         files_that_dont_move = set()
#         r_i = len(mem_tups)-1
#         # print("inter mem tups", len(mem_tups))
#         print("looking to replace:", mem_tups[i], "i =", i)
#         print("r_i", r_i, mem_tups[r_i], "block_length =", block_length)
#         while (mem_tups[r_i][1] > block_length or mem_tups[r_i][0] == ".") and r_i > 0:
#             if r_i not in files_that_dont_move:
#                 files_that_dont_move.add(r_i)
#             r_i -= 1
#             print("inside while:", mem_tups[r_i], "r_i =", r_i)
#
#         replacement_file = mem_tups[r_i]
#         # print("mmmmmm", mem_tups[r_i])
#
#         #ans += i * rev_files[0][0]
#
#         #print("a", i, rev_files[0])
#         for j in range(replacement_file[1]):
#             new_val = mem_tups.pop(r_i-j)
#             ans += i +j* int(replacement_file[0])
#             print("a", i+j, replacement_file[0])
#         print("new_len mem tups", len(mem_tups))
#         mem_tups[i:i+replacement_file[1]] = [(str(replacement_file[0]), mem_tups[i][1]) for _ in range(replacement_file[1])]
#
#         i += replacement_file[1]
#         # print(mem_tups[-1])
#         # print(mem_tups[-1][0])
#         # while mem_tups[-1][0] == ".":
#         #     mem_tups.pop(-1)
#         #     print(mem_tups[-1])
#         #mem_tups.pop(-1)
#
#     else:
#         ans += i * int(ch)
#         print("b", i, ch)
#         i += 1
#     print(ans)
# print(ans)