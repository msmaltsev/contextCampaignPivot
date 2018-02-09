#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def getFlist(d = 'Google'):
    dir_abs = os.path.join(os.getcwd(), d)
    files = os.listdir(dir_abs)
    return [os.path.join(os.getcwd(), d, i) for i in files]


def processGoogleFile(f_abspath):

    required = ['campaign', 'ad group', 'final url', 'headline 1', 'headline 2', 'description']
    result_body = []
    indexes = {}

    f = open(f_abspath, 'r', encoding='utf16').read().split('\n')
    head, body = f[0], f[1:]
    head = head.split('\t')

    for i in range(0, len(head)):
        if head[i].lower() in required:
            indexes[head[i].lower()] = i

    for line in body:
        newline = []
        spline = line.split('\t')
        for field in required:
            try:
                index = indexes[field]
                val = spline[index]
                newline.append(spline[index])
            except:
                pass
        if '' not in newline:
            result_body.append('\t'.join(newline))

    result_arr = result_body
        
    return result_arr




def main():
    result = open('Google_ALL.csv', 'w', encoding='utf16')
    flist = getFlist()
    for f in flist:
        print(f)
        try:
            res = processGoogleFile(f)
            for i in res:
                print(i, file=result)
        except Exception as e:
            print(e)
        print('')
    
    result.close()


if __name__ == '__main__':
    main()