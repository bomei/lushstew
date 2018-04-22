import os

path = os.path.expanduser('~/Desktop/a.docx')

with open(path, encoding='utf8') as f:
    y = f.readlines()
    print(1)
