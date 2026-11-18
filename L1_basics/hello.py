# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")   # 让 Git Bash / 终端正确显示中文
# hello.py —— 第 1 周练习：打印 + 简单计算
# 运行方式（Git Bash 里）：
#   cd ~/Documents/geoscience-ml-portfolio/L1_basics
#   python hello.py

print("Hello, 地质学!")

# 一组蜗牛壳体的长度测量值（cm）
lengths = [2.3, 2.8, 1.9, 3.1, 2.5, 2.7, 2.1, 2.9, 2.4, 2.6]

total = sum(lengths)
count = len(lengths)
average = total / count

print(f"样本数：{count}")
print(f"平均值：{average:.3f} cm")
print(f"最大值：{max(lengths)} cm")
print(f"最小值：{min(lengths)} cm")
print(f"总和：  {total} cm")

# for + if 组合：挑出大于平均值的样本
big = []
for x in lengths:
    if x > average:
        big.append(x)
print(f"大于平均值的样本：{big}")