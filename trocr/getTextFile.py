import os
from pathlib import Path

path = "C:\\Users\\301212298\PycharmProjects\\trocr\\train"

files = os.listdir(path)

jpg_files = [f for f in files if f.endswith('.jpg')]
x_file_content = ''
count = 0
with open("labels.csv", "w") as file:
    for jpg_file in jpg_files:
        try:
            file_name = "C:\\Users\\301212298\\Downloads\\annotated or proofread text files-20230909T145045Z-001\\annotated or proofread text files\\batch1\\{}.txt".format(jpg_file[:-4])
            print(file_name)
            content = Path(file_name).read_text(encoding='utf-8')
            x_file_content += jpg_file + ',"' + content + "\"\n"

            count += 1

            print('finished {}'.format(jpg_file))
            if count == 200:
                break
        except FileNotFoundError:
            # red color print error
            print("\033[91m {}\033[00m" .format('failed {}'.format(jpg_file)))

            continue

x_file = Path('labels.csv').write_text(x_file_content, encoding='utf-8')

