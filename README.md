# geoscience-ml-portfolio

地质与古生物数据分析 / 机器学习项目集（龚宇洲）

## 目录

| 目录 | 内容 |
|---|---|
| `L1_basics/` | Python 入门练习脚本 |
| `L2_pandas/` | 蜗牛数据清洗流程（论文一） |
| `L3_cyclostratigraphy/` | Acycle 旋回地层分析（松科3井复现 + 自研序列），`data/` 放公开 GR/Rb/Sr 序列及来源 DOI |
| `A_core_recognition/` | 任务线A：岩心识别（01_annotation 标注 / 02_train 训练 / 03_digitize 数字化） |
| `B_microfossil/` | 任务线B：微体化石（04_detection 检测 / 05_stats 统计） |
| `C_toc_model/` | 生油判断模型（XGBoost / RandomForest） |
| `notes/` | 每周学习笔记（Markdown） |

## 环境

Miniconda + `geo` 环境（Python 3.11）：

```bash
conda activate geo
pip install numpy pandas matplotlib scipy jupyterlab openpyxl
pip install scikit-learn xgboost lightgbm
pip install torch torchvision
pip install ultralytics
```

## 参考

- Schlitzer, R., Ocean Data View
- Li, M. et al. 2019, Earth-Science Reviews（旋回地层）
