# dynamic_intramolecular

用于 LAMP / PacBio 测序数据探索的 Python 脚本与 Jupyter Notebook，包含序列逐碱基延伸、引物序列匹配和结果表查看。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| [Analysis.ipynb](Analysis.ipynb) | 根据当前检索序列后续碱基的出现频次逐步延伸序列，支持手动切头、切尾和补充碱基。 |
| [interaction.py](interaction.py) | 检查每条序列是否包含指定引物，生成以 `0/1` 标记的匹配表，字段包括 `number,BIP,FIP,B3,F3,LoopB,LoopF,seq`。 |
| [graph.ipynb](graph.ipynb) | 读取并查看匹配结果 CSV；当前版本尚未包含绘图步骤。 |

## 环境

使用 Python 3 和 Jupyter Notebook。`Analysis.ipynb` 的分析代码使用 Python 标准库；其余文件还需要 pandas、seaborn 和 matplotlib。

```bash
python -m pip install notebook pandas seaborn matplotlib
jupyter notebook
```

## 使用方法

### 序列延伸

1. 打开 `Analysis.ipynb`，将 `ordfile` 改为本地输入文件路径。输入为序列文本，按行组织；当前预处理会删除数字、冒号和 `seq ` 前缀。建议使用大写 A/C/G/T，并保留文件末尾换行，避免当前读取方式漏掉最后一条序列。
2. 运行函数定义、路径设置和预处理单元格，再将 `fastq1.start_seq` 与 `fastq1.remember_seq` 设为相同的起始序列并运行初始化单元格。
3. 按需执行 `fastq1.next()` 延伸一个碱基，通过 `fastq1.remember_seq` 查看结果。循环单元格可连续延伸多次；`cut_first()`、`cut_end()` 和 `add('A')` 可用于手动调整。

Notebook 中的切头、切尾单元格会修改当前状态，请按分析需要选择运行。类名虽为 `fastq`，当前代码读取的是预处理后的文本序列，不直接解析 FASTQ 格式。

### 引物匹配与结果查看

1. 准备每行一条序列的 `group1.txt`，放在运行目录中；按实验设计修改 `interaction.py` 中的 `group1` 引物列表。
2. 运行 `python interaction.py`，生成逗号分隔的 `inter1.txt`。匹配采用原样字符串包含判断，区分大小写。
3. 运行前，将脚本末尾及 `graph.ipynb` 中 `pd.read_csv(...)` 的示例路径改为实际结果文件路径，例如 `pd.read_csv('inter1.txt')`，再打开 notebook 查看结果。

## 数据说明

仓库保存分析代码与 notebook，输入数据文件未随仓库提供。代码中的 Windows 路径、起始序列和引物序列均需按实际数据调整；notebook 中保留的输出来自原分析会话。
