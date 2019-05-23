import os
import sys
from collections import defaultdict

split_map = defaultdict(set)

with open('split.txt') as f:
    name = ''
    for line in f:
        if not line.strip():
            name = ''
            continue
        if not name:
            name = line.strip()
            continue
        if '-' in line:
            fr, to = line.split('-')
            fr, to = int(fr), int(to)
        else:
            fr = to = int(line)

        split_map[name].update(range(fr, to+1))

files = sys.argv[1:]
for f in files:
    base_name = os.path.basename(f)
    idx = int(base_name[5:9])
    for name in ['train', 'dev', 'test']:
        if idx in split_map[name]:
            os.rename(f, os.path.join(name, base_name))
