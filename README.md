# Autocorrelation

`data` フォルダにある最初の `.bin` ファイルを読み込み、自己相関を計算して `output` フォルダへ保存します。

## ファイル

```text
autocorr_project/
  data/                 input .bin files
  output/               generated csv/png files
  src/autocorr.py       main script
  requirements.txt      Python dependencies
```

## セットアップ

PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Git Bash / WSL / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 出力

`data` フォルダに `.bin` ファイルを入れてから実行します。

```powershell
python src/autocorr.py
```

出力:

```text
output/autocorrelation.csv
output/autocorrelation.png
```
