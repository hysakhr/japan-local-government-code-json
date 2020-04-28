import os
import sys
import argparse
import json
import pandas as pd
import jaconv

p = argparse.ArgumentParser()
p.add_argument('-i', '--input', help='ファイル名', default='000618153.xls')
p.add_argument('-o', '--output', help='ファイル名', default='pref.json')
args = p.parse_args()


def main():
    input_filename = args.input
    output_filename = args.output

    # validation
    if not os.path.exists(input_filename):
        print(input_filename, 'は存在しません。')
        sys.exit(1)

    # 都道府県、市区町村データを格納する変数
    prefs = {}

    ##################################################
    #
    # 都道府県、市区町村(政令指定都市の区を除く)の処理
    #
    ##################################################
    # excelのシート読み込み
    df_city = pd.read_excel(
        input_filename,
        usecols='A:E',
        header=None,
        skiprows=[0])

    # カラム名変換
    # 団体コード, 都道府県名, 市区町村名, 都道府県名(カナ), 市区町村名(カナ)
    df_city.rename(
        columns={
            0: 'code',
            1: 'pref_name',
            2: 'city_name',
            3: 'pref_yomi_kana',
            4: 'city_yomi_kana'}, inplace=True)

    # 1行ずつ処理
    for i, row in df_city.iterrows():
        pref_code = row['code'] // 10000

        if isinstance(row['city_name'], float):
            # 都道府県
            pref = {
                'name': row['pref_name'],
                'yomi': jaconv.kata2hira(jaconv.h2z(row['pref_yomi_kana'])),
                'yomi_kana': jaconv.h2z(row['pref_yomi_kana']),
                'yomi_kana_han': row['pref_yomi_kana'],
                'cities': {},
                'seirei': {},
            }
            prefs[pref_code] = pref
        else:
            # 市区町村
            city_code = int(row['code'])
            city = {
                'name': row['city_name'],
                'yomi': jaconv.kata2hira(jaconv.h2z(row['city_yomi_kana'])),
                'yomi_kana': jaconv.h2z(row['city_yomi_kana']),
                'yomi_kana_han': row['city_yomi_kana']
            }
            prefs[pref_code]['cities'][city_code] = city

    ####################
    #
    # 政令指定都市の処理
    #
    ####################
    # excelシート読み込み
    df_seirei = pd.read_excel(
        input_filename,
        usecols='A:C',
        sheet_name=1,
        header=None)

    # カラム名変換
    # 団体コード, 市区町村名, 市区町村名(かな)
    df_seirei.rename(
        columns={
            0: 'code',
            1: 'city_name',
            2: 'city_yomi'},
        inplace=True)

    # 1行ずつ処理
    seirei_code = 0
    for i, row in df_seirei.iterrows():
        pref_code = row['code'] // 10000

        if '区' in row['city_name']:
            # 政令指定都市の区
            city_code = row['code']
            city = {
                'name': row['city_name'],
                'yomi': row['city_yomi'],
                'yomi_kana': jaconv.hira2kata(row['city_yomi']),
                'yomi_kana_han': jaconv.hira2hkata(row['city_yomi'])
            }
            prefs[pref_code]['seirei'][seirei_code][city_code] = city
        else:
            # 政令指定都市
            seirei_code = row['code']
            prefs[pref_code]['seirei'][seirei_code] = {}

    ########################
    #
    # jsonファイルに書き出し
    #
    ########################
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(prefs, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
