#-*- coding:utf-8 -*-

import requests, json
import info

class ISBN_Parser:
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    URL = "http://seoji.nl.go.kr/landingPage/SearchAjax.do"

    def __init__(self):
        self.book = dict()

    def parse_bookinfo(self, isbn):
        self.isbn = isbn
        data = 'start=0&tSrch_isbn=' + isbn + '&fq_select=tSrch_isbn&q=' + isbn

        res = requests.post(self.URL, headers = self.headers, data=data)
        
        try:
            if(res.status_code != 200):
                raise RuntimeError
            else:
                res = json.loads(res.text)['response']['docs'][0]
        except:
            print("파싱 중 에러 발생!")
    def print_book(self, book):
        data = [book['TITLE'], book['AUTHOR'], info.CATEGORY[book['EA_ADD_CODE'][2]],
                book['PUBLISHER'], book['PUBLISH_PREDATE'], book['EA_ISBN']]

        for s, d in zip(info.CONTENTS, data):
            print(s, d)
        print()
        
        self.book = {
            '제목' : res['TITLE'],
            '저자' : res['AUTHOR'],
            '분류' : info.CATEGORY[res['EA_ADD_CODE'][2]],
            '출판사' : res['PUBLISHER'],
            '발행일' : res['PUBLISH_PREDATE'],
            #'대상' : info.READER[res['EA_ADD_CODE'][0]],
            'ISBN' : res['EA_ISBN']
        }
    def get_bookinfo(self):
        srch = list()
        for w in '제목', '저자', '출판사':
            print("\n%s을(를) 입력하세요\n%s > " % (w, w), end='')
            srch.append(input())

        fq = 'TITLE_NGRAM : "' + \
            srch[0] + '" AND AUTHOR : "' + srch[1] + \
            '" AND PUBLISHER : "' + srch[2] + '"'
        data = 'start=0&fq_select: tSrch_author&detailSearchYn=Y&fq=' + fq

        return self.parse(data)
        
      
      
    
        return self.book

if __name__ == "__main__":
    p = ISBN_Parser()
    for n in ('9788934998952', '9791164050444'):
        b = p.parse_bookinfo(n)
        for k, v in b.items():
            print(k, v)
        print()
