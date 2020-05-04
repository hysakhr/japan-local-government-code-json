# 全国地方公共団体コード EXCEL→JSON変換ツール
下記ページの「都道府県コード及び市区町村コード」からダウンロード可能なエクセルファイルをもとにJSONデータを生成するpython製のツールです。

総務省 全国地方公共団体コード
https://www.soumu.go.jp/denshijiti/code.html

2020/4/28時点でダウンロードできるエクセルの形式となっています。

# json format
```
{
  "1": {
    "name": "北海道",
    "yomi": "ほっかいどう",
    "yomi_kana": "ホッカイドウ",
    "yomi_kana_han": "ﾎｯｶｲﾄﾞｳ",
    "cities": {
      "11002": {
        "name": "札幌市",
        "yomi": "さっぽろし",
        "yomi_kana": "サッポロシ",
        "yomi_kana_han": "ｻｯﾎﾟﾛｼ"
      },
      "12025": {
        "name": "函館市",
        "yomi": "はこだてし",
        "yomi_kana": "ハコダテシ",
        "yomi_kana_han": "ﾊｺﾀﾞﾃｼ"
      },
      :
    },
    "seirei": {
      "11002": {
        "11011": {
          "name": "札幌市中央区",
          "yomi": "さっぽろしちゅうおうく",
          "yomi_kana": "サッポロシチュウオウク",
          "yomi_kana_han": "ｻｯﾎﾟﾛｼﾁｭｳｵｳｸ"
        },
        "11029": {
          "name": "札幌市北区",
          "yomi": "さっぽろしきたく",
          "yomi_kana": "サッポロシキタク",
          "yomi_kana_han": "ｻｯﾎﾟﾛｼｷﾀｸ"
        },
        :
      }
    }
  },
  "2": {
    "name": "青森県",
    :
```

# require
- python3

# how to use
1. clone & dive
    ```
    git clone https://github.com/hysakhr/japan-local-government-code-json.git
    cd japan-local-government-code-json
    ```

1. 必要なパッケージのインストール
    ```
    pip install -r requirements.txt
    ```

1. エクセルをダウンロードして、同じディレクトリに配置
1. 実行
    ```
    python convert.py
    ```

    デフォルトでは、以下のファイルを対象に動作します。
    - 入力ファイル：000618153.xls
    - 出力ファイル：pref.json

    入力ファイルと出力ファイルの指定も可能です。
    ```
    python convert.py -i [入力ファイル] -o [出力ファイル]
    ```

    全国（都道府県コード = 0）のデータを先頭に追加する
    ```
    python convert.py -n
    ```