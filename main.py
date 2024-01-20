flag = 0
markdown = """# review-2023

写好了吗？写好了快交。AI 写的不算数哦。

- 2022 年的年终总结见：[saveweb/review-2022](https://github.com/saveweb/review-2022)

保持传统，本项目将长期维护（直到2025年初）。

**想要添加您的年终总结？请发 Issue 或编辑 metadata.md 发 PR**

**（不需要填写博客ID，不需要编辑 README.md）。**

---

"""

raw_lines = open('metadata.md', 'r').read().splitlines()

header = raw_lines[0:2]

lines = set(raw_lines[2:])
lines.discard('')

with open('README.md', 'w') as f:
  f.write(markdown+'计数: '+str(len(lines))+' 篇。下表每次 CI 乱序输出。\n\n')
  f.write('\n'.join(header))
  f.write('\n')
  f.write('\n'.join(lines))
