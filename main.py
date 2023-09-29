import os

flag = 0
markdown = """# 2023年终总结

- 2021 年的年终总结见：[saveweb/review-2021](https://github.com/saveweb/review-2021)
- 2022 年的年终总结见：[saveweb/review-2022](https://github.com/saveweb/review-2022)
- 2023 年：就是这里啦！

写好了吗？写好了快交。
"""

with open('metadata.md', 'r') as f:
  file = f.read()
lines = file.splitlines()
header = lines[0:2]
# print(header)
# import sys
# sys.exit(0)
lines = set(lines[2:])
lines.discard('')
lines = list(lines)
lines.sort()

with open('README.md', 'w') as f:
  f.write(markdown+'计数: '+str(len(lines))+' 篇。\n\n')
  for line in header:
    f.write(line+'\n')
  lines = set(lines)
  for line in lines:
    f.write(line+'\n')
