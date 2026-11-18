# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")   # 让 Git Bash / 终端正确显示中文
# check_env.py —— 验证 geo 环境里的科研包能否使用
import numpy as np
import pandas as pd
import matplotlib
import scipy
import sklearn
import torch

print("=" * 52)
print("Python 版本 :", sys.version.split()[0])
print("解释器路径 :", sys.executable)
print("=" * 52)
print("numpy       :", np.__version__)
print("pandas      :", pd.__version__)
print("matplotlib  :", matplotlib.__version__)
print("scipy       :", scipy.__version__)
print("scikit-learn:", sklearn.__version__)
print("torch       :", torch.__version__)
print("=" * 52)

# 真跑一次计算，确认功能正常（而不只是"装了"）
data = np.array([2.3, 2.8, 1.9, 3.1, 2.5])
print("numpy 均值  :", round(float(data.mean()), 3))

df = pd.DataFrame({"长度": data, "站点": ["A", "B", "C", "D", "E"]})
print("\npandas 表格：")
print(df.to_string(index=False))

print("\n[OK] 环境正常，可以开始干活了")