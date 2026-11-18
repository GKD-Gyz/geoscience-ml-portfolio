# -*- coding: utf-8 -*-
"""
调试练习：用这个文件练习「打断点 + 单步执行」

操作步骤：
  1. 在 VS Code 里打开本文件
  2. 在下面第 24 行（total += x 那一行）左侧灰色区域点一下 → 出现红点 = 断点
  3. 按 F5 启动调试
  4. 程序会停在第 24 行，此时把鼠标悬停在 total 和 x 上，能看到当前值
  5. 按 F10（单步跳过）逐行执行，观察 total 每次怎么变
  6. 按 F5 继续到下一个断点，Shift+F5 停止
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 一组蜗牛壳体长度（cm）
lengths = [2.3, 2.8, 1.9, 3.1, 2.5]

total = 0          # ← 第 1 个断点建议设在这里
count = 0

for x in lengths:
    total += x     # ← 第 2 个断点建议设在这里，观察 total 累加
    count += 1

average = total / count

print("样本值 :", lengths)
print("累加和 :", total)
print("样本数 :", count)
print("平均值 :", round(average, 3))