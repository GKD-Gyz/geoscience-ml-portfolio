# geoscience-ml-portfolio

地质与古生物数据分析 / 机器学习项目集（龚宇洲）

## 📍 当前进度

**第 1 周 ✅ 已完成 → 下一步：第 2 周（基本数据类型、分支循环）**

> 每次打开仓库先看 [`notes/进度.md`](notes/进度.md)

## 目录

| 目录 | 内容 |
|---|---|
| `L1_basics/` | 入门练习脚本（hello.py / check_env.py / week1_debug.py） |
| `L2_pandas/` | 蜗牛数据清洗流程（论文一） |
| `L3_cyclostratigraphy/` | Acycle 旋回地层分析（松科3井复现 + 自研序列），`data/` 放公开 GR/Rb/Sr 序列及来源 DOI |
| `A_core_recognition/` | 任务线A：岩心识别（01_annotation / 02_train / 03_digitize） |
| `B_microfossil/` | 任务线B：微体化石（04_detection / 05_stats） |
| `C_toc_model/` | 生油判断模型（XGBoost / RandomForest） |
| `notes/` | 每周学习笔记 + 进度总览 |

## 环境

Miniconda + `geo` 环境（Python 3.11）：

```bash
conda activate geo
pip install numpy pandas matplotlib scipy jupyterlab openpyxl
pip install scikit-learn xgboost lightgbm
pip install torch torchvision
pip install ultralytics
```

自检：

```bash
python env_check.py          # 12 个包全检
python L1_basics/check_env.py  # 带实际计算的验证
```

## 每周速查

| 周 | 主题 | 笔记 |
|---|---|---|
| 1 | 环境 + 第一个脚本 + 调试 | [notes/第1周.md](notes/第1周.md) |
| 2 | 数据类型、分支循环 | 待写 |

## 参考

- Schlitzer, R., Ocean Data View
- Li, M. et al. 2019, Earth-Science Reviews（旋回地层）