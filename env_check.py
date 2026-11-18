"""环境自检：运行 `python env_check.py`，全部通过说明装机完成。"""
import sys

mods = [
    ("numpy", "numpy"), ("pandas", "pandas"), ("matplotlib", "matplotlib"),
    ("scipy", "scipy"), ("jupyterlab", "jupyterlab"), ("openpyxl", "openpyxl"),
    ("scikit-learn", "sklearn"), ("xgboost", "xgboost"), ("lightgbm", "lightgbm"),
    ("torch", "torch"), ("torchvision", "torchvision"), ("ultralytics", "ultralytics"),
]

print(f"Python {sys.version.split()[0]}  |  {sys.executable}\n")
ok = True
for pkg, mod in mods:
    try:
        m = __import__(mod)
        ver = getattr(m, "__version__", "?")
        print(f"  [OK]   {pkg:14s} {ver}")
    except Exception as e:
        ok = False
        print(f"  [FAIL] {pkg:14s} {e}")

print("\nall ok" if ok else "\n有缺失，请检查上面的 FAIL 项")
sys.exit(0 if ok else 1)
