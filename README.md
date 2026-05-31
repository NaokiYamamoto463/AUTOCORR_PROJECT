# Autocorrelation

`data` folderにある最初の `.bin` ファイルを読み込み、自己相関を計算して `output` folderへ保存します。

## Files

```text
autocorr_project/
  data/                 input .bin files
  output/               generated csv/png files
  src/autocorr.py       main script
  requirements.txt      Python dependencies
```

`.venv` はローカル環境用なので、壊れたら作り直して大丈夫です。

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

`data` folderに `.bin` ファイルを入れてから実行します。

```powershell
.\.venv\Scripts\python.exe src\autocorr.py
```

ラグ数を変える場合:

```powershell
.\.venv\Scripts\python.exe src\autocorr.py --max-lag 500
```

出力:

```text
output/autocorrelation.csv
output/autocorrelation.png
```
