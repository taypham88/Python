
# Advent of Code
# --- Day 2: Gift Shop ---

import os

# This gets the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'input_file.txt'

# This joins the script's folder with the filename
file_path = os.path.join(script_dir, file_name)


with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().strip()
    extract = content.split(',')

# Part 1
# process = []
# respository = []
# for code in extract:
#     process.append(code.split('-'))

# for v1,v2 in process:
#     for num in range(int(v1), int(v2)+1):
#         check = str(num)
#         l = len(check)//2
#         # print(num)
#         # print(l, check[:l],check[l:])
#         if len(check) > 1 and check[:l] == check[l:]:
#             respository.append(num)
# Part 2
# (Double String Trick)

repository = []
for entry in extract:
    v1, v2 = entry.split('-')
    for num in range(int(v1), int(v2)+1):
        s = str(num)

        # Part 2 Logic:
        # 1. The string must have at least 2 characters to repeat. (double string trick)
        # 2. Use the (S+S) trick to find if it is periodic.
        # s + s [1:-1] removes the first and last character of the doubled string.
        # print(s, s+s, (s + s)[1:-1])
        if len(s) > 1 and s in (s + s)[1:-1]:
            repository.append(num)

if __name__ == "__main__":
    print(sum(repository))