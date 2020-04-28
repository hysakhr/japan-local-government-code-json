# 全国地方公共団体コード EXCEL→JSON変換ツール
下記ページの「都道府県コード及び市区町村コード」からダウンロード可能なエクセルファイルをもとにJSONデータを生成するpython製のツールです。

総務省 全国地方公共団体コード
https://www.soumu.go.jp/denshijiti/code.html

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


# how to use