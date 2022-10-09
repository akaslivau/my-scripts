import os

dir_path = 'D:\merge'
files = os.listdir(dir_path)

res = []
for file in files:
    file_path = os.path.join(dir_path, file)
    with open(file_path) as f:
        lines = f.readlines()
        count = len(lines)
        print(file_path)
        print(count)
        if len(res) == 0:
            for i in range(count):
                res.append('')
        for i in range(count):
            separator = '@' if len(res[i]) > 0 else ''
            res[i] = res[i] + separator + lines[i].strip()

with open(os.path.join(dir_path, 'merged.txt'), mode='wt', encoding='utf-8') as my_file:
    my_file.write('\n'.join(res))
