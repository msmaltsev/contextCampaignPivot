#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import xlrd


def getFlist(d = 'Яндекс'):
    dir_abs = os.path.join(os.getcwd(), d)
    files = os.listdir(dir_abs)
    return [os.path.join(os.getcwd(), d, i) for i in files]


def processYandexFile(wbname):
    wb = xlrd.open_workbook(filename = wbname)
    ws = wb.sheet_by_index(0)
    rows_res = []

    camp_name = wbname.split('/')[-1][:-4]

    row = 11
    req_cols = [7, 9, 10, 11, 15]

    while row < ws.nrows:
        new_row = [camp_name]
        for col in req_cols:
            cell = ws.cell_value(row, col)
            new_row.append(ws.cell_value(row, col))
        row += 1
        rows_res.append('\t'.join(new_row))

    return rows_res


def main():
    result = open('Yandex_ALL.csv', 'w', encoding='utf16')
    flist = getFlist()
    for f in flist:
        print(f)
        try:
            res = processYandexFile(f)
            for i in res:
                print(i, file=result)
        except Exception as e:
            print(e)
        print('')
    
    result.close()


if __name__ == '__main__':
    main()