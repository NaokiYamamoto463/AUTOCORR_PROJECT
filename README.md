# Autocorrelation Analysis Tool

## 概要

このプログラムは、`.bin` ファイルを読み込み、ビット列の自己相関関数（Autocorrelation Function）を計算するツールです。

主な機能：

* `.bin` ファイルをビット列へ変換
* 自己相関関数の計算
* CSV形式で保存
* グラフ画像（PNG）を生成

---

# ディレクトリ構成

```text
project/
├── .venv/                 # Python仮想環境
├── bindata/               # 入力する .bin ファイル
├── output/                # 出力結果
├── src/
│   └── autocorr.py        # メインプログラム
├── README.md
├── requirements.txt
└── setup.sh
```

---

# 必要環境

* Python 3.10 以上推奨

---

# セットアップ

## 1. 仮想環境作成

```bash
python3 -m venv .venv
```

---

## 2. 仮想環境有効化

### Linux / WSL

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. 必要ライブラリインストール

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```text
numpy
matplotlib
```

---

# 入力データ

`.bin` ファイルを `bindata/` に配置してください。

例：

```text
bindata/random.bin
```

---

# 実行方法

```bash
python src/autocorr.py
```

---

# 出力結果

実行後、`output/` に以下が生成されます。

## autocorrelation.csv

自己相関値を保存したCSVファイル

```text
r(0), r(1), r(2), ...
```

---

## autocorrelation.png

自己相関関数のグラフ画像

* 横軸：Lag h
* 縦軸：Autocorrelation r(h)

---

# 自己相関関数について

自己相関関数は、

「ビット列を h ビットずらしたとき、どれくらい元の列と似ているか」

を表します。

乱数列として理想的な場合：

* r(0) = 1
* r(h) ≈ 0 (h > 0)

となります。

---

# 実装概要

## 1. バイナリ読み込み

```python
np.fromfile()
```

で `.bin` ファイルを1バイト単位で読み込みます。

---

## 2. ビット展開

```python
np.unpackbits()
```

を用いて、

```text
1 byte → 8 bit
```

へ変換します。

---

## 3. 自己相関計算

以下の式を用いて自己相関を計算します。

r(h)=\frac{\sum_{i=0}^{N-h-1}(x_i-\bar{x})(x_{i+h}-\bar{x})}{\sum_{i=0}^{N-1}(x_i-\bar{x})^2}

---

# 注意

* `bindata/` に `.bin` ファイルが存在しない場合、プログラムは終了します。
* 最初に見つかった `.bin` ファイルを自動で読み込みます。
