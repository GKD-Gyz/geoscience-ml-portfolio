# -*- coding: utf-8 -*-
"""
调试练习：用这个文件练习「打断点 + 单步执行」

【怎么判断调试真的停住了】
  暂停时你会看到三样东西同时出现：
    1. 左侧浮出一个调试工具条（继续 / 单步跳过 / 单步进入 / 重启 / 停止）
    2. 当前停住的那一行，整行变成黄色高亮
    3. 底部状态栏变成橙色，显示"正在调试"
  并且终端里只会打印到 "=== 程序开始 ===" 就停住，
  后面的"样本值 / 累加和"不会出现。

【操作顺序】
  F5     启动调试 → 停在第 1 个断点
  F10    单步跳过一行（重复按，逐行执行）
  F11    单步进入（进入函数内部，本例用不到）
  F5     继续到下一个断点
  Shift+F5  停止调试

【注意】不要按 Ctrl+F5，那是"不调试运行"，会无视所有断点。
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

lengths = [2.3, 2.8, 1.9, 3.1, 2.5]

print("=== 程序开始 ===")      # ← 断点设在这里也可以：能先看到这一行再停

total = 0                      # ← 第 1 个断点建议设在这里
count = 0

for x in lengths:
    total += x                 # ← 第 2 个断点建议设在这里，观察 total 累加
    count += 1

average = total / count

print("样本值 :", lengths)
print("累加和 :", total)
print("样本数 :", count)
print("平均值 :", round(averagprint("=== 程序结束 ===")